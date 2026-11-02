import os
from pypdf import PdfWriter

folder_path = "/home/najib/Extra/Merger/data/pdf"

if not os.path.isdir(folder_path):
    print(f"Folder not found: {folder_path}")
    exit()

merger = PdfWriter()

for filename in sorted(os.listdir(folder_path)):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        merger.append(pdf_path)

output_file = os.path.join(folder_path, "merged.pdf")

with open(output_file, "wb") as f:
    merger.write(f)

merger.close()

print(f"Merged file successfully created: {output_file}")