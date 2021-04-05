# Generated by Django 3.1.7 on 2021-03-31 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto_posição',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.CharField(max_length=31)),
                ('quantidade', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deposito.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_destino', models.CharField(max_length=1023)),
                ('status', models.CharField(choices=[('0', 'A separar'), ('1', 'Separado'), ('2', 'Em Falta')], default='0', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deposito.produto')),
            ],
        ),
    ]
