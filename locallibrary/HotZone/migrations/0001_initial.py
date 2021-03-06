# Generated by Django 3.1.2 on 2020-10-29 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseNumber', models.IntegerField()),
                ('date', models.DateTimeField(help_text='Enter the date of infecious', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('XCoordinate', models.IntegerField()),
                ('YCoordinate', models.IntegerField()),
                ('DateFrom', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('DateTo', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('dateofBrith', models.DateTimeField(max_length=100, null=True)),
                ('Case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HotZone.case')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('DateofBrith', models.DateTimeField(max_length=100)),
                ('Case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HotZone.case')),
            ],
        ),
    ]
