# Kubernetes Autoscaling Advisor

A FastAPI application created to practice Docker, FastAPI, and Kubernetes autoscaling concepts.

The API receives workload metrics (CPU, memory, requests per second, and latency) and returns a basic scaling recommendation.
## Technologies

* Python /  FastAPI /  Docker

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

## Example Input

```json
{
  "cpu": 80,
  "memory": 70,
  "rps": 500,
  "latency": 120
}
```
