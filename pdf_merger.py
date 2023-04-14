# Import the necessary PyPDF2 classes.
from PyPDF2 import PdfFileMerger, PdfFileReader

# List the PDF files to be merged.
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# Create a new PdfFileMerger object to store the merged PDFs.
pdf_merger = PdfFileMerger()

# Iterate over each PDF file and add it to the PdfFileMerger object.
for pdf_file in pdf_files:
    # Open the PDF file in read binary mode and add it to the PdfFileMerger object.
    with open(pdf_file, 'rb') as f:
        pdf_merger.append(PdfFileReader(f))

# Write the merged PDFs to a new file.
with open('merged.pdf', 'wb') as f:
    pdf_merger.write(f)

# Close the PdfFileMerger object.
pdf_merger.close()
