def distance(first, second):
    return sum((1 for f, s in zip(first, second) if f != s))
