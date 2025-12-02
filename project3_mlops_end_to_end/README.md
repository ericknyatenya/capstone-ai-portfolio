# Project 3 — MLOps End-to-End

Overview

A complete MLOps pipeline with data versioning (DVC), experiment tracking (MLflow), model packaging, CI/CD workflows, and deployment manifests. Includes example datasets, training scripts, and reproducible workflows.

## Contents

- `src/training/` — model training pipeline
- `src/inference/` — model inference/prediction
- `dvc/` — DVC configuration and params
- `mlflow/` — MLflow experiment tracking config
- `deployments/` — Dockerfile for model server
- `notebooks/` — reproducible experiments
- `tests/` — test suite

## Setup

```bash
cd project3_mlops_end_to_end
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Demo

```bash
cd project3_mlops_end_to_end
PYTHONPATH=.. python -c "
from src.training.train import train_dummy_model
from src.inference.predict import predict_dummy

# Train a model
print('Training model...')
model_path = train_dummy_model()
print(f'Model saved to: {model_path}')

# Make predictions
print('\\nMaking predictions...')
queries = [
    'What is machine learning?',
    'How does deep learning work?',
    'Explain neural networks'
]

for query in queries:
    pred = predict_dummy(model_path, query)
    print(f'  Query: {query}')
    print(f'  Prediction: {pred}')
"
```

Expected output:
```
Training model...
Model saved to: ./model.pkl
Making predictions...
  Query: What is machine learning?
  Prediction: predicted: What is machine learning?
  Query: How does deep learning work?
  Prediction: predicted: How does deep learning work?
  Query: Explain neural networks
  Prediction: predicted: Explain neural networks
```

## DVC (Data Versioning)

Track data and model versions:
```bash
dvc init
dvc add data/
dvc push
```

## MLflow (Experiment Tracking)

Track experiments:
```bash
mlflow ui --backend-store-uri file:./mlruns
```

Visit http://localhost:5000 to view experiments.

## Docker

```bash
docker build -t mlops-model deployments/
docker run mlops-model
```

## Key Concepts

- **Reproducibility**: Versioned data, params, and models via DVC.
- **Experiment Tracking**: Log metrics, params, and artifacts with MLflow.
- **CI/CD**: Automated testing and deployment via GitHub Actions.
- **Containerization**: Package and deploy models via Docker.
- **Monitoring**: Track model performance in production.
