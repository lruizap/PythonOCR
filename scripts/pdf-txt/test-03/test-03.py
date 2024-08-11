
# PyMuPDF
import fitz

import pytesseract

import os

# Ruta al archivo PDF
pdf_path = '../../../media/docs/jpegfile.pdf'

# Abrir el documento
doc = fitz.open(pdf_path)

# crear carpeta para guardar imagenes
if os.path.exists("./pages-img") and os.path.isdir("./pages-img"):
    print("La carpeta ya existe\nGuardando datos...")
else:
    print("Creando la carpeta\nGuardando datos...")
    os.makedirs("./pages-img/")

# Iterar por las páginas
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    pix = page.get_pixmap()

    # Guardar la imagen
    pix.save(f'./pages-img/page_{page_num + 1}.png')

# Cerrar el documento
doc.close()


# Guardamos el texto en un fichero:
fp = open('pdf-txt.txt', 'w+')
for page in os.listdir("./pages-img"):
    if page.endswith(".png"):
        # Pasa la imagen por pytesseract
        text = pytesseract.image_to_string(f"./pages-img/{page}", lang="spa")
        fp.write(text)

print("Documento completado!")

fp.close()
