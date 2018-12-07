# Generated by Django 2.1.3 on 2018-12-06 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winesearch', '0002_auto_20181206_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(default='', max_length=45, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='province',
            name='province_name',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='region1',
            name='region1_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='region2',
            name='region2_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taster',
            name='taster_name',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taster',
            name='twitter_handles',
            field=models.CharField(blank=True, max_length=45, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='variety_name',
            field=models.CharField(default='', max_length=45, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wine',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='winesearch.Country'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='winesearch.Province'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='region1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='winesearch.Region1'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='region2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='winesearch.Region2'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='variety',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='winesearch.Variety'),
        ),
        migrations.AlterUniqueTogether(
            name='province',
            unique_together={('country', 'province_name')},
        ),
        migrations.AlterUniqueTogether(
            name='region1',
            unique_together={('province', 'region1_name')},
        ),
        migrations.AlterUniqueTogether(
            name='region2',
            unique_together={('region1', 'region2_name')},
        ),
    ]