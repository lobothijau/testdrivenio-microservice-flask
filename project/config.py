class BaseConfig:
	"""Base configuration"""
	TESTING = False


class DevelopmentConfig(BaseConfig):
	"""Development confiugration"""
	pass


class TestingConfig(BaseConfig):
	"""Testing configuration"""
	TESTING = True


class ProductionConfig(BaseConfig):
	"""Production configuration"""
	pass