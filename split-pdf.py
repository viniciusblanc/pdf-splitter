from pikepdf import Pdf

pdf = Pdf.open('Certificados.pdf')

for n, page in enumerate(pdf.pages):
    dst = Pdf.new()
    dst.pages.append(page)
    dst.save(f'Certificado{n+1:02d}.pdf')
