from django import forms

from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('image', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')
