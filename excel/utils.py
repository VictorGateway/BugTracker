import xlwt
from django.http import HttpResponse

 
def create_sheet_response(filename, rows_instance):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename={filename}'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Projects Data') # this will make a sheet named Projects Data

    columns = ['Project Number', 'Assignee First Name', 'Assignee First Name', 'Priority', 'Status', 'title','Summary', 'created_by first name', 'created_by last name']

    rows=rows_instance.values_list('project_number','assignee__first_name','assignee__last_name','priority','status', 'title', 'summary', 'author__first_name', 'author__last_name' )

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response