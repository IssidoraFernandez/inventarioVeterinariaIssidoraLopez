from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def personasIndex(request):
    return render(request, 'index.html')

@login_required
def panelAdmin(request):
    if request.user.is_superuser:
        return render(request, 'homeAdmin.html')
    if request.user.is_staff:
        return render(request, 'homeStaff.html')
    else:
        return render(request, 'homeUser.html')
    


"""crear home pa
"""