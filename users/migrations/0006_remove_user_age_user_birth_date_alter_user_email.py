# Generated by Django 4.1.7 on 2023-04-01 14:02

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, validators=[users.models.check_children_age]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, unique=True, validators=[users.models.not_rambler_mail]),
        ),
    ]
