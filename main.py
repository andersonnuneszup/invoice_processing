import PyPDF2


if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    # create file object variable
    # opening method will be rb
    pdffileobj=open('C:\\Users\\ander\\workspace-python\\ocr-stack\\files\\file.pdf','rb')
    
    # create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    
    # This will store the number of pages of this pdf file
    x=pdfreader.numPages
    
    text = ''
    for i in range(x):
        # create a variable that will select the selected number of pages
        pageobj=pdfreader.getPage(i)
        
        # create text variable which will store all text datafrom pdf file
        text += pageobj.extractText()
    
    # save the extracted data from pdf to a txt file
    # we will use file handling here
    # dont forget to put r before you put the file path
    # go to the file location copy the path by right clicking on the file
    # click properties and copy the location path and paste it here.
    # put "\\your_txtfilename"
    file1=open(
        r"C:\\Users\\usuario\\workspace\\ocr-stack\\processed_files\\output.txt",
        "a",
        encoding='utf-8')
    file1.writelines(text)