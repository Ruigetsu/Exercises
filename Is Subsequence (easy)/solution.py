def isSubsequence(s, t):
    new_str = ''
    n = 0
    for i in range(len(t)):
        if s[n] == t[i]:
            new_str += t[i]
            if n < len(s)-1:
                n += 1
            else:
                break
        else:
            continue
    if new_str == s:
        return True, new_str
    else:
        return False, new_str

print(isSubsequence("axc", "ahbgdc"))