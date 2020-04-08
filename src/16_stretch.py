def is_prime(arg):
    for x in range(2, arg):
        if arg % x == 0:
            return False

    return True

