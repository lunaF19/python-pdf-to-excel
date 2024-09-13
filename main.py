from tools.args import get_source_ddl_files_path, get_final_path
from tools.files import get_files_of_dir, get_path
from tools.pdf_to_excel import pdf_to_excel

source_path = get_source_ddl_files_path()
final_path = get_final_path()

list_files = get_files_of_dir(source_path)

for file in list_files:
    file_ext = file["ext"].lower()
    file_name = file["name"]
    file_dir = file["dir"]

    if ("pdf" in file_ext):
        final_path_excel = get_path(final_path, f"{file_name}.xlsx")
        pdf_to_excel(file_dir, final_path_excel)
