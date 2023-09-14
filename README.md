# Some String Matching Algorithms
## Native algorithm
## Z algorithm
<p align="Justify">
  The Z algorithm is a linear time string matching algorithm. It is used to find all occurrences of a pattern in a string. The algorithm works by creating an array, called the Z array, which stores the length of the longest prefix of the string
  that is also a suffix of the string.To create the Z array, we start by initializing all elements of the array to 0.   Then, we iterate over the string, starting from the second character. For each character, we find the longest prefix of 
  the string that is also a suffix of the string starting from the current character. We store this length in the Z array 
  at the current index.Once we have created the Z array, we can find all occurrences of the pattern in the string by looking 
  for indices in the Z array where the value is equal to the length of the pattern.
  Here is an example of how the Z algorithm works. Let's say we have the string "abracadabra" and we want to find all 
  occurrences of the pattern "abra" in the string. The Z array for this string is:
  The value 3 at index 6 indicates that the pattern "abra" is found at index 6 in the string.
</p>
<p>
  [0, 1, 0, 1, 2, 2, 3, 3, 1, 0]
</p>
<p>
  The Z algorithm is a very efficient string matching algorithm. It has a time complexity of O(n), where n is the length of the string. 
  This is because the algorithm only needs to scan the string once.
</p>
