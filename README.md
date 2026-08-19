# demo-django-app

Application Django de demonstration pour la plateforme de qualification
DevSecOps (`modrikh/DevSecOps-pipeline`).

- Django 5.2, PostgreSQL (compose) / SQLite (tests locaux)
- API sante : `GET /api/health/`
- Dockerfile multi-usage (utilisateur non root) + `docker-compose.yml`
- Aucun secret reel : valeurs de dev prefixees `django-insecure-`

## Lancer localement

```bash
docker compose up -d --build   # http://localhost:8090
```

## Tests

```bash
pip install -r requirements.txt
coverage run manage.py test && coverage xml -o coverage.xml
```
