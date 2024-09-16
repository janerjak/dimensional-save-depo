from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

parser = ArgumentParser(
    description="Offload your Satisfactory save file to a (different) dedicated server, to run in the background when you are not playing",
    formatter_class=ArgumentDefaultsHelpFormatter,
)

gui_group = parser.add_argument_group("gui", description="Arguments to configure the UI")
gui_group.add_argument("--nogui", "-nG", action="store_true", help="Do not display a GUI, STDOUT output only")

def obtain_args():
    args = parser.parse_args()
    required_args = []
    if any(getattr(args, arg_name) is None for arg_name in required_args):
        exit(-1)
    return args