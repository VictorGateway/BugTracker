from django.urls import path
from .views import ExcelDownloadAllView, ExcelDownloadOpenView, ExcelDownloadClosedView, ExcelDownloadInProgressView
 
urlpatterns = [
    #static urls
#excel view
    path('export/excel', ExcelDownloadAllView.as_view(), name='excel_download'),
    path('export/excel/open', ExcelDownloadOpenView.as_view(), name='excel_open_download'),
    path('export/excel/closed', ExcelDownloadClosedView.as_view(), name='excel_closed_download'),
    path('export/excel/closed',ExcelDownloadInProgressView.as_view(), name='excel_in_progress_download'),
    path('export/excel/developers',ExcelDownloadInProgressView.as_view(), name='excel_developers_download'),

]