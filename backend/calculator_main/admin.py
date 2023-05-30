from django.contrib import admin

from .models import City, CategoryOffer, Offer, User, CitiesTemplate, MailingType, UrlsContentMail, UrlsContentTransfer, \
    ListAllUrls

admin.site.register(City)
admin.site.register(CategoryOffer)
admin.site.register(Offer)
admin.site.register(User)
admin.site.register(CitiesTemplate)
admin.site.register(MailingType)
admin.site.register(UrlsContentMail)
admin.site.register(UrlsContentTransfer)
admin.site.register(ListAllUrls)

