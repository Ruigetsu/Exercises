def isHappy(n):
        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
            print(n, hset)
        else:
            return True
        


def test(n):
    s = str(n)
    print(sum([int(i) for i in s]))

print(test(12))