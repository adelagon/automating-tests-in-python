# %load src/conftest.py
class Storage:
    """
    Shared variables
    """
    user_id = None
    user_name = None
    response = None

class Config:
    """
    Test configurations
    """
    users_endpoint = "http://localhost:3000/users"
    user_endpoint = "http://localhost:3000/users/{}"
