def swap_case(s):
    newStr = ""
    for i in s:
        if i.isupper():
            newStr += i.lower()
        else:
            newStr += i.upper()

    return newStr


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
