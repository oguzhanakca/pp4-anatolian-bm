from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('date', 'time', 'user', 'name','status',)
    search_fields = ['user__username','user__first_name', 'user__last_name','requested_date']
    list_filter = ('status','requested_date','requested_time',)

    def date(self, obj):
        return obj.requested_date.strftime('%d.%m.%Y')
    def name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    def time(self, obj):
        return obj.requested_time
