# Open the news article file
with open("news_article.txt", "r") as file:
    text = file.read()

while True:
    word = input("Enter a word to count (or type 'quit' to exit): ")
    
    if word.lower() == "quit":
        print("Exiting program.")
        break
    
    count = text.count(word)
    
    if count > 0:
        print(f"The word '{word}' appears {count} times.")
    else:
        print(f"The word '{word}' was not found in the text.")
