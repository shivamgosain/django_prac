from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from .models import Movie


def movies(request):
    data=Movie.objects.all()
    return render(request,'movies/movies.html',{'movies':data})
def home(request):
    return HttpResponse("Homepage")

def detail(request,id):
    data=Movie.objects.get(pk=id)
    return render(request,'movies/detail.html',{'movie':data})

def add(request):
    title=request.POST.get('title')
    year=request.POST.get('year')
    if title and year:
        movie=Movie(title=title,year=year)
        movie.save()
        return redirect('/movies')
    return render(request,'movies/add.html')

def delete(request,id):
    try:
        movie=Movie.objects.get(pk=id).delete()
    except:
        raise Http404("Movie does not exist")
    movie.delete()
    return redirect('/movies')