for i in range(1, 15 + 1):
    result = ""
    if i % 3 == 0:
        result += "fizz"
    if i % 5 == 0:
        result += "buzz"
    print(result or i)
