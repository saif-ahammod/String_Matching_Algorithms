def calculateZ(input):
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
def findMatchPattern(text,pattern):
    concatedText =  pattern+ "$" +text
    index = []
    #Calculate the z index
    z = calculateZ(concatedText)
    # Find the index of matched pattern in text
    for i in range(0,len(z)):
        if len(pattern) == z[i]:
            index.append(i-len(pattern)-1)
    return index

def main():
    text = input("Please input a text")
    pattern = input("Please input a pattern")
    matchIndex = findMatchPattern(text,pattern)
    print(f"Pattern match found at index {matchIndex}")

if __name__ == "__main__":
    main()