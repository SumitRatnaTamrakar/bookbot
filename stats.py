def words_counter(text_from_book):
    words = text_from_book.split()
    words_count = len(words)
    return words_count

def characters_counter(text_from_book):
    words = text_from_book.split()
    char_counts = {}

    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char in char_counts:
                char_counts[lower_char] += 1
            else:
                char_counts[lower_char] = 1
    
    return char_counts

def sort_on(items):
    return items["num"]

def create_char_num_dictionary(num_chars):
    char_num_dictionary_array = []
    for key, value in num_chars.items():
        char_num_instance = {"char": key, "num": value}
        char_num_dictionary_array.append(char_num_instance)
        char_num_dictionary_array.sort(reverse = True, key = sort_on)

    return char_num_dictionary_array
