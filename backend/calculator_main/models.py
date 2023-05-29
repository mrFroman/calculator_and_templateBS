from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'Город калькулятора'
        verbose_name_plural = 'Города калькулятора'


class CategoryOffer(models.Model):
    city_name = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='Город', related_name='categories')
    title = models.CharField('категория предложения', max_length=200)

    def __str__(self):
        return "%s, %s" % (self.city_name, self.title)

    class Meta:
        verbose_name = 'Категория калькулятора'
        verbose_name_plural = 'Категории калькулятора'


class Offer(models.Model):
    category_offer = models.ForeignKey('CategoryOffer', on_delete=models.PROTECT, verbose_name='категория предложения',
                                       related_name='offer')
    name_offer = models.CharField('Наименование предложения', max_length=200)
    price = models.FloatField('Цена', max_length=20)
    discount = models.FloatField('Скидка', max_length=20)

    class Meta:
        verbose_name = 'Наименования предложения'
        verbose_name_plural = 'Наименовании предложений'

    def __str__(self):
        return "%s %s, %s" % (self.name_offer, self.price, self.discount)



# ''' Модели для шаблонизатора '''
#
#
# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('Почтовый адрес должен быть задан')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_user(self, email, password, **extra_fields):
#         extra_fields['is_staff'] = False
#         extra_fields['is_superuser'] = False
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields['is_staff'] = True
#         extra_fields['is_superuser'] = True
#         return self._create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField('Почтовый адрес', max_length=50, db_index=True, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD = 'email'
#     objects = UserManager()
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
