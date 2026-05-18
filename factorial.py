def factorial(n, arr=None):
    """Вычисляет факториал числа n."""
    if arr is None:
        arr = {0: 1, 1: 1}

    try:
        if arr[n] in arr:
            return arr[n]
    except KeyError:
        pass

    arr[n] = factorial(n-1) * n
    return arr[n]

numb = input()
print(factorial(int(numb)))
