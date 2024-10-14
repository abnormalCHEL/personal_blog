from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Profile, Skill, About, Service, Portfolio, Category, Blog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404



def home(request):
    profile = Profile.objects.first() 
    skills = Skill.objects.all()
    about = About.objects.first()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    categories = Category.objects.all()
    posts = Blog.objects.all()
    
    return render(request, 'index.html', 
                  {'user': profile, 
                   'skills': skills,
                   'about': about,
                   'services': services,
                   'portfolios': portfolios,
                   'categories': categories,
                   'posts': posts
                })


def blog(request):
    
    posts = Blog.objects.all()
    if request.method == 'POST':
        search = (request.POST.get('search'))
        posts = posts.filter(title__icontains=search)
        
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    most_watched_posts = Blog.objects.order_by('-view_count')[:3]        
    return render(request, "blog.html", {'posts': posts,'most_watched_posts': most_watched_posts  })



def about(request):
    
    posts = Profile.objects.all()
    if request.method == 'POST':
        search = (request.POST.get('search'))
        posts = posts.filter(title__icontains=search)
        
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
        
    return render(request, "about-us.html", {'posts': posts})


def Paartfolia(request):
    
    posts = Portfolio.objects.all()
    if request.method == 'POST':
        search = (request.POST.get('search'))
        posts = posts.filter(title__icontains=search)
        
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
        
    return render(request, "portfolio.html", {'posts': posts})


def blog_detail(request,pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.view_count +=1
    blog.save()
    
    return render(request,'single-blog.html', {'blog': blog})






