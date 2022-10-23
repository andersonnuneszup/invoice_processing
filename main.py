import PyPDF2


if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    # create file object variable
    # opening method will be rb
    # pdffileobj=open('C:\\Users\\ander\\workspace-python\\ocr-stack\\files\\file.pdf','rb')
    pdffileobj=open('C:\\Users\\anderson.gomes\\Documents\\Projects\\invoice_processing\\files\\Nubank_2022-10-20.pdf','rb')

    # create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    
    # This will store the number of pages of this pdf file
    x=pdfreader.numPages

    # create a variable that will select the selected number of pages
    pageobj=pdfreader.getPage(3)

    # create text variable which will store all text datafrom pdf file
    text = pageobj.extractText()
    

    # save the extracted data from pdf to a txt file
    # we will use file handling here
    # dont forget to put r before you put the file path
    # go to the file location copy the path by right clicking on the file
    # click properties and copy the location path and paste it here.
    # put "\\your_txtfilename"
    file=open(
        r"C:\\Users\\anderson.gomes\\Documents\\Projects\\invoice_processing\\processed_files\\output.txt",
        "a",
        encoding='utf-8')
    file.writelines(text)

    lines = text.split('\n')
    cont = 0
    csv_output = ''
    # Removing the headers lines
    lines.pop(0)
    lines.pop(0)
    lines.pop(0)
    for line in lines:
        if cont == 4:
            cont = 0
            csv_output += '\n'
        if "ANDERSON GOMES NUNES" in line:
            break
        csv_output += line + ';'
        cont += 1
    print(csv_output)
    file=open(
        r"C:\\Users\\anderson.gomes\\Documents\\Projects\\invoice_processing\\processed_files\\output.csv",
        "a",
        encoding='utf-8')
    file.writelines(csv_output)