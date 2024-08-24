from django import forms
from .models import *

#movie add form

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'director', 'main_cast', 'release_date', 'description', 'image', 'trailer_watch_now')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")
