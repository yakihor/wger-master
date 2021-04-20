# Generated by Django 3.1.3 on 2020-12-01 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_auto_20190618_1617'),
        ('mailer', '0002_auto_20190618_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='gym',
            field=models.ForeignKey(editable=False,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='email_log', to='gym.gym'),
        ),
    ]
