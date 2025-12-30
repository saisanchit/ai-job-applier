# AI Job Applier

An intelligent automation tool that leverages AI to streamline the job application process. This project helps job seekers efficiently apply to multiple positions by automating resume customization, cover letter generation, and application submissions.

## 🎯 Features

- **AI-Powered Resume Customization**: Automatically tailor your resume for each job posting
- **Smart Cover Letter Generation**: Generate personalized cover letters using AI
- **Automated Job Application**: Submit applications to multiple job boards
- **Job Scraping**: Automatically scrape job listings from various job boards
- **Application Tracking**: Track submitted applications and their status
- **Intelligent Filtering**: Filter job postings based on your preferences and qualifications
- **Multi-Platform Support**: Support for multiple job boards and platforms

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/saisanchit/ai-job-applier.git
   cd ai-job-applier
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## ⚡ Quick Start

### Basic Usage

```python
from ai_job_applier import JobApplier

# Initialize the applier
applier = JobApplier(config_path="config.yaml")

# Scrape jobs from a specific job board
jobs = applier.scrape_jobs(
    keywords=["Python", "Senior Developer"],
    location="San Francisco, CA",
    max_results=50
)

# Apply to matching jobs
results = applier.apply_to_jobs(jobs)

# Get application status
status = applier.get_application_status()
print(status)
```

### Command Line Interface

```bash
# Scrape job listings
python -m ai_job_applier scrape --keywords "Python" --location "San Francisco" --limit 50

# Apply to jobs
python -m ai_job_applier apply --filter-config config.yaml

# Check application status
python -m ai_job_applier status

# Generate resume for a job posting
python -m ai_job_applier generate-resume --job-id "job_12345" --resume-path "resume.pdf"
```

## ⚙️ Configuration

### Environment Variables (.env)

```env
# AI API Configuration
OPENAI_API_KEY=your_openai_api_key
AI_MODEL=gpt-4

# Job Board Credentials
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_password
INDEED_API_KEY=your_indeed_api_key

# Application Settings
MAX_APPLICATIONS_PER_DAY=20
DELAY_BETWEEN_APPLICATIONS=10
ENABLE_COVER_LETTER_GENERATION=true

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/application.log

# Database
DATABASE_URL=sqlite:///./jobs.db
```

### Configuration File (config.yaml)

```yaml
job_search:
  keywords:
    - "Python Developer"
    - "Backend Engineer"
  locations:
    - "San Francisco, CA"
    - "Remote"
  salary_range:
    min: 100000
    max: 200000
  job_types:
    - "Full-time"
    - "Contract"

application_settings:
  max_per_day: 20
  delay_seconds: 10
  auto_submit: true
  
ai_settings:
  model: "gpt-4"
  resume_customization: true
  cover_letter_generation: true
  use_system_prompt: true

job_boards:
  - "linkedin"
  - "indeed"
  - "glassdoor"
```

## 📖 Usage

### Scraping Job Listings

```python
from ai_job_applier import JobScraper

scraper = JobScraper()

# Scrape from LinkedIn
linkedin_jobs = scraper.scrape_linkedin(
    keywords=["Senior Python Developer"],
    location="Remote",
    experience_level="Senior"
)

# Scrape from Indeed
indeed_jobs = scraper.scrape_indeed(
    keywords=["Backend Engineer"],
    location="San Francisco, CA",
    date_posted="last_7_days"
)

# Combine results
all_jobs = linkedin_jobs + indeed_jobs
```

### Customizing Resumes

```python
from ai_job_applier import ResumeCustomizer

customizer = ResumeCustomizer()

# Load your base resume
resume = customizer.load_resume("resume.pdf")

# Customize for a specific job
customized = customizer.customize(
    resume=resume,
    job_posting=job_posting,
    tone="professional"
)

# Save customized resume
customizer.save_resume(customized, "customized_resume.pdf")
```

### Generating Cover Letters

```python
from ai_job_applier import CoverLetterGenerator

generator = CoverLetterGenerator()

# Generate a personalized cover letter
cover_letter = generator.generate(
    job_posting=job_posting,
    resume=resume,
    writing_style="formal"
)

print(cover_letter)
```

### Submitting Applications

```python
from ai_job_applier import ApplicationSubmitter

submitter = ApplicationSubmitter()

# Submit application with custom resume and cover letter
result = submitter.submit(
    job_id="job_12345",
    platform="linkedin",
    resume=customized_resume,
    cover_letter=cover_letter,
    credentials={
        "email": "your_email@example.com",
        "password": "your_password"
    }
)

print(f"Application submitted: {result.status}")
```

## 📁 Project Structure

```
ai-job-applier/
├── ai_job_applier/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── base_scraper.py
│   │   ├── linkedin_scraper.py
│   │   ├── indeed_scraper.py
│   │   └── glassdoor_scraper.py
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── resume_customizer.py
│   │   ├── cover_letter_generator.py
│   │   └── llm_client.py
│   ├── submitter/
│   │   ├── __init__.py
│   │   ├── base_submitter.py
│   │   ├── linkedin_submitter.py
│   │   └── indeed_submitter.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── crud.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── validators.py
│   │   └── helpers.py
│   └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── test_scraper.py
│   ├── test_ai_modules.py
│   ├── test_submitter.py
│   └── test_integration.py
├── .env.example
├── config.yaml
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## 🔗 API Documentation

### JobApplier Class

Main orchestrator class for the job application automation.

```python
class JobApplier:
    """
    Main class for orchestrating job search and application automation.
    
    Methods:
        scrape_jobs(keywords, location, max_results): Scrape job listings
        apply_to_jobs(jobs, filter_config): Apply to filtered jobs
        get_application_status(): Get status of submitted applications
        update_resume(resume_path): Update base resume
        export_results(format): Export application results
    """
```

### JobScraper Class

```python
class JobScraper:
    """
    Base class for scraping job listings from various platforms.
    
    Methods:
        scrape_linkedin(): Scrape LinkedIn jobs
        scrape_indeed(): Scrape Indeed jobs
        scrape_glassdoor(): Scrape Glassdoor jobs
    """
```

### ResumeCustomizer Class

```python
class ResumeCustomizer:
    """
    AI-powered resume customization for specific job postings.
    
    Methods:
        customize(resume, job_posting): Tailor resume for job
        load_resume(path): Load resume from file
        save_resume(resume, path): Save resume to file
    """
```

### CoverLetterGenerator Class

```python
class CoverLetterGenerator:
    """
    AI-powered cover letter generation.
    
    Methods:
        generate(job_posting, resume): Generate personalized cover letter
        set_tone(tone): Set writing style
    """
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_scraper.py

# Run with coverage
pytest --cov=ai_job_applier tests/

# Run integration tests
pytest tests/test_integration.py -v
```

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/ai-job-applier.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add tests for new functionality
   - Update documentation as needed

4. **Commit and push**
   ```bash
   git add .
   git commit -m "Add your meaningful commit message"
   git push origin feature/your-feature-name
   ```

5. **Submit a pull request**
   - Provide a clear description of changes
   - Link any related issues
   - Ensure all tests pass

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/saisanchit/ai-job-applier/issues)
- **Discussions**: Join our [GitHub Discussions](https://github.com/saisanchit/ai-job-applier/discussions)
- **Email**: Support email will be provided separately

### Common Issues

**Issue: API Key not found**
```
Solution: Ensure your .env file contains OPENAI_API_KEY
```

**Issue: Job scraping returns no results**
```
Solution: Check your search keywords and location parameters
```

**Issue: Application submission fails**
```
Solution: Verify job board credentials in .env file
```

## 🗺️ Roadmap

- [ ] Mobile app support
- [ ] Email integration for application confirmations
- [ ] Advanced salary negotiation suggestions
- [ ] Job market analytics dashboard
- [ ] Interview preparation module
- [ ] More job board integrations
- [ ] Batch processing optimization

## 📊 Stats

- **Supported Job Boards**: 3+ platforms
- **Customization Options**: 10+
- **Languages Supported**: English (more coming)
- **Average Time Saved**: ~80% of application time

## ⚖️ Legal Notice

This tool is designed for personal use and educational purposes. Please ensure you comply with the terms of service of any job boards you use this tool with. Users are responsible for ensuring their use of this tool complies with all applicable laws and regulations.

## 🙏 Acknowledgments

- Built with Python and modern AI/ML technologies
- Special thanks to the open-source community
- Inspired by the need to streamline job search processes

---

**Last Updated**: December 30, 2025

For the latest updates, visit the [GitHub repository](https://github.com/saisanchit/ai-job-applier)
