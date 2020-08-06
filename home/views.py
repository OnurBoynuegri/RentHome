import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from house.models import House, Category, Images
from home.forms import SearchForm, SignUpForm


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = House.objects.all()[:4]
    category = Category.objects.all()
    randhouse = House.objects.all().order_by('?')
    lasthouseFirst = House.objects.all().order_by('-id')[:3]
    lasthouseSecond = House.objects.all().order_by('-id')[3:6]
    context = {'setting': setting,
               'sliderdata': sliderdata,
               'category': category,
               'randhouse': randhouse,
               'lasthouseFirst': lasthouseFirst,
               'lasthouseSecond': lasthouseSecond,
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    if request.method == 'POST':  # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kuruldu
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesasjınız başarılı bir şekilde gönderildi. Teşekkürler")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting,
               'form': form,
               'category': category}
    return render(request, 'iletisim.html', context)


def category_houses(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    house = House.objects.filter(category_id=id)
    context = {'house': house,
               'category': category,
               'categorydata': categorydata}
    return render(request, 'houses.html', context)

    image_tag.short_description = 'Image'


def house_detail(request, id, slug):
    category = Category.objects.all()
    house = House.objects.get(pk=id)
    images = Images.objects.filter(house_id=id)
    context = {'category': category,
               'house': house,
               'images': images,
               }
    return render(request, 'house_detail.html', context)


def house_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                houses = House.objects.filter(title__icontains=query)
            else:
                houses = House.objects.filter(title__icontains=query, category_id=catid)
            context = {'houses': houses,
                       'category': category}
            return render(request, 'house_search.html', context)
    return HttpResponseRedirect('/')


def house_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        house = House.objects.filter(title__icontains=q)
        results = []
        for rs in house:
            house_json = {}
            house_json = rs.title
            results.append(house_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Login Hatası!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup.html', context)
