

class AppError(Exception):      
    """Base class for application-specific exceptions."""
    """Exception is a built-in Python class for all exceptions ie errors"""
    
    def __init__(self,message:str,status_code:int = 500): 
        super().__init__(message) # Call the base class constructor with the message
        self.message = message
        self.status_code = status_code
   
        
class NotFoundError(AppError):   # we can now create custom exceptions inheriting from AppError
    """Raised when a requested resource is not found."""
    
    def __init__(self,resource:str):
        super().__init__(f"{resource} not found",404)
  
        
class ValidationError(AppError):
    """Raised when data validation fails."""
    
    def __init__(self,message:str):
        super().__init__(message,400)
        

