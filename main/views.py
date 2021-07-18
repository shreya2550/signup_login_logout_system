from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import beneficiary
from .forms import beneficiaryForm
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator

import os
from twilio.rest import Client

# Create your views here.
def home(request):
    data=beneficiary.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        data=beneficiary.objects.filter(Q(full_name__icontains=q)|Q(phone_number__icontains=q)|Q(email__icontains=q))
    paginator=Paginator(data,1)
    page_number=request.GET.get('page',1)
    data=paginator.get_page(page_number)
    return render(request,'home.html',{'data':data})

#Add Beneficiary
def addBeneficiary(request):
    form=beneficiaryForm
    if request.method=='POST':
        saveForm=beneficiaryForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Beneficiary has been added successfully.')
    print("Inserted")
    return render(request,'add-beneficiary.html',{'form':form})

#Update Beneficiary
def updateBeneficiary(request,id):
    Beneficiary=beneficiary.objects.get(id=id)
    if request.method=='POST':
        saveForm=beneficiaryForm(request.POST,instance=Beneficiary)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Beneficiary details has been updated successfully.')
    form=beneficiaryForm(instance=Beneficiary)
    return render(request,'update-beneficiary.html',{'form':form})

#Delete Beneficiary
def deleteBeneficiary(request,id):
    beneficiary.objects.filter(id=id).delete()
    return redirect('/')

#Sending Email Reminder
def sendEmail(request,id):
    Beneficiary=beneficiary.objects.get(id=id) 
    #send_mail(
    #    'Next Renewal Reminder',
    #  'Your Renewal deadline is on '+ str(Beneficiary.next_renewal_date),
    #    'admin@example.com',
      #  [Beneficiary.email],
        #fail_silently=False,
    #)

    account_sid = "##ENTER SID##"
    auth_token = "##ENTER AUTH TOKEN##"

    client = Client(account_sid, auth_token)

    client.messages.create(from_="##ENTER TWILIO PHONE NUMBER##",
                       to=str(Beneficiary.phone_number),
                       body='You just sent an SMS from Python using Twilio! https://accounts.google.com/')

    messages.success(request,'Mail has been sent.')
    return redirect('/')

