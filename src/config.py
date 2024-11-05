import os
from dotenv import load_dotenv

load_dotenv()

def get_env_var(var_name: str) -> str:
    """Retrieve environment variables and handle missing variables."""
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' is not set.")
    return value

# Load API keys and tokens
google_api_key = get_env_var("GEMINI_API_KEY")
bearer_token = get_env_var("bearer_token")
api_key = get_env_var("api_key")
api_secret = get_env_var("api_secret")
access_token = get_env_var("access_token")
access_token_secret = get_env_var("access_token_secret")