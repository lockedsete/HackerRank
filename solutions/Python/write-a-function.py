def is_leap(year):
    leap = False

    # ↓ Write your logic here ↓
    if year % 4 != 0:
        return False
    else:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    # ↑ Write your logic here ↑

    return leap

year = int(input())
print(is_leap(year))