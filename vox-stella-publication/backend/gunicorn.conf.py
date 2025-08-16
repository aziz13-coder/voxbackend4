import os

bind = f"0.0.0.0:{os.environ.get('PORT', 5000)}"
workers = 2
threads = 2
timeout = 120
graceful_timeout = 30
keepalive = 2
accesslog = "-"
errorlog = "-"