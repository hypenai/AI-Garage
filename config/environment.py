# Environment-specific configuration

import os
from config import Config

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'sqlite:///dev_ai_garage.db')

class ProductionConfig(Config):
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///prod_ai_garage.db')
