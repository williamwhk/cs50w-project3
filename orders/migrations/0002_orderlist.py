from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('orderid', models.IntegerField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
            ],
        ),
    ]