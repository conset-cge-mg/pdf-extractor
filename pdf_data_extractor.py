# pdf_data_extractor.py
import pdfplumber
import pandas as pd


class PDFDataExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = ""
        self.data = []

    def extract_text(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                self.text += page.extract_text()

    def process_text(self):
        lines = self.text.split("\n")

        for line in lines:
            columns = line.split("\t")  # Adjust delimiter

            row_dict = {
                "column1_name": columns[0],
                "column2_name": columns[1],
                # Add more columns as needed
            }
            self.data.append(row_dict)

    def create_dataframe(self):
        self.df = pd.DataFrame(self.data)

    def get_dataframe(self):
        return self.df
