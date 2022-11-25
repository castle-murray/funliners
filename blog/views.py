from django.shortcuts import render, redirect, reverse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DetailView,
                                  DeleteView,
                                  )
from .models import (Post, Comment)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostDetailView(DetailView):
    model = Post
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect("post-detail", pk=post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context


# def CpostDetailView(request, pk):
    # post = Post.objects.get(pk=pk)
    # form = PostCommentForm(request.POST)
#
    # pk = request.POST.get('id')
    # context = {
        # 'post': post,
        # 'form': form
    # }
#
#    def form_valid(self, form):
#        form.instance.post_id = self.kwargs['pk']
#        form.instance.c_author = self.request.user
#        return super().form_valid(form)
    # if request.method == 'POST':
        # def post(self, request, *args, **kwargs):
        # if form.is_valid():
        # post = self.get_object()
        # form.instance.c_author = request.user
        # form.instance.original_post = post
        # form.save()
        # return redirect(reverse("post",))
        # return render(request, 'blog/new_post_detail.html', context)
    # else:
        # return render(request, 'blog/new_post_detail.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# class PostDetailView(DetailView):
#    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'use', 'problem', 'context', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'use', 'problem', 'context', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')
