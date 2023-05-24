from django import forms
from .models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        exclude =["post"]
        labels ={
            "user_name": "Your Name",
            "user_email":"Your Email",
            "text":"Your Comment"
        }