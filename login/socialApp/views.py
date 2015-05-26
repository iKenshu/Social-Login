from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView, View

class LoginTemplateView(TemplateView):
	template_name = "login.html"

class HomeTemplateView(TemplateView):
	template_name = "home.html"

	@method_decorator(login_required(login_url='/'))
	def dispatch(self, request, *args, **kwargs):
		return super(HomeTemplateView, self).dispatch(request, *args, **kwargs)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('/')