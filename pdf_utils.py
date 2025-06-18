from markdown2 import markdown
from xhtml2pdf import pisa

def guardar_informe_pdf(texto_markdown, nombre_archivo_pdf):
    html = markdown(texto_markdown)
    with open(nombre_archivo_pdf, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)
    return not pisa_status.err

