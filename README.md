# Kubernetes Autoscaling Advisor

A FastAPI application built to practice Docker, FastAPI, and Kubernetes autoscaling concepts. The API receives workload metrics (CPU, memory, requests per second, and latency) and returns a scaling recommendation.

## Features

- Accepts workload metrics via a REST endpoint
- Calculates system load status (low to critical)
- Recommends a scaling layer (Pod, Deployment, or Node) and replica count
- Estimates monthly cost based on recommended replicas

## Technologies

| Technology | Purpose |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | REST API framework |
| [Pydantic](https://docs.pydantic.dev/) | Request validation |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [Docker](https://www.docker.com/) | Containerization |

## Project Structure

```text
.
├── app/
│   ├── main.py        # FastAPI app and endpoints
│   ├── models.py       # Pydantic data models
│   └── analyzer.py     # Scaling and cost calculation logic
├── requirements.txt
├── Dockerfile
└── README.md
```

## Installation

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run locally
```bash
uvicorn app.main:app --reload
```

Open the interactive API docs:
```text
http://localhost:8000/docs
```

### Run with Docker
```bash
docker build -t k8s-autoscaling-advisor .
docker run -p 8000:8000 k8s-autoscaling-advisor
```

## API

### `POST /analyze`

**Request body:**
```json
{
  "cpu": 80,
  "memory": 70,
  "rps": 500,
  "latency": 120
}
```

**Response:**
```json
{
  "input_metrics": {
    "cpu": 80,
    "memory": 70,
    "rps": 500,
    "latency": 120
  },
  "system_status": "high_load",
  "recommended_layer": "Deployment",
  "recommended_replicas": 6,
  "estimated_monthly_cost_usd": 120,
  "recommendation": "System status is high_load. Recommended scaling layer is Deployment with 6 replicas."
}
```

## Notes

- Thresholds for status, replicas, and layer are defined in `analyzer.py` and can be adjusted as needed.
- Cost estimation uses a fixed rate of $20 per replica per month.
- This project is for learning purposes and does not connect to a real Kubernetes cluster.
