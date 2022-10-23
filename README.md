# pdf-ocr-stack
* This stack is designed to facilitate the retrieval of texts from pdfs so that they can be used as needed.

## Objective
* The purpose of this stack is to make it easier for you to get data from PDFs for general processing. It will be the basis to assist in simple OCR projects where there will be more fixed PDF templates.

## Prerequisites
* As a prerequisite the user needs a valid PDF to be processed.

## How to use
* Run the commands above to create the ambient:
```bash
python -m venv venv
. ./venv/Scripts/activate
python -m pip install --upgrade pip
pip install PyPDF2
```
* Insert the PDF file to be processed in the files folder.
* Insert the PDF file to be processed in the files folder.
* Now just run the main.py file and check the result in the output.txt file that will be created in the processed_files folder.
```bash
python main.py
```