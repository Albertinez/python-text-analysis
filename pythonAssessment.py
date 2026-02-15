import string
from collections import Counter


# -----------------------------
# Function 1: Count Specific Word
# -----------------------------
def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0

    # Normalize text
    text = text.lower()
    search_word = search_word.lower()

    words = text.split()
    count = 0

    for word in words:
        word = word.strip(string.punctuation)
        if word == search_word:
            count += 1

    return count


# -----------------------------
# Function 2: Identify Most Common Word
# -----------------------------
def identify_most_common_word(text):
    if not text.strip():
        return None

    text = text.lower()
    words = text.split()

    clean_words = [
        word.strip(string.punctuation)
        for word in words
        if word.strip(string.punctuation)
    ]

    word_counts = Counter(clean_words)
    most_common = word_counts.most_common(1)

    return most_common[0][0] if most_common else None


# -----------------------------
# Function 3: Calculate Average Word Length
# -----------------------------
def calculate_average_word_length(text):
    if not text.strip():
        return 0

    words = text.split()

    clean_words = [
        word.strip(string.punctuation)
        for word in words
        if word.strip(string.punctuation)
    ]

    total_length = sum(len(word) for word in clean_words)
    total_words = len(clean_words)

    return total_length / total_words if total_words > 0 else 0


# -----------------------------
# Function 4: Count Paragraphs
# -----------------------------
def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = text.split("\n\n")
    clean_paragraphs = [p for p in paragraphs if p.strip()]

    return len(clean_paragraphs)


# -----------------------------
# Function 5: Count Sentences
# -----------------------------
def count_sentences(text):
    if not text.strip():
        return 1

    sentence_endings = ".!?"
    count = 0

    for char in text:
        if char in sentence_endings:
            count += 1

    return count


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    try:
        with open("news_article.txt", "r", encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        print("Error: news_article.txt not found.")
        return

    print("\n--- NEWS ARTICLE ANALYSIS ---\n")

    # Count specific word
    word_to_search = input("Enter a word to count: ")
    word_count = count_specific_word(article, word_to_search)
    print(f"\nThe word '{word_to_search}' appears {word_count} times.")

    # Most common word
    most_common = identify_most_common_word(article)
    print(f"Most common word: {most_common}")

    # Average word length
    avg_length = calculate_average_word_length(article)
    print(f"Average word length: {avg_length:.2f}")

    # Paragraph count
    paragraphs = count_paragraphs(article)
    print(f"Number of paragraphs: {paragraphs}")

    # Sentence count
    sentences = count_sentences(article)
    print(f"Number of sentences: {sentences}")


if __name__ == "__main__":
    main()
