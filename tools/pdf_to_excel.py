# File getting from https://github.com/LadyKerr/pdf-to-excel/blob/main/pdf_to_excel.py
from tabula.io import read_pdf
import pandas as pd


def pdf_to_excel(pdf_file_path, excel_file_path):
    # Read PDF file
    tables = read_pdf(pdf_file_path, pages='all')

    # Write each table to a separate sheet in the Excel file
    with pd.ExcelWriter(excel_file_path) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f'Sheet{i+1}')
