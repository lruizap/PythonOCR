# documentación: https://www.jaided.ai/easyocr/

import cv2
import easyocr

# Idioma de lectura
reader = easyocr.Reader(["es", "en", "pt"], gpu=False)

# Leer la imagen
image_path = '../../media/img/others/el-puente-internacional-tancredo-nevez.jpg'
image = cv2.imread(image_path)

# Comprobar si la imagen existe
if image is None:
    print(f"Error: Could not read the image from {image_path}")
else:
    # Leer texto
    result = reader.readtext(image)

    for res in result:
        print("res: ", res)
        pt0 = res[0][0]
        pt1 = res[0][1]
        pt2 = res[0][2]
        pt3 = res[0][3]

        cv2.rectangle(image, pt0, (pt1[0], pt1[1] - 23), (166, 56, 242), -1)
        cv2.putText(image, res[1], (pt0[0], pt0[1]-3),
                    2, 0.8, (255, 255, 255), 1)

        cv2.rectangle(image, pt0, pt2, (166, 56, 242), 2)

        cv2.circle(image, pt0, 2, (255, 0, 0), 2)
        cv2.circle(image, pt1, 2, (0, 255, 0), 2)
        cv2.circle(image, pt2, 2, (0, 0, 255), 2)
        cv2.circle(image, pt3, 2, (0, 255, 255), 2)

        cv2.imshow("Image", image)
        cv2.waitKey(0)

cv2.destroyAllWindows()
