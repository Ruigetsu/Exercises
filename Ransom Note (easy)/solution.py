def ransomNote(s, t):
    new_str = ''
    for i in range(len(s)):
        for n in range(len(t)):
            if s[i] == t[n]:
                new_str += s[i]
                t = t.replace(t[n], " ", 1)
                break
            else:
                continue
    if new_str == s:
        return True, new_str, s, t
    else:
        return False, new_str, s, t


print(ransomNote("aa", 'vbgfdgfdagdgda'))