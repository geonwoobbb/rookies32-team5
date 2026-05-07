from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
from crawling import crawling
from datetime import datetime

now = datetime.now().strftime("%Y%m%d_%H%M")

def create_excel_report(crawling_data):
    wb = Workbook()
    ws = wb.active
    ws.title = "Price_List"

    # Header
    header = ["No", "Title", "Price"]
    ws.append(header)

    # 헤더 스타일링
    header_fill = PatternFill(start_color="FF00FF", fill_type='solid')
    header_font = Font(color='FFFFFF', bold=True)
    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill
    

    # 데이터 추가
    for i, poke in enumerate(crawling_data, 1):
        row = [i, poke['title'], poke['price']]
        ws.append(row)

    wb.save(f"PokePriceReport_{now}.xlsx")
    print("생성 완료")


crawling_data = crawling()
create_excel_report(crawling_data)