import numpy as np


def mypackage_func() -> float:
    return np.pi


def mypy_func(x: int) -> None:
    print("This is mypy test: x = {}".format(x))
    return


def main():
    print(mypackage_func())


if __name__ == "__main__":
    main()
