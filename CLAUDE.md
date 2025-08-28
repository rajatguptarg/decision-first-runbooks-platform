# CLAUDE.md

Follow the documents in the steering directory to understand the project's structure and purpose.

The steering files are organized as follows:

1. `.kiro/steering/product.md` - Product overview covering:

- Core purpose and business value
- Key features and capabilities
- Target users (incident responders, editors, system administrators)
- Business impact on incident response standardization

2. `.kiro/steering/tech.md` - Technology stack and build system covering:

- Complete tech stack (FastAPI, React, MongoDB, Docker)
- Common development commands for setup, testing, and database operations
- Environment variables and configuration
- Code style conventions for both Python and React
- Validation rules and API response formats

3. `.kiro/steering/structure.md` - Project organization covering:

- Complete directory structure for both backend and frontend
- Data model organization (MongoDB collections and Pydantic models)
- API endpoint organization with clear routing structure
- Configuration files and their purposes
- Naming conventions for files, directories, databases, and APIs

These steering files will help guide on AI assistant working on this project by providing:

- Clear understanding of the product goals and user needs
- Technical context about the stack and development workflows
- Structural guidelines for maintaining consistent code organization
- Conventions for naming and organizing code components

The specs for the project can be found under `.kiro/specs/{feature-name}/` with the following files:

- `design.md`: The comprehensive design document based on the requirements and research. The design ensures the system can safely execute commands in isolated environments while providing the interactive decision-tree navigation and comprehensive session tracking required for effective incident response.
- `requirements.md`: A comprehensive requirements document based on your product overview. The requirements are structured with user stories and detailed acceptance criteria in EARS format, covering all the key features
- `tasks.md`: The implementation plan with actionable coding tasks based on the requirements and design.

The files are concise but comprehensive, capturing the essential information needed for effective development while following the project's established patterns and conventions.

After making the changes, always perform the following:

- Create or update the `CHANGELOG.md` file to reflect the changes made to the project.
- Create or update the `README.md` file to reflect the changes made to the project.
- Create or update the `CONTRIBUTING.md` to update the guide to test, run locally and contribute to the project.
- Create or update the `.github/workflows/ci.yml` file to reflect the changes made to the project.
- Update any steering documents, if needed.

These updates ensure that the project's documentation remains accurate and up-to-date, facilitating clear communication and collaboration among team members.
