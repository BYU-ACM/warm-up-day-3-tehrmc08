def Coin_Combinations(coins, value):
  """
    A Generalized solution to the coins problem provided by project euler #31
    Read it for more specifications
    coins: a list of coins that can be used
    value: the value that the coins should add to
    returns:
     number of possible combinations to make value with givin coins in "coins"
  """
  ways_to_make = [1] + [0]*value
  for coin in coins:
    for index in range(coin, value+1):
      ways_to_make[index] += ways_to_make[index-coin]
  return ways_to_make[value]
