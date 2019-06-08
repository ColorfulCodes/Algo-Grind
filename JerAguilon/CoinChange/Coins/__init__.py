def coinChange(coins, amount):
    need = [0] + [amount + 1] * amount
    if len(coins) == 0:
        raise ValueError('Must insert a list of coin types')

    for c in coins:
        for a in range(c, amount+1):
            need[a] = min(need[a], need[a - c] + 1)
    if need[-1] <= amount:

      return need[-1]
    else:
      return -1

# coinChange([1, 2, 5],11)
# coinChange(0,11)
