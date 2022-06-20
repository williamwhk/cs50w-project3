from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_delete_orderlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('pizzaname', models.CharField(max_length=1000)),
                ('count', models.IntegerField()),
                ('total', models.FloatField()),
            ],
        ),
    ]