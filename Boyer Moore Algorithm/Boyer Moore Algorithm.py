from collections import defaultdict
def calculateZ(input):
    print("calculateZ(input)")
    #initializing z array and values of left and right of z box
    left = 0
    right = 0
    z = [0]*(len(input))
    for k in range(1, len(input)):
        # Check if the k is outside the z box
        if k > right:
            left = right = k
            while right < len(input):
                if input[right] == input[right - left]:
                    right = right + 1
                else:
                    break
            z[k] = right-left
            right = right -1
        #if the value of k is inside z box
        else:
            #then if the value do not touch the right side of the z box
            k1 = k-left
            if(z[k1]<right-k-1):
                z[k] = z[k1]
            #if the value do touch the right side of the z box
            else:
                left = k
                while right < len(input):
                    if input[right] == input[right - left]:
                        right = right + 1
                    else:
                        break
                z[k] = right - left
                right = right - 1
    return z

def ExtendedBadCharTable(pattern):
    print("ExtendedBadCharTable(pattern)")
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
    print("GoodSuffixTable(pattern):")
    #Reversing the pattern
    patternRev = pattern[::-1]
    #Calculating the Z value
    Z = calculateZ(patternRev)
    #Calculating the N value
    N = Z
    N.reverse()

    #Calculating  L prime
    n = len(pattern)
    Lprime = [0] * n
    for j in range (0,n-1):
        i = n - N[j]+1
        if i < n:
            Lprime[i-1] = j

    #Calculating l prime value
    lprime = [0] * n
    flag = 0
    for j in range(0,n):
        if N[j] == j+1:
            flag = N[j]
        lprime[n-j-1] = flag
    lprime[0] = n
    return Lprime, lprime


#Calculating the shift in extended bad character rule
def BadCharacterTableShift(BCTable, character, Currentindex, n):
    print("BadCharacterTableShift(BCTable, character, Currentindex, n):")
    # loading the list of the charecter
    list = BCTable[character]
    # If list empty
    if list == None:
        return n - Currentindex;
    # If list not empty
    for x in list:
        if x < Currentindex:
            return Currentindex-x;
    return 1

#Calculating the shift in good suffex table
def GoodSuffixTableShift(Lprime, lprime, Currentindex, n):
    print("GoodSuffixTableShift(Lprime, lprime, Currentindex, n):")
    if Currentindex == n-1:
        return 1
    else:
        if Lprime[Currentindex] > 0:
            return n-Lprime[Currentindex]
        else:
            if lprime[Currentindex] > 0:
                return n - lprime[Currentindex]
            else:
                return 1

def BoyerMoore(text, pattern):
    print("BoyerMoore(text, pattern):")
    m = len(text)
    n = len(pattern)
    BadCharTable = ExtendedBadCharTable(pattern)
    print(f"Bad Character Table:{BadCharTable}")
    GoodSuffTab =GoodSuffixTable(pattern)
    Lprime = GoodSuffTab[0]
    print(f"L prime Table:{Lprime}")
    lprime = GoodSuffTab[1]
    print(f"l prime Table:{lprime}")
    k = n-1
    while k < m:
        i = n-1
        h = k
        while i >= 0 & bool(pattern[i] == text[i]):
            i = i-1
            h = h-1

        if i < 0:
            print(f"Index of Pattern: {pattern} matched with text at {k-n-1}")
            if n > 1 & lprime[1] > 0:
                k = k + n - lprime[1]
            else:
                k = k + 1
        else:
            BCS = BadCharacterTableShift(BadCharTable,text[h],i,n)
            GSS = GoodSuffixTableShift(Lprime,lprime,i,n)
            shift = max(BCS,GSS)
            k = k + shift

def main():
    #Input Text
    text = "aabaabaaaaaaaabaaaaaaabaa"
    #Input Pattern
    pattern = "aabaa"
    #Search the pattern if it exist in text
    BoyerMoore(text, pattern)

if __name__ == '__main__':
    main()