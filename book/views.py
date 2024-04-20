from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def updatebook(request):
    return render(request,'update.html')

def addbook(request):
    return render(request,'add.html')

def listbook(request):
    return render(request,'delete.html')
 
def searchofbook(request):
    if request.method=="POST":
        title=request.POST.get("title")
        dic={}
        dic["_id"]=title
        print(dic)

    return render(request,"success.html")