from django.contrib import admin

from bob.models import LottoTicket


class LottoTicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(LottoTicket, LottoTicketAdmin)
