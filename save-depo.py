from enums.play_observation_method import PlayObservationMethod
from helpers import global_fields as g
from helpers.args import obtain_args
from helpers.config_loader import obtain_config
from helpers.cli_utility import print_in_color_and_to_gui as printc
from modules.process_polling import process_polling_thread_entry

from asyncio import run


async def main_thread_selection(_args, _config) -> bool:
    if g.config.play_observation.method.type == PlayObservationMethod.PROCESS_POLLING:
        return await process_polling_thread_entry()

    return False

async def main(_args, _config) -> None:
    g.config = _config
    g.args = _args

    if await main_thread_selection(_args, _config):
        printc("Done.", initial_color="green")
    else:
        printc("Terminating.", initial_color="red")

if __name__ == "__main__":
    _args = obtain_args()
    _config = obtain_config(_args, __file__)
    run(main(_args, _config))