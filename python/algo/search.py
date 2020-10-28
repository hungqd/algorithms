from typing import TypeVar

T = TypeVar("T")


def __binary_search(data: list, value: T, low: int, high: int) -> int:
    mid = (high - low) // 2 + low
    if low > high:
        return None
    elif data[mid] == value:
        return mid
    elif data[mid] > value:
        return __binary_search(data, value, low, mid - 1)
    else:
        return __binary_search(data, value, mid + 1, high)


def binary_search(data: list, value: T) -> int:
    return __binary_search(data, value, 0, len(data) - 1)


if __name__ == "__main__":
    pass
