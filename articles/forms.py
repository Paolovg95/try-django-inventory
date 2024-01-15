from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__iexact=title)
        if qs.exists():
            self.add_error('title', 'This title already exists')
        return data

# class ArticleFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

#     def clean_title(self):
#         cleaned_data = self.cleaned_data # returns a dictionary
#         title = cleaned_data.get('title')
#         if title.lower().strip() == 'abc':
#             self.add_error('title',"Can't input ABC as title")
#             # raise forms.ValidationError("ABC not accepted as title")
#         return title
