# AI Job Applier

An intelligent automation tool for applying to job listings using AI.

## Project Structure

```
ai-job-applier/
├── app.py                 # Main application entry point
├── config.py              # Configuration management
├── .env.example           # Example environment variables
├── README.md              # Project documentation
├── modules/               # Application modules
│   ├── job_scraper/       # Job listing scraper
│   │   ├── __init__.py
│   │   └── scraper.py
│   ├── ai_applier/        # AI-powered application handler
│   │   ├── __init__.py
│   │   └── applier.py
│   └── utilities/         # Helper functions and utilities
│       ├── __init__.py
│       └── helpers.py
└── requirements.txt       # Python dependencies
```

## Getting Started

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure your settings
6. Run the application: `python app.py`

## Modules

- **job_scraper**: Handles finding and scraping job listings from various job boards
- **ai_applier**: Uses AI to automatically fill out and submit job applications
- **utilities**: Provides helper functions for configuration validation and data formatting

## License

MIT
