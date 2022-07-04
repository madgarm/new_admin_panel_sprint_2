from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE content.person ALTER COLUMN created SET DEFAULT NOW();'
            'ALTER TABLE content.person ALTER COLUMN modified SET DEFAULT NOW();'
            'ALTER TABLE content.genre ALTER COLUMN created SET DEFAULT NOW();'
            'ALTER TABLE content.genre ALTER COLUMN modified SET DEFAULT NOW();'
            'ALTER TABLE content.film_work ALTER COLUMN created SET DEFAULT NOW();'
            'ALTER TABLE content.film_work ALTER COLUMN modified SET DEFAULT NOW();'
            'ALTER TABLE content.person_film_work ALTER COLUMN created SET DEFAULT NOW();'
            'ALTER TABLE content.genre_film_work ALTER COLUMN created SET DEFAULT NOW();'
        ),
    ]
