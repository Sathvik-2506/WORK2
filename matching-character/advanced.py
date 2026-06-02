def string_matching(a, b):

    a = a.strip().lower().replace(" ", "")
    b = b.strip().lower().replace(" ", "")

    if not a or not b:
        print("One of the given strings is empty!")
    elif a in b:
        print("String1 is present in String2")
        print("Occurrences:")
        

    if not str1 or not str2:
        print("One of the strings is empty!")
        return

    matches = 0
    mismatches = []

    min_len = min(len(str1), len(str2))

    for i in range(min_len):

        if str1[i] == str2[i]:
            matches += 1
            print(f"Position {i}: {str1[i]} == {str2[i]} ✓")

        else:
            mismatches.append(i)
            print(f"Position {i}: {str1[i]} != {str2[i]} ✗")

    max_len = max(len(str1), len(str2))

    similarity = (matches / max_len) * 100

    print("\n----- RESULT -----")
    print("String 1:", str1)
    print("String 2:", str2)
    print("Matching Characters:", matches)
    print("Mismatched Positions:", mismatches)
    print("Similarity Percentage:", round(similarity, 2), "%")

    if similarity == 100:
        print("Perfect Match")
    elif similarity >= 75:
        print("High Similarity")
    elif similarity >= 50:
        print("Moderate Similarity")
    else:
        print("Low Similarity")


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

string_matching(str1, str2)