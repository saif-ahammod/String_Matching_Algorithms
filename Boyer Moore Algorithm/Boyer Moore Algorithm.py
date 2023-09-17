from collections import defaultdict
def ExtendedBadCharTable(pattern):
    table = defaultdict(list)
    for index, x in enumerate(pattern):
        value = len(pattern) - index - 1
        if x in table:
            table[x].append(value)
        else:
            table[x] = []
            table[x].append(value)
    return table
def GoodSuffixTable(pattern):
    print("Good Suffix Table")


def BoyerMoore(text, pattern):
    X =ExtendedBadCharTable(pattern)
    GoodSuffixTable(pattern)
    print(X)





def main():
    text = "World's simplest online text line randomizer for web developers and programmers."
    pattern = "abcabc"
    BoyerMoore(text, pattern)

if __name__ == '__main__':
    main()