# Project Structure & Organization

## Root Directory Layout

```
/
├── .git/                    # Git repository metadata
├── .gitignore              # Git ignore patterns
├── .kiro/                  # Kiro IDE configuration
│   ├── steering/           # AI assistant steering rules
│   └── specs/              # Project specifications
├── README.md               # Main project documentation
├── SYSTEM_DESIGN.md        # System architecture documentation
├── AGENTS.md               # OpenAI Codex guidance
├── CLAUDE.md               # Claude AI guidance
├── GEMINI.md               # Google Gemini guidance
├── LICENSE                 # Project license
├── UI.png                  # Reference UI mockup
├── docker-compose.yml      # Multi-container orchestration
├── backend/                # Python FastAPI backend
└── frontend/               # React frontend application
```

## Backend Structure (MVC Architecture)

```
backend/
├── app.py                  # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── Dockerfile             # Backend container configuration
├── .env                   # Environment variables (not in git)
├── config.py              # Application configuration
├── deps.py                # FastAPI dependencies
├── seed.py                # Database seeding script
├── models/                # Models (Data layer)
│   ├── __init__.py
│   ├── user.py            # User data model
│   ├── runbook.py         # Runbook data model
│   ├── session.py         # Session data model
│   └── base.py            # Base model utilities
├── controllers/           # Controllers (Business logic layer)
│   ├── __init__.py
│   ├── auth_controller.py # Authentication business logic
│   ├── runbook_controller.py # Runbook business logic
│   └── session_controller.py # Session business logic
├── views/                 # Views (Presentation layer - API routes)
│   ├── __init__.py
│   ├── auth_routes.py     # Authentication endpoints
│   ├── runbook_routes.py  # Runbook CRUD endpoints
│   └── session_routes.py  # Session management endpoints
├── services/              # Service layer (External integrations)
│   ├── __init__.py
│   ├── database.py        # Database connection and utilities
│   ├── auth_service.py    # Authentication utilities (JWT, hashing)
│   └── validation_service.py # Data validation utilities
└── tests/                 # Backend test suite
    ├── __init__.py
    ├── conftest.py        # Pytest configuration
    ├── test_auth.py       # Authentication tests
    ├── test_runbooks.py   # Runbook operation tests
    └── test_sessions.py   # Session management tests
```

## Frontend Structure

```
frontend/
├── index.html             # HTML entry point
├── package.json           # Node.js dependencies and scripts
├── package-lock.json      # Dependency lock file
├── vite.config.js         # Vite build configuration
├── tailwind.config.js     # Tailwind CSS configuration
├── Dockerfile             # Frontend container configuration
├── .env                   # Environment variables (not in git)
├── src/                   # Source code
│   ├── main.jsx           # React application entry point
│   ├── App.jsx            # Main application component
│   ├── api/               # API client utilities
│   │   └── client.js      # Axios HTTP client configuration
│   ├── components/        # Reusable React components
│   │   ├── Pill.jsx       # Severity indicator component
│   │   ├── SectionCard.jsx # Card layout component
│   │   ├── CopyButton.jsx # Copy-to-clipboard component
│   │   ├── RunbookViewer.jsx # Decision tree viewer
│   │   ├── RunbookList.jsx # Runbook listing component
│   │   └── Header.jsx     # Navigation header
│   └── pages/             # Page-level components
│       ├── ViewerPage.jsx # Main viewer interface
│       ├── EditorPage.jsx # Runbook editor interface
│       └── LoginPage.jsx  # Authentication page
└── public/                # Static assets
    └── favicon.ico        # Application favicon
```

## Data Model Organization

### Collections (MongoDB)
- **runbooks**: Main runbook documents with decision trees
- **incident_sessions**: User session tracking and timelines
- **users**: User accounts with roles and authentication

### Key Models (Pydantic)
- **User**: Authentication and role management
- **Runbook**: Complete runbook with metadata and decision tree
- **DecisionNode**: Individual nodes in decision trees
- **DecisionOption**: Options within decision nodes
- **IncidentSession**: Session state and timeline tracking
- **TimelineEvent**: Individual events in session timelines

## API Organization

### Base URL: `/api`

#### Authentication Routes (`/auth`)
- `POST /auth/register` - User registration
- `POST /auth/login` - User login with cookie setting
- `POST /auth/refresh` - Token refresh
- `POST /auth/logout` - User logout with cookie clearing

#### Runbook Routes (`/runbooks`)
- `GET /runbooks` - List runbooks with search/filter
- `GET /runbooks/{id}` - Get specific runbook
- `POST /runbooks` - Create new runbook (editor only)
- `PUT /runbooks/{id}` - Update runbook (editor only)
- `DELETE /runbooks/{id}` - Delete runbook (editor only)
- `GET /runbooks/{id}/export` - Export runbook as JSON

#### Session Routes (`/sessions`)
- `POST /sessions` - Create new incident session
- `GET /sessions/{sessionId}` - Get session details
- `POST /sessions/{sessionId}/choose` - Make decision choice
- `POST /sessions/{sessionId}/reset` - Reset session to root

#### Utility Routes
- `GET /health` - Health check endpoint

## Configuration Files

### Docker Configuration
- `docker-compose.yml`: Multi-service orchestration
- `backend/Dockerfile`: Python FastAPI container
- `frontend/Dockerfile`: Node.js React container

### Build Configuration
- `backend/requirements.txt`: Python package dependencies
- `frontend/package.json`: Node.js package dependencies
- `frontend/vite.config.js`: Vite build tool configuration
- `frontend/tailwind.config.js`: Tailwind CSS configuration

### Development Configuration
- `.gitignore`: Version control exclusions
- `backend/.env`: Backend environment variables
- `frontend/.env`: Frontend environment variables

## Naming Conventions

### Files and Directories
- Use lowercase with hyphens for directories: `incident-sessions`
- Use PascalCase for React components: `RunbookViewer.jsx`
- Use snake_case for Python files: `test_runbooks.py`
- Use camelCase for JavaScript files: `apiClient.js`

### Database Collections
- Use snake_case: `incident_sessions`, `runbooks`, `users`

### API Endpoints
- Use kebab-case for multi-word resources: `/incident-sessions`
- Use plural nouns for collections: `/runbooks`
- Use specific IDs for individual resources: `/runbooks/{id}`

### Environment Variables
- Use UPPER_SNAKE_CASE: `MONGODB_URI`, `JWT_SECRET`