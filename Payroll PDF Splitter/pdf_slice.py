import PyPDF2, datetime

filename = input("Enter PDF name: \n")
filename += ".pdf"
list_of_names = []

today = datetime.date.today().isoformat().replace("-","_")

document = open(filename, "rb")
reader = PyPDF2.PdfFileReader(document)

for i in range(reader.getNumPages()):
    input_name = input("Employee %d: " % (i+1))
    list_of_names.append(input_name)

for i in range(reader.getNumPages()):
    output = PyPDF2.PdfFileWriter()
    output.addPage(reader.getPage(i))

    with open("Payroll_%s_%s.pdf" % (list_of_names[i], today), "wb") as outputStream:
        output.write(outputStream)

document.close()