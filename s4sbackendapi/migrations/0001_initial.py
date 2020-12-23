# Generated by Django 3.1.4 on 2020-12-23 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='s4sUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('loudness', models.CharField(max_length=50)),
                ('audio_url', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('date_added', models.CharField(max_length=30)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.s4suser')),
            ],
        ),
        migrations.CreateModel(
            name='Sexes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.samples')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.s4suser')),
            ],
        ),
        migrations.CreateModel(
            name='Spectra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain', models.CharField(max_length=30)),
                ('resonance', models.CharField(max_length=30)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.samples')),
            ],
        ),
        migrations.CreateModel(
            name='SampleRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=50)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.samples')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s4sUser', to='s4sbackendapi.s4suser')),
            ],
        ),
        migrations.AddField(
            model_name='s4suser',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.sexes'),
        ),
        migrations.AddField(
            model_name='s4suser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('date_added', models.CharField(max_length=30)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.samples')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s4sbackendapi.s4suser')),
            ],
        ),
    ]
