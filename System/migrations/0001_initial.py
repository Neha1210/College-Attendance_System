# Generated by Django 4.0 on 2022-07-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=300, null=True)),
                ('fsub', models.CharField(choices=[('DBMS', 'DBMS'), ('CN', 'CN'), ('SDA', 'SDA'), ('DMDW', 'DMDW'), ('DSA', 'DSA')], max_length=200, null=True)),
                ('subtype', models.CharField(choices=[('theory', 'theory'), ('lab', 'lab'), ('tutorial', 'tutorial')], default='theory', max_length=20, null=True)),
                ('batch', models.CharField(max_length=200, null=True)),
                ('div', models.CharField(choices=[('SY_A', 'SY_A'), ('SY_B', 'SY_B'), ('SY_C', 'SY_C'), ('TY_A', 'TY_A'), ('TY_B', 'TY_B'), ('TY_C', 'TY_C'), ('BTech_A', 'BTech_A'), ('BTech_B', 'BTech_B'), ('BTech_C', 'BTech_C')], max_length=7, null=True)),
                ('total', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch', models.CharField(max_length=9, null=True)),
                ('div', models.CharField(choices=[('SY_A', 'SY_A'), ('SY_B', 'SY_B'), ('SY_C', 'SY_C'), ('TY_A', 'TY_A'), ('TY_B', 'TY_B'), ('TY_C', 'TY_C'), ('BTech_A', 'BTech_A'), ('BTech_B', 'BTech_B'), ('BTech_C', 'BTech_C')], default='SY_A', max_length=7, null=True)),
                ('sheet', models.FileField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Upload2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=10, null=True)),
                ('sdiv', models.CharField(max_length=10, null=True)),
                ('cnum', models.CharField(max_length=200, null=True)),
                ('roll_no', models.CharField(max_length=200, null=True)),
                ('Sname', models.CharField(max_length=200, null=True)),
                ('Ph_no', models.CharField(max_length=200, null=True)),
                ('Remark', models.CharField(choices=[('p', 'p'), ('A', 'A')], default='p', max_length=1, null=True)),
            ],
        ),
    ]
