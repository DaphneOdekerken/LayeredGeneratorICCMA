from py_arg.abstract_argumentation_classes.abstract_argumentation_framework \
    import AbstractArgumentationFramework
from py_arg.abstract_argumentation_classes.defeat import Defeat
from py_arg.aspic_classes.argumentation_theory import ArgumentationTheory


def convert_at_to_af(argumentation_theory: ArgumentationTheory) -> \
        AbstractArgumentationFramework:
    arguments = argumentation_theory.all_arguments
    defeats = [Defeat(a, b) for a in arguments for b in arguments
               if argumentation_theory.rebuts(a, b)]
    af = AbstractArgumentationFramework(arguments=arguments, defeats=defeats)
    return af
