from  django.shortcuts import render,redirect




def index(request):
    return render(request,'index.html')



def list(request):
    return render(request,'listing.html')


def product(request):
    return render(request,'product-detail.html')