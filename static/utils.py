from reportlab.lib.pagesizes import A4
import base64
import os
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')


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
        "static\\header.png",
        0,
        A4height - 197 ,
        width = 589,
        height = 300,
        mask = 'auto'
        
    )
    
def footer (canvas, doc):
    A4width, A4height = A4
    canvas.drawImage(
        "static\\footer.png",
        0,
        0,
        width = A4width - 1,
        height = 80,
        mask='auto'
    )   

def get_date():

    data = datetime.now()

    day = data.day
    month = data.strftime("%B")
    year = data.year

    month_encode = month.encode('utf-8')
    month = month_encode.decode('utf-8', errors='replace')

    return day, month, year


