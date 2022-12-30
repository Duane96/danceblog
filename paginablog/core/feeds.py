from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
    titulo = 'Mi Blog'
    link = reverse_lazy('blog:post_list')
    descripcion = 'Nuev post de mi blog'
    def items(self):
        return Post.publicado.all()[:5]
    def item_titulo(self, item):
        return item.titulo
    def item_descripcion(self, item):
        return truncatewords(item.body, 30)