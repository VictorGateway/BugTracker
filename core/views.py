from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BugTracker, Developer
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


#static pages
class HomePageView(TemplateView):
    template_name='home.html'

class IndexPageView(TemplateView):
    template_name='index.html'

class AboutPageView(TemplateView):
    template_name='about.html'

#AllBugListView
class BugListView(LoginRequiredMixin, ListView):
    template_name="bug_list.html"
    model=BugTracker
    

class BugDetailView(LoginRequiredMixin, DetailView):
    template_name="bug_detail.html"
    model=BugTracker

class BugCreateView(LoginRequiredMixin, CreateView):
    template_name="bug_create.html"
    model=BugTracker
    fields= ( "title","priority", "summary", )

    def form_valid(self, form):
         form.instance.author=self.request.user
         return super().form_valid(form)

class BugUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name="bug_update.html"
    model=BugTracker
    fields= ("title","assignee","priority", "summary", "status" )

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

class BugDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name="bug_delete.html"
    model=BugTracker
    success_url=reverse_lazy("bug_list")

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

#OpenProjectsTasks
class OpenBugListView(BugListView):
    template_name='open_projects.html'

#ClosedProjectsTasks
class ClosedBugListView(BugListView):
    template_name='closed_projects.html' 

#WorkingProjectsTasks
class WorkingBugListView(BugListView):
    template_name='working_projects.html'

#UpdateRecently
class UpdatedRecentlyBugListView(BugListView):
    template_name='updated_recently.html'

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.order_by('-updated_at')
#Opened tasks by me
class MyTasksBugListView(BugListView):
    template_name='my_tasks.html'

#The following are classes for Developer Model
class DeveloperListView(ListView):
    template_name="developer_list.html"
    model=Developer

class DeveloperDetailView(DetailView):
    template_name="developer_detail.html"
    model=Developer

class DeveloperCreateView(CreateView):
    template_name="developer_create.html"
    model=Developer
    fields = '__all__'

class DeveloperUpdateView(UpdateView):
    template_name="developer_update.html"
    model=Developer
    fields= '__all__'

class DeveloperDeleteView(DeleteView):
    template_name="developer_delete.html"
    model=Developer 
    success_url=reverse_lazy("developer_list")   

class DashboardTemplateView(TemplateView):
    template_name="dashboard.html"
    model=BugTracker

    def get_context_data(self, **kwargs):
        context=super().get_context_data()

        open_query = BugTracker.objects.filter(status="Open").count()
        closed_query = BugTracker.objects.filter(status="Closed").count()
        in_progress_query = BugTracker.objects.filter(status="In Progress").count()

        labels = ['Open Projects', "in Progress Projects", "Closed Projects"]
        data=[open_query, closed_query ,in_progress_query ]

        context['labels']=labels
        context['data']=data
        return context

