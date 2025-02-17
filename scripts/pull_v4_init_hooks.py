import spice
import pandas as pd
import time

max_retries = 5
retry_delay = 10

for attempt in range(max_retries):
    try:
        df = spice.query(4733012, refresh=True) 
        if not df.is_empty():
            break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
    time.sleep(retry_delay)
else:
    print("Failed to retrieve data after several attempts.")
    df = pd.DataFrame()  # Create an empty DataFrame if all attempts fail

if not df.is_empty():
    print(df.head(10))
    df.write_csv('data/v4_init_hooks.csv')
else:
    print("No data to export.")