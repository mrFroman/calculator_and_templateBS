# Generated by Django 4.2.1 on 2023-05-30 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='категория предложения')),
            ],
            options={
                'verbose_name': 'Категория калькулятора',
                'verbose_name_plural': 'Категории калькулятора',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Город калькулятора',
                'verbose_name_plural': 'Города калькулятора',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_offer', models.CharField(max_length=200, verbose_name='Наименование предложения')),
                ('price', models.FloatField(max_length=20, verbose_name='Цена')),
                ('discount', models.FloatField(max_length=20, verbose_name='Скидка')),
                ('category_offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offer', to='calculator_main.categoryoffer', verbose_name='категория предложения')),
            ],
            options={
                'verbose_name': 'Наименования предложения',
                'verbose_name_plural': 'Наименовании предложений',
            },
        ),
        migrations.AddField(
            model_name='categoryoffer',
            name='city_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='calculator_main.city', verbose_name='Город'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='Почтовый адрес')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
