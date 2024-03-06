from django import forms

from .models import ServiceType, BeforeMadeBy, Addons, LengthType, QuantityOfAddons, Service


class LoginForm(forms.Form):
    """Form for login user"""
    logname = forms.CharField(max_length=64, label="Nazwa użytkownika")
    passwd = forms.CharField(widget=forms.PasswordInput(), label="Hasło")


class RegistrationForm(forms.Form):
    """Form to register a new user"""
    logname = forms.CharField(max_length=64, label="Nazwa użytkownika")
    passwd = forms.CharField(widget=forms.PasswordInput(), max_length=64, label="Hasło")
    confirm_passwd = forms.CharField(widget=forms.PasswordInput(), max_length=64, label="Powtórz hasło")
    first_name = forms.CharField(max_length=64, label="Imię")
    last_name = forms.CharField(max_length=64, label="Nazwisko")
    email = forms.CharField(max_length=64, label="e-mail")


class VisitRegistrationForm(forms.Form):
    """Form to register of visit"""
    first_name = forms.CharField(max_length=64, label="Imię")
    second_name = forms.CharField(max_length=64, label="Nazwisko")
    email = forms.CharField(max_length=64, label="e-mail")
    phone = forms.CharField(max_length=12, label="Numer telefonu")
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    # service_type = forms.ModelChoiceField(queryset=ServiceType.objects.all(), label="Typ usługi")
    # length_type = forms.ModelChoiceField(queryset=LengthType.objects.all(), label="Długość (wymiar na formie)")

    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="Typ usługi - długość (wymiar na formie)")

    # length_type = forms.ModelChoiceField(queryset=Service.objects.filter(service_type_id=service_type_id),
    # label="Długość (wymiar na formie)")

    made_by = forms.ModelChoiceField(queryset=BeforeMadeBy.objects.all(), label="Czy masz na sobie stylizację wykonaną "
                                                                                "w innym salonie?")
    addons = forms.ModelMultipleChoiceField(queryset=Addons.objects.all().exclude(name='Brak'), label="Dodatki",
                                            widget=forms.CheckboxSelectMultiple, required=False)


class PhotoForm(forms.Form):
    """Form to upload photos"""
    name = forms.CharField(max_length=64, label="Nazwa zdjęcia")
    description = forms.CharField(widget=forms.Textarea, label="Opis zdjęcia")
    photo = forms.FileField()
