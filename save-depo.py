from helpers import global_fields as g
from helpers.args import obtain_args
from helpers.config_loader import obtain_config

from colorama import Fore, Style


def main(_args, _config) -> bool:
    g.config = _config
    g.args = _args

    return True

if __name__ == "__main__":
    _args = obtain_args()
    _config = obtain_config(_args, __file__)
    if main(_args, _config):
        print(f"{Fore.GREEN}Done.{Fore.RESET}")
    else:
        print(f"{Fore.RED}Terminating.{Fore.RESET}")