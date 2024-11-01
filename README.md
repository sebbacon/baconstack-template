# Python Web App Template for Baconstack

A modern Python web application template supporting FastAPI, Flask, and Django with integrated deployment to Dokku.

## Features

- 🚀 Multi-framework support (FastAPI, Flask, Django)
- 📦 Modern dependency management with uv
- 🔄 Zero-downtime deployments with health checks
- 🔍 Built-in logging with Loki support
- 🛠️ Development tools preconfigured:
  - Ruff for linting and formatting
  - pytest for testing
  - aider-chat for AI-assisted development
  - pre-commit hooks
- 🔐 Environment variable management
- 📊 Database migrations (Alembic/Django)
- 🐳 Dokku deployment ready

## Usage

This template is designed to be used with the `baconstack` CLI tool. However, you can also use it directly with copier:

```bash
# Using baconstack (recommended)
baconstack new myproject

# Using copier directly
copier copy gh:yourusername/baconstack-template myproject
```

[Rest of README same as before, with 'webstack' replaced with 'baconstack']

## See Also

- [baconstack CLI tool](https://github.com/yourusername/baconstack) - CLI tool for creating and managing projects
- [Dokku documentation](https://dokku.com/docs/)
