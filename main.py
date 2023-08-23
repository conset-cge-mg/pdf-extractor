# main.py
from pdf_data_extractor import PDFDataExtractor

def main():
    pdf_path = 'path_to_your_pdf_file.pdf'
    pdf_extractor = PDFDataExtractor(pdf_path)
    pdf_extractor.extract_text()
    pdf_extractor.process_text()
    pdf_extractor.create_dataframe()
    df = pdf_extractor.get_dataframe()

    print(df)

if __name__ == "__main__":
    main()
