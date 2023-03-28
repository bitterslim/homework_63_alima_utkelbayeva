from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, FormView

from accounts.models import Account
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment, Like


class PostDetailView(DetailView):
    template_name = 'post.html'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['post_form'] = PostForm()
        post = self.object
        comments = post.comments.order_by('id')
        context['comments'] = comments
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)

        if form.is_valid():
            description = form.cleaned_data.get('description')
            image = form.cleaned_data.get('image')
            user = request.user
            if not Post.objects.filter(description=description).exists():
                post = Post.objects.create(description=description, image=image, user=user)
        else:
            form = {'text': 'Smth went wrong, post did not create'}
        return redirect('post_detail', pk=post.id)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentForm
    template_name = 'comment_add.html'

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        user = request.user
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data.get('comment_text')
            Post.objects.create(user=user, comment_text=comment_text, post=post)
        return redirect('post_detail', pk=post.pk)

class SubscribeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        account = get_object_or_404(Account, id=request.POST.get('user_id'))
        if account == request.user:
            pass
        elif account.subs.filter(id=request.user.id).exists():
            account.subs.remove(request.user)
        else:
            account.subs.add(request.user)
        return redirect('profile', pk=kwargs['pk'])



@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if Like.objects.filter(user=user, post=post).exists():
        messages.error(request, 'You have already liked this publication.')
    else:
        like = Like(user=user, post=post)
        like.save()
        post.likes += 1
        post.save()

    return redirect('post_detail', pk=post_id)


