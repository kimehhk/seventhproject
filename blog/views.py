from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    objs = Blog.objects
    return render(request, 'home.html', {'obj' : objs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def add(request):
    return render(request, 'add.html')

def create(request):
    if request.method == 'POST':
        blog = Blog()
        blog.image = request.FILES['image']
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/'+str(blog.id))
    
    else:
        return render(request, 'add.html')


def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
   
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.image = request.FILES['image']
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blog/'+str(blog.id))
    
    return render(request, 'update.html', {'blogs':blog})


def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')