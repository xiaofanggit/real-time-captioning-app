## 🎧 Real Time Captioning App

A full-stack real time caption app built with:

- **FastAPI (Python)** for the backend
- **React + Vite + Material UI** for the frontend
- **Docker** for local development

### ⚙️ Prerequisites

Install [Docker Desktop](https://www.docker.com/products/docker-desktop) for:

- **Mac**
- **Windows**

Verify installation:

```bash
docker --version
docker compose version
```

Clone the repo

git clone https://github.com/xiaofanggit/real-time-captioning-app.git

Build the container:

```bash
docker compose build # (Old version: docker-compose build)
```

▶️Start the app:

```bash
docker compose up # (Old version: docker-compose up)
```

Open in browser

Frontend: http://localhost:5173

Backend Swagger API: http://127.0.0.1:8000/docs

## Note: You could also open backend and frontend using the below ways

### 🔙 backend

- virtual env instead of docker

```bash
cd real-time-captioning-app/backend
rm -rf venv # remove broken virtual env in case
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install requirements-dev.txt
```

✅ python3 run.py

### 🎨 frontend

```bash
npm create react
```
