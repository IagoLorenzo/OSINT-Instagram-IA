# Proyecto OSINT con imágenes

Este proyecto analiza imágenes descargadas, aplicando técnicas de inteligencia artificial con Gemini de Google AI Studio. Extrae información relevante como ubicaciones, relaciones personales, marcas, estilo de vida y mucho más.

## Estructura
- `analisis/`: lógica de análisis con Gemini.
- `pdf_utils.py`: generación automática de informes en PDF.
- `main.py`: ejecución principal del programa.

## Uso
1. Coloca imágenes en `perfiles_descargados/imagenes/`.
2. Ejecuta `python3 main.py`.
3. El informe se guarda como `informe_osint_completo.pdf`.

¡El archivo `.env` debe contener tu clave de API de la siguiente manera!:

GEMINI_API_KEY= "substituye por tu API key"

