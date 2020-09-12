from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'notes/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'notes/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        return super().form_valid(form) 

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        return super().form_valid(form)

    def test_func(self):
        return True

class PostDeleteView(DeleteView):
    model = Post
    