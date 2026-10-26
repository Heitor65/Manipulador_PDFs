import pikepdf
from pdf2image import convert_from_path

def turn_pdf_2_png(pdf_path):

	images = convert_from_path(pdf_path)

	for i, img in enumerate(images):
		img.save(f"pagina_{i+1}.png", "PNG")

def turn_up_side_down(pdf_path):
	with pikepdf.Pdf.open(pdf_path) as pdf:
		for page in pdf.pages:
			page.rotate(180, relative=True) # Gira 180° em relação à orientação atual
		pdf.save('rotated.pdf')