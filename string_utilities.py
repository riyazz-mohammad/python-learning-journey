def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count

def count_words(text):
    words=text.split()
    return len(words)

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    cleaned=text.lower().replace(" ","")
    return cleaned==cleaned[::-1]

def capitalize_words(text):
    return text.title()

print("=== STRING UTILITIES ===")
user_text = input("Enter a sentence: ")

print(f"\nVowels: {count_vowels(user_text)}")
print(f"Words: {count_words(user_text)}")
print(f"Reversed: {reverse_string(user_text)}")
print(f"Is Palindrome: {is_palindrome(user_text)}")
print(f"Capitalized: {capitalize_words(user_text)}")


test_words=["radar", "hello", "level", "python", "madam"]
print("==Palindrome Test==")

for word in test_words:
    result="Yes" if is_palindrome(word) else "No"
    print(f"{word}:{result}")

    

    