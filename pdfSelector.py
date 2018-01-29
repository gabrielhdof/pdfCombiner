#! /usr/bin/python3
# coding:utf-8


import os, PyPDF2

endereço = input("Qual o endereço do arquivo a ser cortado?")
paginas = input("Quais páginas devem ser selecionadas? Digite-as separadas por vírgulas > ")

pdfWriter = PyPDF2.PdfFileWriter()

pdfFileObj = open(endereço, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for pagina in paginas.split(','):
	pagina = int(pagina)
	pageObj = pdfReader.getPage(pagina)
	pdfWriter.addPage(pageObj)
	
pdfOutput = open(os.path.dirname(endereço)+os.sep+"CUT"+os.path.basename(endereço), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
