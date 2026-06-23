import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read variables from .env
app_id = os.getenv("ADZUNA_APP_ID")
app_key = os.getenv("ADZUNA_APP_KEY")
location = os.getenv("LOCATION")

print("CCNA Job Tracker Bot")
print("--------------------")
print(f"Location: {location}")

if app_id and app_key:
    print("SUCCESS: API credentials loaded.")
else:
    print("ERROR: API credentials not found.")
