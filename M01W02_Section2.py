char_count = {}
word = "Levenshtein"
for char in word:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
print(char_count)
