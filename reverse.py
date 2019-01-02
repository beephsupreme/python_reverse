def reverse(s):
    
    l = len(s)
    r = ""
    
    while l >= 0:
        r += s[l - 1]
        l -= 1
        
    return r
    
reverse("testing")
