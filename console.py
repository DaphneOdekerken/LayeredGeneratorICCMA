import argparse
import pathlib

from src.convert_at_to_abaf import convert_at_to_abaf
from src.convert_at_to_af import convert_at_to_af
from src.export_abaf import export_abaf
from src.export_af import export_af
from src.generate_aspic_at import generate_layered_aspic_at


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Layered argumentation theory generator'
    )

    # Number of literals
    parser.add_argument('nr_literals', type=int)

    # Number of instances
    parser.add_argument('nr_instances', type=int)

    # Export folder
    parser.add_argument('path')

    # Export format
    parser.add_argument('format', choices=['af', 'aba'])

    return parser


def main():
    parser = init_argparse()
    args = parser.parse_args()
    for instance_nr in range(args.nr_instances):
        at = generate_layered_aspic_at(args.nr_literals)
        if args.format == 'af':
            af = convert_at_to_af(at)
            filename = 'af_' + str(instance_nr + 1) + '_' + str(
                args.nr_literals) + 'literals.txt'
            path = pathlib.Path(args.path) / filename
            export_af(af, str(path))
            print(path)
        else:
            abaf = convert_at_to_abaf(at)
            filename = 'aba_' + str(instance_nr + 1) + '_' + str(
                args.nr_literals) + 'literals.txt'
            path = pathlib.Path(args.path) / filename
            export_abaf(abaf, str(path))
            print(path)


if __name__ == '__main__':
    main()
