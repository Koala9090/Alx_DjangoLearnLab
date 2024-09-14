from django.contrib.auth import login, views as auth_views
from django.db.models.query import QuerySet
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from django.db.models import Q
from .forms import PostForm, CommentForm
from django.urls import reverse



# Create your views here.
auth_views.LoginView.as_view()
auth_views.LogoutView.as_view()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile page
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/templates/blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.user.email = email
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/templates/blog/profile.html')

# ListView for all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

# DetailView for individual post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView for new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView for editing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/templates/blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView for deleting post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post_id)
        else:
            form = CommentForm()
        return render(request, 'blog/add_comment.html', {'form': form})
    
@login_required
def edit_comment(requset, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if requset.method == 'POST':
        form = CommentForm(requset.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post_id)
        else:
            form = CommentForm(instance=comment)
        return render(requset, 'blog/edit_comment.html', {'form': form})
class CommentDeleteView( DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    def get_queryset(self):
        querySet = super().get_queryset()
        return querySet.filter(author=self.request.user)