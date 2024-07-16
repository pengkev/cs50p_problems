from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Courier","B",24)
pdf.cell(50,40,align = 'C')
pdf.cell(text="CS50 Shirtificate")
pdf.cell(-190,0,align = 'C')
pdf.ln(40)
pdf.image("shirtificate.png",w=191,keep_aspect_ratio=True)
pdf.set_y(0)
pdf.set_font("Helvetica","B",16)
pdf.set_text_color(255,255,255)
pdf.set_y(150)
pdf.set_x(85)
pdf.cell(40,40,text=f"{input("Name: ")} took CS50",align='C')
pdf.output("shirtificate.pdf")

