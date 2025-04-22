from py_arg.aba_classes.aba_framework import ABAF
from py_arg.aba_classes.rule import Rule
from py_arg.aspic_classes.argumentation_theory import ArgumentationTheory


def convert_at_to_abaf(argumentation_theory: ArgumentationTheory) -> ABAF:
    # ABA language and contraries based on ASPIC+ language and contraries.
    aba_language = set()
    aba_contraries = {}
    aspic_language = \
        argumentation_theory.argumentation_system.language.values()
    for literal in aspic_language:
        aba_language.add(literal.s1)
        # contradictory = list(literal.contraries_and_contradictories)[0]
        # aba_contraries[literal.s1] = contradictory.s1

    # For each ASPIC+ rule: make a literal for it and one contrary.
    aba_rules = set()
    assumptions = set()
    for rule in argumentation_theory.argumentation_system.rules:
        # Additional atoms/literals and contraries
        rule_holds_literal = f'rule_{rule.id}_holds'
        rule_does_not_hold_literal = f'rule_{str(rule.id)}_does_not_hold'
        aba_language.add(rule_holds_literal)
        aba_language.add(rule_does_not_hold_literal)
        aba_contraries[rule_holds_literal] = rule_does_not_hold_literal
        # aba_contraries[rule_does_not_hold_literal] = rule_holds_literal

        # One ABA rule is the ASPIC+ rule with as an additional antecedent
        # that the rule should actually hold.
        antecedents = {antecedent.s1 for antecedent in rule.antecedents}
        antecedents.add(rule_holds_literal)
        aba_aspic_rule = Rule(rule_id=f'aspic_rule_{rule.id}',
                              body=antecedents,
                              head=rule.consequent.s1)
        aba_rules.add(aba_aspic_rule)

        # Another ABA rule: if the consequent is not derived, then the rule
        # did not hold.
        not_consequent = list(rule.consequent.contraries_and_contradictories)[
            0].s1
        aba_not_hold_rule = Rule(rule_id=f'not_aspic_rule_{rule.id}',
                                 body={not_consequent},
                                 head=rule_does_not_hold_literal)
        aba_rules.add(aba_not_hold_rule)

        assumptions.add(rule_holds_literal)

    return ABAF(assumptions, aba_rules, aba_language, aba_contraries)
