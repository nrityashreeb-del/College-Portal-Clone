from django.shortcuts import render, redirect
from .models import contact
from .forms import contactForm

def campus(request):
    return render(request, 'pcps/campus.html')
def ABOUT(request):
    return render(request, 'pcps/ABOUT.html')
def academic(request):
    return render(request, 'pcps/academic.html')
def activities(request):
    return render(request, 'pcps/activities.html')
def area(request):
    return render(request, 'pcps/area.html')
def contact(request):
    return render(request, 'pcps/contact.html')
def departments(request):
    return render(request, 'pcps/departments.html')
def examination(request):
    return render(request, 'pcps/examination.html')
def faculties(request):
    return render(request, 'pcps/faculties.html')
def gallery(request):
    return render(request, 'pcps/gallery.html')
def notices(request):
    return render(request, 'pcps/notices.html')
def placements(request):
    return render(request, 'pcps/placements.html')
def students(request):
    return render(request, 'pcps/students.html')
def civil(request):
    return render(request, 'pcps/civil.html')
def cse(request):
    return render(request, 'pcps/cse.html')
def arch(request):
    return render(request, 'pcps/arch.html')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print("DATA SAVED SUCCESSFULLY !")
            return redirect('contact')      
        else: print("FORM ERRORS:", form.errors)

    else:

        form = contactForm()
    return render(request, 'pcps/contact.html', {'form': form})



# Create your views here.
