def countNumberOfWords(book: str):
    numberOfWords = book.split()
    
    return len(numberOfWords)  

def countCharacters(text):
    # Contar la cantidad de cada carácter
    char_count = {}
    for char in text:
        if char.isalpha():  # Solo contar caracteres alfabéticos
            char = char.lower()  # Convertir a minúsculas para contar correctamente
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(character_dict):
    return character_dict["num"]


def chars_sorted_list(num_characters):
    sorted_list = []
    for character in num_characters:
        sorted_list.append({"char": character, "num": num_characters[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list