from django.shortcuts import render
import csv
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_bank(self):
    with open('C:\\Users\\hp\\OneDrive\\Desktop\\Django projects\\Nani\\Scripts\\project37\\app\\bank.csv','r') as FO:
        IDO = csv.reader(FO)
        for i in IDO:
            bn = i[0].strip()
            BO = Bank(bank_name=bn)
            BO.save()
    return HttpResponse('<center><h1>Banks data is successfully inserted')


def bank_data(request):
    BOD = Bank.objects.all()
    d={'BOD':BOD}

    return render(request,'bank_data.html',d)




def insert_branch(self):
    with open('C:\\Users\\hp\\OneDrive\\Desktop\\Django projects\\Nani\\Scripts\\project37\\app\\branch1.csv','r') as FO:
        IDO = csv.reader(FO)
        next(IDO)
        for i in IDO:
            bn = i[0]
            BO = Bank.objects.filter(bank_name=bn)
            if BO:
                ifs = i[1]
                br = i[2]
                ad = i[3]
                co = i[4]
                ci = i[5]
                di = i[6]
                st = i[7]
                BRO = Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=di,state=st)
                BRO.save()
    return HttpResponse('<center><h1>Branchs data is successfully inserted')

def bank_fulldetail(request):
    BRDO = Branch.objects.all()
    d={'BRDO':BRDO}
    return render(request,'bank_fulldetail.html',d)