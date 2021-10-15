from django.db import models
from .utils import Preference
from pygments import lexers, highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    mime = models.CharField(max_length=100, help_text='MIME to use when sending snippet as file.')
    file_extension = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.lang_code)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('djangobin:trending_snippets', args=[self.slug])

    class Meta:
        ordering = ['name']

    
def get_default_language():
    lang = Language.objects.get_or_create(
        name='Plain text',
        lang_code='text',
        slug='text',
        mime='text_plain',
        file_extension='.txt',
    )
    return lang[0].id

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    default_language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                         default=get_default_language)
    default_exposure = models.CharField(max_length=10, choices=Preference.exposure_choices,
                                        default=Preference.SNIPPET_EXPOSURE_PUBLIC)
    default_expiration = models.CharField(max_length=10, choices=Preference.expiration_choices,
                                        default=Preference.SNIPPET_EXPIRE_NEVER)
    private = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " : " + self.email
    
    def get_absolute_url(self):
        return reverse("djangobin:profile", args=[self.user.username])
    
    def get_snippet_count(self):
        return self.user.snippet_set.count()

class Snippet(models.Model):
    title = models.CharField(max_length=200, blank=True, default="Untitled")
    original_code = models.TextField()
    highlighted_code = models.TextField()
    expiration = models.CharField(max_length=10, choices=Preference.expiration_choices)
    exposure = models.CharField(max_length=10, choices=Preference.exposure_choices)
    visits = models.IntegerField(default=0)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='snippets')
    tags = models.ManyToManyField('Tag', related_name='snippets')

    def highlight(self):
        formatter = HtmlFormatter(linenos=True)
        return highlight(self.original_code, self.language.get_lexer(), formatter)

    def __str__(self):
        return self.title + ' - ' + self.language.name

    def get_absolute_url(self):
        return reverse('djangobin:trending_snippets', args=[self.slug])

    class Meta:
        ordering = ['-created_on']

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name + " : " + self.slug

    def get_absolute_url(self):
        return reverse('djangobin:trending_snippets', args=[self.slug])
    
    class Meta:
        ordering = ['name']