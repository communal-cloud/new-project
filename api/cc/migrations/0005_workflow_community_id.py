# Generated by Django 2.1.8 on 2019-05-11 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0004_auto_20190511_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='Community_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cc.Community'),
        ),
    ]