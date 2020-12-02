from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Property, Users_Property
from realtors.models import Realtors
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices


def index(request):
    realtors = Realtors.objects.all()
    property_details = Property.objects.all()[:6]
    property_details_users = Users_Property.objects.all()[:6]

    context = {
        "property_details": property_details,
        'realtors': realtors,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'property_details_users': property_details_users
    }
    return render(request, 'property/index.html', context)


def view_more(request):
    property_details = Property.objects.all()

    paginator = Paginator(property_details, 6)

    page = request.GET.get('page')
    paged_property = paginator.get_page(page)

    context = {
        "property_details": paged_property,
    }
    return render(request, 'property/property_list.html', context)


def about(request):
    return render(request, 'property/about.html')


def services(request):
    return render(request, 'property/services.html')


# Add Property
def add_property(request):
    if request.method == 'POST':
        
        property_details = Property(
            realtor_id=request.POST['realtor_id'],
            title=request.POST['title'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            zipcode=request.POST['zipcode'],
            description=request.POST['description'],
            price=request.POST['price'],
            rooms=request.POST['rooms'],
            bathrooms=request.POST['bathrooms'],
            sqft=request.POST['sqft'],
            plot_size=request.POST['plot_size'],
            property_image_main=request.FILES['property_image_main'],
            property_image1=request.FILES['property_image1'],
            is_active=request.POST['is_active'])
        property_details.save()
        return redirect('/manage_property')
    else:
        realtors = Realtors.objects.all()
        return render(request, 'property/add_property.html', {'realtors': realtors})


# Manage Property
def manage_property(request):
    property_details = Property.objects.all()
    return render(request, 'property/manage_property.html', {'property_details': property_details})


# Edit Property
def edit_property(request, id):
    if request.method == 'POST':
        property_details = Property.objects.get(id=id)
        property_details.title = request.POST['title']
        property_details.address = request.POST['address']
        property_details.city = request.POST['city']
        property_details.state = request.POST['state']
        property_details.zipcode = request.POST['zipcode']
        property_details.tidescriptiontle = request.POST['description']
        property_details.price = request.POST['price']
        property_details.rooms = request.POST['rooms']
        property_details.bathrooms = request.POST['bathrooms']
        property_details.sqft = request.POST['sqft']
        property_details.plot_size = request.POST['plot_size']
        property_details.is_active = request.POST['is_active']
        property_details.save()
        return redirect('/manage_property')
    else:
        property_details = Property.objects.get(id=id)
        return render(request, 'property/edit_property.html', {'property_details': property_details})


# Delete Property
def delete_property(request, id):
    property_details = Property.objects.get(id=id)
    property_details.delete()
    return redirect('/manage_property')


# Showing property via title wise
def property_details(request, slug):
    property_data = Property.objects.filter(property_slug=slug)
    return render(request, 'property/property_details.html', {'property_data': property_data})


def search(request):
    queryset_list = Property.objects.order_by('-created_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'rooms' in request.GET:
        rooms = request.GET['rooms']
        if rooms:
            queryset_list = queryset_list.filter(rooms__lte=rooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'properties': queryset_list,
        'values': request.GET,
    }

    return render(request, 'property/search.html', context)


# User Add property
# def user_property_add(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         title = request.POST['title']
#         address = request.POST['address']
#         city = request.POST['city']
#         state = request.POST['state']
#         zipcode = request.POST['zipcode']
#         description = request.POST['description']
#         price = request.POST['price']
#         rooms = request.POST['rooms']
#         bedrooms = request.POST['bedrooms']
#         sqft = request.POST['sqft']
#         plot_size = request.POST['plot_size']
#         property_image_main = request.FILES['property_image_main']
#         property_image1 = request.FILES['property_image1']
#         property_image2 = request.FILES['property_image2']
#         property_image3 = request.FILES['property_image3']
#         property_image4 = request.FILES['property_image4']

#         property_details = Users_Property(
#             user_id=user_id,
#             title=title,
#             address=address,
#             city=city,
#             state=state,
#             zipcode=zipcode,
#             description=description,
#             price=price,
#             rooms=rooms,
#             bedrooms=bedrooms,
#             sqft=sqft,
#             plot_size=plot_size,
#             property_image_main=property_image_main,
#             property_image1=property_image1,
#             property_image2=property_image2,
#             property_image3=property_image3,
#             property_image4=property_image4,
#         )
#         property_details.save()
#         return redirect('/manage_property')
#     else:
#         return render(request, 'property/user_property_add.html')
