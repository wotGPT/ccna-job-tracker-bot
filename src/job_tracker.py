import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")
LOCATION = os.getenv("LOCATION")

SEARCH_TERMS = [
    "NOC Technician",
    "Network Technician",
    "Junior Network Administrator",
    "Network Support Technician",
    "Help Desk Network",
    "CCNA"
]

url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

for term in SEARCH_TERMS:

    print()
    print("=" * 60)
    print(f"Searching for: {term}")
    print("=" * 60)

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": term,
        "where": LOCATION,
        "results_per_page": 5
    }

    response = requests.get(url, params=params)

    print("Status Code:", response.status_code)

    data = response.json()

    jobs = data.get("results", [])

    print("Jobs Found:", len(jobs))

    for job in jobs:

        title = job.get("title", "Unknown Title")

        company = job.get(
            "company", {}
        ).get(
            "display_name",
            "Unknown Company"
        )

        print()
        print(f"Title: {title}")
        print(f"Company: {company}")
