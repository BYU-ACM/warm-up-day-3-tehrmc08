import pytest
import numpy as np
from real_sol import Coin_Combinations


coin_sets = [[1,2,3,4], [1,2,5], [1,5,10,25], [1,5,10,25,50]]
values = [10, 200, 500, 1000]
answers = [23, 2081, 19006, 801451]

params = zip(coin_sets, values, answers)

@pytest.mark.parametrize("coins,value,answer", params)
def test_Coin_Combinations(coins, value, answer):
  assert Coin_Combinations(coins, value) == answer


def test_stuff_not_imported():
  with open('sol.py') as solution_files:
    data = solution_files.read().replace('\n', '')
    assert ('numpy' not in data)
    assert ('scipy' not in data)
