import cv2
import easyocr
from PIL import Image
import pytesseract
import numpy as np


def preprocess_image(image_path):
    """Carga y preprocesa la imagen para mejorar la extracción de texto."""
    # Leer la imagen
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(
            f"Error: No se pudo leer la imagen desde {image_path}")

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral adaptativo para binarizar la imagen
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return image, thresh


def detect_text_with_easyocr(image):
    """Usa EasyOCR para detectar texto en la imagen."""
    reader = easyocr.Reader(["en"], gpu=False)
    results = reader.readtext(image)
    return results


def display_results(image, results):
    """Dibuja los resultados en la imagen y muestra la imagen."""
    for res in results:
        bbox, text, confidence = res

        # Convertir coordenadas a enteros
        (pt0, pt1, pt2, pt3) = bbox
        pt0 = tuple(map(int, pt0))
        pt1 = tuple(map(int, pt1))
        pt2 = tuple(map(int, pt2))
        pt3 = tuple(map(int, pt3))

        # Dibujar rectángulo alrededor del texto detectado
        cv2.rectangle(image, pt0, pt2, (166, 56, 242), 2)

        # Fondo para el texto
        cv2.rectangle(image, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)

        # Añadir el texto detectado
        cv2.putText(image, text, (pt0[0], pt0[1] - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Opcional: marcar las esquinas del bounding box
        cv2.circle(image, pt0, 2, (255, 0, 0), 2)
        cv2.circle(image, pt1, 2, (0, 255, 0), 2)
        cv2.circle(image, pt2, 2, (0, 0, 255), 2)
        cv2.circle(image, pt3, 2, (0, 255, 255), 2)

    # Mostrar la imagen
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_text_to_file(results, output_path):
    """Guarda el texto detectado en un archivo de texto."""
    with open(output_path, 'w', encoding='utf-8') as file:
        for res in results:
            text = res[1]  # El texto extraído
            file.write(f"{text}\n")


def main():
    image_path = '../../media/img/others/water.jpg'
    output_text_path = 'output_text.txt'

    # Preprocesar la imagen
    image, preprocessed_image = preprocess_image(image_path)

    # Detectar texto usando EasyOCR
    results = detect_text_with_easyocr(preprocessed_image)

    # Mostrar los resultados
    display_results(image, results)

    # Guardar el texto en un archivo
    save_text_to_file(results, output_text_path)
    print(f"Texto guardado en {output_text_path}")


if __name__ == "__main__":
    main()
