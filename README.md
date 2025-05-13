# PDF OCR Translator

Este projeto realiza **extração de texto (OCR)** de arquivos PDF e tradução automática para o português utilizando **Tesseract OCR** e a API do Google Translate (via deep-translator), com suporte completo ao Docker.

## Funcionalidades

- Divide arquivos PDF em blocos de páginas.
- Extrai o texto de cada página via OCR com Tesseract.
- Traduz automaticamente o conteúdo extraído para o português.
- Gera arquivos .txt com o resultado de cada bloco.
- Tudo pode ser executado via Docker, sem necessidade de configurar o ambiente manualmente.


## Executando com Docker

### 1. Clone o repositório
bash
git clone https://github.com/joaomarafiotti/pdf-ocr-translator.git
cd pdf-ocr-translator

### 2. Coloque seu PDF na pasta `input/`
> Exemplo: `input/sample.pdf`

### 3. Construa a imagem Docker
bash
docker build -t pdf-ocr .

### 4. Execute o contêiner para extrair o texto (OCR)
docker run -v "$PWD:/app" pdf-ocr

### 5. Traduzir um bloco específico
docker run -v "$PWD:/app" pdf-ocr python translate_block.py blocos_ocr/texto_001_050.txt


## Estrutura do Projeto
pdf-ocr-translator/
main_ocr.py               # Extração de texto via OCR
translate_block.py        # Tradução de arquivos extraídos
Dockerfile                # Ambiente Docker automatizado
requirements.txt          # Dependências Python
input/                    # PDF de entrada (ex: sample.pdf)
blocos_ocr/               # Arquivos .txt gerados com os textos

## Tecnologias Usadas
Python 3.10
Tesseract OCR
Poppler-utils
PDF2Image
Deep-Translator
Docker
