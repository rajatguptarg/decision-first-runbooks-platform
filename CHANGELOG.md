# Changelog

All notable changes to the Decision First Runbooks Platform will be documented in this file.

## [Unreleased]

### Added
- **Project Structure**: Created comprehensive directory structure for both backend (FastAPI) and frontend (React) applications
- **Docker Compose Setup**: Multi-service development environment with MongoDB, backend, and frontend services
- **Development Tooling**: 
  - Pre-commit hooks configuration with Black, Ruff, ESLint, and Prettier
  - Python linting and formatting with pyproject.toml configuration
  - Enhanced .gitignore patterns for Python and Node.js
- **Core Dependencies**:
  - Backend: FastAPI 0.104.1, Motor 3.3.2 (MongoDB async), JWT authentication, Docker SDK, pytest
  - Frontend: React 18, Vite build tool, Tailwind CSS, Framer Motion, Axios, TypeScript support
- **Basic Application Framework**:
  - FastAPI application with health check endpoints and CORS configuration
  - React application with Tailwind CSS integration and responsive design setup
  - Environment configuration templates for both backend and frontend
  - MongoDB initialization script with database schema and indexes
- **Documentation**: Updated README.md with comprehensive setup instructions and development commands
- **CI/CD**: Added GitHub Actions workflow for continuous integration