def wordPattern(pattern, s):
    s = s.split(" ")
    n = []
    new_list = []
    for i in pattern:
        if i not in n:
            n.append(pattern.index(i))
        else:
            continue
    for m in range(len(s)):
        if s[n[m]] == s[m]:
            new_list.append(s[n[m]])
        else: 
            new_list.append('')
    if new_list == s:
        return True
    else:
        return False

print(wordPattern("abba","dog cat cat dog"))