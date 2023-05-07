from django.contrib import admin
from django.contrib.auth.models import *
from KPI.models import *

admin.site.site_header = "KPI PROJECT PANEL"
admin.site.site_title = "KPI PROJECT PANEL"


class EmployeeDetails(admin.ModelAdmin):
    fields = (
        "name",
        "department",
        "tone_of_voice",
        "starting_script",
        "ending_script",
        "resolution_time",
        "choice_of_words",
        "clarity",
        "onCallComplaintChecking",
        "handlingUnderPressure",
        "ticketRaising",
        "billableTime",
    )
    list_display = [
        "name",
        "department",
        "monthly_rating",
        "last_month_rating",
        "displaymonth",
    ]
    list_display_links = [
        "name",
    ]
    list_filter = ("name", "monthly_rating", "department")
    search_fields = ("name",)

    

    def displaymonth(self, obj):
        kpis = [
            obj.tone_of_voice,
            obj.starting_script,
            obj.ending_script,
            obj.resolution_time,
            obj.choice_of_words,
            obj.clarity,
            obj.onCallComplaintChecking,
            obj.handlingUnderPressure,
            obj.ticketRaising,
            obj.billableTime,
        ]
        return "{}".format(round(sum(kpis) / len(kpis), 1))


admin.site.register(Employee, EmployeeDetails)
admin.site.register(Department)
admin.site.register(Address)
admin.site.unregister(Group)
