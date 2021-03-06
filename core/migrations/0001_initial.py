# Generated by Django 2.2.3 on 2021-01-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('rua', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('capacidade', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=20)),
                ('categoria_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='core.CategoriaEvento')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
            ],
            options={
                'ordering': ('conteudo',),
            },
        ),
    ]
