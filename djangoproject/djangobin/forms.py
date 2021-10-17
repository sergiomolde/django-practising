from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Textarea
from .models import Language

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'
        labels = {
            'mime': 'MIME type',
            'lang_code': 'Language Code'
        },
        help_texts = {
            'lang_code': 'Short name of the Pygment lexer to use',
            'file_extension': 'Sepecify extension like *.txt, *.md etc;'
        }
        widgets = {
            'file_extension': Textarea(attrs={'rows': 5, 'cols': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'djangobin' or name == 'DJANGOBIN':
            raise ValidationError("name can't be {0}" % name)
        return name
    
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

    def clean(self):
        cleaned_data = super(LanguageForm, self).clean()
        slug = cleaned_data.get('slug')
        mime = cleaned_data.get('mime')
        if slug == mime:
            raise ValidationError("Slug and MIME shouldn't be same.")
        return cleaned_data

    def save(self):
        new_lang = Language.objects.create(
            name = self.cleaned_data['name'],
            lang_code = self.cleaned_data['lang_code'],
            slug = self.cleaned_data['slug'],
            mime = self.cleaned_data['mime'],
            created_on = self.cleaned_data['created_on'],
            updated_on = self.cleaned_data['updated_on'],
        )
        return new_lang
    
    def clean_slug(self):
        slug = self.cleaned_data['slug'].lower()
        r = Language.objects.filter(slug=slug)
        if r.count:
            raise ValidationError("{0} already exists" % slug)

        return slug.lower()