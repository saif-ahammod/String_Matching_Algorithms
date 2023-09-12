# preprocessing for strong good suffix rule
def preprocess_strong_suffix(shift, bpos, pat, m):
    # m is the length of pattern
    i = m
    j = m + 1
    bpos[i] = j
    while i > 0:
        while j <= m and pat[i - 1] != pat[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            # Update the position of next border
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j
# Preprocessing for case 2
def preprocess_case2(shift, bpos, pat, m):
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]


def BoyerMooreSearch(text, patttern):
    # s is shift of the pattern with respect to text
    s = 0
    m = len(patttern)
    n = len(text)

    bpos = [0] * (m + 1)

    # initialize all occurrence of shift to 0
    shift = [0] * (m + 1)

    # do preprocessing
    preprocess_strong_suffix(shift, bpos, patttern, m)
    preprocess_case2(shift, bpos, patttern, m)

    while s <= n - m:
        j = m - 1
        while j >= 0 and patttern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"pattern occurs at shift = {s}")
            s += shift[0]
        else:
            s += shift[j + 1]
# Driver Code
if __name__ == "__main__":
    text = "ILOVENSU"
    pattern = "NSU"
    BoyerMooreSearch(text, pattern)
