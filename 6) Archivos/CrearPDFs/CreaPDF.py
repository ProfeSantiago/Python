#-------------------------------------------------------
#    Para este ejercicio hay que correr estos comandos desde el Terminal o Consola:
#
#    pip install --upgrade pip
#    python -m pip install fpdf
#-------------------------------------------------------

from fpdf import FPDF

def creaPDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Al Infinito y mas alla!", ln=1, align="C")
    pdf.output("miPrimerPDF.pdf")

def creaPDF2():
    pdf = FPDF(orientation='P', unit='mm', format='letter')
    pdf`.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(100, 10, txt="Al Infinito y mas alla!", ln=1, align="L")
    pdf.cell(200, 20, txt="El espacio, la frontera final", ln=2, align="R")
    pdf.output("SegundoPDF.pdf")

def main():
    creaPDF()
    creaPDF2()

main()