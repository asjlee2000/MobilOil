# Payroll PDF Splitter

The two files pdf_split and pdf_slice are both used to split a single multi-page payroll document, which has the payroll information of every employee, into multiple single-page documents with one page per employee.

## pdf_slice

pdf_slice.py is the predecessor to pdf_split.py.

pdf_slice.exe is the executable file for pdf_slice.py.

It utilizes the Python module PyPDF2 to read in the original PDF and write out the single-page PDFs.

It works by:

1. Reading in the PDF by prompting the user to enter in the name of the file.
2. Asking for the employee names in order as shown in the PDF.
3. Writing single-page PDFs for each employee with titles formatted: "Payroll_[name]_[today's date].pdf".

## pdf_split

pdf_split.py is the successor to pdf_slice.py.

pdf_split.exe is the executable file for pdf_split.py.

It utilizes the Python modules PyPDF2 and pdfplumber to read the in the original PDF and write out the single-page PDFs.

**The algorithm for pdf_split automatically detects the Employee's name from the PDF and eliminates the need for the user to input the names in order as shown in the PDF, unlike pdf_slice.**

It works by:

1. Reading in the PDF by prompting the user to enter in the name of the file.
2. Asking for the date (allows for custom dates in the filenames instead of today's date).
3. Writing single-page PDFs for each employee with titles formatted: "Payroll_[name]_[custom date].pdf".
