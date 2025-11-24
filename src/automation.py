from pywinauto.application import Application
from pywinauto import Desktop
import time
from pywinauto.mouse import click


ZOOM_PATH = r"C:\Users\Ujjwal Sharma\AppData\Roaming\Zoom\bin\Zoom.exe"
EMAIL = "ujjwal.sharma@cctech.co.in"
PASSWORD = "Bhole@3201"

def wait_for_window(title_keyword, timeout=20):
    """Wait for any window containing keyword in title"""
    for _ in range(timeout):
        for w in Desktop(backend="uia").windows():
            if title_keyword.lower() in w.window_text().lower():
                return w
        time.sleep(1)
    return None


print("Launching Zoom")
app = Application(backend="uia").start(ZOOM_PATH)
time.sleep(5)


print("Detecting Zoom main window")
zoom_window = wait_for_window("zoom")

if not zoom_window:
    print("Zoom window not found.")
    exit()

print(f"Selected Zoom window: {zoom_window.window_text()}")
zoom_window.set_focus()
time.sleep(1)

# CLICK "SIGN IN"

print("Searching for Sign In button")

sign_in_button = None
for ctrl in zoom_window.descendants():
    name = ctrl.window_text().lower()
    if "sign in" in name.strip():
        sign_in_button = ctrl
        break

if not sign_in_button:
    print("Sign In button NOT found.")
    exit()

print("Clicking Sign In")
sign_in_button.click_input()
time.sleep(4)

# ENTER EMAIL

print("Looking for Email input")

email_field = None
for _ in range(20):
    for ctrl in zoom_window.descendants():
        if ctrl.element_info.control_type == "Edit":
            email_field = ctrl
            break
    if email_field:
        break
    time.sleep(1)

if not email_field:
    print("Email field not found!")
    exit()

print("Typing email")
email_field.click_input()
email_field.type_keys(EMAIL, with_spaces=True)

time.sleep(1)

# CLICK "NEXT"

print("Looking for NEXT button")

next_button = None
for ctrl in zoom_window.descendants():
    if "next" in ctrl.window_text().lower():
        next_button = ctrl
        break

if not next_button:
    print("NEXT button not found.")
    exit()

print("Clicking NEXT")
next_button.click_input()
time.sleep(4)


# FIND PASSWORD FIELD (ADVANCED)

print("Searching for Password field")

password_field = None

for _ in range(25):
    for ctrl in zoom_window.descendants():
        cname = ctrl.element_info.name.lower()
        ctype = ctrl.element_info.control_type

        # Method 1: Actual name contains password
        if ctype == "Edit" and ("password" in cname or "pwd" in cname):
            password_field = ctrl
            break

        # Method 2: Masked characters (•••• or *****)
        if ctype == "Edit":
            try:
                legacy = ctrl.legacy_properties()
                val = str(legacy.get("Value", ""))
                if "•" in val or "*" in val:
                    password_field = ctrl
                    break
            except:
                pass

        # Method 3: UIA IsPassword property
        try:
            if "IsPassword" in ctrl.get_available_properties():
                password_field = ctrl
                break
        except:
            pass

        # Method 4: Unnamed Edit field after NEXT
        if ctype == "Edit" and cname.strip() == "":
            password_field = ctrl
            break

    if password_field:
        break

    time.sleep(1)

if not password_field:
    print("Password field not found. UI changed.")
    exit()

print("Typing password")
password_field.click_input()
password_field.type_keys(PASSWORD, with_spaces=True)
time.sleep(1)

password_field.type_keys("{ENTER}")
print("Login automation completed successfully!")



