# Contributing to Decision First Runbooks Platform

Thank you for your interest in contributing to the Decision First Runbooks Platform! This guide will help you get started with development, testing, and contributing to the project.

## Table of Contents

- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Project Structure](#project-structure)

## Development Setup

### Prerequisites

- **Docker & Docker Compose**: For containerized development environment
- **Node.js 18+**: For frontend development
- **Python 3.11+**: For backend development
- **Git**: For version control

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd decision-first-runbooks-platform
   ```

2. **Set up environment variables:**
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```
   
   Edit the `.env` files as needed for your local development environment.

3. **Start the development environment:**
   ```bash
   docker-compose up --build
   ```

4. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - MongoDB: localhost:27017

### Local Development (Without Docker)

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start MongoDB (ensure it's running on localhost:27017)
# Then start the backend
uvicorn app:app --reload
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Development Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code standards below

3. **Run tests and linting:**
   ```bash
   # Backend
   cd backend
   python -m pytest
   ruff check .
   black --check .
   
   # Frontend
   cd frontend
   npm test
   npm run lint
   ```

4. **Run pre-commit hooks:**
   ```bash
   pre-commit install  # First time only
   pre-commit run --all-files
   ```

5. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

6. **Push and create a pull request**

## Code Standards

### Backend (Python/FastAPI)

- **Code Style**: Black formatter with 88 character line length
- **Linting**: Ruff for fast Python linting
- **Type Hints**: Required for all function parameters and return values
- **Async/Await**: Use async/await for all database operations
- **Error Handling**: Consistent error response format:
  ```python
  # Success
  {"ok": True, "data": <response_data>}
  
  # Error
  {"ok": False, "error": {"code": "string", "message": "string", "details": "optional"}}
  ```

#### Backend File Organization

```
backend/
├── models/           # Pydantic data models
├── controllers/      # Business logic layer
├── views/           # API routes (presentation layer)
├── services/        # External integrations and utilities
└── tests/          # Test files
```

#### Backend Naming Conventions

- Use `snake_case` for Python files: `user_controller.py`
- Use `PascalCase` for classes: `UserModel`, `RunbookService`
- Use `snake_case` for functions and variables: `get_user_by_id`

### Frontend (React/TypeScript)

- **Code Style**: Prettier with 2-space indentation
- **Linting**: ESLint with React and TypeScript rules
- **Components**: Functional components with hooks (no class components)
- **Styling**: Tailwind CSS utility classes (avoid custom CSS)
- **State Management**: React hooks and context for state
- **File Extensions**: `.jsx` for JavaScript, `.tsx` for TypeScript

#### Frontend File Organization

```
frontend/src/
├── components/      # Reusable React components
├── pages/          # Page-level components
├── api/            # API client utilities
└── utils/          # Helper functions
```

#### Frontend Naming Conventions

- Use `PascalCase` for React components: `RunbookViewer.jsx`
- Use `camelCase` for JavaScript files: `apiClient.js`
- Use `kebab-case` for directories: `runbook-viewer/`

## Testing

### Backend Testing

```bash
cd backend

# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_runbooks.py -v

# Run with coverage
python -m pytest --cov=. --cov-report=html
```

#### Test Structure

- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test database operations and external services
- **API Tests**: Test HTTP endpoints using FastAPI TestClient

### Frontend Testing

```bash
cd frontend

# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

#### Test Files

- Place test files next to the components they test
- Use `.test.js` or `.test.tsx` extensions
- Test user interactions and component behavior

## Database Operations

### MongoDB Connection

The application uses Motor (async MongoDB driver) for database operations.

### Running Database Commands

```bash
# Connect to MongoDB container
docker exec -it runbooks-mongodb mongosh

# Use the runbooks database
use runbooks_db

# View collections
show collections

# Seed database (if seed script exists)
cd backend && python seed.py
```

### Database Schema

Collections:
- `users`: User accounts with roles and authentication
- `runbooks`: Runbook documents with decision trees
- `sessions`: Incident session tracking and timelines

## Submitting Changes

### Pull Request Guidelines

1. **Title**: Use conventional commit format:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for adding tests

2. **Description**: Include:
   - What changes were made and why
   - Any breaking changes
   - Instructions for testing the changes

3. **Checklist**: Ensure your PR includes:
   - [ ] Tests for new functionality
   - [ ] Updated documentation if needed
   - [ ] Code follows project standards
   - [ ] All tests pass
   - [ ] Pre-commit hooks pass

### Code Review Process

- All changes require review from at least one maintainer
- Address feedback and update your branch as needed
- Keep your branch up to date with the main branch

### Continuous Integration (CI)

All pull requests are automatically tested using GitHub Actions. The CI pipeline runs the following checks:

- **Backend**: Lints, formats, and runs tests for the FastAPI application.
- **Frontend**: Lints, tests, and builds the React application.

Please ensure that all CI checks pass before requesting a review. You can see the status of the checks on your pull request page.

## Common Development Tasks

### Adding a New API Endpoint

1. Create the Pydantic model in `backend/models/`
2. Add business logic in `backend/controllers/`
3. Create the route in `backend/views/`
4. Add tests in `backend/tests/`

### Adding a New React Component

1. Create the component in `frontend/src/components/`
2. Add proper TypeScript types
3. Style with Tailwind CSS classes
4. Add tests for the component

### Database Schema Changes

1. Update the MongoDB initialization script in `scripts/init-mongo.js`
2. Create migration scripts if needed
3. Update corresponding Pydantic models
4. Test with fresh database

## Getting Help

- Check existing issues and discussions
- Review the project documentation in `.kiro/`
- Ask questions in pull request comments
- Follow the project's code standards and conventions

## Environment Variables

### Backend (.env)
```
MONGODB_URI=mongodb://admin:password123@localhost:27017/runbooks_db?authSource=admin
JWT_SECRET=your-super-secret-jwt-key-change-in-production
ACCESS_TOKEN_TTL_MIN=15
REFRESH_TOKEN_TTL_MIN=43200
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000/api
```

Thank you for contributing to the Decision First Runbooks Platform!