d  # O(Nlog(N))T and O(N)S


def non_constructible_change(coins):
    coins.sort()    # O(Nlog(N))T

    current_change_created = 0
    for coin in coins:
        if coin > current_change_created+1:
            return current_change_created+1
        current_change_created += coin

    return current_change_created+1


coins = [5, 7, 1, 1, 2, 3, 22]
non_constructible_change(coins)
