from KPI.models import Employee
from django.db.models import F, Avg
from django.db.models.functions import Round
from ninja import Router, Schema
from KPI.predictions import train_and_save_model


train_router = Router(tags=["train endpoint"])

class mse(Schema):
    MeanSquaredError: float

data = Employee.objects.values(
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
).annotate(
    monthlyrating=Round(
        Avg(
            (
                F("tone_of_voice")
                + F("starting_script")
                + F("ending_script")
                + F("resolution_time")
                + F("choice_of_words")
                + F("clarity")
                + F("onCallComplaintChecking")
                + F("handlingUnderPressure")
                + F("ticketRaising")
                + F("billableTime")
            )
            / 10
        ),
        1,
    ),
    kpi=Round(
        Avg(
            (
                F("tone_of_voice")
                + F("starting_script")
                + F("ending_script")
                + F("resolution_time")
                + F("choice_of_words")
                + F("clarity")
                + F("onCallComplaintChecking")
                + F("handlingUnderPressure")
                + F("ticketRaising")
                + F("billableTime")
            )
            / 10
        ),
        1,
    )
    + 0.5,
)
save_path = "trained_model.joblib"

@train_router.get('/train', response=mse)
def users(request):
    mse = train_and_save_model(data, save_path)
    return {"MeanSquaredError": mse}