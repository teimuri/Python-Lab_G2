def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    # If the last charecter is the same in s and t 
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])

    return res

print(LD("Python", "Pehn"))
