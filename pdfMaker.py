#! /usr/bin/python3
# coding:utf-8

import PyPDF2, os

directory = input('Em qual diretório devo procurar? > ')
pdfFiles = []

print('Identificando pdfs no diretório...')
for filename in os.listdir(directory):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)
print("PDF's identificados: ")
for pdf in pdfFiles:
	print("\t"+pdf)


pdfWriter = PyPDF2.PdfFileWriter()

print("Combinando PDF's...")
os.chdir(directory)
for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	print("Copiando %s..."%filename)
	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
print("PDF's combinados com sucesso!")

pdfOutput = open('PDFGERAL.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
