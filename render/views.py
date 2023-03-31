from django.shortcuts import render

# Create your views here.

from render.models import Post,Categoria
# Create your views here.

def index(request):
    posts=Post.objects.all()
    return render(request,'render/index.html', {"posts":posts})
def blog(request):
    posts=Post.objects.all()
    return render(request,'render/index.html',{"posts":posts})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request,"render/index.html",{'categoria':categoria,"posts":posts})