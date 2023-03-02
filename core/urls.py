from django.urls import path
from .views import IndexPageView, BugListView, BugCreateView, BugDetailView, BugDeleteView, BugUpdateView, DeveloperListView, OpenBugListView, ClosedBugListView, WorkingBugListView, AboutPageView, DeveloperCreateView, DeveloperDetailView, DeveloperDeleteView, DeveloperUpdateView, UpdatedRecentlyBugListView, MyTasksBugListView, DashboardTemplateView
 
urlpatterns = [
    #static urls
    
    path('', IndexPageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    #All project urls
    path('all-projects/', BugListView.as_view(), name='bug_list'),
    path('projects/create/', BugCreateView.as_view(), name='bug_create'),
    path('projects/<int:pk>/', BugDetailView.as_view(), name='bug_detail'), 
    path('projects/<int:pk>/delete/', BugDeleteView.as_view(), name='bug_delete'),
    path('projects/<int:pk>/update/', BugUpdateView.as_view(), name='bug_update'),
    #Open Projects
    path('open-projects/', OpenBugListView.as_view(), name='open_projects'),
    #Working Projects
    path('working-projects', WorkingBugListView.as_view(), name='working_projects'),
    #Projects that were updated recently
    path('updated-recently/', UpdatedRecentlyBugListView.as_view(), name='updated_recently'),
    #Projects that were opened by the user
    path('my_tasks/', MyTasksBugListView.as_view(), name="my_tasks"), 
    #All developer urls
    path('closed-projects/', ClosedBugListView.as_view() ,name='closed_projects'),
    path('developers/', DeveloperListView.as_view(), name='developer_list'), 
    path('developers/create', DeveloperCreateView.as_view(), name='developer_create'),
    path('developers/<int:pk>/', DeveloperDetailView.as_view(), name='developer_detail'), 
    path('developers/<int:pk>/delete', DeveloperDeleteView.as_view(), name='developer_delete'), 
    path('developers/<int:pk>/update', DeveloperUpdateView.as_view(), name='developer_update'), 
    #dashboard view
    path('dashboard/', DashboardTemplateView.as_view(), name="dashboard"), 
]

#find out why projects/open is not recognizable