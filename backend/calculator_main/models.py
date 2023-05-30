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
        return "%s, %s" % (self.price, self.discount)



''' Модели для шаблонизатора '''

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Почтовый адрес должен быть задан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почтовый адрес', max_length=50, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class CitiesTemplate(models.Model):
    city = models.CharField('Город', max_length=30)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города шаблонизатора'

    def __str__(self):
        return self.city


class MailingType(models.Model):
    mail_type = models.CharField('Вид рассылки', max_length=30)

    class Meta:
        verbose_name = 'Вид рассылки'
        verbose_name_plural = 'Виды рассылок'

    def __str__(self):
        return self.mail_type


class UrlsContentMail(models.Model):
    poster_url = models.URLField('Ссылка на мероприятие', db_index=True)
    text_content = models.TextField('Описание мероприятия')
    event_category = models.CharField('Категория мероприятия', max_length=20)
    name_event = models.CharField('Название мероприятия', max_length=30)
    rate = models.CharField('Ценз', max_length=3)
    date_event = models.CharField('Дата мероприятия', max_length=10)
    time_event = models.CharField('Время мероприятия', max_length=10)
    venue = models.CharField('Площадка', max_length=30)
    price = models.CharField('Цена', max_length=15)
    img_poster = models.ImageField('Афиша', upload_to='main')

    class Meta:
        verbose_name = 'Информация о мероприятии'
        verbose_name_plural = 'Мероприятия шаблонизатора'

    def __str__(self):
        return self.poster_url


class UrlsContentTransfer(models.Model):
    number_phone_links = models.CharField('Ссылка на телефон', max_length=30)
    number_phone = models.CharField('Номер телефона', max_length=30)
    alert_date = models.CharField('Дата переноса', max_length=10)
    labels = models.CharField('UTM-метки', max_length=300)
    pixels = models.CharField('Пиксель', max_length=300)
    key = models.CharField('Ключ рассылки', max_length=300)
    social = models.CharField('Соцсети', max_length=300)

    class Meta:
        verbose_name = 'Информация о переносе'
        verbose_name_plural = 'Данные для переноса'


class ListAllUrls(models.Model):
    city_mail = models.ForeignKey('CitiesTemplate', on_delete=models.PROTECT, verbose_name='Город',
                                  related_name='list_city')
    date_create_mail = models.DateField('Дата рассылки')
    type_mail = models.ForeignKey('MailingType', on_delete=models.PROTECT, verbose_name='Вид рассылки',
                                  related_name='list_mail_type')
    user_create = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Созатель рассылки',
                                  related_name='list_user')
    urls_content = models.ForeignKey('UrlsContentMail', on_delete=models.PROTECT, verbose_name='Ссылка на рассылку',
                                  related_name='list_urls_content')
    urls_transfer = models.OneToOneField('UrlsContentTransfer', on_delete=models.PROTECT, null=True, blank=True,
                                         verbose_name='Содержимое для переноса', related_name='list_url_transfer')

    class Meta:
        verbose_name = 'Ссылка на мероприятие'
        verbose_name_plural = 'Ссылки на мероприятия'

    def __str__(self):
        return "%s: %s, %s" % (self.city_mail, self.type_mail, self.date_create_mail)



