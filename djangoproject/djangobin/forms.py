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
            'file_extension': 'Specify extension like *.txt, *.md etc;'
        }
        widgets = {
            'file_extension': Textarea(attrs={'rows': 5, 'cols': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'djangobin' or name == 'DJANGOBIN':
            raise ValidationError("el nombre no puede ser {0}".format(name))
        return name

    def clean_slug(self):
        slug = self.cleaned_data['slug'].lower()
        r = Language.objects.filter(slug=slug)
        if len(r) > 0:
            raise ValidationError("{0} ya existe".format(slug))
        return slug.lower()

    def clean(self):
        cleaned_data = super(LanguageForm, self).clean()
        slug = cleaned_data.get('slug')
        mime = cleaned_data.get('mime')
        if slug == mime:
            raise ValidationError("Slug y MIME no pueden ser el mismo.")
        return cleaned_data