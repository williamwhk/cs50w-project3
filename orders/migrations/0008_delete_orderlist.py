from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderList',
        ),
    ]