from decimal import Decimal

T = int(raw_input().strip())
phoneBook = {}
for i in range(T):
    name, number = (raw_input().split(" "))
    print input
    phoneBook[name] = number
print phoneBook
try:
    while(True):
        x = str(raw_input())
        if x != "":
            if (x in phoneBook):
                print x

        else:
            break
except Exception:
    print ""
