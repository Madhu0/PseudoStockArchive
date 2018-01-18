import csv
from datetime import datetime
from PseudoStockArchiveApp.models import Company, TradingData
from openpyxl import load_workbook

wb = load_workbook('/Users/madhusudhan/MyCoding/Python/PseudoStockArchive/companiesdata.xlsx', read_only=True)
ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])
allRows = ws.rows
next(allRows)
for row in allRows:
    try:
        company = Company(symbol=row[0].value, name=row[1].value, marketCap=row[2].value, sector=row[3].value, industry=row[4].value)
        company.save()
    except Exception:
        pass

print('Company data added')

# with open('/Users/madhusudhan/MyCoding/Python/PseudoStockArchive/data.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     row1 = next(reader)
#     for row in reader:
#         print(row[0], row[1])
#         try:
#             company = Company.objects.get(symbol=row[1])
#             try:
#                 timestamp = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
#             except Exception:
#                 timestamp = datetime.strptime(row[0], "%Y-%m-%d")
#             tradingData = TradingData(timestamp=timestamp, company=company, open=float(row[2]), close=float(row[3]),
#                                       low=float(row[4]), high=float(row[5]), volume=float(row[6]))
#             tradingData.save()
#         except Exception:
#             pass