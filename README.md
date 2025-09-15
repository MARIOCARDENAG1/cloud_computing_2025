# cloud_computing_2025


This repo contains a public notes platform built with:
- **Back-end**: Flask (Python)
- **Database**: MongoDB
- **Local load-balancer**: HAProxy (Docker Compose demo)
- **Local orchestration**: Docker Compose
- **Kubernetes deployment**: Deployments, Services & Ingress

# Project Structure
cloud_computing_2025/
├── app/ # Flask application code
│ ├── app.py
│ ├── Dockerfile
│ ├── requirements.txt
│ └── templates/ # HTML views
│ ├── create.html
│ ├── search.html
│ └── user.html
├── db/ # MongoDB Dockerfile
│ └── Dockerfile
├── lb/ # HAProxy for local demo
│ ├── Dockerfile
│ └── haproxy.cfg
├── docker-compose.yml # Local orchestration
├── k8s/ # Kubernetes manifests
│ ├── db-pvc.yaml
│ ├── db-deployment.yaml
│ ├── mongo-svc.yaml
│ ├── web-deployment.yaml
│ ├── web-svc.yaml
│ └── ingress.yaml
├── .gitignore # Git ignores
└── README.md # This file

## Prerequisites
- Docker & Docker Compose  
- kubectl & a Kubernetes cluster (e.g. Docker Desktop)  
- Python 3.8+

## Local Docker-Compose Deployment
git clone https://gitlab.hof-university.de/mariocardenag/cloud_computing_2025.git
cd cloud_computing_2025

## Build and containers
docker compose up -d --build

## Links for browser
   Web1:    http://localhost:5001/create
   Web2:    http://localhost:5002/create
   HAProxy: http://localhost:8080/create

## Deployment of Kubernetes

(Re)build images if code changed
docker build -t notes-db:latest ./db
docker build -t notes-app:latest ./app

Apply K8s manifests
kubectl apply -f k8s/db-pvc.yaml
kubectl apply -f k8s/db-deployment.yaml
kubectl apply -f k8s/mongo-svc.yaml
kubectl apply -f k8s/web-deployment.yaml
kubectl apply -f k8s/web-svc.yaml
kubectl apply -f k8s/ingress.yaml

 Verify resources
kubectl get pods,svc,ingress

Port-forward Ingress
kubectl -n ingress-nginx port-forward svc/ingress-nginx-controller 8081:80

 Open in browser:
   Create note:  http://localhost:8081/create
   Search tag:   http://localhost:8081/search
   View user:    http://localhost:8081/user/your-email@example.com

The history that I used for this project was
Flask app skeleton

Dockerfiles for services

Docker-Compose setup

Kubernetes manifests & Services

Ingress implementation

Final documentation

Thank you teacher for watch my project!
