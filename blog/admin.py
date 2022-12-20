from django.contrib import admin
from blog.models import UserProfile, Product, Order, Detail, Account, HighScore
# Register your models here.

# admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Detail)
admin.site.register(Account)
admin.site.register(HighScore)



