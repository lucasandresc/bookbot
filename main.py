from stats import countCharacters, countNumberOfWords, chars_sorted_list
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    try:
        with open(path) as f:
            file_contents = f.read()
            numbers_of_words = countNumberOfWords(file_contents)
            number_of_characters = countCharacters(file_contents)
            sorted_characters = chars_sorted_list(number_of_characters)
            
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {path}")
            print("------------ Word Count -----------")
            print(f"Found {numbers_of_words} total words")
            print("---------- Character Count --------")
            
            # Imprimir el resultado
            for character in sorted_characters:
                print(f"{character['char']}: {character['num']}")
    
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no se encontró.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()
