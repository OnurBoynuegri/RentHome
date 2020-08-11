from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from house.models import Category, House
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import UserRentHouseForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile}
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile': profile,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarıyla değişti')
            return redirect('change_password')
        else:
            messages.error(request, 'Hatalı işlem', '<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        return render(request, 'change_password.html', {
            'form': form,
            'category': category,
            'profile': profile,
        })


@login_required(login_url='/login')
def user_rent(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    house = House.objects.filter(user_id=current_user.id)
    form = UserRentHouseForm()
    context = {
        'category': category,
        'house': house,
        'profile': profile,
        'form': form
    }
    return render(request, 'user_rent.html', context)


@login_required(login_url='/login')
def add_rent(request):
    if request.method == 'POST':
        form = UserRentHouseForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = House()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.address = form.cleaned_data['address']
            data.price = form.cleaned_data['price']
            data.room = form.cleaned_data['room']
            data.balcony = form.cleaned_data['balcony']
            data.heating = form.cleaned_data['heating']
            data.stuff = form.cleaned_data['stuff']
            data.status = 'False'
            data.detail = form.cleaned_data['detail']
            data.slug = form.cleaned_data['slug']
            data.save()
            messages.success(request, "Başarıyla eklendi")
            return HttpResponseRedirect('/user/userrent')
        else:
            messages.success(request, " Hata")
            return HttpResponseRedirect('/')
    else:
        category = Category.objects.all()
        form = UserRentHouseForm()
        context = {
            'category': category,
            'form': form
        }
        return render(request, 'user_addrent.html', context)
