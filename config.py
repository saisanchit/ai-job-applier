"""Configuration module for the AI Job Applier application."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration class."""

    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    # Job search settings
    JOB_SEARCH_QUERY = os.getenv('JOB_SEARCH_QUERY', '')
    LOCATION = os.getenv('LOCATION', '')
    
    # API settings
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))

    # Database settings (if needed)
    DATABASE_URL = os.getenv('DATABASE_URL', '')

    def __repr__(self):
        return f"<Config DEBUG={self.DEBUG}, LOG_LEVEL={self.LOG_LEVEL}>"
