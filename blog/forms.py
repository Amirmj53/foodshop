from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(widget=forms.Textarea)

 