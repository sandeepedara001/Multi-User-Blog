from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from users.models import Profile
from django.db.models import Q
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                )

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.filter(author=request.user.id)
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 5
    context_object_name = "posts"

    # def get_context_data(self, **kwargs):
    #     # posts = Post.objects.filter(author=self.request.user.id).order_by('-date_posted')
    #     posts = Post.objects.all().order_by('-date_posted')
    #     context = {'posts':posts}
    #     return context

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id).order_by('-date_posted')

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    paginate_by = 5
    context_object_name = "posts"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).filter(type="Public").order_by('-date_posted')




class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False



@login_required
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

@login_required
def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        user = User.objects.filter(username=query).first()
        if user:
            posts = Post.objects.filter(author=user.id).filter(type="Public").order_by('-date_posted')
            if posts:
                status = "Posts by "+str(user)
                context = {'posts':posts, 'status':status}
            else:
                status = "No posts to show for "+str(user)
                context = {'status':status}
        else:
            status = "No user exists with that name."
            context = {'status':status}
    return render(request, 'blog/search.html', context)
