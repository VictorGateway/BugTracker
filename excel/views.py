from django.views.generic import TemplateView
from core.models import BugTracker, Developer
from django.urls import reverse_lazy
import xlwt
from django.http import HttpResponse
from .utils import create_sheet_response
#The classes below are functionality for an excel document that provide all of the project filters. See utils.py from the main response function

class ExcelDownloadAllView(TemplateView):
    def get(self, request, *args, **kwargs):
        rows_instance = BugTracker.objects.all() 
        filename ='All_Projects.xls'
        return create_sheet_response(filename, rows_instance)

class ExcelDownloadOpenView(ExcelDownloadAllView):
    def get(self, request, *args, **kwargs):
        rows_instance = BugTracker.objects.all().filter(status='Open')
        filename ='All_Open_Projects.xls'
        return create_sheet_response(filename, rows_instance)

class ExcelDownloadClosedView(ExcelDownloadAllView):
    
    def get(self, request, *args, **kwargs):
        rows_instance = BugTracker.objects.all().filter(status='Closed')
        filename ='All_Closed_Projects.xls'
        return create_sheet_response(filename, rows_instance)

class ExcelDownloadInProgressView(ExcelDownloadAllView):
    
    def get(self, request, *args, **kwargs):
        rows_instance = BugTracker.objects.all().filter(status='In Progress')
        filename ='All_Closed_Projects.xls'
        return create_sheet_response(filename, rows_instance)

class ExcelDownloadInProgressView(ExcelDownloadAllView):
    
    def get(self, request, *args, **kwargs):
        rows = Developer.objects.all().values_list('first_name','lastname','email' )
        filename ='All_Developer_Projects.xls'
        
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('All Projects Data') # this will make a sheet named Projects Data

        columns = ['firstname','lastname','email']

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