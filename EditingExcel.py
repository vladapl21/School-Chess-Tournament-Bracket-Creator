from openpyxl import Workbook, load_workbook

wb = load_workbook("Chess_Tournament.xlsx")
ws = wb.active
print(ws["A2"].value)
