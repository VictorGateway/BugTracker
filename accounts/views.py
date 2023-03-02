from django.views.generic import CreateView, RedirectView
from .forms import CustomCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

class SignUpView(CreateView):
    form_class=CustomCreationForm
    success_url=reverse_lazy("bug_list")
    template_name="registration/signup.html"

class GuestLoginView(RedirectView):
    url=reverse_lazy('bug_list') 

    def get(self, request, *args, **kwargs):
        guest_user=authenticate(username="guest@email.com", password= "Victor@12!",)
        login(self.request, guest_user)
        return super().get(request, *args, **kwargs)

    
        

