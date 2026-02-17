# Python Link Scraper

A Python web scraping tool that extracts all links from a webpage and saves them into a text file.

---

## Features
- Accepts any website URL
- Automatically fixes missing https/http
- Fetches webpage content
- Extracts all links
- Removes duplicate links
- Saves links to file
- Displays total link count
- Error handling for invalid URLs

---

## How It Works
The script sends a request to a website, parses its HTML, extracts all anchor tags, and saves unique links into a text file.

---

## Example Output

Website Title: Example Domain

Total unique links found: 14

Saved to:
links.txt

---

## Installation

Install dependencies:

pip install requests beautifulsoup4

---

## Usage

Run:

python scraper.py

Enter website URL when prompted.

---

## Technologies Used
- Python
- Requests
- BeautifulSoup

---

## Use Cases
- Lead collection
- Data mining
- SEO analysis
- Link auditing
- Research automation

---

## Author
Vinayak R B
