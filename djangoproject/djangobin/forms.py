from django import forms
from django.core.exceptions import ValidationError
from .models import Snippet, Language, Author, Tag
from .utils import Preference, get_current_user


class SnippetForm(forms.ModelForm):

    snippet_tags = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={
                               'class': 'selectpicker form-control',
                               'placeholder': 'Enter tags (optional)'
                            }))

    class Meta:
        model = Snippet
        fields = ('original_code', 'language', 'expiration', 'exposure', 'title',)
        widgets = {
            'original_code': forms.Textarea(attrs={'class': 'form-control', 'rows': '10',
                                                        'spellcheck': 'false'}),
            'language': forms.Select(attrs={'class': 'selectpicker foo form-control',
                                            'data-live-search': 'true',
                                            'data-size': '5'}),
            'expiration': forms.Select(attrs={'class': 'selectpicker form-control'}),
            'exposure': forms.Select(attrs={'class': 'selectpicker form-control'}),
            'title': forms.TextInput(attrs={'class': 'selectpicker form-control',
                                            'placeholder': 'Enter Title (optional)'}),            
        }

    def save(self, request):
        snippet = super(SnippetForm, self).save(commit=False)
        snippet.user = get_current_user(request)
        snippet.save()
        tag_list = [tag.strip().lower() 
                   for tag in self.cleaned_data['snippet_tags'].split(',') if tag ]
        if len(tag_list) > 0:
            for tag in tag_list:
                t = Tag.objects.get_or_create(name=tag)
                snippet.tags.add(t[0])
        return snippet