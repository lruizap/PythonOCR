from PIL import Image
import pytesseract

# List of languages
print(pytesseract.get_languages(config='.'))

img = Image.open("../media/img/others/esto_es_un_texto.jpg")
img.load()

# Specify language to look after!
text = pytesseract.image_to_string(img, lang="spa")

print(text)
