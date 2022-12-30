from django.contrib import admin
from .models import Post, Comentarios





# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicacion', 'status')
    list_filter = ('status', 'creado', 'publicacion', 'autor')
    search_fields = ('titulo', 'body')
    prepopulated_fields = {'slug':('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicacion'
    ordering = ('status', 'publicacion')
    
    
    
    
@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'post', 'creado', 'activo')
    list_filter = ('activo', 'creado', 'modificado')
    search_fields = ('nombre', 'email', 'body')