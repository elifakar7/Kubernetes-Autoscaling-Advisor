from fastapi import FastAPI
from app.models import Metrics
from app.analyzer import (
    calculate_status,
    calculate_replicas,
    calculate_layer,
    estimate_monthly_cost,
    generate_recommendation,
)

app = FastAPI(title="Kubernetes Autoscaling Advisor")


@app.get("/")
def home():
    return {
        "message": "Kubernetes Autoscaling Advisor is running",
        "docs": "/docs"
    }


@app.post("/analyze")
def analyze(metrics: Metrics):
    status = calculate_status(metrics.cpu, metrics.memory, metrics.latency)
    replicas = calculate_replicas(
        metrics.cpu,
        metrics.memory,
        metrics.rps,
        metrics.latency
    )
    layer = calculate_layer(metrics.rps)
    estimated_cost = estimate_monthly_cost(replicas)
    recommendation = generate_recommendation(status, layer, replicas)

    return {
        "input_metrics": {
            "cpu": metrics.cpu,
            "memory": metrics.memory,
            "rps": metrics.rps,
            "latency": metrics.latency
        },
        "system_status": status,
        "recommended_layer": layer,
        "recommended_replicas": replicas,
        "estimated_monthly_cost_usd": estimated_cost,
        "recommendation": recommendation
    }