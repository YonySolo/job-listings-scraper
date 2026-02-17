# Job Listings Scraper

A Python script that scrapes job listings from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website and saves them to a CSV file.

Built as a learning project from [roadmap.sh](https://roadmap.sh/projects/job-listings-scraper).

## What It Extracts

For each of the 100 listings on the page, the scraper pulls:

- Job title
- Company name
- Location
- Link to the full job posting

Missing fields are handled gracefully and marked as `N/A`.

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/job-listings-scraper.git
cd job-listings-scraper
pip install -r requirements.txt
python scraper.py
```

This creates `job_listings.csv` in the project folder.

## Technologies

- **Requests** — fetches the webpage
- **Beautiful Soup 4** — parses the HTML and extracts data
- **CSV** (built-in) — writes results to file

## License

[MIT](LICENSE)
