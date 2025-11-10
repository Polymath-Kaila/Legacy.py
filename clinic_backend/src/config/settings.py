"""handles configuration management: 
   reading environment variables, setting defaults
   and centralizing configuration access for the app.
"""


import os                      # for accessing environment variables
from dotenv import load_dotenv # for loading .env files

# Load environment variables from a .env 
load_dotenv() #reads `.env` file and loads all key-value pairs into environment variables

class Settings:
    """Centralized configuration settings for the app"""
    
    def __init__(self): # Initialize settings with environment variables or defaults
        self.APP_NAME = os.getenv("APP_NAME","ClinicBackend")
        self.ENV      = os.getenv("ENV","development")
        self.DEBUG    = os.getenv("DEBUG","true").lower()=="true"  # Convert to boolean
        
        # Database configuration
        self.DB_HOST  = os.getenv("DB_HOST","localhost")          # Database host
        self.DB_PORT  = os.getenv("DB_PORT","5432")               # Database port
        self.DB_NAME  = os.getenv("DB_NAME","clinic_db")          # Database name
        self.DB_USER  = os.getenv("DB_USER","postgres")           # Database user
        self.DB_PASSWORD = os.getenv("DB_PASSWORD","password")    # Database password
        
        # Logging level
        self.LOG_LEVEL = os.getenv("LOG_LEVEL","INFO")            # Logging level
        
# create a single settings instance to be used throughout the app
settings = Settings()        
        