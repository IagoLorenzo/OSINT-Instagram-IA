import os
from analisis.analizar_imagen import analizar_imagen
from analisis.consolidar_informe import consolidar_informe
from pdf_utils import guardar_informe_pdf  # Función para crear PDF, te la paso abajo

def main():
    carpeta = "perfiles_descargados/imagenes"
    imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith((".jpg", ".png"))]

    respuestas = []

    for imagen in imagenes:
        ruta = os.path.join(carpeta, imagen)
        print(f"Analizando imagen: {imagen}")
        respuesta = analizar_imagen(ruta)
        print("➡️ Resultado resumido:")
        print(respuesta[:500], "...\n")  # Muestra solo lo primero
        respuestas.append(respuesta)

    print("\nGenerando informe consolidado...\n")
    informe_final = consolidar_informe(respuestas)

    if informe_final.startswith("ERROR"):
        print(informe_final)  # En caso de error en consolidación
    else:
        nombre_informe_pdf = "informe_osint_completo.pdf"
        guardar_informe_pdf(informe_final, nombre_informe_pdf)
        print(f"Informe final generado y guardado en: {nombre_informe_pdf}")

if __name__ == "__main__":
    main()

