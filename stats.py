def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return(file_contents)


def word_count(returned_contents):
    split_words = returned_contents.split()
    words = len(split_words)
    return(words)

def repeat_chars(returned_contents):
    stored_chars = {}

    lowered_chars = returned_contents.lower()

    for chars in lowered_chars:
        if chars in stored_chars:
            stored_chars[chars] += 1
        else:
            stored_chars[f"{chars}"] = 1
    
    return(stored_chars)

def sorted_dict(num_chars):
    num_list = []
    for char, count in num_chars.items():
        num_list.append({'char': char, 'num': count})
    
    num_list.sort(reverse=True, key=lambda item: item["num"])
    return(num_list)