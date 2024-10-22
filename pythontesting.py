def distance(x, y, p = 2):
    
    result = sum(abs(x - y) ** (p)) ** (1/p)
    
    """calculates Lp distance between point x and point y
    Args:
        x (np.ndarray): datapoint x
        y (np.ndarray): datapoint y
        p (int): order of Lp norm
    """
    return result

print(distance(5, 2, p = 2))

print(distance(1, 3, p = 1))

print("please push one more time")