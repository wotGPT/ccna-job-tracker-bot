import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read values from .env
app_id = os.getenv("ADZUNA_APP_ID")
app_key = os.getenv("ADZUNA_APP_KEY")
location = os.getenv("LOCATION")

print("CCNA Job Tracker Bot")
print("--------------------")
print(f"Location: {location}")

# Security check
if app_id and app_key:
    print("API credentials loaded successfully.")
else:
    print("ERROR: API credentials not found.")
