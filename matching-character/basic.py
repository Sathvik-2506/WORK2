str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

matches = 0

min_len = min(len(str1), len(str2))

for i in range(min_len):
    if str1[i] == str2[i]:
        matches += 1

max_len = max(len(str1), len(str2))

similarity = (matches / max_len) * 100

print("Matching characters:", matches)
print("Similarity Percentage:", round(similarity, 2), "%")