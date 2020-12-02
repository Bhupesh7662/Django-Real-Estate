from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Contact, Inquiry
from realtors.models import Realtors
from property.models import Property


def contact(request):
    if request.method == 'POST':
        contact_data = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            message=request.POST['message'])
        contact_data.save()
        return redirect('/contact')
    return render(request, 'contact/contact_us.html')


def feedback(request):
    contact_data = Contact.objects.all()
    context = {
        'contact_data': contact_data
    }
    return render(request, 'contact/feedback.html', context)


def delete_feedback(request, id):
    contact_data = Contact.objects.get(id=id)
    contact_data.delete()
    return redirect('/contact/feedback')


# Inquiries
def make_inquiry(request):
    if request.method == 'POST':
        property_detail = request.POST.get('property_detail')
        property_image = request.POST.get('property_image')
        realtor_email = request.POST['realtor_email']
        realtor_mobile = request.POST['realtor_mobile']
        inquiry_email = request.POST['inquiry_email']
        inquiry_phone_number = request.POST['inquiry_phone_number']
        inquiry_name = request.POST['inquiry_name']

        inquiry_data = Inquiry(
            inquiry_name=request.POST['inquiry_name'],
            inquiry_email=request.POST['inquiry_email'],
            inquiry_phone_number=request.POST['inquiry_phone_number'],
            inquiry_message=request.POST['inquiry_message'],
            property_id=request.POST['property_id'],
            user_id=request.POST['user_id'],
            property_detail=property_detail,
            property_image=property_image)
        slug = request.POST['slug']

        if request.user.is_authenticated:
            inquiry = Inquiry.objects.all()
            user_id = request.user.id
            property_id = request.POST['property_id']

            has_contacted = Inquiry.objects.all().filter(
                user_id=user_id, property_id=property_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this property')
                return redirect('/property_details/' + slug)

        inquiry_data.save()

        # Sending Mails
        realtor_mail = ''' There has been an inquiry for Property you have added. Sign into to webiste for more details'''

        # To Realtor
        send_mail(
            'Property Inquiry: ' + property_detail,
            realtor_mail + ', Contact details of inquiry user:  ' +
            inquiry_name + ' ' + inquiry_phone_number,
            'yourmail@gmail.com',
            [realtor_email, 'yourmail@gmail.com'],
            fail_silently=False
        )
        # To Inquiry Customer
        user_mail = '''You have made inquiry for: '''
        send_mail(
            'Property Inquiry: ' + property_detail,
            user_mail + ' ' + property_detail + '. Realtor will get back to you soon' +
            ' or contact reatil: Contact details of realtor: ' + realtor_mobile,
            'yourmail@gmail.com',
            [inquiry_email, 'yourmail@gmail.com'],
            fail_silently=False
        )


        messages.success(
            request, "Your inquiry has been submitted successfully, Realtor will get back to you soon")
        return redirect('/property_details/' + slug)

    return render(request, '/property_details')


def inquiry(request):
    inquiry_data = Inquiry.objects.all()
    context = {
        'inquiry_data': inquiry_data
    }
    return render(request, 'contact/user_inquiries.html', context)


def delete_inquiry(request, id):
    inquiry_data = Inquiry.objects.get(id=id)
    inquiry_data.delete()
    return redirect('/contact/inquiry')
