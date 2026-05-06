import openpyxl


def read_excel_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []

    # Iterate through rows, skipping the header (min_row=2)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data