from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Realtors
from property.models import Property


# Create Realtors
def add_realtors(request):
    if request.method == 'POST':
        realtors_data = Realtors(realtor_username=request.POST['realtor_username'],
                                 realtor_name=request.POST['realtor_name'],
                                 email=request.POST['email'],
                                 mobile=request.POST['mobile'],
                                 created_by=request.POST['created_by'],
                                 realtor_description=request.POST['realtor_description'],
                                 realtor_image=request.FILES['realtor_image'])
        realtors_data.save()
        return redirect('/manage_realtors')
    else:
        return render(request, 'realtors/add_realtors.html')


# Read Realtors
def manage_realtors(request):
    realtors = Realtors.objects.filter()
    return render(request, 'realtors/manage_realtors.html', {'realtors': realtors})


# Edit Realtor
def edit_realtor(request, id):

    if request.method == 'POST':
        realtors = Realtors.objects.get(id=id)
        realtor_image = request.FILES.get('realtor_image')
        # realtor_username = request.POST.get('realtor_username')
        # realtors.realtor_username = realtor_username
        realtors.realtor_name = request.POST['realtor_name']
        realtors.email = request.POST['email']
        realtors.realtor_description = request.POST['realtor_description']
        if request.FILES or None:
            realtors.realtor_image = realtor_image
        realtors.mobile = request.POST['mobile']
        realtors.created_by = request.POST['created_by']
        realtors.save()
        return redirect('/manage_realtors')
    else:
        realtors = Realtors.objects.get(id=id)
        return render(request, 'realtors/edit_realtor.html', {'realtors': realtors})


# Delete Realtors
def delete_realtors(request, id):
    realtors = Realtors.objects.get(id=id)
    realtors.delete()
    return redirect('/manage_realtors')


# Realtors Profile
def realtor_profile(request, slug):
    realtor_data = Realtors.objects.filter(realtor_slug=slug)
    context = {
        'realtor_data': realtor_data
    }
    return render(request, 'realtors/realtor_profile.html', context)


def all_realtors(request):
    realtor_data = Realtors.objects.all()
    context = {
        'realtor_data': realtor_data
    }
    return render(request, 'realtors/all_realtors_list.html', context)
