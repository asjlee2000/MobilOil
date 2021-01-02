import PyPDF2, datetime, pdfplumber

print("============================================================================================")
print("██████╗ ██████╗ ███████╗    ███████╗██████╗ ██╗     ██╗████████╗    ██╗   ██╗ ██╗   ██████╗ ")
print("██╔══██╗██╔══██╗██╔════╝    ██╔════╝██╔══██╗██║     ██║╚══██╔══╝    ██║   ██║███║   ╚════██╗")
print("██████╔╝██║  ██║█████╗      ███████╗██████╔╝██║     ██║   ██║       ██║   ██║╚██║    █████╔╝")
print("██╔═══╝ ██║  ██║██╔══╝      ╚════██║██╔═══╝ ██║     ██║   ██║       ╚██╗ ██╔╝ ██║    ╚═══██╗")
print("██║     ██████╔╝██║         ███████║██║     ███████╗██║   ██║        ╚████╔╝  ██║██╗██████╔╝")
print("╚═╝     ╚═════╝ ╚═╝         ╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝         ╚═══╝   ╚═╝╚═╝╚═════╝ ")
print("============================================================================================")
print()

filename = input("Enter PDF name without '.pdf' extension: \n")
print()
filename += ".pdf"

list_of_names = []

day = input("Enter date [today] or [YYYY_MM_DD]: \n")
print()
day = day.lower()

if (day == "today"):
    day = datetime.date.today().isoformat().replace("-","_")

document = open(filename, "rb")
reader = PyPDF2.PdfFileReader(document)

with pdfplumber.open(document) as pdf:
    for i in range(len(pdf.pages)):
        words = pdf.pages[i].extract_words()
        namefound = False
        for word in words:
            if (word["top"] > 150 and word["bottom"] < 165 and not namefound):
                list_of_names.append(word["text"])
                namefound = True

for i in range(reader.getNumPages()):
    output = PyPDF2.PdfFileWriter()
    output.addPage(reader.getPage(i))

    with open("Payroll_%s_%s.pdf" % (list_of_names[i], day), "wb") as outputStream:
        output.write(outputStream)

document.close()