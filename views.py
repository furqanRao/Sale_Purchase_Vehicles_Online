from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from vehicles_app.forms import UserForm, AddFile
from .models import Posts, UserInfo
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse, resolve
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sys
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    queryset = Posts.objects.all().order_by('-date')
    #navbar search filter query
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(city__icontains=query) or queryset.filter(title__icontains=query) or queryset.filter(details__icontains=query)
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()


    #sidebar full search filter query
    cat_query = request.GET.get("category")
    city_query = request.GET.get("city")
    brand_query = request.GET.get("brand")
    model_query = request.GET.get("modelyear")
    condition_query = request.GET.get("condition")
    mileage_from_query = request.GET.get("mileagefrom")
    mileage_to_query = request.GET.get("mileageto")
    price_from_query = request.GET.get("pricefrom")
    price_to_query = request.GET.get("priceto")

    if (cat_query and city_query and brand_query and condition_query and mileage_from_query and mileage_to_query and price_from_query and price_to_query) or model_query:
        queryset = queryset.filter(Q(category=cat_query) & Q(city=city_query) & Q(brand=brand_query) & Q(condition=condition_query) or Q(modelyear=model_query))
        queryset = queryset.filter(Q(mileage__gte=mileage_from_query) & Q(price__gte=price_from_query))
        queryset = queryset.filter(Q(mileage__lte=mileage_to_query) & Q(price__lte=price_to_query))
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()



    paginator = Paginator(queryset, 5)
    page = request.GET.get('page' , 1)
    context = paginator.page(page)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'vehicles_app/index.html',  {'context':context, 'queryset':queryset, 'query':query,
                                    'city_query':city_query, 'brand_query':brand_query, 'model_query':model_query,
                                    'condition_query':condition_query, 'mileage_from_query':mileage_from_query,
                                    'mileage_to_query':mileage_to_query, 'price_from_query':price_from_query,
                                    'price_to_query':price_to_query, 'cat_query':cat_query})


def cars(request):
    queryset = Posts.objects.filter(category="cars").order_by('-date')

    #navbar search filter
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(city__icontains=query) or queryset.filter(title__icontains=query) or queryset.filter(details__icontains=query)
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()

    #sidebar full search filter query
    cat_query = request.GET.get("category")
    city_query = request.GET.get("city")
    brand_query = request.GET.get("brand")
    model_query = request.GET.get("modelyear")
    condition_query = request.GET.get("condition")
    mileage_from_query = request.GET.get("mileagefrom")
    mileage_to_query = request.GET.get("mileageto")
    price_from_query = request.GET.get("pricefrom")
    price_to_query = request.GET.get("priceto")

    if (cat_query and city_query and brand_query and condition_query and mileage_from_query and mileage_to_query and price_from_query and price_to_query) or model_query:
        queryset = queryset.filter(Q(category=cat_query) & Q(city=city_query) & Q(brand=brand_query) & Q(condition=condition_query) or Q(modelyear=model_query))
        queryset = queryset.filter(Q(mileage__gte=mileage_from_query) & Q(price__gte=price_from_query))
        queryset = queryset.filter(Q(mileage__lte=mileage_to_query) & Q(price__lte=price_to_query))
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()



    paginator = Paginator(queryset, 5)
    page = request.GET.get('page' , 1)
    context = paginator.page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'vehicles_app/cars.html',  {'context':context, 'queryset':queryset, 'query':query,
                                    'city_query':city_query, 'brand_query':brand_query, 'model_query':model_query,
                                    'condition_query':condition_query, 'mileage_from_query':mileage_from_query,
                                    'mileage_to_query':mileage_to_query, 'price_from_query':price_from_query,
                                    'price_to_query':price_to_query, 'cat_query':cat_query})

def bikes(request):
    queryset = Posts.objects.filter(category="motorbikes").order_by('-date')

    #navbar search filter
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(city__icontains=query) or queryset.filter(title__icontains=query) or queryset.filter(details__icontains=query)
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()

    #sidebar full search filter query
    cat_query = request.GET.get("category")
    city_query = request.GET.get("city")
    brand_query = request.GET.get("brand")
    model_query = request.GET.get("modelyear")
    condition_query = request.GET.get("condition")
    mileage_from_query = request.GET.get("mileagefrom")
    mileage_to_query = request.GET.get("mileageto")
    price_from_query = request.GET.get("pricefrom")
    price_to_query = request.GET.get("priceto")

    if (cat_query and city_query and brand_query and condition_query and mileage_from_query and mileage_to_query and price_from_query and price_to_query) or model_query:
        queryset = queryset.filter(Q(category=cat_query) & Q(city=city_query) & Q(brand=brand_query) & Q(condition=condition_query) or Q(modelyear=model_query))
        queryset = queryset.filter(Q(mileage__gte=mileage_from_query) & Q(price__gte=price_from_query))
        queryset = queryset.filter(Q(mileage__lte=mileage_to_query) & Q(price__lte=price_to_query))
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()

    paginator = Paginator(queryset, 5)
    page = request.GET.get('page' , 1)
    context = paginator.page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'vehicles_app/bikes.html',  {'context':context, 'queryset':queryset, 'query':query,
                                    'city_query':city_query, 'brand_query':brand_query, 'model_query':model_query,
                                    'condition_query':condition_query, 'mileage_from_query':mileage_from_query,
                                    'mileage_to_query':mileage_to_query, 'price_from_query':price_from_query,
                                    'price_to_query':price_to_query, 'cat_query':cat_query})

def trucks(request):
    queryset = Posts.objects.filter(category="trucks").order_by('-date')

    #navbar search filter
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(city__icontains=query) or queryset.filter(title__icontains=query) or queryset.filter(details__icontains=query)
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()

    #sidebar full search filter query
    cat_query = request.GET.get("category")
    city_query = request.GET.get("city")
    brand_query = request.GET.get("brand")
    model_query = request.GET.get("modelyear")
    condition_query = request.GET.get("condition")
    mileage_from_query = request.GET.get("mileagefrom")
    mileage_to_query = request.GET.get("mileageto")
    price_from_query = request.GET.get("pricefrom")
    price_to_query = request.GET.get("priceto")

    if (cat_query and city_query and brand_query and condition_query and mileage_from_query and mileage_to_query and price_from_query and price_to_query) or model_query:
        queryset = queryset.filter(Q(category=cat_query) & Q(city=city_query) & Q(brand=brand_query) & Q(condition=condition_query) or Q(modelyear=model_query))
        queryset = queryset.filter(Q(mileage__gte=mileage_from_query) & Q(price__gte=price_from_query))
        queryset = queryset.filter(Q(mileage__lte=mileage_to_query) & Q(price__lte=price_to_query))
        for q in queryset:
            obj = Posts.objects.get(id=q.id)
            obj.search_counter = obj.search_counter+1
            obj.save()

    paginator = Paginator(queryset, 5)
    page = request.GET.get('page' , 1)
    context = paginator.page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'vehicles_app/trucks.html',  {'context':context, 'queryset':queryset, 'query':query,
                                    'city_query':city_query, 'brand_query':brand_query, 'model_query':model_query,
                                    'condition_query':condition_query, 'mileage_from_query':mileage_from_query,
                                    'mileage_to_query':mileage_to_query, 'price_from_query':price_from_query,
                                    'price_to_query':price_to_query, 'cat_query':cat_query})


@login_required
def myposts(request):
    queryset = Posts.objects.filter(user=request.user).order_by('-date')

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(city__icontains=query) or queryset.filter(title__icontains=query) or queryset.filter(details__icontains=query)


    #sidebar full search filter query
    cat_query = request.GET.get("category")
    city_query = request.GET.get("city")
    brand_query = request.GET.get("brand")
    model_query = request.GET.get("modelyear")
    condition_query = request.GET.get("condition")
    mileage_from_query = request.GET.get("mileagefrom")
    mileage_to_query = request.GET.get("mileageto")
    price_from_query = request.GET.get("pricefrom")
    price_to_query = request.GET.get("priceto")

    if (cat_query and city_query and brand_query and condition_query and mileage_from_query and mileage_to_query and price_from_query and price_to_query) or model_query:
        queryset = queryset.filter(Q(category=cat_query) & Q(city=city_query) & Q(brand=brand_query) & Q(condition=condition_query) or Q(modelyear=model_query))
        queryset = queryset.filter(Q(mileage__gte=mileage_from_query) & Q(price__gte=price_from_query))
        queryset = queryset.filter(Q(mileage__lte=mileage_to_query) & Q(price__lte=price_to_query))


    paginator = Paginator(queryset, 5)
    page = request.GET.get('page' , 1)
    context = paginator.page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'vehicles_app/myposts.html',  {'context':context, 'queryset':queryset, 'query':query,
                                    'city_query':city_query, 'brand_query':brand_query, 'model_query':model_query,
                                    'condition_query':condition_query, 'mileage_from_query':mileage_from_query,
                                    'mileage_to_query':mileage_to_query, 'price_from_query':price_from_query,
                                    'price_to_query':price_to_query, 'cat_query':cat_query})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



class FileDelete(DeleteView):
    model = Posts
    success_url = reverse_lazy('index')
    success_message = "Post deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FileDelete, self).delete(request, *args, **kwargs)


def update_post(request, post_id):
    post_form = Posts.objects.get(pk=post_id)
    list_count = 2
    if request.method == "POST":
        form = AddFile(request.POST, request.FILES, instance=post_form)
        if form.is_valid():
            form.category = request.POST.get('category')
            form.title = request.POST.get('title')
            form.city = request.POST.get('city')
            form.price = request.POST.get('price')
            form.brand = request.POST.get('brand')
            form.modelyear = request.POST.get('modelyear')
            form.condition = request.POST.get('condition')
            form.mileage = request.POST.get('mileage')
            form.details = request.POST.get('details')
            form.full_name = request.POST.get('full_name')
            form.phone = request.POST.get('phone')
            form.image = request.POST.get('image')
            form.image1 = request.POST.get('image1')
            form.image2 = request.POST.get('image2')
            form.image3 = request.POST.get('image3')
            form.image4 = request.POST.get('image4')
            form.image5 = request.POST.get('image5')
            form.image6 = request.POST.get('image6')
            form.image7 = request.POST.get('image7')
            form.image8 = request.POST.get('image8')
            form.image9 = request.POST.get('image9')
            form.user = request.user
            form.save()

            messages.success(request, 'Post updated Successfully!')
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = AddFile(request.FILES, instance=post_form)
    return render(request, 'vehicles_app/update_post.html', {'form': form, 'post_form':post_form, 'post_id': post_id, 'list_count':list_count})


def frequently_searched(request):
    queryset = Posts.objects.filter(search_counter__gte=2).order_by('-search_counter')

    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(city__icontains=query) or queryset.filter(title__icontains=query) or queryset.filter(details__icontains=query)


    #sidebar full search filter query
    cat_query = request.GET.get("category")
    city_query = request.GET.get("city")
    brand_query = request.GET.get("brand")
    model_query = request.GET.get("modelyear")
    condition_query = request.GET.get("condition")
    mileage_from_query = request.GET.get("mileagefrom")
    mileage_to_query = request.GET.get("mileageto")
    price_from_query = request.GET.get("pricefrom")
    price_to_query = request.GET.get("priceto")

    if (cat_query and city_query and brand_query and condition_query and mileage_from_query and mileage_to_query and price_from_query and price_to_query) or model_query:
        queryset = queryset.filter(Q(category=cat_query) & Q(city=city_query) & Q(brand=brand_query) & Q(condition=condition_query) or Q(modelyear=model_query))
        queryset = queryset.filter(Q(mileage__gte=mileage_from_query) & Q(price__gte=price_from_query))
        queryset = queryset.filter(Q(mileage__lte=mileage_to_query) & Q(price__lte=price_to_query))



    paginator = Paginator(queryset, 5)
    page = request.GET.get('page' , 1)
    context = paginator.page(page)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'vehicles_app/frequently_searched.html', {'context':context, 'queryset':queryset, 'query':query,
                                    'city_query':city_query, 'brand_query':brand_query, 'model_query':model_query,
                                    'condition_query':condition_query, 'mileage_from_query':mileage_from_query,
                                    'mileage_to_query':mileage_to_query, 'price_from_query':price_from_query,
                                    'price_to_query':price_to_query, 'cat_query':cat_query})


def compare(request):
    cars_query = Posts.objects.filter(category='cars')
    bikes_query = Posts.objects.filter(category='motorbikes')
    trucks_query = Posts.objects.filter(category='trucks')
    if request.method == "POST":
        query1 = request.POST.get("firstcar")
        query2 = request.POST.get("secondcar")
        queryset1 = Posts.objects.filter(id=query1)
        queryset2 = Posts.objects.filter(id=query2)

        return render(request, 'vehicles_app/compare.html', {'queryset1':queryset1, 'queryset2':queryset2, 'cars_query':cars_query, 'bikes_query':bikes_query, 'trucks_query':trucks_query})

    return render(request, 'vehicles_app/compare.html', {'cars_query':cars_query, 'bikes_query':bikes_query, 'trucks_query':trucks_query})


def data(request, post_id):
    if request.method == "GET":
        que = Posts.objects.filter(id=post_id)
        queryset = que
        length = len(queryset)


    return render(request, 'vehicles_app/data.html', {'queryset':queryset , 'length':range(length)})


def signUp(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        em = request.POST.get('email')
        if User.objects.filter(username=user).exists() or User.objects.filter(email=em).exists():
            return HttpResponse("Account already exists with this username or email!")
        else:
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                messages.success(request, 'You have been registered successfully!')
                return HttpResponseRedirect(reverse('index'))

            else:
                print(user_form.errors)

    else:
        user_form = UserForm()


    return render(request,'vehicles_app/signUp.html',{'user_form':user_form,})




def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account is not Active")
        else:
            return HttpResponse("Invalid Login")
    else:
        return render(request,'vehicles_app/user_login.html',{})


@login_required
def addfile(request):
    if request.method == 'POST':
        form = AddFile(request.POST, request.FILES)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.user = request.user
            post_form.save()


            messages.success(request, 'Post submitted Successfully!')
            return HttpResponseRedirect(reverse('index'))

        else:
            print(form.errors)
    else:
        form = AddFile()

    return render(request,'vehicles_app/addfile.html',
                        {'form': form,})
