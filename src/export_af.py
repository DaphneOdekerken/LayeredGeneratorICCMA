from py_arg.abstract_argumentation_classes.abstract_argumentation_framework \
    import AbstractArgumentationFramework
from py_arg.import_export.argumentation_framework_to_iccma23_format_writer \
    import ArgumentationFrameworkToICCMA23FormatWriter


def export_af(af: AbstractArgumentationFramework, write_path: str):
    af_str = ArgumentationFrameworkToICCMA23FormatWriter.write_to_str(af)
    with open(write_path, 'w') as writer:
        writer.write(af_str)
