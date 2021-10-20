from django.shortcuts import render,redirect
from .models import Contact,Blog,Portfolio,Files
# Create your views here.
def home(request):
    c=Blog.objects.all()
    d=Portfolio.objects.all()
    r=Files.objects.filter(sno=1)
    cont={'blog':c,'project':d,'r':r}
    return render(request,'index.html',cont)
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject=request.POST['subject']
        content = request.POST['content']
        c=Contact(name=name,email=email,subject=subject,content=content)
        c.save()
    return redirect('/')
def blog(request):
    return render(request,'blog-single.html')
def blogPost(request, slug): 
    post=Blog.objects.filter(sno=slug).first()
    blog=Blog.objects.all()
    content={'post':post,'blogs':blog}
    return render(request,'blog.html',content)
    
def Portfoli(request):
    return render(request,'portfolio-details.html')


