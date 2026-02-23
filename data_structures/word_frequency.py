def count_words(text):
    words=text.lower().split()

    word_count={}
    for word in words:
        word=word.strip(":;!.?")
        word_count[word]=word_count.get(word,0)+1
    return word_count

def display_frequencies(word_count,top_n=10):
    sorted_words=sorted(word_count.items(),key=lambda x:x[1],reverse=True)

    print(f"\n==Top {top_n} Words==")
    for word,count in sorted_words[:top_n]:
        print(f"{word}:{count}")

def get_statistics(word_count):
    total_words=sum(word_count.values())
    unique_words=len(word_count)
    most_common=max(word_count.items(),key=lambda x:x[1])
    print("\n=== TEXT STATISTICS ===")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Most common word: '{most_common[0]}' ({most_common[1]} times)")

# Sample text
sample_text = """
Python is a high-level programming language. Python is easy to learn.
Python is widely used for web development, data science, and automation.
Many programmers love Python because Python is versatile and powerful.
"""

print("=== WORD FREQUENCY COUNTER ===")
print("\nAnalyzing sample text...")

word_count = count_words(sample_text)
display_frequencies(word_count)
get_statistics(word_count)

# User input option
print("\n" + "="*50)
user_choice = input("\nAnalyze your own text? (yes/no): ")

if user_choice.lower() == "yes":
    print("Enter your text (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    user_text = " ".join(lines)
    user_count = count_words(user_text)
    display_frequencies(user_count)
    get_statistics(user_count)

