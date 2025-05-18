def count_words(current_book):
    raw_words = current_book.split()
    return len(raw_words)   

def count_chars(current_book):
    char_dict = {}
    
    for char in current_book.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]

def letter_sort(char_count):
    final_dict_list = []

    for letter, count in char_count.items():
        if letter.isalpha():
            temp_dict = {"char": letter, "num":count}
            final_dict_list.append(temp_dict)
        
        final_dict_list.sort(key=sort_on, reverse=True)
    
    return final_dict_list

