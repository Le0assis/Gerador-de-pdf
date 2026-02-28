from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
import base64



def convert_signature_base64 (signature_base64):

    signature_base64 = signature_base64.split(",")[1]
    signature_bytes = base64.b64decode(signature_base64)
    
    with open("signature.png", "wb")as f:
        f.write(signature_bytes)

    return "assets\\signature.png"


def add_header_footer(canvas, doc):
    header(canvas, doc)
    footer(canvas, doc)


def header(canvas, doc):
    
    A4width, A4height = A4
    
    canvas.drawImage(
        "assets\header.png",
        0,
        A4height -3*cm,
        width = 21*cm,
        height = 3*cm
    )
    
def footer (canvas, doc):
        
    canvas.drawImage(
        "assets\\footer.png",
        0,
        0,
        width = 21*cm,
        height = 2*cm
    )   
    