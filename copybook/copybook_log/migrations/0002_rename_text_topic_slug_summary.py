# Generated by Django 4.2.3 on 2023-07-20 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('copybook_log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='text',
            new_name='slug',
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=255)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copybook_log.topic')),
            ],
            options={
                'verbose_name_plural': 'summarys',
            },
        ),
    ]
