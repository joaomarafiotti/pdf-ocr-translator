# Imagem base com Python
FROM python:3.10-slim

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && apt-get clean