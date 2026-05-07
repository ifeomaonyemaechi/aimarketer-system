# run_upwork_agent.py
# Master runner for the Upwork Proposal Agent.
# Paste job URLs when prompted.
# Fetches job details, generates proposals, saves output.
# One command does everything.

import urllib.request
import json
import os
import re
import anthropic
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PROPOSAL_GUIDELINES = """
FIRST LINE - choose one based on the job post:
Option A (if they mention a time/volume problem):
"You're describing a [email/content/outreach] bottleneck - I've built the system that solves exactly that."

Option B (if they mention a specific tool like Klaviyo):
"I specialise in building AI systems on top of Klaviyo - not just using it, but automating the workflow around it."

Option C (if they mention wanting AI but seem unsure):
"Most AI freelancers will give you prompts. I build pipelines - Python + Claude API systems your team actually runs."

PARAGRAPH 1 - Prove you understand their problem (2-3 sentences):
Reflect their specific situation back at them using their language. Do not describe yourself yet.

PARAGRAPH 2 - Relevant proof (1-2 sentences):
Reference ONE portfolio project closest to their use case. State the metric, not the process.

PARAGRAPH 3 - What you would do for them (3-5 bullet points):
Specific deliverables. Use numbers where possible. No vague language.

CLOSING - One question + CTA:
Ask one diagnostic question that shows you have read their brief. Then a single clear call to action.
"""

PORTFOLIO_CASES = """
PORTFOLIO CASE STUDIES - use the most relevant one per proposal:

1. AI Email Campaign System - FemFit.fit
   Result: 13 emails across 4 campaign types generated in under 20 minutes.
   Built: Welcome series, promotional campaigns, re-engagement sequence, post-purchase flow.
   Stack: Python + Claude API + Klaviyo-ready output.

2. Brand Voice and Content Strategy Builder - FemFit.fit
   Result: 600+ line brand strategy document generated in 161 seconds.
   Built: Brand voice guide, 30-day content calendar, channel strategy, quick reference cards.
   Stack: Python + Claude API.

3. Lead Generation and Outreach Pipeline - Ifeoma Automation
   Result: 36 touchpoints across 6 leads generated in 264 seconds.
   Built: Lead qualification, cold email, LinkedIn and Instagram DM, 3-touch follow-up per lead.
   Stack: Python + Claude API.

4. Marketing Audit and Strategy Report - FemFit.fit
   Result: 5-channel audit with revenue projections generated in 221 seconds.
   Built: Email, Instagram, TikTok, website, SMS audit plus 90-day action plan.
   Stack: Python + Claude API.

5. Social Media Content Engine - FemFit.fit
   Result: 8 pieces of content including captions, carousel scripts, video briefs in 122 seconds.
   Built: Weekly content pack across Instagram and TikTok with production briefs.
   Stack: Python + Claude API.
"""

ABOUT_IFEOMA = """
Name: Ifeoma Onyemaechi
Business: Ifeoma Automation
Website: ifeomaautomation.com
Email: hello@ifeomaautomation.com
Location: Benoni, Gauteng, South Africa - works EST-compatible hours
Background: Claude AI Co-Worker Specialist and marketing automation specialist.
Specialises in building Python + Claude API systems for eCommerce and Klaviyo email marketing.
All 8 Anthropic Academy courses completed. Claude Code certified.
GitHub: github.com/ifeomaonyemaechi
"""

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
        print(f"  Could not fetch page: {e}")
        return None

def extract_job_details(html, url):
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', html)
    title = title_match.group(1).strip() if title_match else "Unknown Title"
    title = title.replace(" | Upwork", "").strip()

    desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
    description = desc_match.group(1).strip() if desc_match else ""

    if not description:
        og_match = re.search(r'<meta property="og:description" content="([^"]+)"', html)
        description = og_match.group(1).strip() if og_match else "No description extracted."

    return {
        "title": title,
        "description": description,
        "link": url,
        "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_proposal(job):
    prompt = f"""
You are writing an Upwork proposal on behalf of Ifeoma Onyemaechi of Ifeoma Automation.

ABOUT IFEOMA:
{ABOUT_IFEOMA}

PROPOSAL GUIDELINES - follow this format exactly:
{PROPOSAL_GUIDELINES}

PORTFOLIO CASE STUDIES - pick the single most relevant one:
{PORTFOLIO_CASES}

JOB TO WRITE A PROPOSAL FOR:
Title: {job['title']}
Description: {job['description']}
URL: {job['link']}

INSTRUCTIONS:
- Follow the proposal format exactly
- Pick the best first line option based on what the client described
- Pick the single most relevant portfolio case study
- Write specific deliverables based on what this client actually needs
- Close with one smart diagnostic question and a clear CTA
- Never use em dashes - use hyphens or colons instead
- Never use words like "leverage", "synergy", "optimize workflows", or "game-changing"
- Keep the whole proposal under 250 words
- Write in a confident, direct, numbers-driven tone
- Do not mention Ifeoma Automation as AIMarketer.co

Write the proposal now. No preamble. Start with the first line directly.
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text

def save_output(jobs, proposals):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/upwork_proposals_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("UPWORK PROPOSALS - Ifeoma Automation\n")
        f.write(f"Generated: {datetime.now().strftime('%d %B %Y, %H:%M')}\n")
        f.write(f"Total proposals: {len(proposals)}\n")
        f.write("=" * 60 + "\n")

        for i, p in enumerate(proposals, 1):
            f.write(f"\n{'=' * 60}\n")
            f.write(f"PROPOSAL {i} OF {len(proposals)}\n")
            f.write(f"Job: {p['job_title']}\n")
            f.write(f"URL: {p['job_url']}\n")
            f.write(f"{'=' * 60}\n\n")
            f.write(p["proposal_text"])
            f.write("\n")

    return filename

if __name__ == "__main__":
    print("=" * 60)
    print("UPWORK PROPOSAL AGENT - Ifeoma Automation")
    print("=" * 60)
    print("\nPaste your Upwork job URLs below.")
    print("One URL per line. Press Enter twice when done.\n")

    urls = []
    while True:
        line = input().strip()
        if line == "":
            if urls:
                break
            else:
                print("No URLs entered yet. Paste at least one URL.")
        else:
            urls.append(line)
            print(f"  Added: {line[:60]}...")

    print(f"\n{len(urls)} job(s) received. Fetching details...\n")

    jobs = []
    for url in urls:
        print(f"Fetching: {url[:60]}...")
        html = fetch_job_page(url)
        if html:
            job = extract_job_details(html, url)
            print(f"  Title: {job['title'][:60]}")
            print(f"  Description: {job['description'][:80]}...")
            jobs.append(job)
        else:
            print(f"  Skipped - could not fetch page.")

    if not jobs:
        print("\nNo jobs could be fetched. Check your URLs and try again.")
        exit()

    print(f"\n{len(jobs)} job(s) fetched. Generating proposals...\n")

    proposals = []
    for i, job in enumerate(jobs, 1):
        print(f"Writing proposal {i} of {len(jobs)}: {job['title'][:50]}...")
        proposal_text = generate_proposal(job)
        proposals.append({
            "job_title": job["title"],
            "job_url": job["link"],
            "proposal_text": proposal_text
        })
        print(f"  Done.")

    filename = save_output(jobs, proposals)

    print("\n" + "=" * 60)
    print(f"COMPLETE: {len(proposals)} proposal(s) generated.")
    print(f"Saved to: {filename}")
    print("=" * 60)
    print("\nOpen the file, review each proposal, copy and paste to Upwork.")