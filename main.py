import sys
import datetime
from importlib import import_module
from pathlib import Path
from time import perf_counter
from aoc2024.util import get_day_data, print_result
import shutil
from colorama import init as colorama_init, Fore


colorama_init(autoreset=True)
today = datetime.datetime.today()

def get_target_day():
    if len(sys.argv) == 1:
        if today.year != 2024 or today.month != 12:
            print(f'{Fore.RED}Error: Can\'t run without specific day outside of competition time')
            exit(1)
        return str(datetime.datetime.today().day)
    else:
        return sys.argv[1]
    
def generate_day(day: str = None):
    target_day = day or str(today.day).zfill(2)
    shutil.copyfile('template/day.py', f'aoc2024/days/day{target_day}.py')
    print(f'{Fore.GREEN}Generated template for day {int(target_day)}.')

def run_day(target_day: str):
    day_data = get_day_data(target_day)
    day_module = import_module(f'aoc2024.days.day{target_day}')
    start_time = perf_counter()
    results = day_module.execute(day_data)
    end_time = perf_counter() - start_time
    print_result(*results)
    print(f'{Fore.LIGHTBLACK_EX}Perf: Took {end_time:.3f} seconds')

if __name__ == "__main__":
    target_day = get_target_day().zfill(2)
    if not Path(f'aoc2024/days/day{target_day}.py').exists():
        generate_day(target_day)
    run_day(target_day)
