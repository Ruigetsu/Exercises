def isIsomorphic(s,t):
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            else:
                s = s.replace(s[i], t[i])             
        if s == t:
            return True
        else: 
            return False
    else:
        return 'Error'

print(isIsomorphic("paper", "title"))