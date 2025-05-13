from deep_translator import GoogleTranslator
import sys
import os

if len(sys.argv) < 2:
    print("Uso: python translate_block.py <arquivo_entrada>")
    sys.exit(1)

input_file = sys.argv[1]
if not os.path.exists(input_file):
    print(f"Arquivo não encontrado: {input_file}")
    sys.exit(1)

output_file = input_file.replace("texto_", "traduzido_")

with open(input_file, "r", encoding="utf-8") as f:
    original_text = f.readlines()

translated_lines = []
translator = GoogleTranslator(source='en', target='pt')
for line in original_text:
    if line.strip():
        try:
            translated = translator.translate(line.strip())
            translated_lines.append(translated + "\n")
        except Exception as e:
            translated_lines.append(f"[Erro: {e}]\n")
    else:
        translated_lines.append("\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(translated_lines)

print(f"Tradução salva em: {output_file}")