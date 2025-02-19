def main():
    book_path = "books/frankenstein.txt"

    def get_num_words(text):
        words = text.split()
        return len(words)


    def get_book_text(path):
        with open(path) as f:
            return f.read()

    def get_num_chars(text):
        chars = {}
        for char in text:
            if char.isalpha():
              char = char.lower()    
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        return chars
        
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document\n")

    num_char = get_num_chars(text)

    for char, count in num_char.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")     

main()
