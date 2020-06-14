from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    # success_url = reverse('login') # will throw an error since URLConf is not loaded
    # can't use reverse with success_url, 
    # because then reverse is called when the module is imported, 
    # before the urls have been loaded.
    # https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin
    template_name = 'signup.html'    


