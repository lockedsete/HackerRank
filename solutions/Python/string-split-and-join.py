def split_and_join(line):
    #  ↓ write your code here  ↓
    a = line.split(" ")
    b = "-".join(a)
    return b
    #  ↑ write your code here  ↑

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)