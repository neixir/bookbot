def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    text = text.lower()
    report = {}
    
    for c in text:
        if c in report:
            report[c] += 1
        else:
            report[c] = 1

    return report

def sort_on(dict):
    return dict['num']

def get_sorted_list(input_dict):
    characters = []

    for char in input_dict:
        new_char = {}
        new_char['char'] = char
        new_char['num'] = input_dict[char]
        characters.append(new_char)
    
    characters.sort(reverse=True, key=sort_on)
    return characters

