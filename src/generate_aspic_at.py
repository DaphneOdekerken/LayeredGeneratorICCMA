from py_arg.aspic_classes.argumentation_theory import ArgumentationTheory
from py_arg.generators.argumentation_system_generators.\
    layered_argumentation_system_generator import \
    LayeredArgumentationSystemGenerator
from py_arg.generators.incomplete_argumentation_theory_generators.\
    incomplete_argumentation_theory_generator import \
    IncompleteArgumentationTheoryGenerator


def generate_layered_aspic_at(nr_of_literals) -> ArgumentationTheory:
    nr_of_rules = 1.5 * nr_of_literals

    rule_antecedent_distribution = {1: int(nr_of_rules / 3),
                                    2: int(nr_of_rules / 3),
                                    3: int(nr_of_rules / 9),
                                    4: int(nr_of_rules / 9)}
    rules_left = nr_of_rules - sum(rule_antecedent_distribution.values())
    rule_antecedent_distribution[5] = rules_left

    literal_layer_distribution = {0: 2 * nr_of_literals / 3,
                                  1: nr_of_literals / 10,
                                  2: nr_of_literals / 10,
                                  3: nr_of_literals / 10}
    literals_left = nr_of_literals - sum(literal_layer_distribution.values())
    literal_layer_distribution[4] = literals_left

    layered_argumentation_system_generator = \
        LayeredArgumentationSystemGenerator(
            nr_of_literals=nr_of_literals,
            nr_of_rules=nr_of_rules,
            rule_antecedent_distribution=rule_antecedent_distribution,
            literal_layer_distribution=literal_layer_distribution,
            strict_rule_ratio=0)

    # Generate the argumentation system, and keep the "layers" of literals.
    arg_sys, layered_language = \
        layered_argumentation_system_generator.generate(
            return_layered_language=True,
            add_rule_preferences=False)

    # Generate an incomplete argumentation theory, where only literals on the
    # first layer can be queryable.
    positive_queryable_candidates = {
        arg_sys.language[str(literal).replace('-', '')] for literal in
        layered_language[0]}
    iat_generator = IncompleteArgumentationTheoryGenerator(
        argumentation_system=arg_sys,
        positive_queryable_candidates=list(positive_queryable_candidates),
        queryable_literal_ratio=0.5,
        knowledge_queryable_ratio=0.5,
        axiom_knowledge_ratio=1
    )
    iat = iat_generator.generate()

    # Now only keep the "complete" part (omitting the queryables)
    at = ArgumentationTheory(argumentation_system=arg_sys,
                             knowledge_base_axioms=iat.knowledge_base_axioms,
                             knowledge_base_ordinary_premises=[],
                             ordinary_premise_preferences=None)
    return at
