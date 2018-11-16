from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager, Server
from apps import create_app

app = create_app()
manage = Manager(app)
manage.add_command('run', Server(port=8000))  # 多线程
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
