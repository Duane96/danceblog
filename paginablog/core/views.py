from django.shortcuts import render, get_object_or_404
from .models import Post, Comentarios

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

from .forms import EmailPostForm, ComentariosForm

from django.core.mail import send_mail

from taggit.models import Tag

from django.db.models import Count

# Create your views here.

def post_list(request, tag_slug=None):
    object_list = Post.publicado.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/post/list.html', {'page':page,'posts':posts, 'tag': tag})
    
#Vista de Lista basada en Clase:
"""class PostListView(ListView):
    queryset = Post.publicado.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'"""


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publicado',
                             publicacion__year=year,
                             publicacion__month=month,
                             publicacion__day=day)
    
    comentarios = post.comentarios.filter(activo=True)
    new_comentario = None
    if request.method == 'POST':
        comentario_form = ComentariosForm(data=request.POST)
        if comentario_form.is_valid():
            new_comentario = comentario_form.save(commit=False)
            new_comentario.post = post
            new_comentario.save()
    else:
        comentario_form = ComentariosForm()
        
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.publicado.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publicacion')[:4]
            
    return render(request, 'blog/post/detail.html', {'post':post, 'comentarios': comentarios, 'new_comentarios': new_comentario, 'comentario_form': comentario_form, 'similar_posts': similar_posts})



def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publicado')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url)
            subject = f"{cd['name']} recomienda que leas"\
                f"{post.titulo}"
            message = f"Lee {post.titulo} en: \n\n {post_url}\n\n" f"{cd['name']}\' comenta: \n\n {cd['comments']}"
            
            send_mail(subject, message, 'dduane.abreu@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
    