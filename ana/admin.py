from django.contrib import admin

from ana.models import LottoTicket


class LottoTicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(LottoTicket, LottoTicketAdmin)
