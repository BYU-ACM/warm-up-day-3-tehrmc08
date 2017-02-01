def rep(coins, curr, last):
  myCoins = coins[::-1]
  count = 0
  for i in range(len(coins)):
    if myCoins[i] <= last and curr - myCoins[i] >= 0:
      count = count + rep(coins, curr - myCoins[i], myCoins[i])
  if curr == 0:
    return 1
  return count

def Coin_Combinations(coins, value):
  """
    A Generalized solution to the coins problem provided by project euler #31
    Read it for more specifications
    coins: a list of coins that can be used
    value: the value that the coins should add to
    returns:
     number of possible combinations to make value with givin coins in "coins"
  """
  return rep(coins, value, coins[len(coins)-1]+1)
