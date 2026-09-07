from loader import load_pdf


pdf_path = "data/documents/SI BENDI (BENTENG DIGITAL) final.pdf"

pages = load_pdf(pdf_path)

print(f"Jumlah halaman: {len(pages)}")

for page in pages[:4]:
    print("\n--- PAGE", page["page"], "---")
    print(page["text"][:1000])
