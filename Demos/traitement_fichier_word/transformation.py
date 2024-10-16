from docx import Document
#pip install python-docx

def capitalize_after_period(text):
    new_text = ''
    capitalize = True  # La première lettre doit être mise en majuscule

    for char in text:
        if capitalize and char.isalpha():
            new_text += char.upper()
            capitalize = False
        else:
            new_text += char
        if char == '.':
            capitalize = True  # True pour mettre en majuscule après le point
    
    return new_text

def process_word_file(input_path, output_path):
    # Ouverture du fichier Word
    doc = Document(input_path)
    
    # Itération sur chaque paragraphe pour appliquer les transformations
    for para in doc.paragraphs:
        para.text = capitalize_after_period(para.text)
    
    # Sauvegarde des modifications
    doc.save(output_path)


input_file = r"D:\Users\Amine\Prgm\Python\Python.Bureautique\Demos\traitement_fichier_word\input.docx"
output_file = r"D:\Users\Amine\Prgm\Python\Python.Bureautique\Demos\traitement_fichier_word\output.docx"
# Transformation du fichier
process_word_file(input_file, output_file)
print(f'Le fichier {output_file} a été généré')
