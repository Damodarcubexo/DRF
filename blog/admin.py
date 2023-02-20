from django.contrib import admin
from blog.models import UserProfile, Product, Order, Detail, Account, HighScore, Snippet
# Register your models here.

admin.site.register(Snippet)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Detail)
admin.site.register(Account)
admin.site.register(HighScore)



