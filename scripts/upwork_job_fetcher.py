# upwork_job_fetcher.py
# Takes Upwork job URLs you paste manually.
# Fetches job details from each URL.
# Saves results to outputs/ for the proposal generator to use.

import urllib.request
import json
import os
import re
from datetime import datetime

# Paste your Upwork job URLs here
JOB_URLS = [
    # Example - replace with real URLs:
    # "https://www.upwork.com/jobs/~01abc123def456",
]

def fetch_job_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  Could not fetch {url}: {e}")
        return None

def extract_job_details(html, url):
    # Pull title
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', html)
    title = title_match.group(1).strip() if title_match else "Unknown Title"
    title = title.replace(" | Upwork", "").strip()

    # Pull description from meta tag
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
    description = desc_match.group(1).strip() if desc_match else ""

    # Pull og:description as fallback
    if not description:
        og_match = re.search(r'<meta property="og:description" content="([^"]+)"', html)
        description = og_match.group(1).strip() if og_match else "No description extracted."

    return {
        "title": title,
        "description": description,
        "link": url,
        "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def save_jobs(all_jobs):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/upwork_jobs_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(all_jobs)} jobs to {filename}")
    return filename

if __name__ == "__main__":
    print("=" * 50)
    print("UPWORK JOB FETCHER")
    print(f"Jobs to process: {len(JOB_URLS)}")
    print("=" * 50)

    if not JOB_URLS:
        print("\nNo URLs found in JOB_URLS list.")
        print("Open upwork_job_fetcher.py and paste your job URLs into the JOB_URLS list.")
        exit()

    all_jobs = []
    for url in JOB_URLS:
        print(f"\nFetching: {url}")
        html = fetch_job_page(url)
        if html:
            job = extract_job_details(html, url)
            print(f"  Title: {job['title']}")
            print(f"  Description preview: {job['description'][:100]}...")
            all_jobs.append(job)

    save_jobs(all_jobs)