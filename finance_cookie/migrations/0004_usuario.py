from django.db import migrations, models
import django.utils.timezone as dj_timezone


class Migration(migrations.Migration):
    dependencies = [
        ('finance_cookie', '0003_alter_compra_data_alter_entrada_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('senha_hash', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(default=dj_timezone.now)),
                ('saldo_fisico', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('saldo_online', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={},
        ),

    ]

