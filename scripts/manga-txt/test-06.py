import cv2
import easyocr

# Idioma de lectura
reader = easyocr.Reader(["es"], gpu=False)

# Leer la imagen
image_path = '../../media/img/manga/op-test-01.jpg'
image = cv2.imread(image_path)

# Comprobar si la imagen existe
if image is None:
    print(f"Error: No se pudo leer la imagen desde {image_path}")
else:
    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para convertir la imagen a binaria
    threshold_img = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Leer texto
    result = reader.readtext(threshold_img)

    for res in result:
        print("Resultado: ", res)
        bbox, text, confidence = res

        # Convertir coordenadas de bounding box a enteros
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
