from fastapi import FastAPI, HTTPException

from api.schemas import ComplaintRequest
from fastapi.middleware.cors import CORSMiddleware

from api.model_loader import (
    priority_model,
    sla_model,
    resolution_model,
    tfidf
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():

    return {
        "message": "ONGC Complaint Analytics API Running"
    }


@app.post("/predict-all")
def predict_all(
    request: ComplaintRequest
):

    if len(request.text.strip()) < 5:

        raise HTTPException(
            status_code=400,
            detail="Complaint too short"
        )

    combined_text = (
        request.text
        + " "
        + request.department
        + " "
        + request.group
        + " "
        + request.software
    )

    vector = tfidf.transform(
        [combined_text]
    )

    # Priority
    priority = priority_model.predict(
        vector
    )[0]

    # Resolution Time
    resolution = resolution_model.predict(
        vector
    )[0]

    # SLA Rule Engine

    if priority == "Critical":

        sla_limit = 24

    elif priority == "High":

        sla_limit = 48

    elif priority == "Medium":

        sla_limit = 72

    else:

        sla_limit = 96

    if resolution <= sla_limit:

        sla = "Within SLA"

    else:

        sla = "SLA Breached"

    return {

        "priority": priority,

        "sla_prediction": sla,

        "estimated_resolution_hours":
        round(
            float(resolution),
            2
        )
    }