# Generated by Django 2.0.9 on 2019-04-30 22:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='commentinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1024)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='forumdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_header', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1024)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(50000)])),
                ('pic', models.ImageField(default='static/userlogin/images/default-img.png', upload_to='requests')),
                ('by_date', models.DateField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forumdetails'),
        ),
    ]
