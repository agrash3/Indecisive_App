<<<<<<< HEAD
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
=======
<<<<<<< HEAD

=======
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
>>>>>>> c915ff6c59d82525151f3696c383766d57fd83e2
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pollster.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()