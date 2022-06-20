from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderList',
        ),
    ]