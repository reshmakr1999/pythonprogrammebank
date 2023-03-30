from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth, messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse


#
# # Create your views here.

def home(request):
    return render(request,"home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if password and confirm_password match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        # Create new user object
        user = User.objects.create_user(username=username, password=password)

        # Log the user in and redirect to home page
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new_page_view')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')





def new_page_view(request):
    return render(request, 'new_page.html')




# def new_registration(request):
#     # Code to handle form submission would go here
#     return render(request, 'registration_form.html')
# def new_registration(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         dob = request.POST['dob']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone = request.POST['phone']
#         email = request.POST['mail_id']
#         address = request.POST['address']
#         district = request.POST['district']
#         branch = request.POST['branch']
#         account_type = request.POST['account_type']
#         materials = ','.join(request.POST.getlist('materials_provided'))
#
#         user=User(name=name, dob=dob, age=age, gender=gender, phone=phone, mail_id=email, address=address, district=district, branch=branch, account_type=account_type, materials_provided=materials)
#         user.save();
#
#         return redirect('registration_success')
#     else:
#         return render(request, 'registration_form.html')

from django.shortcuts import render, redirect

# from .models import  Registration
# from .forms import RegistrationForm
#
#
# def new_registration(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             dob = form.cleaned_data['dob']
#             age = form.cleaned_data['age']
#             gender = form.cleaned_data['gender']
#             phone_number = form.cleaned_data['phone_number']
#             email = form.cleaned_data['email']
#             address = form.cleaned_data['address']
#             district = form.cleaned_data['district']
#             branch = form.cleaned_data['branch']
#             account_type = form.cleaned_data['account_type']
#             materials_provide = form.cleaned_data['materials_provide']
#             # city = form.cleaned_data['city']
#             # country = form.cleaned_data['country']
#
#             reg_obj = Registration(
#                 name=name,
#                 dob=dob,
#                 age=age,
#                 gender=gender,
#                 phone_number=phone_number,
#                 email=email,
#                 address=address,
#                 district=district,
#                 branch=branch,
#                 account_type=account_type,
#                 materials_provide=materials_provide,
#                 # city = city,
#                 # country =country
#             )
#             reg_obj.save()
# #
#             return render(request, 'success.html')
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'new_registration.html', {'form': form})
#


from django.shortcuts import render, redirect
from .forms import RegistrationForm

def new_registration(request):
      if request.method == 'POST':

        # form = RegistrationForm(request.POST)
        # if form.is_valid():
        #     form.save()
            return redirect('success')
      else:
        form = RegistrationForm(request)
      return render(request, 'registration_form.html', {'form': form})



from django.http import JsonResponse



from django.http import JsonResponse
def getbranches(request):
    district = request.GET.get('district', None)
    branches = []
    if district == 'Ernakulam':
        branches = ['Aluva', 'Edapally', 'Kakkanad']
    elif district == 'Thrissur':
        branches = ['Irinjalakuda', 'Kodungallur']
    elif district == 'Kozhikode':
        branches = ['Calicut', 'Koyilandy']
    return JsonResponse({'branches': branches})


#
def success(request):
    return render(request, 'success.html')

def home(request):
    return render(request, 'home.html')



# def get_branches(request):
#     district = request.GET.get('district')
#     # Retrieve the list of branches for the selected district from the database
#     branches = ['Aluva', 'Edapally', 'Kakkanad'] # Sample branches
#     options = '<option value="" disabled selected>Select your branch</option>'
#     for branch in branches:
#         options += f'<option value="{branch}">{branch}</option>'
#     return JsonResponse({'options': options})



def logout_view(request):
    logout(request)
    return redirect('login')



# def get_branches(request, district_id):
#     branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
#     return JsonResponse(list(branches), safe=False)



# def get_branches(request):
#     district_id = request.GET.get('district_id')
#     branches = Branch.objects.filter(district_id=district_id).values_list('name', flat=True)
#     options = '<option value="" disabled selected>Select your branch</option>'
#     for branch in branches:
#         options += f'<option value="{branch}">{branch}</option>'
#     return JsonResponse({'options': options})

# def get_branches(request, district_id):
#     branches = Branch.objects.filter(district=district_id)
#     data = [{'id': Branch.id, 'name': Branch.name} for Branch in branches]
#     return JsonResponse(data, safe=False)
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# from .forms import PersonCreationForm
# from .models import Person,Branch


# def person_create_view(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person_add')
#     return render(request, 'persons/home.html', {'form': form})
#
#
# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})
#
#
# # AJAX
# def load_branches(request):
#     district_id = request.GET.get('district_id')
#     branches = Branch.objects.filter(country_id=district_id).all()
#     return render(request, 'persons/branch.html', {'branches': branches})
#     return JsonResponse(list(cities.values('id', 'name')), safe=False)


#