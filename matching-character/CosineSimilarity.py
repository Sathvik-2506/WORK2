import math
from collections import Counter

def cosine_similarity(text1, text2):
    """Calculate cosine similarity between two texts."""
    # Create frequency vectors
    vec1 = Counter(text1.lower().split())
    vec2 = Counter(text2.lower().split())
    
    # Get all unique words
    all_words = set(vec1.keys()) | set(vec2.keys())
    
    if not all_words:
        return 0.0
    
    # Calculate dot product
    dot_product = sum(vec1[word] * vec2[word] for word in all_words)
    
    # Calculate magnitudes
    mag1 = math.sqrt(sum(count ** 2 for count in vec1.values()))
    mag2 = math.sqrt(sum(count ** 2 for count in vec2.values()))
    
    if mag1 == 0 or mag2 == 0:
        return 0.0
    
    # Calculate cosine similarity
    return dot_product / (mag1 * mag2)

if __name__ == "__main__":
    print("=== Cosine Similarity Calculator ===")
    text1 = input("Enter first text: ")
    text2 = input("Enter second text: ")
    
    similarity = cosine_similarity(text1, text2)
    print(f"\nCosine Similarity: {similarity:.2f}")
