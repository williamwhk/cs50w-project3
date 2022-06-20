from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderList',
        ),
    ]