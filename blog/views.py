from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    # CreateView
)
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostcreateForm
from .serializers import PostSerializer
from rest_framework import viewsets, generics

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content']

    # template_name_suffix = '_update_form'
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
    ordering = ('-date',)
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'user_post.html'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')
        

class PostDetailView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'detail.html'




def about(request):
    return render(request,'about.html')