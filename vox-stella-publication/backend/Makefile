.PHONY: run dev health

run:
	@gunicorn -c gunicorn.conf.py backend.app:app

dev:
	@FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0 --port=5000

health:
	@curl -fsS http://127.0.0.1:5000/healthz || \
		curl -fsS http://127.0.0.1:5000/api/health || true
