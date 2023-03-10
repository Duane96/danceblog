# Generated by Django 4.1.4 on 2022-12-27 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publicacion')),
                ('body', models.TextField()),
                ('publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modificado', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('borrado', 'Borrado'), ('publicado', 'Publicado')], default='borrado', max_length=10)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publicacion',),
            },
        ),
    ]
