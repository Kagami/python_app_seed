from python_app_seed.config import *


class TestConfig(object):
    """
    Simple example to get your feet wet with pytest.
    Actually you need much more comprehensive test suite.
    """

    EXAMPLE_CONFIG_PATH = "python_app_seed.yaml.example"

    def test_init(self):
        init_config(self.EXAMPLE_CONFIG_PATH)

    def test_example_config(self):
        assert config.db_login == "test"
        assert config.port == 8000
        assert config.debug is True

    def test_config_assignment(self):
        config.test = False
        assert config['test'] is False

    def test_clear(self):
        config.clear()
        assert len(config.items) == 0
