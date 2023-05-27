import textwrap


def wrap(string, max_width):
    wrappedString = ""
    count = 0

    for i in string:
        wrappedString += i
        count += 1

        if count % max_width == 0:
            wrappedString += "\n"

    return wrappedString


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
