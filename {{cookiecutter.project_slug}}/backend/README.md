# Proejct: {{ cookiecutter.project_name }}

# Develop usage:
uvicorn app.app:app --host=0.0.0.0 --port={{ cookiecutter.application_port }} --log-level=debug --reload

# Production usage:
gunicorn -k uvicorn.workers.UvicornWorker -w 2 api.app:app -b 0.0.0.0:{{ cookiecutter.aplication_port }}