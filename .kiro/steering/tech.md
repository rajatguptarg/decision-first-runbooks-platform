# Technology Stack & Build System

## Tech Stack

### Backend
- **Framework**: Python FastAPI with async/await support
- **Database Driver**: Motor (async MongoDB driver)
- **Server**: Uvicorn ASGI server
- **Authentication**: JWT tokens with HTTP-only cookies
- **Password Hashing**: bcrypt via passlib
- **Validation**: Pydantic models with automatic request/response validation
- **Testing**: httpx AsyncClient for API tests

### Frontend
- **Framework**: React 18 with functional components and hooks
- **Build Tool**: Vite for fast development and optimized builds
- **Styling**: Tailwind CSS utility classes
- **Animations**: Framer Motion for interactive elements
- **Icons**: Lucide React icon library
- **HTTP Client**: Axios with automatic cookie handling
- **Routing**: React Router for client-side navigation

### Database
- **Primary**: MongoDB 7 with document-based storage
- **Indexes**: Text indexes on title/owner, compound indexes for queries
- **Connection**: Single Motor client with connection pooling

### Infrastructure
- **Containerization**: Docker and Docker Compose
- **Development**: Hot reload for both frontend and backend
- **Observability**: Structured logging and basic request metrics

## Common Commands

### Development Setup
```bash
# Start all services
docker-compose up

# Start with rebuild
docker-compose up --build

# Backend only (port 8000)
cd backend && uvicorn app:app --reload

# Frontend only (port 5173)
cd frontend && npm run dev
```

### Testing
```bash
# Backend tests
cd backend && python -m pytest

# Frontend tests
cd frontend && npm test

# Run specific test file
cd backend && python -m pytest tests/test_runbooks.py -v
```

### Database Operations
```bash
# Connect to MongoDB
docker exec -it <mongo_container> mongosh

# View collections
use runbooks
show collections

# Seed database
cd backend && python seed.py
```

## Environment Variables

### Backend (.env)
- `MONGODB_URI`: MongoDB connection string
- `DB_NAME`: Database name (default: runbooks)
- `JWT_SECRET`: Secret key for JWT signing
- `ACCESS_TOKEN_TTL_MIN`: Access token TTL in minutes (default: 15)
- `REFRESH_TOKEN_TTL_MIN`: Refresh token TTL in minutes (default: 43200)
- `EDITOR_BOOTSTRAP_EMAIL`: Initial editor account email
- `EDITOR_BOOTSTRAP_PASSWORD`: Initial editor account password

### Frontend (.env)
- `VITE_API_BASE`: API base URL (default: /api)

## Code Style & Conventions

### Python (Backend)
- Use async/await for all database operations
- Pydantic models for all data validation
- FastAPI dependency injection for database connections
- Consistent error response format: `{"ok": false, "error": {...}}`
- Type hints for all function parameters and return values

### JavaScript/React (Frontend)
- Functional components with hooks (no class components)
- Consistent API client usage with error handling
- Tailwind utility classes (avoid custom CSS)
- Framer Motion for interactive animations
- Proper error boundaries and loading states

## Validation Rules

### Runbook Validation
- All node IDs must be unique within a runbook
- Decision graph must be a tree with no cycles
- Leaf nodes must have actions and no options
- Date format: YYYY-MM-DD for lastUpdated field

### API Response Format
- Success: `{"ok": true, "data": <response_data>}`
- Error: `{"ok": false, "error": {"code": "string", "message": "string", "details": "optional"}}`