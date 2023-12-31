# Generated by Django 4.1.3 on 2023-08-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_in_latin', models.CharField(max_length=255, verbose_name='Име изписано на латинеца')),
                ('email', models.EmailField(max_length=254, verbose_name='Служебен Email')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'AFM лаборатория'), (2, 'CF лаборатория'), (3, 'Техник'), (4, 'Студент, включен в проект')])),
                ('research_interests', models.TextField(blank=True, verbose_name='Research Interests')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('short_cv', models.TextField(blank=True, null=True, verbose_name='По желание - кратко CV')),
                ('full_cv', models.TextField(blank=True, null=True, verbose_name='По желание - пълно научно CV/списък с публикации')),
                ('scopus', models.URLField(blank=True, null=True)),
                ('google_scholar', models.URLField(blank=True, null=True)),
                ('web_of_science', models.URLField(blank=True, null=True)),
                ('orcid', models.URLField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Друга информация, която бихте желали да има в личната Ви страница')),
            ],
        ),
    ]
