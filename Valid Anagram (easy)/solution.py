def isAnagram(s,t):
    new_str = ""
    if len(s) == len(t):
        for i in range(len(s)): 
            if s[i] not in t:
                break
            for m in range(len(t)):
                if s[i] == t[m]:
                    new_str += t[m]
                    t = t.replace(t[m], "", 1)
                    break
                else:
                    continue
    else:
        return "Error"
    return True if new_str == s else False
    
#print(isAnagram('anagram', 'nagaram'))

def test(i,j):
    return abs(i-j)

print(test(4,1))