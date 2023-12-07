from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import SignUpForm

# Create your views here.
def personasIndex(request):
    return render(request, 'index.html')

@login_required
def panelAdmin(request):
    if request.user.is_superuser:
        return render(request, 'homeAdmin.html')
    else:
        return render(request, 'homeUser.html')
    

def signUp(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')


    return render(request, 'signUp.html', {'form': form})
    


"""crear home pa
"""