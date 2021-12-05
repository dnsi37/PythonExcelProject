import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

excel.Visible = True

workbook = excel.Workbooks.Add()  # WorkBooks 생성

sheet = workbook.Worksheets("Sheet1")

# 데이터 입력

sheet.Range("A1").Value = 1

sheet.Range("A2").Value = "A2"

sheet.Range("A3").Value = "A3"

sheet.Range("A4").Value = True

sheet.Range("A5").Value = None

# 
for i in range(1,6):
    if str(type(sheet.Range("A"+str(i)).Value)) == "<class 'float'>" or str(type(sheet.Range("A"+str(i)).Value)) == "<class 'int'>":
        sheet.Range("A" + str(i)).Interior.ColorIndex = 3
    elif str(type(sheet.Range("A"+str(i)).Value)) == "<class 'str'>" :
        sheet.Range("A" + str(i)).Interior.ColorIndex = 4

    elif str(type(sheet.Range("A"+str(i)).Value)) == "<class 'bool'>" :
        sheet.Range("A" + str(i)).Interior.ColorIndex = 6
    elif str(type(sheet.Range("A"+str(i)).Value)) == "<class 'NoneType'>" :
        sheet.Range("A" + str(i)).Interior.ColorIndex = 7 