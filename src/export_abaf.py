from py_arg.aba_classes.aba_framework import ABAF


def export_abaf(aba_framework: ABAF, write_path: str):
    atom_to_index = {}
    for index, atom in enumerate(aba_framework.language, 1):
        atom_to_index[atom] = index

    with open(write_path, 'w') as writer:
        writer.write(f'p aba {str(len(atom_to_index))}\n')

        for index in atom_to_index.values():
            writer.write(f'a {str(index)}\n')

        for contrary_a, contrary_b in aba_framework.contraries.items():
            writer.write(f'c {str(atom_to_index[contrary_a])} '
                         f'{str(atom_to_index[contrary_b])}\n')

        for rule in aba_framework.rules:
            body_elements = [str(atom_to_index[antecedent])
                             for antecedent in rule.body]
            body_str = ' '.join(body_elements)
            writer.write(f'r {str(atom_to_index[rule.head])} {body_str}\n')
