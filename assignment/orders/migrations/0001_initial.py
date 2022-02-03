# Generated by Django 4.0.2 on 2022-02-03 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.deal')),
            ],
        ),
    ]
