from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid:
            username = form.cleaned_data.get('username')
            messages.success(request, 'Welcome {}, your account has been created', format(username))
            
            form.save()
            return redirect('products:index')
    
    else:
        form = UserCreationForm()

        context = {
            'form':form
        }
    
        return render(request, 'users/register.html', context)
