import logging
from src.config.settings import settings

def setup_logger():
    """"Configures and returns a logger insatance"""
    logger = logging.getLogger(settings.APP_NAME)      # Initialize logger with app name
    logger.setLevel(settings.LOG_LEVEL)                # Set logging level from settings
    
    #Avoid duplicate handlers if logger is already configured
    
    if logger.hasHandlers():
        return logger
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  "%Y-%m-%d %H:%M:%S")                    # Define log message format
    
    console_handler = logging.StreamHandler()                           # Create console handler
    console_handler.setFormatter(formatter)                             # Set formatter for console handler
    logger.addHandler(console_handler)                                 # Add console handler to logger
    
    return logger
logger = setup_logger()  # Create a global logger instance