from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add a New Comment'}),
        }
