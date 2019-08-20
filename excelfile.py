import xlrd, xlsxwriter
from xlwt import Workbook

wb = xlsxwriter.Workbook("test2.xlsx")
sheet = wb.add_worksheet()

sheet.write("A1", "ABC")

wb.close()
# wb1 = xlrd.open_workbook("test2.xlsx")
# sh = wb1.sheet_by_index(0)
#
# sh.cell_value(0, 0)
#
# for i in range(sh.nrows):
#     print(sh.cell(i, 0))