import os

DEBUG = os.getenv('DEBUG', False)

if DEBUG:
    print("we are in DEBUG")
    from pathlib import Path
    from dotenv import load_dotenv
    env_path = Path('.') / '.env.debug'
    load_dotenv(env_path)
    from .settings_files.development import *
else:
    print("we are in Production")
    from .settings_files.product import *
