# Generated by Django 3.1.2 on 2020-10-15 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('surname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Surname')),
                ('picture', models.ImageField(blank=True, max_length=200, null=True, upload_to='profile_picture', verbose_name='Profile picture')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address')),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonials', verbose_name='Picture')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtitle')),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('value', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Value')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Picture')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Url')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('ending_date', models.DateField(verbose_name='Ending date')),
                ('type_experience', models.CharField(choices=[('Education', 'Education'), ('Professional Experience', 'Professional Experience'), ('Pre-professional practices', 'Pre-professional practices')], max_length=100, verbose_name='Type experience')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Subtitle')),
                ('content_exerience', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
