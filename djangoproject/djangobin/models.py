from django.db import models
from django.db.models.deletion import DO_NOTHING
from .utils import Preference
from pygments import lexers, highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import time
import random

class Language(models.Model):
    name = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, default=str(time.time()).replace(".", ""))
    mime = models.CharField(max_length=100)
    # Se le puede añadir , help_text='MIME to use when sending snippet as file.' para que aparezca como ayuda en el html del formulario
    file_extension = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.lang_code)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trending_snippets', args=[self.slug])

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
    default_language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                         default=get_default_language)
    default_exposure = models.CharField(max_length=10, choices=Preference.exposure_choices,
                                        default=Preference.SNIPPET_EXPOSURE_PUBLIC)
    default_expiration = models.CharField(max_length=10, choices=Preference.expiration_choices,
                                        default=Preference.SNIPPET_EXPIRE_NEVER)
    private = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    user = models.OneToOneField(User, related_name='profile', on_delete=DO_NOTHING)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', args=[self.user.username])

    def get_snippet_count(self):
        return self.user.snippet_set.count()

@receiver(post_save, sender=User)
def create_author(sender, **kwargs):
    if kwargs.get('created', False):
        Author.objects.get_or_create(user=kwargs.get('instance'))

class Snippet(models.Model):
    title = models.CharField(max_length=200, blank=True, default="Untitled")
    original_code = models.TextField()
    highlighted_code = models.TextField()
    expiration = models.CharField(max_length=10, choices=Preference.expiration_choices)
    exposure = models.CharField(max_length=10, choices=Preference.exposure_choices)
    visits = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    slug = models.SlugField(default=random.randrange(0, 100000000))
    created_on = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='snippets')

    def highlight(self):
        formatter = HtmlFormatter(linenos=True)
        return highlight(self.original_code, self.language.get_lexer(), formatter)

    def __str__(self):
        return self.title + ' - ' + self.language.name

    def get_absolute_url(self):
        return reverse('trending_snippets', args=[self.slug])

    class Meta:
        ordering = ['-created_on']

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=str(time.time()).replace(".", ""))

    def __str__(self):
        return self.name + " : " + self.slug

    def get_absolute_url(self):
        return reverse('trending_snippets', args=[self.slug])
    
    class Meta:
        ordering = ['name']