from helpers import global_fields as g
from helpers.cli_utility import print_in_color_and_to_gui as printc

from asyncio import sleep
from colorama import Fore, Style
from psutil import process_iter
        
def is_game_process_running() -> bool:
    return any(
        process for process in process_iter()
        if process.name() == g.config.game.executable_name
	)

async def process_polling_thread_entry():
    # Wait until Satisfactory is running at least once until doing anything to ensure no valuable save-games are overwritten
    # TODO: Replace this with a server health check. Decide what to do based on whether the server is running
    #while not is_game_process_running():
    #    printc(f"{Style.DIM}Satisfactory is not running", initial_color="yellow", hide_from_gui=True)
    #    await sleep(g.config.play_observation.method.args.interval_in_seconds)
    #printc("Satisfactory is running", initial_color="green")
    is_server_healthy = True

    if is_server_healthy:
        printc("The server health check indicated that the server is running and in a healthy state", initial_color="cyan")
        printc("Thus it is assumed that the save file needs to be downloaded from the server, once Satisfactory starts", initial_color="yellow")
        return await case_initial_health_check_healthy()
    else:
        printc("The server health check could not be performed or indicated that the server is in an unhealthy state", initial_color="cyan")
        printc("Thus it is assumed that the save file needs to be uploaded to the server, once Satisfactory is no longer running", initial_color="yellow")
        return await case_initial_health_check_unhealthy()

async def case_initial_health_check_healthy():
    return await main_polling_loop(first_wait_for_no_longer_running=False)

async def case_initial_health_check_unhealthy():
    return await main_polling_loop(first_wait_for_no_longer_running=True)

async def main_polling_loop(first_wait_for_no_longer_running: bool):
    first_iteration = True
    while True:
        # NOTE: Skip the first check in the first iteration, if we should first wait for running Satisfactory to download the save
        if first_wait_for_no_longer_running or not first_iteration:
            while is_game_process_running():
                printc(f"{Style.DIM}Satisfactory is still running", initial_color="yellow", hide_from_gui=True)
                await sleep(g.config.play_observation.method.args.interval_in_seconds)
            printc("Satisfactory is no longer running, start uploading save sequence", initial_color="green")
            # TODO: Continue with uploading save
            printc("Server is now continuing to simulate your factory in the background", initial_color="green")

        printc("Waiting for Satisfactory. Once running, we will stop the server and download the most recent save", initial_color="yellow")
        while not is_game_process_running():
            printc(f"{Style.DIM}Satisfactory is not running", initial_color="yellow", hide_from_gui=True)
            await sleep(g.config.play_observation.method.args.interval_in_seconds)
        printc("Satisfactory is running, start downloading save sequence", initial_color="green")
        # TODO: Continue with downloading save

        printc("Server has been stopped. Have fun playing!", initial_color="green")
        printc("Waiting for Satisfactory to close. Once no longer running, we will start the server and upload the most recent save", initial_color="yellow")

        first_iteration = False
    return True