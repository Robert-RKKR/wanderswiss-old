# Python - colorama import:
from colorama import init
from colorama import Fore
from colorama import Style
from colorama import Back

# WanderSwiss - constance import:
from wanderswiss.base.constants.notification import SeverityChoices

# Initialize colorama:
init()

# Error message:
def cli_message(severity, value_to_print):
    # Validate provided data:
    if not isinstance(severity, SeverityChoices):
        raise TypeError('Provided severity value is not a valid '\
            f'severity object.\nProvided: {type(severity)}')
    elif not isinstance(value_to_print, str):
        raise TypeError('Provided value_to_print value is not a valid '\
            f'string value.\nProvided: {type(value_to_print)}')
    # Check type of CLI message:
    if severity == SeverityChoices.CRITICAL:
        # Print Critical CLI message:
        print(f'{Fore.YELLOW}{Back.MAGENTA}{Style.BRIGHT}'\
            f'! CRITICAL: {value_to_print}{Style.RESET_ALL}')
    elif severity == SeverityChoices.ERROR:
        # Print Error CLI message:
        print(f'{Fore.RED}{Style.BRIGHT}'\
            f'! ERROR:    {value_to_print}{Style.RESET_ALL}')
    elif severity == SeverityChoices.WARNING:
        # Print Warning CLI message:
        print(f'{Fore.MAGENTA}{Style.BRIGHT}'\
            f'! WARNING:  {value_to_print}{Style.RESET_ALL}')
    elif severity == SeverityChoices.INFO:
        # Print Info CLI message:
        print(f'{Fore.YELLOW}{Style.BRIGHT}'\
            f'! INFO:     {value_to_print}{Style.RESET_ALL}')
    elif severity == SeverityChoices.DEBUG:
        # Print Debug CLI message:
        print(f'{Fore.GREEN}{Style.BRIGHT}'\
            f'! DEBUG:    {value_to_print}{Style.RESET_ALL}')
