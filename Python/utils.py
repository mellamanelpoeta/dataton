import pandas as pd
import requests
import os

def load_or_download_csv(path, gdrive_link):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        print(f"File not found at {path}. Attempting to download from Google Drive...")
        
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            # Download the file
            response = requests.get(gdrive_link)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            with open(path, 'wb') as f:
                f.write(response.content)
            
            print(f"File downloaded successfully to {path}")
            return pd.read_csv(path)
        
        except requests.RequestException as e:
            raise Exception(f"Failed to download the file: {str(e)}")