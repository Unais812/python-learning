# While learning, you use print() to see what your code is doing. 
# That is fine for a quick check. But in real software, you use logging instead.
# Logging is a proper record of what happened, with control over how much detail you keep and where it goes

import logging 

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Memory is running low")
logging.error("Failed to connect to database")

# Logging inside a data-processing function

def process_rows(rows: list[dict]) -> int:
    logging.info(f"Starting to process {len(rows)} rows")
    processed = 0
    for row in rows:
        if not row.get("id"):
            logging.warning(f"Skipping row with no id: {row}")
            continue
        processed = processed + 1
    logging.info(f"Finished. Processed {processed} rows")
    return processed

data = [{"id": 1}, {"id": 2}, {"name": "no id here"}]
process_rows(data)

def logging_exercise(numbers: list[int]):
    logging.info("Started function 'logging_exercise'")
    if len(numbers) == 0:
        logging.error(f"List is empty, cannot continue")
        return
    for number in numbers:
        if number < 0:
            logging.warning(f"{number} is a negative number")
        
numbers = [13, 24, 54, 15, 78, 33, 10, -849, 9]
function = []
logging_exercise(function)

