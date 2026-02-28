from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
import base64
import os



def convert_signature_base64 (signature_base64):

    if not signature_base64:
        return None

    if "," in signature_base64:
        signature_base64 = signature_base64.split(",")[1]
    
    signature_bytes = base64.b64decode(signature_base64)
    
    path = os.path.join("static", "signature.png")
    
    with open(path, "wb")as f:
        f.write(signature_bytes)

    return path


def add_header_footer(canvas, doc):
    header(canvas, doc)
    footer(canvas, doc)


def header(canvas, doc):
    
    A4width, A4height = A4
    
    canvas.drawImage(
        "static\header.png",
        0,
        A4height - 197 ,
        width = 590,
        height = 300,
        mask = 'auto'
        
    )
    
def footer (canvas, doc):
    A4width, A4height = A4
    canvas.drawImage(
        "static\\footer.png",
        0,
        0,
        width = A4width,
        height = 80,
        mask='auto'
    )   
    