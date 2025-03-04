def get_file_text(path_to_file):
    file_text = ""
    with open(path_to_file) as f:
        file_text = f.read()
    return file_text

def get_num_words(file_string):
    word_list = file_string.split()
    return len(word_list)

def get_character_count(file_string):
    character_count = {}
    file_string = file_string.lower()
    for c in file_string:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count

def sort_on(dict):
    return dict["num"]
# Takes the dictionary of characters:occurances and returns a sorted list of dictionaries 
def sorted_list(dict):
    
    new_list = []
    for c in dict:
        new_list.append(
            {"char": c, "num": dict[c]}
        )

    new_list.sort(reverse=True, key=sort_on)
    return new_list


    