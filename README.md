# Ninja Crawl

**Ninja Crawl** is the scraping engine for the [Street Ninja](https://streetninja.ca) ecosystem. It receives raw HTML or PDF data and returns clean, normalized JSON — powering the backend database behind the [Streetlight API](https://github.com/FirstFlush/streetlight-api).

This project is fully open source to document the scraping work behind Street Ninja, and to inspire similar civic tech efforts in other cities.


## 🧠 What It Does

Ninja Crawl is a standalone FastAPI service that transforms raw HTML and PDF content into structured resource data (e.g. shelters, food programs, hygiene facilities). It is **not** a general-purpose web scraper — it's purpose-built to feed accurate data into the Streetlight API.

Ninja Crawl does **not**:

- Fetch or crawl URLs itself
- Connect to a database
- Schedule or retry jobs
- Validate data
- Serve a public API

Those responsibilities are handled by the [Streetlight API](https://github.com/FirstFlush/streetlight-api). Ninja Crawl focuses on **pure parsing**.


## 🧱 Tech Stack

- **Python 3.11**
- **FastAPI** — for exposing a simple `/scrape` endpoint
- **Pydantic** — for modeling and schema validation
- **pdfplumber** — for parsing tabular and structured PDF layouts
- **BeautifulSoup (lxml)** — for HTML extraction
