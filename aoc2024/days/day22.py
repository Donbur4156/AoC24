from typing import List
from ..util import *
from math import floor
from more_itertools import windowed
from collections import Counter

def mix(value, secret):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def calc_next_secret(secret: int):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(floor(secret / 32), secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

def get_price(secret):
    return int(str(secret)[-1])

def calc_next_secrets(secret: int, times):
    prices = []
    price_changes = []
    price = get_price(secret)
    prices.append(price)
    for _ in range(times):
        secret = calc_next_secret(secret)
        price = get_price(secret)
        price_changes.append(price - prices[-1])
        prices.append(price)
        
    return secret, prices, price_changes

def execute(data: List[str], test_data: List[str]):
    secrets = list(map(int, data))
    secrets_2000th = []
    buyers = []
    for secret in secrets:
        secret_2000th, prices, price_changes = calc_next_secrets(secret, 2000)
        secrets_2000th.append(secret_2000th)
        buyers.append([prices, price_changes])

    buyers_combinations = Counter()
    for buyer in buyers:
        combinations = Counter()
        for e, comb in enumerate(windowed(buyer[1], 4)):
            if not comb in combinations:
                combinations.update({comb: buyer[0][e+4]})
        buyers_combinations += combinations

    r1 = sum(secrets_2000th)
    r2 = max(buyers_combinations.values())


    return r1, r2
