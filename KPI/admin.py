from django.contrib import admin
from django.contrib.auth.models import *
from KPI.models import *
from KPI.actions import export_as_xls
from KPI.predictions import load_model_and_predict

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
        "displaymonth",
        "prediction",
    ]
    list_display_links = [
        "name",
    ]
    list_per_page = 5
    list_filter = ("name", "monthly_rating", "department")
    search_fields = ("name",)
    actions = [export_as_xls]

    def prediction(self,obj):
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
        kpi = [
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
            round(sum(kpis)/len(kpis),1),
        ]
        data = kpi
        prediction = load_model_and_predict([data], "trained_model.joblib")
        return prediction

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
