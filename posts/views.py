# Create your views here.
from ast import Return
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
)

from django.contrib.auth.mixins import (
	LoginRequiredMixin, UserPassesTestMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
	template_name = "posts/list.html"
	model = Post

class PostDetailView(DetailView):
	template_name = "posts/detail.html"
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	template_name = "posts/new.html"
	model = Post
	fields = ["title", "subtitle", "body"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	template_name = "posts/edit.html"
	model = Post
	fields = ["title", "subtitle", "body"]

	def test_func(self):
		obj = self.get_object()
		return obj.author==self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author==self.request.user
