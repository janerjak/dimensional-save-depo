from colorama import Fore, Style

import helpers.global_fields as g

def is_input_prompt_positive(response_input : str):
    return response_input.lower().startswith("y")

def print_in_color_and_to_gui(message: str, initial_color: str | None = None, hide_from_gui: bool = False):
    print(f"{getattr(Fore, initial_color.upper())}{message}{Style.RESET_ALL}")
    if not hide_from_gui and not g.args.nogui:
        # TODO
        pass