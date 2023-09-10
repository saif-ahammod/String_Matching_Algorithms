def naiveStringSearch(text, pattern):
    matches = []
    i = 0
    while i < len(text) - len(pattern) + 1:
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
        else:
            matches.append(i)
        i += 1
    return matches

def main():
  text = input("Please enter the text:  ")
  pattern = input("Please enter the pattern:  ")

  matchIndex = naiveStringSearch(text, pattern)

  if matchIndex != -1:
    print(f"The pattern {pattern} is found at index: {matchIndex}")
  else:
    print(f"The pattern {pattern} is not found")

if __name__ == "__main__":
  main()