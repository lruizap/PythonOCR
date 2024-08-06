# OCR

## Introducción

En este repositorio estarán las pruebas de código para aprender a usar OCR (Reconocimiento Óptico de Caracteres) utilizando herramientas como Tesseract y su envoltura en Python, pytesseract. El objetivo principal de este proyecto es proporcionar ejemplos prácticos y explicaciones detalladas sobre cómo implementar OCR en Python, incluyendo la instalación de dependencias, el procesamiento de imágenes y la extracción de texto.

## Requisitos de Software

1. **Python**
   - Versión recomendada: 3.6 o superior.

2. **Tesseract OCR**
   - Motor de OCR necesario para la extracción de texto.
   - **Instalación**: Debes instalar el software Tesseract OCR en tu sistema operativo. Se puede descargar desde el [repositorio de Tesseract OCR](https://github.com/tesseract-ocr/tesseract) o instalar a través de un gestor de paquetes.

3. **pytesseract**
   - Wrapper de Python para usar Tesseract OCR.
   - **Instalación**: `pip install pytesseract`.

4. **OpenCV**
   - Biblioteca para el procesamiento de imágenes.
   - **Instalación**: `pip install opencv-python`.

5. **Pillow (PIL)**
   - Biblioteca de imágenes para Python, útil para cargar y manipular imágenes.
   - **Instalación**: `pip install pillow`.

### Requisitos del Sistema

1. **Sistema Operativo**
   - Tesseract OCR es compatible con Windows, macOS y Linux.

2. **Dependencias del Sistema**
   - **Windows**: Es posible que necesites instalar Visual C++ Redistributable.
   - **Linux**: Los comandos para instalar Tesseract pueden variar según la distribución (por ejemplo, `sudo apt-get install tesseract-ocr` en Ubuntu).

3. **Fuentes de Datos**
   - Archivos de imágenes: Tesseract y pytesseract trabajan con imágenes como entrada. Los formatos comunes incluyen PNG, JPEG, BMP, etc.

4. **Archivos de Idioma de Tesseract**
   - Archivos `.traineddata` que contienen modelos de reconocimiento para diferentes idiomas. Se pueden descargar adicionalmente si necesitas soporte para idiomas específicos.

### Recomendaciones

1. **Conocimientos en Python**
   - Familiaridad con conceptos básicos de Python y manejo de paquetes.

2. **Conocimientos en Procesamiento de Imágenes**
   - Comprensión básica de técnicas de preprocesamiento de imágenes, como la conversión a escala de grises y la binarización, para mejorar la precisión del OCR.

3. **Acceso a Documentación y Recursos**
   - Es útil tener acceso a documentación y ejemplos de Tesseract y pytesseract para facilitar la resolución de problemas y mejorar el rendimiento del OCR.

### Ejemplo de Comandos de Instalación

```sh
# Instalar librerías
pip install -r requirements.txt
```
