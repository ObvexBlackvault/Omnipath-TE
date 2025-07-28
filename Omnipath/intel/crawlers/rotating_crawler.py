import requests
import time
from utils.helpers import now, generate_id, log_event, safe_json

TARGET_URLS = [
    "https://huggingface.co/datasets",
    "https://data.gov",
    "https://registry.opendata.aws/",
    "https://www.kaggle.com/datasets",
    "https://paperswithcode.com/datasets",
    "https://arxiv.org/list/cs.AI/recent",
    "https://ai.google/discover",
    "https://ai.facebook.com/research"
]

def fetch_url(url):
    print(f"[CRAWLER] Pulling data from: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        size = len(response.text)
        print(f"[CRAWLER] SUCCESS: {url} - {size} bytes")

        log_data = {
            "url": url,
            "timestamp": now(),
            "status": "success",
            "size_bytes": size
        }
        print(safe_json(log_data))
        return response.text

    except requests.exceptions.HTTPError as http_err:
        print(f"[ERROR] HTTP error for {url}: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"[ERROR] Request failed for {url}: {req_err}")

    log_data = {
        "url": url,
        "timestamp": now(),
        "status": "failed"
    }
    print(safe_json(log_data))
    return None

def run_crawler():
    print("[CRAWLER] Starting rotating target fetch...")
    for url in TARGET_URLS:
        fetch_url(url)
        time.sleep(1)

if __name__ == "__main__":
    run_crawler()
