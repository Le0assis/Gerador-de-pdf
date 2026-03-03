from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.lib.units import cm
from static.utils import convert_signature_base64, add_header_footer, get_date
from generator.contraste import gerar_pdf as gerar_contraste
import io
import os


app = Flask(__name__)

BUILDERS = {
    "declaracao-de-contraste": gerar_contraste
}

@app.route("/")
def home():

    templates = "templates"

    archives = os.listdir(templates)
    documents = []

    for archive in  archives:
        if archive.endswith(".html") and archive != "home.html":
            name = archive.replace(".html", "")
            documents.append(name)
    
    return render_template("home.html", documents=documents)

@app.route("/documento/<type>", methods=["GET", "POST"])
def documento(type):

    if type not in BUILDERS:
        return f""" Documento não encontrado
                    TIPO RECEBIDO: {type}
                    CHAVES DISPONIVEIS {BUILDERS.keys()}""", 404

    if request.method == "POST":
        dados = request.form.to_dict()
        return BUILDERS[type](dados)

    return render_template(f"{type}.html")


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)