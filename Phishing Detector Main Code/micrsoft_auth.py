import msal
import webbrowser

# Define the necessary OAuth 2.0 variables
CLIENT_ID = '7e357ed5-04b5-4066-813c-e00d85c8706a'
TENANT_ID = '9980fc88-5e45-4f9a-893d-ad3026c9bb91'
CLIENT_SECRET = 'gWh8Q~WfJL0VC~XJ0AaSC0f2d0MIpvIFKlp7Xc2G'
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_URI = 'http://localhost:8000'  # Your redirect URI
SCOPES = ['https://graph.microsoft.com/.default']

# Create a PublicClientApplication instance (for user-interactive flows)
app = msal.PublicClientApplication(
    CLIENT_ID,
    authority=AUTHORITY
)

# Initiate the authentication process
def get_access_token():
    # First, attempt to acquire the token silently from the cache
    accounts = app.get_accounts()
    result = None
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])

    # If no token is found in the cache, initiate interactive authentication
    if not result:
        # Start the authorization code flow
        flow = app.initiate_device_flow(scopes=SCOPES)

        if "user_code" not in flow:
            raise Exception("Failed to create device flow")

        print(flow["message"])  # Message to direct user to enter the code at the given URL
        webbrowser.open(flow["verification_uri"])

        # Polling for the authentication
        result = app.acquire_token_by_device_flow(flow)

    if "access_token" in result:
        return result['access_token']
    else:
        print(f"Error: {result.get('error')}")
        print(f"Error Description: {result.get('error_description')}")
        print(f"Correlation ID: {result.get('correlation_id')}")
        return None

# Fetch the access token
token = get_access_token()

if token:
    print(f"Access Token: {token}")
else:
    print("Failed to acquire access token.")