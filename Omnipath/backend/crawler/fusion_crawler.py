import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import datetime
from backend.core.trace_log import write_trace
from utils.helpers import generate_id

SAVE_DIR = os.path.expanduser("~/Omnipath/backend/memory/crawler_parsed")
os.makedirs(SAVE_DIR, exist_ok=True)

CRAWL_TARGETS = [
    "https://huggingface.co/datasets",
    "https://data.gov",
    "https://registry.opendata.aws/",
    "https://www.kaggle.com/datasets",
    "https://paperswithcode.com/datasets",
    "https://arxiv.org/list/cs.AI/recent",
]

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return {"error": f"{url} returned status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def parse_content(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string if soup.title else "Untitled"
    headers = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
    links = [a.get("href") for a in soup.find_all("a", href=True)]
    return {
        "title": title,
        "headers": headers,
        "links": links,
    }

def save_json(data, url, tag="parsed"):
    uid = generate_id()
    filename = os.path.join(SAVE_DIR, f"{tag}_{uid}.json")
    with open(filename, "w") as f:
        json.dump({
            "url": url,
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }, f, indent=2)
    return filename

def run_crawler():
    for url in CRAWL_TARGETS:
        print(f"[CRAWLER] Pulling data from: {url}")
        html = fetch_page(url)
        if isinstance(html, dict) and "error" in html:
            print(f"[ERROR] {html['error']}")
            write_trace("crawl_fail", metadata={"url": url, "error": html["error"]})
        else:
            structured = parse_content(html)
            path = save_json(structured, url)
            write_trace("crawl_success", metadata={"url": url, "output": path})

if __name__ == "__main__":
    run_crawler()
