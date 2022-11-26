from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post


# class PostCommentForm(forms.ModelForm):
#     class Meta:
#         model = PostComment
#         fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['content'].widget.attrs.update({'class': 'comment-form'})
