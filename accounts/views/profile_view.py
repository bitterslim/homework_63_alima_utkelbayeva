from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, UpdateView
from accounts.forms import UserChangeForm, PasswordChangeForm
from accounts.models import Account


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'

class UserChangeView(UpdateView):
    model = Account()
    form_class = UserChangeForm
    template_name = 'user_change.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

class PasswordChangeView(UpdateView):
    model = get_user_model()
    template_name = 'change_password.html'
    form_class = PasswordChangeForm

