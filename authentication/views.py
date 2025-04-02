from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import SignUpForm

"""
class LoginPage(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'
    message = ""

    def get(self, request):
        form = self.form_class()
        template = self.template_name
        message = self.message
        return render(request, template, context={"form": form, "message" : message})

    def post(self, request):
        message = ""
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
        message = "Identifiant invalide."
        return render(request, self.template_name, context={"form": form, "message" : message})"""

def logout_page(request):
    logout(request)
    return redirect("login")

def signup_page(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "authentication/signup.html", {"form": form})
