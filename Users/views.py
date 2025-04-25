#from django.contrib.auth.views import LoginView
from django.contrib.auth import login,authenticate,logout
#from django.urls import reverse_lazy
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render,redirect
# Create your views here.
'''
class Login_User(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('/') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

    '''

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})
    elif request.method == 'POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('/')


    return render(request,'users/login.html',{'form':form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        