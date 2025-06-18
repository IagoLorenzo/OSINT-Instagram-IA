import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

PROMPT_OSINT = """
Eres un experto en OSINT. Analiza detalladamente esta imagen y extrae TODO dato útil para perfilar a la persona mostrada: ubicaciones, nombres, relaciones personales, mascotas, marcas, texto legible, cualquier pista identificable. 
Incluye detalles como nombres de familiares, profesión, estilo de vida, aficiones, ubicaciones aproximadas, y cualquier dato que pueda servir para inteligencia humana. 
Devuelve un texto detallado pero claro, sin nada irrelevante. 
Si no ves información útil, indícalo claramente.
"""

def analizar_imagen(path):
    try:
        with open(path, "rb") as f:
            image_bytes = f.read()
        mime_type = "image/png" if path.endswith(".png") else "image/jpeg"
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "inlineData": {
                                "mimeType": mime_type,
                                "data": image_base64
                            }
                        },
                        {
                            "text": PROMPT_OSINT
                        }
                    ]
                }
            ]
        }

        headers = { "Content-Type": "application/json" }
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()

        resultado = response.json()
        texto = resultado["candidates"][0]["content"]["parts"][0]["text"]
        return texto

    except Exception as e:
        return f"Error analizando {path}: {str(e)}"

