#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from main import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boilerplate_backend.settings.dev")
    execute_from_command_line(sys.argv)
