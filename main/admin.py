from django.contrib import admin

from .models import Pizza, Pizza_List, Customer, Manager, Cart, Restaurant_Branch



class PizzaInline(admin.TabularInline):
	model = Pizza
	extra = 3

class PizzaListAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['id']}),
		("Date Created", {'fields': ['Created_At'], 'classes': ['collapse']}),
	]
	inlines = [PizzaInline]
	list_display = ('id', 'Created_At', 'was_published_recently')
	list_filter = ['Created_At']
	search_fields = ['id']

admin.site.register(Pizza_List, PizzaListAdmin)
