from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from blogs.models import *

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-published_at')
    paginator = Paginator(posts, 5)  # Show 5 blogs per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {"page_obj": page_obj})

def detail(request, slug):
    post_obj = Post.objects.get(slug=slug)
    return render(request, 'detail.html', {'post':post_obj})



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", 'content']
    template_name = "addpost.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def comments(request, slug):
    post_obj = Post.objects.get(slug=slug)
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(content=content, post=post_obj, author=request.user)
    comments = Comment.objects.filter(post=post_obj).order_by('-created_at')
    return render(request, 'comments.html', {'comments':comments, 'slug':slug})