import sys


def test_demo(n):
    print(f"{n}")
    return n


def main():
    test_demo(sys.argv[1])


if __name__ == '__main__':
    test_demo(sys.argv[1])
