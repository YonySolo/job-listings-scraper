"""
Job Listings Scraper
Scrapes job listings from the Fake Python Jobs website
and saves the results to a CSV file.
"""
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "job_listings.csv"

def fetch_page(url): 
    """Fetches the HTML content of a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"something went wrong; {error}")
        exit(1)

    return response.text

def parse_job_cards(html):
    """Parses job cards from HTML and returns a list of job dictionaries."""
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_="card-content") 
    
    jobs = []
    for card in cards:
        title_tag = card.find("h2", class_="title")
        company_tag = card.find("h3", class_="company")
        location_tag = card.find("p", class_="location")
        apply_tag = card.find("a", string="Apply")
        
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        company = company_tag.get_text(strip=True) if company_tag else "N/A"
        location = location_tag.get_text(strip=True) if location_tag else "N/A"
        apply_link = apply_tag["href"] if apply_tag else "N/A"
        job = {
            "title": title,
            "company": company,
            "location": location,
            "apply_link": apply_link,
        }
        
        jobs.append(job)

    return jobs


def save_to_csv(jobs, filename):
    """Writes a list of job dictionaries to a CSV file."""
    fieldnames = ["title", "company", "location", "apply_link"]
    with open(filename, mode="w" , newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)

if __name__ == "__main__":
    print(f"Fetching job from {URL} ...")
    html = fetch_page(URL)
    print("Parsing job listings ...")
    jobs = parse_job_cards(html)
    print(f"Found {len(jobs)} job listings.")

    if jobs:
        save_to_csv(jobs, OUTPUT_FILE)
        print(f"Saved results to {OUTPUT_FILE}")
    else:
        print("No jobs found - nothing to save")


