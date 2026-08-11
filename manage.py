#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# khud add kri hu
from dotenv import load_dotenv

# Load .env from project root
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Optional: print to verify
print("OpenRouter Key:", os.getenv("OPENROUTER_KEY"))







def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crop_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
