from django import db
from prompt_toolkit import Application
from prompt_toolkit.filters import app


class TestApplication(object):

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_create_app(self):
        application = Application()
        assert application.name == 'python_messenger'

    def test_get_ready_app_object(self):
        assert app.name == 'python_messenger'

    def test_bd_connection(self):
        assert db.check_connection()

    def test_make_config(self):
        assert app.config["SERVER"]["HOST"] == "127.0.0.1"
        assert app.config["SERVER"]["PORT"] == 8010

    def test_set_config_attr(self):
        app.config['GEEK_HOST'] = "https://geekbrains.ru"
        assert app.config["GEEK_HOST"] == "https://geekbrains.ru"