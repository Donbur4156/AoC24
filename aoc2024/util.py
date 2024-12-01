import pathlib
from typing import List

import requests
import json
from colorama import Fore, Style

__all__ = ['print_result', 'get_config', 'get_day_data']


def print_result(r1, r2):
    if r1 is None:
        print(f'Part {1}: {Fore.YELLOW}Unsolved')
    else:
        print(f'Part {1}: {Style.BRIGHT}{Fore.GREEN}{r1}')
    if r2 is None:
        print(f'Part {2}: {Fore.YELLOW}Unsolved')
    else:
        print(f'Part {2}: {Style.BRIGHT}{Fore.GREEN}{r2}')


def get_config() -> dict:
    with open('config.json') as _f:
        return json.load(_f)


def get_day_data(day: str) -> List[str]:
    path = pathlib.Path(f'data/{day}.txt')

    if path.exists():
        with open(path.absolute()) as _f:
            return _f.read().splitlines()

    cfg = get_config()

    headers = {
        'cookie': f'session={cfg["session_token"]}'
        #'user-agent': f'{cfg["repo"]} by {cfg["email_adress"]}'
    }
    r = requests.get(f'https://adventofcode.com/2024/day/{int(day)}/input', headers=headers)
    text = r.text.splitlines()
    if text[0].startswith("Please don't repeatedly request this endpoint before it unlocks!"):
        print(f"The data from day {day} is not available")
        exit(1)
    with open(path.absolute(), 'w') as _f:
        _f.writelines('\n'.join(text))
    return text