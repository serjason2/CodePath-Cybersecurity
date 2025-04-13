# CVE: Common Vulnerabilites and Exposures
    # Example Lookup URL: https://cve.circl.lu/api/cve/CVE-2015-3194
# Looking up a given CVE using CIRCL
# Week 8 Project 7: Threat Analysis

import requests
import json

def get_cve(cve):
    try:
        response = requests.get(f"https://cve.circl.lu/api/cve/{cve}")
        response.raise_for_status()
        result = response.json()
        print(json.dumps(result, indent=4))

        return result
    
    except:
        return 0
    
    return None

get_cve("CVE-2015-3194")