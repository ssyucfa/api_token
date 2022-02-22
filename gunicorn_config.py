command = '/root/code/project/bin/start_gunicorn.sh'
pythonpath = '/root/code/project/api_token/'
bind = '127.0.0.1:800'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=core.settings'
