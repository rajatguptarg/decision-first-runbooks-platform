# Decision First Runbooks Platform

[![CI](https://github.com/Vibe-Inc/decision-first-runbooks-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Vibe-Inc/decision-first-runbooks-platform/actions/workflows/ci.yml)

A production-ready implementation that manages and displays decision-first incident runbooks for effective incident response.

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd decision-first-runbooks-platform
```

2. Set up environment variables:
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

3. Start all services with Docker Compose:
```bash
docker-compose up --build
```

4. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- MongoDB: localhost:27017

### Local Development (without Docker)

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Architecture

- **Backend**: FastAPI with MongoDB (Motor async driver)
- **Frontend**: React 18 + Vite + Tailwind CSS
- **Database**: MongoDB 7 with document-based storage
- **Authentication**: JWT with HTTP-only cookies
- **Containerization**: Docker and Docker Compose

## Development Commands

### Testing
```bash
# Backend tests
cd backend && python -m pytest

# Frontend tests
cd frontend && npm test
```

### Code Quality
```bash
# Run pre-commit hooks
pre-commit run --all-files

# Backend linting
cd backend && ruff check . && black --check .

# Frontend linting
cd frontend && npm run lint
```

## Project Structure

```
├── backend/              # Python FastAPI backend
├── frontend/             # React frontend
├── scripts/              # Database initialization scripts
├── docker-compose.yml    # Multi-container orchestration
└── .kiro/               # Project specifications and steering
```
