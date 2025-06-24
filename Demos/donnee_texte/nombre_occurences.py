import string

def count_words_in_file(file_path):
    word_counts = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            # Remove punctuation and convert to lowercase
            text = text.translate(str.maketrans('', '', string.punctuation)).lower()

            # Split text into words
            words = text.split()

            # Count word occurrences
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

        return word_counts

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

counts = count_words_in_file("sample.txt")
print(counts)
