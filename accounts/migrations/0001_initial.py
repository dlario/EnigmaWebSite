# Generated by Django 2.1.1 on 2018-09-03 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_bt_id', models.IntegerField()),
                ('company_name', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='Grande Prairie', max_length=255)),
                ('province', models.CharField(default='Alberta', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('box_number', models.CharField(default='', max_length=255)),
                ('postal_code', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=255)),
                ('contact_type', models.CharField(default='', max_length=255)),
                ('contact', models.CharField(default='', max_length=255)),
                ('preferred', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_bt_id', models.IntegerField()),
                ('first_name', models.CharField(default='', max_length=255)),
                ('middle_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Person'),
        ),
        migrations.AddField(
            model_name='companyperson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Person'),
        ),
    ]
