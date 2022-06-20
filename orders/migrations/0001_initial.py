from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_price', models.FloatField()),
                ('min_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_price', models.FloatField()),
                ('min_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RegularPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_price', models.FloatField()),
                ('min_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_price', models.FloatField()),
                ('min_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_price', models.FloatField()),
                ('min_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('max_price', models.FloatField()),
                ('min_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SubsExtras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]