
# Wisecow Kubernetes Deployment

This project demonstrates how to containerize and deploy the Wisecow application on Kubernetes, with CI/CD automation and basic system/app health scripts.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Run Locally](#run-locally)
  - [Run with Docker](#run-with-docker)
  - [Deploy to Kubernetes](#deploy-to-kubernetes)
- [CI/CD Pipeline](#cicd-pipeline)
- [Health Monitoring Scripts](#health-monitoring-scripts)
- [License](#license)

---

## Overview

- **Wisecow** is a simple Bash-based web server that returns a random fortune using cowsay.
- The app is containerized with Docker and can be deployed to Kubernetes.
- Includes GitHub Actions workflow for automated Docker builds and pushes.
- Includes Python scripts for system and application health checks.

---

## Project Structure

```
wisecow-k8s-main/
│
├── Dockerfile                # Container build instructions
├── wisecow.sh                # Main Bash app
├── k8s/
│   ├── deployment.yaml       # Kubernetes Deployment
│   ├── namespace.yaml        # Kubernetes Namespace
│   └── service.yaml          # Kubernetes Service
├── .github/
│   └── workflows/
│       └── ci-cd.yaml        # GitHub Actions workflow
├── system_health_monitor.py  # System health check script
├── app_health_checker.py     # App health check script
├── README.md                 # Project documentation
└── LICENSE
```

---

## How It Works

- **wisecow.sh**: Listens on port 4499, returns a random fortune in cowsay format.
- **Dockerfile**: Packages the app and its dependencies.
- **Kubernetes Manifests**: Deploy the app in a cluster, expose it via NodePort.
- **CI/CD**: GitHub Actions builds and pushes the Docker image to GitHub Container Registry (GHCR) on every push to main.
- **Python Scripts**: Check system health and app availability.

---

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Git Bash](https://gitforwindows.org/) or [WSL](https://docs.microsoft.com/en-us/windows/wsl/) (for running Bash scripts on Windows)
- [Docker](https://www.docker.com/products/docker-desktop) (optional, for containerization)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) and a local Kubernetes cluster (e.g., Minikube or Kind) for Kubernetes deployment

---

### Run Locally (Bash)

1. Open Git Bash or WSL.
2. Install dependencies:
	```
	sudo apt update
	sudo apt install fortune cowsay netcat-openbsd
	```
3. Navigate to the project folder:
	```
	cd /c/Users/hp/Downloads/wisecow-k8s-main/wisecow-k8s-main
	```
4. Run the app:
	```
	bash wisecow.sh
	```
5. In another terminal, test:
	```
	curl http://localhost:4499
	```

---

### Run with Docker

1. Build the Docker image:
	```
	docker build -t wisecow .
	```
2. Run the container:
	```
	docker run -p 4499:4499 wisecow
	```
3. Test:
	```
	curl http://localhost:4499
	```

---

### Deploy to Kubernetes

1. Update `k8s/deployment.yaml` with your GitHub username in the image field.
2. Apply the manifests:
	```
	kubectl apply -f k8s/namespace.yaml
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml
	```
3. Find the NodePort:
	```
	kubectl get svc -n wisecow
	```
4. Access the app:
	```
	curl http://localhost:<NodePort>
	```

---

## CI/CD Pipeline

- The workflow in `.github/workflows/ci-cd.yaml` automatically builds and pushes the Docker image to GHCR on every push to the main branch.

---

## Health Monitoring Scripts

- **system_health_monitor.py**: Checks CPU, memory, and disk usage. Alerts if thresholds are exceeded.
  ```
  python system_health_monitor.py
  ```
- **app_health_checker.py**: Checks if the app is running and responding.
  ```
  python app_health_checker.py http://localhost:4499
  ```

---

## License

This project is licensed under the MIT License.

---
