from django.contrib import admin

# Register your models here.

# import your model
from parties.models import Party

# set up automated slug creation
class PartyAdmin(admin.ModelAdmin):
	model = Party
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}
# and register it
admin.site.register(Party, PartyAdmin)