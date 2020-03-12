# Generated by Django 2.2.9 on 2020-01-30 17:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('atelier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_tailor', models.BooleanField(blank=True, default=False, help_text='User can be a tailor to have administrator access within his atelier', verbose_name='tailor')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='tailor',
        ),
        migrations.AddField(
            model_name='order',
            name='is_closed',
            field=models.BooleanField(blank=True, default=False, verbose_name='closed'),
        ),
        migrations.AddField(
            model_name='order',
            name='performer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='performer'),
        ),
        migrations.AlterField(
            model_name='allowancediscount',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='allowancediscount',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='complicationelement',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='complicationelement',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='fabric',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='minimalstyle',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='minimalstyle',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.date(2020, 2, 13), null=True, verbose_name='deadline'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_updated_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Tailor',
        ),
        migrations.AddField(
            model_name='profile',
            name='atelier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atelier.Atelier', verbose_name='atelier'),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]