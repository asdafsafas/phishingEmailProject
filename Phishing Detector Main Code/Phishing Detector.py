from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Scrollbar, VERTICAL
from tkinter import Label
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import msal
import requests

ASSETS_PATH = Path(__file__).parent / "assets"


# Define the necessary OAuth 2.0 variables
CLIENT_ID = '7e357ed5-04b5-4066-813c-e00d85c8706a'
TENANT_ID = '9980fc88-5e45-4f9a-893d-ad3026c9bb91'
CLIENT_SECRET = 'gWh8Q~WfJL0VC~XJ0AaSC0f2d0MIpvIFKlp7Xc2G'
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_URI = 'http://localhost:8000'  # Your redirect URI

# Define separate scopes for Google and Microsoft
GOOGLE_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
MICROSOFT_SCOPES = ['https://graph.microsoft.com/Mail.Read']


def display_logo(canvas):
    # Load and display the logo at a fixed position
    logo_image = PhotoImage(file=relative_to_assets("Logo.png"))
    logo = canvas.create_image(111.0, 45.0, image=logo_image)
    canvas.image = logo_image  # Keep reference to avoid garbage collection

# Helper function to get image paths
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Microsoft Authentication function
def authenticate_microsoft():
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY
    )

    # Interactive login flow
    result = app.acquire_token_interactive(scopes=MICROSOFT_SCOPES)

    if "access_token" in result:
        return result["access_token"]
    else:
        print(f"Error: {result.get('error_description')}")
        return None



# Gmail Authentication function
def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', GOOGLE_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', GOOGLE_SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

# Function to remove email
def remove_email(email_id, service, email_widget):
    try:
        # Move email to trash
        service.users().messages().trash(userId='me', id=email_id).execute()
        print(f"Email {email_id} moved to trash.")
        # Remove email from the UI
        email_widget.destroy()
    except Exception as e:
        print(f"Error moving email to trash: {e}")

# Function to display emails dynamically in the UI
def show_notifications(root, email_details, service):
    root.title("Notifications")
    root.geometry("450x400")
    root.configure(bg="#FFFFFF")

    canvas = Canvas(
        root,
        bg="#FFFFFF",
        height=400,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Display the logo on the notifications page
    display_logo(canvas)

    # Load Settings button image and keep reference
    settings = PhotoImage(file=relative_to_assets("settings.png"))
    button_3 = Button(
    image=settings,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("settings clicked"),  # Placeholder for settings page transition
    relief="flat"
)
    button_3.image = settings  # Keep reference to avoid garbage collection
    button_3.place(x=396.0, y=33.0, width=24.0, height=25.0)

    # Load Notifications button image and keep reference
    notifications = PhotoImage(file=relative_to_assets("notification bell.png"))
    button_4 = Button(
    image=notifications,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_notifications(window, email_details, service),  # Transition to notifications page
    relief="flat"
)
    button_4.image = notifications  # Keep reference to avoid garbage collection
    button_4.place(x=360.0, y=33.0, width=24.0, height=25.0)

    # Add a scrollable frame for emails
    frame = Frame(canvas, bg="#FFFFFF")
    frame.place(x=30, y=120, width=390, height=250)

    # Add scrollbar
    scrollbar = Scrollbar(frame, orient=VERTICAL)
    scrollbar.pack(side="right", fill="y")

    email_canvas = Canvas(frame, yscrollcommand=scrollbar.set, bg="#F5F5F5")
    scrollbar.config(command=email_canvas.yview)
    email_canvas.pack(side="left", fill="both", expand=True)

    email_frame = Frame(email_canvas, bg="#F5F5F5")
    email_canvas.create_window((0, 0), window=email_frame, anchor="nw")

    # Display total emails detected
    canvas.create_text(
        30.0,
        81.0,
        anchor="nw",
        text=f"{len(email_details)} Emails Detected",
        fill="#C94949",
        font=("OpenSans Bold", 16 * -1)
    )

    # Add email subjects and snippets to the UI
    for index, (email_id, subject, snippet) in enumerate(email_details):
        # Display email subject
        Label(email_frame, text=f"Subject: {subject}", anchor="nw", bg="#F5F5F5", font=("OpenSans Semibold", 12)).grid(row=index*4, column=0, sticky="w", pady=(10, 0), padx=10)

        # Display email snippet (body)
        Label(email_frame, text=f"Snippet: {snippet}", anchor="nw", bg="#F5F5F5", font=("OpenSans", 12)).grid(row=index*4+1, column=0, sticky="w", padx=10)

        # Separator line
        Canvas(email_frame, bg="#BDBDBD", height=1, width=350).grid(row=index*4+2, column=0, pady=(5, 5))

        # Add keep and remove buttons for each email
        button_keep_image = PhotoImage(file=relative_to_assets("keep email.png"))
        button_keep = Button(
            email_frame,
            image=button_keep_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(f"Keep email {email_id}"),
            relief="flat"
        )
        button_keep.image = button_keep_image  # Keep reference to avoid garbage collection
        button_keep.grid(row=index*4+3, column=0, sticky="w", padx=10, pady=5)

        button_remove_image = PhotoImage(file=relative_to_assets("remove email.png"))
        button_remove = Button(
            email_frame,
            image=button_remove_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(f"Remove email {email_id}"),
            relief="flat"
        )
        button_remove.image = button_remove_image  # Keep reference to avoid garbage collection
        button_remove.grid(row=index*4+3, column=1, sticky="e", padx=10, pady=5)

    email_frame.update_idletasks()
    email_canvas.config(scrollregion=email_canvas.bbox("all"))



# Function to handle Google login and fetch emails
def google_login():
    creds = authenticate_gmail()
    if creds:
        print("Google login successful!")
        service = build('gmail', 'v1', credentials=creds)
        
        # Fetch emails
        results = service.users().messages().list(userId='me', maxResults=5).execute()
        messages = results.get('messages', [])
        
        email_details = []  # Initialize an empty list to store email details
        
        if messages:
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                headers = msg.get('payload', {}).get('headers', [])
                
                # Safely get the subject and snippet
                subject = next((header['value'] for header in headers if header['name'] == 'Subject'), 'No Subject')
                snippet = msg.get('snippet', 'No Snippet')
                email_details.append((message['id'], subject, snippet))
        
         # Transition to notifications page BEFORE returning
        show_notifications(window, email_details, service)

# Function to handle Microsoft login and fetch emails
def microsoft_login():
    try:
        access_token = authenticate_microsoft()
        if access_token:
            print("Microsoft login successful!")
            # Fetch emails from Microsoft Graph API
            email_details = fetch_microsoft_emails(access_token)
            # Transition to the notifications page
            show_notifications(window, email_details, service=None)
    except Exception as e:
        print(f"Error logging in with Microsoft: {e}")

def fetch_microsoft_emails(access_token):
    url = "https://graph.microsoft.com/v1.0/me/messages"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    email_details = []
    if response.status_code == 200:
        messages = response.json().get('value', [])
        for message in messages:
            message_id = message.get('id')
            subject = message.get('subject', 'No Subject')
            snippet = message.get('bodyPreview', 'No Snippet')
            email_details.append((message_id, subject, snippet))
    else:
        print(f"Error fetching Microsoft emails: {response.status_code}, {response.text}")
    return email_details



# Initialize Tkinter window for login
window = Tk()
window.geometry("450x400")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    205.0,
    114.0,
    anchor="nw",
    text="Login",
    fill="#333333",
    font=("OpenSans Bold", 16 * -1)
)

canvas.create_text(
    108.0,
    142.0,
    anchor="nw",
    text="Select an option below to get started",
    fill="#333333",
    font=("OpenSans Semibold", 14 * -1)
)

# Display the logo on the settings page
display_logo(canvas)


# Google login button 
button_image_1 = PhotoImage(file=relative_to_assets("google login.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=google_login,  # Call the Google login function when clicked
    relief="flat"
)
button_1.place(x=115.0, y=181.0, width=222.0, height=45.0)

# Microsoft login button
button_image_2 = PhotoImage(
    file=relative_to_assets("microsoft login.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=microsoft_login,  # Call Microsoft login function
    relief="flat"
)
button_2.place(
    x=115.0,
    y=241.0,
    width=222.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()

