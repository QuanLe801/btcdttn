# Generated by Django 4.2.4 on 2023-09-02 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_dictionaryentry_pronounce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vnconversation', models.CharField(max_length=500)),
                ('enconversation', models.CharField(max_length=500)),
            ],
        ),
    ]