#!python
#log/views.py
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .odoo import get_odoo_instance

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="/login")
def home(request):
    return render(request,"home.html")

@login_required(login_url="/login")
def home_url(request):
    return render(request,"home.html")

@login_required(login_url="/login")
def po_list(request):
    return render(request,"po_list.html")

def test(request):
    print 'test calling'
    return render(request,"test.html")

def index(request):
    print request.user.is_authenticated()
    if request.user.is_authenticated():
        return render(request, "home.html")
    else:
        return render(request, "index.html")

@login_required(login_url="/login")
def so_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    if 'product.product' in get_odoo_instance.odoo.env:
        Product = get_odoo_instance.odoo.env['product.product']
        product_ids = Product.search([])
        product_list_with_names = Product.search_read([], ['name','categ_id','type'])
        print product_list_with_names
        print product_ids
    return render(request, "so_list.html",{'product_ids': product_list_with_names})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'so_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_delete(request,pk):
    obj=Post.objects.get(id=pk)
    obj.delete()
    posts = Post.objects.all()
    return render(request, "so_list.html", {'posts': posts})