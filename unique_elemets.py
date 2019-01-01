def unique(S):
    checker = 0
    for i in S:
        val = ord(i) - ord("a")
        if (checker & (1 << val)) > 0:
            return False
        checker = checker | (1 << val)
    return True
    
S = "shivangagarwal"
print(unique(S))
