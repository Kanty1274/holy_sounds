from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from.forms import LoginForm


def user_login(request):
    """
    Handles user login.

    This function handles the user login process. If the HTTP request method is 'POST',
    it attempts to validate the login form. If the form is valid, it retrieves the username
    and password from the form's cleaned data and attempts to authenticate the user.

    :param request (HttpRequest):   The HTTP request object sent by the client.

    :returns:   HttpResponse: If the method is 'POST' and the form is valid, the function attempts
                to authenticate the user using the provided username and password. If successful,
                the user is logged in, and they will have an active session. If authentication fails,
                the user will remain unauthenticated, and they can try logging in again.

                If the HTTP request method is not 'POST', it means the user is accessing the login
                page for the first time or using the 'GET' method. In this case, it renders the
                'login.html' template, allowing the user to enter login credentials.
            
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
    else:
        return render(request, 'authentication/login.html')


def authenticate_user(request):
    """
    Authenticate and log in a user.

    This function handles the authentication and login process for a user. It expects the
    HTTP request to be a 'POST' request containing the 'username' and 'password' fields.

    If the 'username' and 'password' provided in the request match a valid user account,
    the user is authenticated, and their login session is created. The function then redirects
    the user to the 'song_list' URL, where they can view a list of songs.

    If the provided 'username' and 'password' do not match any valid user account, the
    function redirects the user back to the 'login' URL, where they can try logging in again.

    :param request (HttpRequest): The HTTP request object sent by the client. It is expected to
        be a 'POST' request containing the 'username' and 'password' fields.

    :returs: HttpResponseRedirect: If the user is authenticated successfully, the function
        redirects the user to the 'song_list' URL, where they can view a list of songs.
        If the authentication fails, the function redirects the user back to the 'login'
        URL to try logging in again.
        
    :rtype: HttpResponseRedirect
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('band:song_list')
        )


def show_user(request):
    """
    Display user information.

    This function displays the user information on the 'user.html' template. It retrieves the
    currently logged-in user's username and password from the request's user object. However,
    displaying the user's password is generally not recommended for security reasons, and in
    most cases, the password should not be displayed to the user.

    :param request (HttpRequest): The HTTP request object sent by the client.

    :returs: HttpResponse: The rendered response containing the 'user.html' template. The context
        variables 'username' and 'password' will be used to display the user information.
        
    :rtype: HttpResponse
    """
    print(request.user.username)  # Printing the username (for debugging purposes)

    # Retrieving the currently logged-in user's username and password.
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
