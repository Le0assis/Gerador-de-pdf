from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import cm
from assets.utils import convert_signature_base64, add_header_footer
import io



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Declaracao-de-contraste.html")



@app.route("/gerar", methods=["POST"])

def gerar_pdf():
    
    elements = []
    name = request.form["name"]
    signature = convert_signature_base64( request.form["signature"])

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        topMargin=4*cm,
        bottomMargin=3*cm
    )

   
    
    title_style = ParagraphStyle(
        name="TituloPersonalizado",
        fontName="Helvetica-BoldOblique",  
        fontSize=24,                      
        alignment=TA_CENTER,                      
    )
    text_style = ParagraphStyle(
        name="TextoEsilizado",
        fontSize=14,                      
        alignment=TA_CENTER,  
    )


    title = "Declaração"
    
    text = f"""Eu {name} declaro que fui submetido(a) ao
        exame de imagem, com uso de contraste, conforme solicitação médica.
        Estou ciente que, de acordo com as condutas médicas e protocolos de radiologia, além do
        médico solicitante, também é de responsabilidade do médico radiologista indicar a
        utilização de contraste, a fim de garantir uma melhor definição das imagens e um
        diagnóstico preciso."""
    
    signature = Image("signature.png", width=6*cm,  height=2*cm)
   
    signature_text = "Assinatura do paciente"
    
        
    data = [
        [signature],
        [signature_text]
    ]
    
    signature_table = Table(data, colWidths=300)
    signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LINEABOVE', (0, 1), (-1, 1), 1, colors.black)  # linha acima do texto
    ]))
    elements.append(Spacer(1, 2*cm)) 
    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph(text, text_style))
    elements.append(Spacer(1, 2*cm)) 
    elements.append(signature_table)
    
    doc.build(
        elements,
        onFirstPage=add_header_footer,
        onLaterPages=add_header_footer
    )
    
    buffer.seek(0)
    
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"{name}.pdf",
        mimetype="application/pdf"
    )
    
if __name__ == "__main__":
    app.run(debug=True)
    
    