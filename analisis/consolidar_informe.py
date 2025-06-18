import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def consolidar_informe(lista_respuestas):
    # Construimos un prompt que contiene todo lo obtenido para que la IA lo sintetice y valide
    prompt_final = "Eres un experto analista OSINT. Has recibido los siguientes datos extraídos de imágenes de un perfil. Valida, compara, corrige inconsistencias y sintetiza toda la información para generar un INFORME FINAL COMPLETO y bien estructurado, destacando ubicaciones, nombres, relaciones, mascotas, marcas, profesiones, estilo de vida y cualquier detalle relevante.\n\n"
    for i, resp in enumerate(lista_respuestas):
        prompt_final += f"Datos imagen {i+1}:\n{resp}\n\n"
    prompt_final += "\nElabora un informe coherente, organizado y sin repetir información. Usa secciones claras."

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_final
                    }
                ]
            }
        ]
    }

    headers = { "Content-Type": "application/json" }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()

        resultado = response.json()
        texto = resultado["candidates"][0]["content"]["parts"][0]["text"]
        return texto

    except Exception as e:
        return f"Error consolidando informe: {str(e)}"

