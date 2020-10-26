import cmath

if __name__ == "__main__":

    n = input(str())

    _mod = abs(complex(n))
    _angle = cmath.phase(complex(n))

    print(_mod)
    print(_angle)
