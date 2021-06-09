# Generated by Django 3.1.12 on 2021-06-09 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('survival_guide', '0004_auto_20210609_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image_caption',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='section',
            name='image_credit',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image'),
        ),
        migrations.DeleteModel(
            name='SectionImage',
        ),
    ]