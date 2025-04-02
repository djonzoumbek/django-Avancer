from django.urls import path
from  .views import  logout_page, signup_page
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path('login/', LoginView.as_view( template_name= "authentication/login.html", redirect_authenticated_user = True), name='login'),
    path('logout/', logout_page, name='logout'),
    path('change-password/', PasswordChangeView.as_view(template_name="authentication/change_password_form.html"), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('signup/', signup_page, name='signup'),

]