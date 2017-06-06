def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    1
    >>> num_buses(150)
    3
    >>> num_buses(235)
    4
    >>> num_buses(-3)
    0
    >>>
    """
    if n >= 0:
        return n // 50
    return 0

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([-0.3, -0.23, 0.5, 0.02, -0.12, 0, 0.47])
    (0.99,-0.05)
    """
    price_chang_gain = []
    price_chang_loss = []

    for i in price_changes:
        if i >= 0:
            price_chang_gain.append(i)
        elif i < 0:
            price_chang_loss.append(i)
    return (sum(price_chang_gain), sum(price_chang_loss))
            

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [10, 13, 7, 9]
    >>> swap_k(nums, 2)
    >>> nums
    [7, 9, 10, 13]
    """
    if (k > len(L) // 2) or (k < 0):
        return L
    
    if (k>= 0) and (k <= len(L)//2):
        lst = []
        for i in L[-k:]:
            lst.append(i)
        for i in L[k:(len(L)-k)]:
            lst.append(i)
        for i in L[:k]:
            lst.append(i)
        return lst
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
