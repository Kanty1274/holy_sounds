from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    """
    Register a new user.

    This function handles the user registration process. If the HTTP request method is 'POST',
    it attempts to validate and save the user registration form. If the form is valid, the
    new user is saved to the database, and the user is redirected to the '/user_auth/' URL.

    If the HTTP request method is not 'POST', it means the user is accessing the registration
    page for the first time or using the 'GET' method. In this case, it initializes an empty
    registration form and renders the 'register.html' template, allowing the user to enter
    registration details.

    :param response (HttpRequest): The HTTP request object sent by the client.

    :return: If the method is 'POST' and the form is valid, the function redirects
			the user to the '/user_auth/' URL. If the method is not 'POST', it renders the
			'register.html' template with the 'form' context variable.
    
    :rtype: HttpResponse 
    """
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/user_auth")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})






