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

    # Validation
    if len(request.text.strip()) < 5:

        raise HTTPException(
            status_code=400,
            detail="Complaint too short"
        )

    # Create text exactly like training data
    combined_text = (
        request.text
        + " "
        + request.department
        + " "
        + request.group
        + " "
        + request.software
    )

    # Convert text to TF-IDF vector
    vector = tfidf.transform(
        [combined_text]
    )

    # Priority Prediction
    priority = priority_model.predict(
        vector
    )[0]

    # SLA Prediction
    sla = sla_model.predict(
        vector
    )[0]

    # Resolution Time Prediction
    resolution = resolution_model.predict(
        vector
    )[0]

    return {

        "priority": priority,

        "sla_prediction": sla,

        "estimated_resolution_hours":
        round(
            float(resolution),
            2
        )
    }