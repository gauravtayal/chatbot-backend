try:
    from ingestion.pdf_loader import load_pdf
except ModuleNotFoundError:
    from pdf_loader import load_pdf

documents = load_pdf("./data/hr/employeeHandbook.pdf")

print("Number of pages:", len(documents))

for document in documents[:2]:

    print("-----")

    print(document.page_content[:500])

    print(document.metadata)

