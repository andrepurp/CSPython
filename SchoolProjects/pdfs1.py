from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

pdf = canvas.Canvas("teste.pdf")
utilizadores=["João", "Maria", "Pedro", "Ana"]
ips=['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
tipos=['Privado', 'Público', 'Privado', 'Público']
dados=[]


y=750
total=300
pdf.setFont("Helvetica-Bold", 18)
pdf.drawCentredString(297,750, 'Relatório de Segurança')
pdf.line(100,735,500,735)
y=700
pdf.drawString()
