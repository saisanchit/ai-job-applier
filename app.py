"""Main entry point for the AI Job Applier application."""

import logging
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Initialize and run the AI Job Applier application."""
    logger.info("Starting AI Job Applier application")
    config = Config()
    logger.info(f"Configuration loaded: {config}")
    # Application logic will be implemented here


if __name__ == "__main__":
    main()
