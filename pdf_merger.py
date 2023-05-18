import PyPDF2

pdf_files=["1.pdf","2.pdf","3.pdf"]
# n=int(input("Enter no. of PDF you want to merge: "))
# pdf_files=[]
# print("Enter the PDF name with extension (.pdf)")
# for i in range(1,n+1):
#     pdf_files[i]=(input(f"Enter the PDF{i} name : "))
# print("done")

merger= PyPDF2.PdfMerger()
for filename in pdf_files:
    pdf_files=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdf_files)
    merger.append(pdfReader)
pdf_files.close()
merger.write("Merged.pdf")
