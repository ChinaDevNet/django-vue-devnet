## 初版目标
1. 验证TEXTFSM解析器集成，统一数据模型。
2. 验证配置备份功能对接git




```angular2html
├── application
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── dispatch.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── conf
├── del_migrations.py
├── docker_start.sh
├── logs
│├── error.log
│└── server.log
├── manage.py
├── media
│├── config_files
│├── textfsm_templates
└── tools
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── parser_tmp.py  # textfsm解析验证
    ├── tests.py
    └── views.py

```