str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

def jaccard_similarity(str1, str2):
    set1 = set(str1.strip().lower().replace(" ", ""))
    set2 = set(str2.strip().lower().replace(" ", ""))

    if not set1 or not set2:
        print("One of the strings is empty!")
        return

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    similarity = (len(intersection) / len(union)) * 100

    print("\n----- RESULT -----")
    print("String 1:", str1)
    print("String 2:", str2)
    print("Jaccard Similarity:", round(similarity, 2), "%")

    if similarity == 100:
        print("Perfect Match")
    elif similarity >= 75:
        print("High Similarity")
    elif similarity >= 50:
        print("Moderate Similarity")
    else:
        print("Low Similarity")

jaccard_similarity(str1, str2)