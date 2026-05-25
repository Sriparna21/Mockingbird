import logging
import os
from datetime import datetime

os.makedirs('logs', exist_ok = True)



# This code only helps keep latest 10 log files in the system
log_files = sorted(
    [f for f in os.listdir('logs') if f.endswith('.log')],
    reverse = True
)

if len(log_files) >= 10:

    older = log_files[10:]

    for log in older:
        os.remove(os.path.join('logs',log))

t = datetime.now().strftime('%Y-%m-%d')        


logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(f'logs/app-{t}.log'),
        logging.StreamHandler()
    ]

)

logger = logging.getLogger(__name__)