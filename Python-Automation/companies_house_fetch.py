import requests
import csv

API_KEY = "44630fb9-8b2d-4087-a2d7-4e0e63e971a5"
INPUT_FILE = "companies.txt"
OUTPUT_FILE = "companies_output.csv"

def search_company(name):
    url = f"https://api.company-information.service.gov.uk/search/companies?q={name}"
    response = requests.get(url, auth=(API_KEY, ""))
    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        item = data["items"][0]
        return item.get("company_number"), item.get("title")
    return None, None


def get_company_details(company_number):
    url = f"https://api.company-information.service.gov.uk/company/{company_number}"
    response = requests.get(url, auth=(API_KEY, ""))
    data = response.json()

    return {
        "number": data.get("company_number"),
        "name": data.get("company_name"),
        "status": data.get("company_status"),
        "date_of_creation": data.get("date_of_creation"),
        "sic_codes": ", ".join(data.get("sic_codes", [])) if data.get("sic_codes") else None,
        "address": ", ".join(
            str(data.get("registered_office_address", {}).get(k, ""))
            for k in ["address_line_1", "address_line_2", "locality", "postal_code"]
            if data.get("registered_office_address", {}).get(k)
        )
    }


# Read input companies
with open(INPUT_FILE, "r") as f:
    companies = [line.strip() for line in f if line.strip()]

results = []

for c in companies:
    print("Searching:", c)
    number, official_name = search_company(c)

    if number:
        details = get_company_details(number)
        details["input_name"] = c
        results.append(details)
    else:
        results.append({
            "input_name": c,
            "number": None,
            "name": None,
            "status": None,
            "date_of_creation": None,
            "sic_codes": None,
            "address": None
        })

# Write CSV
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "input_name", "number", "name", "status",
        "date_of_creation", "sic_codes", "address"
    ])
    writer.writeheader()
    writer.writerows(results)

print("Done. Saved to companies_output.csv")