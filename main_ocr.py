from pdf2image import convert_from_path
import pytesseract
import os
import sys

# >>>>> CAMINHO DO PDF VIA ARGUMENTO <<<<<
if len(sys.argv) < 2:
    print("Uso: python main_ocr.py <nome_do_pdf>")
    sys.exit(1)

pdf_path = sys.argv[1]

# Descobre número de páginas automaticamente
from PyPDF2 import PdfReader
reader = PdfReader(pdf_path)
total_pages = len(reader.pages)

pages_per_block = 50
output_dir = "blocos_ocr"
os.makedirs(output_dir, exist_ok=True)

for start in range(1, total_pages + 1, pages_per_block):
    end = min(start + pages_per_block - 1, total_pages)
    print(f"Processando páginas {start} a {end}...")

    images = convert_from_path(pdf_path, first_page=start, last_page=end)
    all_text = ""
    for i, img in enumerate(images):
        page_number = start + i
        text = pytesseract.image_to_string(img, lang='eng')
        all_text += f"\n\n--- Página {page_number} ---\n\n{text}"

    output_name = f"{output_dir}/texto_{str(start).zfill(3)}_{str(end).zfill(3)}.txt"
    with open(output_name, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"Salvo: {output_name}")

print("OCR Finalizado!")