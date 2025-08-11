# Seeker

A simple tool to triangulate IP addresses and phone numbers using public APIs.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set your API tokens in the scripts.

## Usage

Run any script and follow the prompts.

# Example for IPinfo token
import os
token = os.getenv('IPINFO_TOKEN')
if not token:
    print("IPINFO_TOKEN environment variable not set.")
    return