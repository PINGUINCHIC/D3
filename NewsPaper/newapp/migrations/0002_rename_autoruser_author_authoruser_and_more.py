

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='autorUser',
            new_name='authorUser',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='ratingAutor',
            new_name='ratingAuthor',
        ),
    ]
