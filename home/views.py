from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from house.models import House, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = House.objects.all()[:4]
    category = Category.objects.all()
    context = {'setting': setting,
               'sliderdata': sliderdata,
               'category': category}
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