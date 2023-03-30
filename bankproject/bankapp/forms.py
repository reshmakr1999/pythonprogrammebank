# from django import forms
#
# from .import views
#
# class RegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     age = forms.IntegerField()
#     gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')))
#     phone_number = forms.CharField(max_length=20)
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea)
#     district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select district")
#     branch = forms.ModelChoiceField(queryset=Branch.objects.none(), empty_label="Select branch")
#     # country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select district")
#     # city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select district")
#
#     account_type = forms.ChoiceField(choices=(('SA', 'Savings Account'), ('CA', 'Current Account')))
#     materials_provide = forms.MultipleChoiceField(choices=(('DC', 'Debit Card'), ('CC', 'Credit Card'), ('CB', 'Cheque Book')), widget=forms.CheckboxSelectMultiple)
#
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['branch'].queryset = Branch.objects.none()
#
#         if 'district' in self.data:
#             try:
#                 district_id = int(self.data.get('district'))
#                 self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass
#
#
#
#
# from django import forms
#
# from bankapp.models import Person,Branch,District
#
#
# class PersonCreationForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = '__all__'
#
#     def __init__(self, args, *kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['city'].queryset = Branch.objects.none()
#
#         if 'country' in self.data:
#             try:
#                 country_id = int(self.data.get('country'))
#                 self.fields['city'].queryset = Branch.objects.filter(country_id=country_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

from django.shortcuts import render
from .models import Registration


def RegistrationForm(request):
    if request.method == 'get':
        # Retrieve the data from the form and save it to the database
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        materials_provide = request.POST.getlist('materials_provide')

        registration = Registration(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
            materials_provide=','.join(materials_provide),
        )
        registration.save()

        return render(request, 'success.html')
    else:
        # Render the registration form
        return render(request, 'registration_form.html')


