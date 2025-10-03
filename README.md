# DevOps Web App Deployment to Kubernetes with CI/CD

## Project Overview

This project demonstrates an end-to-end DevOps workflow for deploying a simple Python Flask web application to a Kubernetes cluster using Docker for containerization and GitHub Actions for Continuous Integration/Continuous Deployment (CI/CD).

It showcases key skills in:
- **Infrastructure as Code (IaC) principles** (though not explicitly using Terraform here, the Kubernetes manifests represent IaC for application deployment)
- **Containerization** with Docker
- **Container Orchestration** with Kubernetes
- **CI/CD Pipeline Automation** with GitHub Actions
- **Cloud-native application deployment**

## Architecture

The project consists of the following components:

1.  **Flask Web Application (`app/app.py`):** A minimal Python Flask application that serves a "Hello, World!" message.
2.  **Dockerfile (`Dockerfile`):** Defines how to build a Docker image for the Flask application.
3.  **Kubernetes Manifests (`k8s/deployment.yaml`, `k8s/service.yaml`):**
    *   `deployment.yaml`: Defines a Kubernetes Deployment to manage multiple replicas of the web application.
    *   `service.yaml`: Defines a Kubernetes Service to expose the web application to the internet via a LoadBalancer.
4.  **GitHub Actions Workflow (`.github/workflows/main.yml`):** An automated pipeline that builds the Docker image and pushes it to a container registry upon every push to the `main` branch.

## Getting Started

Follow these steps to set up and deploy this project.

### Prerequisites

*   **Docker Hub Account:** Required to store your Docker images. Replace `YOUR_DOCKER_HUB_USERNAME` in `k8s/deployment.yaml` and `.github/workflows/main.yml` with your actual Docker Hub username.
*   **Kubernetes Cluster:** Access to a Kubernetes cluster (e.g., Minikube, Kind, GKE, EKS, AKS). For local testing, Minikube or Kind are recommended.
*   **`kubectl`:** Kubernetes command-line tool configured to connect to your cluster.
*   **GitHub Repository:** A new GitHub repository where you will push this project.

### 1. Clone the Repository (after creating it on GitHub)

First, create a new **public** GitHub repository (e.g., `devops-webapp-k8s`). Do NOT initialize it with a README or license. Then, clone this project locally and push it to your new GitHub repository:

```bash
git init
git add .
git commit -m "Initial commit: DevOps Web App to K8s"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/devops-webapp-k8s.git # Replace with your GitHub username and repo name
git push -u origin main
```

### 2. Configure GitHub Secrets

For the GitHub Actions workflow to push Docker images, you need to configure secrets in your GitHub repository:

1.  Go to your GitHub repository settings.
2.  Navigate to `Secrets and variables` > `Actions`.
3.  Click `New repository secret` and add the following:
    *   `DOCKER_USERNAME`: Your Docker Hub username.
    *   `DOCKER_PASSWORD`: Your Docker Hub access token or password (it's recommended to use an access token for security).

### 3. GitHub Actions CI/CD (Automated Build & Push)

Once you push the code to your `main` branch and configure the secrets, the GitHub Actions workflow (`.github/workflows/main.yml`) will automatically trigger. It will:

*   Build the Docker image for the Flask application.
*   Tag the image with `latest` and the GitHub SHA.
*   Push the tagged images to your Docker Hub repository.

You can monitor the progress of the workflow in the "Actions" tab of your GitHub repository.

### 4. Manual Deployment to Kubernetes

After the Docker image is successfully pushed to Docker Hub by the CI pipeline, you can manually deploy the application to your Kubernetes cluster.

1.  **Ensure `kubectl` is configured** to point to your target Kubernetes cluster.
2.  **Apply the Kubernetes manifests:**

    ```bash
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

3.  **Verify the deployment:**

    ```bash
    kubectl get deployments
    kubectl get pods
    kubectl get services
    ```

4.  **Access the application:**

    Once the service is provisioned (this might take a few minutes for a LoadBalancer), you can get the external IP address:

    ```bash
    kubectl get services devops-webapp-service
    ```

    Look for the `EXTERNAL-IP` in the output. You can then access your "Hello, World!" application by navigating to `http://<EXTERNAL-IP>` in your web browser.

## Future Enhancements (Ideas for further development)

*   **Automated Kubernetes Deployment in CI/CD:** Integrate the `kubectl apply` step directly into the GitHub Actions workflow. This would require securely configuring Kubernetes credentials (e.g., `KUBE_CONFIG` as a GitHub Secret) in the pipeline.
*   **Helm Charts:** Package the Kubernetes manifests into a Helm chart for easier management and deployment.
*   **Monitoring:** Add Prometheus and Grafana to monitor the application and cluster health.
*   **Terraform for Cluster Provisioning:** Use Terraform to provision the Kubernetes cluster itself (e.g., GKE cluster on GCP, EKS on AWS).
*   **Testing:** Implement unit and integration tests for the Flask application and add them to the CI pipeline.
*   **Rollback Strategy:** Define and implement a rollback strategy for deployments.

## Contributing

Feel free to fork this repository and adapt it to your needs. Contributions are welcome!


