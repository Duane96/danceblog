from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager

from tinymce.models import HTMLField

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='publicado')


class Post(models.Model):
    STATUS_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado','Publicado')
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publicacion')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = HTMLField()
    publicacion = models.DateTimeField(default=timezone.now)
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='borrado')
    
    objects = models.Manager()
    publicado = PublishedManager()
    tags = TaggableManager()

    
    class Meta:
        ordering = ('-publicacion',)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publicacion.year,self.publicacion.month,self.publicacion.day,self.slug])
    
    

class Comentarios(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('creado',)
        
    def __str__(self):
        return f'Comentado por {self.nombre} en {self.post}'

    