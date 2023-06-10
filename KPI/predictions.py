from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib
from KPI.models import Employee
from django.db.models import F, Avg
from django.db.models.functions import Round


def train_and_save_model(data, save_path):
    print(data)
    # Create a DataFrame from the given list of data
    df = pd.DataFrame(
        data,
        columns=[
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
            "monthlyrating",
            "kpi",
        ],
    )

    # Split the data into features (X) and target variable (y)
    X = df.drop("kpi", axis=1)
    y = df["kpi"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create a linear regression model and fit it to the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)

    # Save the trained model to a file
    joblib.dump(model, save_path)

    return mse


def load_model_and_predict(data, model_path):
    # Create a DataFrame from the given list of data
    df = pd.DataFrame(
        data,
        columns=[
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
            "monthlyrating",
        ],
    )

    # Load the trained model from the file
    model = joblib.load(model_path)

    # Make predictions using the loaded model
    predictions = model.predict(df)

    return predictions


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
train_data = data
save_path = "trained_model.joblib"

mse = train_and_save_model(train_data, save_path)
print("Mean Squared Error:", mse)

# test_data = [
#     [1, 2, 3, 25, 4, 5, 0, 1, 1, 6, 8],
#     [0, 1, 2, 35, 3, 4, 0, 0, 0, 4, 8],
#     [2, 3, 4, 40, 2, 3, 1, 1, 1, 5, 8],
# ]

model_path = "trained_model.joblib"

predictions = load_model_and_predict(data[:10], model_path)
print("Predictions:", predictions)
