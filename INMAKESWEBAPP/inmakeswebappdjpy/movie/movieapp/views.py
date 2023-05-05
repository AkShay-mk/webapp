from django.shortcuts import render,redirect
from . models import movie
from .forms import movieform


# Create your views here.
def index(request):
    moviee=movie.objects.all()
    return render(request,'index.html',{'mv':moviee})
    
def detail(request,movie_id):
    moviee=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'moviee':moviee})
    
def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        year=request.POST.get('year',)
        desc=request.POST.get('desc',)
        img=request.FILES['imag']
        moviee=movie(name=name,year=year,desc=desc,imag=img)
        moviee.save()
        
    return render(request,'add.html')
    
    
def update(request,id):
    moviee=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=moviee )
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'moviee':moviee})

def delete(request,id):
    if request.method=='POST':
        moviee=movie.objects.get(id=id)
        moviee.delete()
        return redirect('/')
    return render(request,'delete.html')
    