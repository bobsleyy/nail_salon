from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegistrationForm, LoginForm, VisitRegistrationForm, PhotoForm
from .models import VisitRegistration, Service, QuantityOfAddons, Addons, Photos, BeforeMadeBy


# Create your views here.


class HomepageView(View):
    """Widok strony domowej"""
    def get(self, request):
        if request.user.has_perm('nail_salon_app.view_all_visits'):
            if request.user.has_perm('nail_salon_app.view_my_visits'):
                all_visits = 1
                my_visits = 1
            else:
                all_visits = 1
                my_visits = 0
        elif request.user.has_perm('nail_salon_app.view_my_visits'):
            all_visits = 0
            my_visits = 1
        else:
            all_visits = 0
            my_visits = 0
        return render(request, "homepage.html", {"all_visits": all_visits, "my_visits": my_visits})


class RegistrationView(View):
    """Widok strony rejestracji"""
    def get(self, request):
        form = RegistrationForm
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            logname = form.cleaned_data['logname']
            passwd = form.cleaned_data['passwd']
            confirm_passwd = form.cleaned_data['confirm_passwd']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            if User.objects.filter(username=logname).exists():
                form.add_error('logname', 'Ten login jest już zajęty.')
                return render(request, 'registration.html', {'form': form})

            if passwd != confirm_passwd:
                form.add_error('confirm_passwd', 'Hasła nie są identyczne.')
                return render(request, 'registration.html', {'form': form})

            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Podany adres e-mail jest już używany.')
                return render(request, 'registration.html', {'form': form})

            else:
                user = User.objects.create_user(username=logname,
                                                password=passwd,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email)
                perm_view_my_visits = Permission.objects.get(codename='view_my_visits')
                user.user_permissions.add(perm_view_my_visits)
                user.save()
                userexist = 1
                logname = form.cleaned_data['logname']
                return render(request, 'registration.html', {'logname': logname,
                                                                            'userexist': userexist})
        else:
            return render(request, 'registration.html', {'form': form})


class LoginView(View):
    """Widok strony logowania"""
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            logname = form.cleaned_data['logname']
            passwd = form.cleaned_data['passwd']
            user = authenticate(username=logname, password=passwd)
            if user is not None:
                login(self.request, user)
                return redirect('homepage')
            else:
                logerror = 1
                return render(request,
                              'login.html',
                              {'logerror': logerror,
                                        'form': form})

        else:
            return render(request, 'exercises_app/login.html', {'form': form})


class LogoutView(View):
    """Funkcja wylogowania"""
    def get(self, request):
        logout(request)
        return redirect('/')


class VisitRegistrationView(View):
    """Widok rejestracji wizyty"""
    def get(self, request):
        form = VisitRegistrationForm()
        return render(request, "visit_registration.html", {'form': form})

    def post(self, request):
        form = VisitRegistrationForm(request.POST)
        if form.is_valid():

            datetime = f"{form.cleaned_data['date']} {form.cleaned_data['time']}"

            # service_type = form.cleaned_data['service_type']
            # service_type_id = service_type.id
            # length_type = form.cleaned_data['length_type']
            # length_type_id = length_type.id
            # service = Service.objects.filter(service_type_id=service_type_id).filter(length_type_id=length_type_id),

            service = form.cleaned_data['service']

            addons = form.cleaned_data['addons']
            addons_list = []
            for addon in addons:
                addons_list.append(addon)
            quantity = len(addons_list)
            quantity_ = QuantityOfAddons.objects.filter(quantity=quantity)

            if VisitRegistration.objects.filter(datetime=datetime).exists():
                form.add_error('time', 'Ten termin jest już zajęty.')
                return render(request, "visit_registration.html", {'form': form})

            new_visit = VisitRegistration.objects.create(
                first_name=form.cleaned_data['first_name'],
                second_name=form.cleaned_data['second_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                made_by=form.cleaned_data['made_by'],
                datetime=datetime,
                # service=service[0][0],
                service=service,
                quantity=quantity_[0],
            )
            if quantity == 0:
                new_visit.addons.add(Addons.objects.get(name='Brak'))
            else:
                new_visit.addons.add(*addons)

            visitexist = 1

            return render(request,
                          'visit_registration.html',
                          {'visitexist': visitexist, 'form': form})
            # return redirect('visit_registration')
        else:
            return render(request, "visit_registration.html", {'form': form})


class GalleryAddView(View):
    """"Widok dodawania zdjęć do galerii"""
    def get(self, request):
        form = PhotoForm

        return render(request, "gallery_add.html", {'form': form})

    def post(self, request):
        if request.user.has_perm('nail_salon_app.add_photos'):
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo_add = Photos.objects.create(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description'],
                    upload=request.FILES['photo']
                )
                photo_add.save()
                added_photo = 1
                return render(request, 'gallery_add.html', {'form': form, 'added_photo': added_photo})
            else:
                return render(request, "gallery_add.html", {'form': form})
        else:
            cant_add_photo = 1
            return render(request, "gallery_add.html", {'cant_add_photo': cant_add_photo})


class GalleryView(View):
    """Widok galerii"""
    def get(self, request):
        photos = Photos.objects.all()
        if request.user.has_perm('nail_salon_app.add_photos'):
            has_permm = 1
        else:
            has_permm = 0
        return render(request, "gallery.html", {'photos': photos, 'has_permm': has_permm})


class AllVisitsView(View):
    """Widok wszystkich wizyt (dla właściciel/administratora)"""
    def get(self, request):
        if request.user.has_perm('nail_salon_app.view_all_visits'):
            visits = VisitRegistration.objects.all()
            can_view_all_visits = 1
            return render(request, "all_visits.html", {'visits': visits,
                                                       'can_view_all_visits': can_view_all_visits})
        else:
            can_view_all_visits = 0
            return render(request, "all_visits.html", {'can_view_all_visits': can_view_all_visits})


class VisitDetailsView(View):
    """Widok detali konkretnej wizyty (dla właściciel/administratora)"""
    def get(self, request, id):
        if request.user.has_perm('nail_salon_app.view_all_visits'):
            visit = VisitRegistration.objects.get(id=id)
            addons = visit.addons.all()
            add = ""
            a = 0
            for addon in addons:
                if a >= 1:
                    add += f", {addons[a]}"
                    a += 1
                else:
                    add += f"{addons[a]}"
                    a += 1

            quan = QuantityOfAddons.objects.get(id=visit.quantity_id)
            before_made = BeforeMadeBy.objects.get(id=visit.made_by_id)

            cost = visit.service.cost + quan.add_cost + before_made.add_cost
            addon_time = 0
            for addon in addons:
                addon_time += addon.add_time
            duration = visit.service.execution_time + quan.add_time + addon_time
            h = round(duration / 60, 2)

            can_view_all_visits = 1

            ctx = {
                'first_name': visit.first_name,
                'second_name': visit.second_name,
                'email': visit.email,
                'phone': visit.phone,
                'datetime': visit.datetime,
                'duration': duration,
                'h': h,
                'service': visit.service,
                'addons': add,
                'cost': cost,
                'can_view_all_visits': can_view_all_visits
            }

            return render(request, "visit_details.html", ctx)
        else:
            can_view_all_visits = 0
            return render(request, "visit_details.html",
                          {'can_view_all_visits': can_view_all_visits})


class VisitsListView(View):
    """Widok listy wizyt (dla zwykłego użytkownika)"""
    def get(self, request):
        if request.user.has_perm('nail_salon_app.view_my_visits'):
            visits = VisitRegistration.objects.filter(first_name=request.user).values()
            can_view_my_visits = 1
            return render(request, "visits_list.html", {'visits': visits,
                                                       'can_view_my_visits': can_view_my_visits})
        else:
            can_view_my_visits = 0
            return render(request, "visits_list.html", {'can_view_my_visits': can_view_my_visits})






# class VisitsListView(View):
#     def get(self, request):
#         return render(request, "visits_list.html")



#
# class VisitsListView(View):
#     def get(self, request):
#         if request.user.has_perm('nail_salon_app.view_my_visits'):
#
#             visits = VisitRegistration.objects.filter(first_name=request.user).values()
#
#             datetime_list = []
#             duration_list = []
#             h_list = []
#             service_list = []
#             addons_list = []
#             cost_list = []
#
#             i = 0
#             ctx = {}
#             for visit in visits:
#
#                 addons = visit.addons.all()
#                 add = ""
#                 a = 0
#                 for addon in addons:
#                     if a >= 1:
#                         add += f", {addons[a]}"
#                         a += 1
#                     else:
#                         add += f"{addons[a]}"
#                         a += 1
#
#                 quan = QuantityOfAddons.objects.get(id=visit.quantity_id)
#                 before_made = BeforeMadeBy.objects.get(id=visit.made_by_id)
#
#                 cost = visit.service.cost + quan.add_cost + before_made.add_cost
#                 addon_time = 0
#                 for addon in addons:
#                     addon_time += addon.add_time
#                 duration = visit.service.execution_time + quan.add_time + addon_time
#                 h = round(duration / 60, 2)
#
#                 datetime_list.append(visit.datetime)
#                 duration_list.append(duration)
#                 h_list.append(h)
#                 service_list.append(visit.service)
#                 addons_list.append(add)
#                 cost_list.append(cost)
#
#
#
#
#             ctx.update({
#                     'datetime_list': datetime_list,
#                     'duration_list': duration_list,
#                     'h_list': h_list,
#                     'service_list': service_list,
#                     'addons_list': addons_list,
#                     'cost_list': cost_list,
#                     'visits': visits
#                 })
#             can_view_my_visits = 1
#             ctx.update({'can_view_my_visits': can_view_my_visits})
#             return render(request, "visits_list.html", ctx)
#         else:
#             can_view_my_visits = 0
#             return render(request, "visits_list.html",
#                           {'can_view_all_visits': can_view_my_visits})

#
# {%  extends "base.html" %}
# {% block title %}
#     Lista wizyt nails_l3lack - salon paznokci
# {% endblock %}
# {% block content %}
#     <h2>Lista wizyt</h2>
#     {% if can_view_my_visits %}
#         {{visit.first_name}}<br>
# #             {{visit.second_name}}<br>
#     {% else %}
#         <p>Nie masz uprawnień do przeglądania wizyt</p><br><br>
#     {% endif %}
# {% endblock %}