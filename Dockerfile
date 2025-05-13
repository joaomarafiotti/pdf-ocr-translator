# Imagem base com Python
FROM python:3.10-slim

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && apt-get clean

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos para dentro do contêiner
COPY . .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão: executar OCR em input/sample.pdf (se existir)
CMD ["python", "main_ocr.py", "input/sample.pdf"]