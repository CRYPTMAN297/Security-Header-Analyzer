import requests
from prettytable import PrettyTable

# List of important security headers
SECURITY_HEADERS = [
    "Strict-Transport-Security",  # HSTS - Enforces HTTPS
    "Content-Security-Policy",    # CSP - Prevents XSS attacks
    "X-Frame-Options",            # Prevents Clickjacking
    "X-XSS-Protection",           # Cross-site scripting protection
    "Referrer-Policy",            # Controls referrer information
    "Permissions-Policy"          # Controls browser features access
]

def analyze_headers(url):
    # Ensure the URL starts with HTTP/HTTPS
    if not url.startswith(("http://", "https://")):
        url = "https://" + url  # Default to HTTPS for security
    
    try:
        # Send a request to get the headers
        response = requests.get(url, timeout=5)
        headers = response.headers

  # Create a table for a neat display
        table = PrettyTable(["Security Header", "Present", "Value"])
        
        for header in SECURITY_HEADERS:
            value = headers.get(header, "Not Found")
            table.add_row([header, "✔" if value != "Not Found" else "❌", value])

        print(f"\nSecurity Headers Analysis for {url}:\n")
        print(table)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers: {e}")

if __name__ == "__main__":
    site = input("Enter website URL (without https://): ")
    analyze_headers(site)