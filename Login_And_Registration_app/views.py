from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.

def registration_page(request):
    print('======'*15)
    print('****this is the REGISTRATION_PAGE method****')

    return render(request, "index.html")

def registration_process(request):
    print('======'*15)
    print('****this is the REGISTRATION_PROCESS method****')

    print(request.POST)

    errors = User.objects.validateRegistration(request.POST)

    if errors:
        print('****there are some errors to FIX*****')
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')


    # turning the password received from POST into Hash
    registered_post_password = request.POST['user_registered_password']
    print(registered_post_password + "~~~ this is the users registered password ~~~")
    registered_pw_hash = bcrypt.hashpw(registered_post_password.encode(), bcrypt.gensalt()).decode()
    print(registered_pw_hash)

    new_user = User.objects.create(
        first_name = request.POST['user_first_name'], #first error here multivalue dict ~~why doesnt it read POST?~~ *FIXED*
        last_name = request.POST['user_last_name'],
        email_address = request.POST['user_registered_email_address'],
        #enters hashed password into database
        password = registered_pw_hash,
    )
    print (User.objects.all())
    print(new_user.id)


    # User.objects.create(email_address=request.POST['user_registered_email_address']), login_post_password=pw_hash)

    return redirect('/registration_success')

def registration_success(request):
    print('======'*15)
    print('****this is the REGISTRATION SUCCESS method****')
    return render(request,'registration-success.html')

def login_process(request):
    print('======'*15)
    print('****this is the LOGIN_PROCESS method****')

    errors = User.objects.validateLogin(request.POST)
    print(errors)

    if errors:
    # if len(errors) == 0:
        print("try again...")

        for key, value in errors.items():
            messages.error(request, value)
            
        return redirect('/')

    # Have to check if user is in database to login

    # getting login info from user
    this_user = User.objects.filter(email_address=request.POST['user_login_email_address'])
    if this_user:
        logged_user = this_user[0]
    #if user is in database do bottom code
        if bcrypt.checkpw(request.POST['user_login_password'].encode(), logged_user.password.encode()): #checking hashed password? whole object
            print("~~~password is a match...adding into session~~~~")
            request.session['session_user_id'] = logged_user.id
            return redirect('/login_success')
        else:
            messages.error(request, "failed password try again...")
            print("**failed password try again...")
            return redirect('/')
    else:
        return redirect('/')



        # mess with during validation 
        # messages.add_messages(request,messages.INFO,'wrong credentials provided') 
    
    

def login_success(request):
    print('======'*15)
    print('****this is the LOGIN_SUCCESS method****')
    
    return render(request,'login-success.html')

def logout(request):
    print('======'*15)
    print('**** LOGGING OUT ****')
    request.session.clear()

    return redirect('/')