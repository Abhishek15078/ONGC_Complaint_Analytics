from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"

priority_model = joblib.load(
    MODELS_DIR / "priority_model.pkl"
)

sla_model = joblib.load(
    MODELS_DIR / "sla_model.pkl"
)

resolution_model = joblib.load(
    MODELS_DIR / "resolution_time_model.pkl"
)

tfidf = joblib.load(
    MODELS_DIR / "tfidf.pkl"
)