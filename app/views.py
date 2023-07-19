from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    d={'usfo':UserForm(),'pfo':ProfileForm()}

    if request.method=='POST' and request.FILES:
        usfd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if usfd.is_valid() and pfd.is_valid():
            nsufo=usfd.save(commit=False)
            spw=usfd.cleaned_data['password']#spw=SubmittedPassWord
            nsufo.set_password(spw)
            nsufo.save()

            nspfo=pfd.save(commit=False)
            nspfo.username=nsufo
            nspfo.save()

            return HttpResponse('data is submited')
        return HttpResponse('data is not valid')

    return render(request,'registration2.html',d)