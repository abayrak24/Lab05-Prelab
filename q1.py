def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    n = len(s)
    best = ""
    
    for i in range(n):
        for j in range(i+2,n+1):
            piece = s[i:j]
            if piece == piece[::-1] and len(piece) > len(best):
                best = piece
    return best