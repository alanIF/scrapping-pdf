# importa as bibliotecas necessárias
import PyPDF2
import re

# Abre o arquivo pdf 
# lembre-se que para o windows você deve usar essa barra -> / 
# lembre-se também que você precisa colocar o caminho absoluto
pdf_file = open('media/dados.pdf', 'rb')

#Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)
# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()
for i in range(0,number_of_pages):
    #lê a primeira página completa
    page =  read_pdf.getPage(i)  
    text = page.extractText()
    print(text)
    
    
