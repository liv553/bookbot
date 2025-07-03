def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    characters = {}
    for char in lower_text:
        if char in characters:
            characters[char]+=1
        else:
            characters[char]=1
    return characters

def sort_on(d):
    return d["num"]

def sort_list(count_characters_var):
    sorted_list = []
    for char, num in count_characters_var.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
