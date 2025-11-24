# import time
# from pywinauto.application import Application

# def launch_zoom():
#     app = Application(backend="uia").start(r"C:\Users\Public\Zoom\bin\Zoom.exe")
#     time.sleep(5)
#     return app

# def login_zoom(email, password):
#     print("Login automation placeholder")

# def logout_zoom():
#     print("Logout automation placeholder")

# if __name__ == "__main__":
#     print("Running Zoom automation")

# import time
# import subprocess
# from pywinauto.application import Application
# from pywinauto import Desktop

# # CONFIG
# ZOOM_PATH = r"C:\Users\Ujjwal Sharma\AppData\Roaming\Zoom\bin\Zoom.exe"
# EMAIL = "ujjwal.sharma@cctech.co.in"
# PASSWORD = "Bhole@3201"


# def launch_zoom():
#     print("Launching Zoom...")
#     subprocess.Popen(ZOOM_PATH)
#     time.sleep(5)


# def find_zoom_window():
#     print("Waiting for Zoom window...")

#     window_titles = [
#         "Zoom", "Zoom Workplace", "Zoom Cloud Meetings",
#         "Sign In", "Zoom - Sign In", "Sign in to Zoom"
#     ]

#     for _ in range(30):
#         windows = Desktop(backend="uia").windows()
#         for w in windows:
#             title = w.window_text().strip()
#             for match in window_titles:
#                 if match.lower() in title.lower():
#                     print(f"Window detected: {title}")
#                     # convert UIAWrapper → WindowSpecification
#                     app = Application(backend="uia").connect(handle=w.handle)
#                     return app.window(handle=w.handle)
#         time.sleep(1)

#     print("Error: Zoom login window not found.")
#     return None


# def login_zoom(win):
#     try:
#         win.set_focus()
#         time.sleep(1)

#         print("Looking for Email field...")
#         email_box = win.child_window(title_re=".*email.*", control_type="Edit")
#         email_box.wait("ready", timeout=10)
#         email_box.type_keys(EMAIL, with_spaces=True)

#         print("Looking for Password field...")
#         pass_box = win.child_window(title_re=".*password.*", control_type="Edit")
#         pass_box.wait("ready", timeout=10)
#         pass_box.type_keys(PASSWORD, with_spaces=True)

#         print("Looking for Sign In button...")
#         sign_btn = win.child_window(title_re=".*Sign In.*", control_type="Button")
#         sign_btn.wait("ready", timeout=10)
#         sign_btn.click_input()

#         print("Login clicked.")

#     except Exception as e:
#         print(f"Login failed: {e}")


# def main():
#     launch_zoom()
#     win = find_zoom_window()
#     if win:
#         login_zoom(win)


# if __name__ == "__main__":
#     main()

# import time
# from pywinauto.application import Application
# from pywinauto import Desktop

# ZOOM_PATH = r"C:\Users\Ujjwal Sharma\AppData\Roaming\Zoom\bin\Zoom.exe"

# EMAIL = "ujjwal.sharma@cctech.co.in"
# PASSWORD = "Bhole@3201"

# print("Launching Zoom...")
# app = Application(backend="uia").start(ZOOM_PATH)
# time.sleep(5)

# print("Detecting correct Zoom window...")

# zoom_window = None

# # Get all possible zoom windows
# all_windows = Desktop(backend="uia").windows()

# for w in all_windows:
#     title = w.window_text().lower()

#     # pick the correct one based on title & size
#     if ("zoom" in title or "zoom workplace" in title) and w.element_info.control_type == "Window":
#         try:
#             rect = w.rectangle()
#             if rect.width() > 300 and rect.height() > 300:  
#                 # exclude splash screens (very small)
#                 zoom_window = w
#                 break
#         except:
#             continue

# if not zoom_window:
#     print("Error: Could not detect the proper Zoom window.")
#     exit()

# print(f"Selected Zoom window: {zoom_window.window_text()}")

# zoom_window.set_focus()
# time.sleep(1)

# # -------------------------
# # CLICK SIGN IN
# # -------------------------
# print("Searching for Sign In button...")

# sign_in_button = None

# try:
#     for c in zoom_window.descendants():
#         if "sign in" in c.window_text().lower():
#             sign_in_button = c
#             break
# except:
#     pass

# if sign_in_button:
#     print("Clicking Sign In...")
#     sign_in_button.click_input()
# else:
#     print("No Sign In button found. UI changed or already logged in.")
#     # try pressing ALT+S
#     zoom_window.type_keys("%s")

# time.sleep(4)

# # -------------------------
# # FIND EMAIL FIELD
# # -------------------------
# print("Searching for Email input field...")

# email_field = None
# for _ in range(20):
#     try:
#         for c in zoom_window.descendants():
#             if c.element_info.control_type == "Edit":
#                 email_field = c
#                 break
#     except:
#         pass
#     if email_field:
#         break
#     time.sleep(1)

# if not email_field:
#     print("Error: Email field not found.")
#     exit()

# print("Typing email...")
# email_field.click_input()
# email_field.type_keys(EMAIL, with_spaces=True)

# time.sleep(1)

# # PASSWORD FIELD
# password_field = None
# for c in zoom_window.descendants():
#     if c.element_info.control_type == "Edit" and c != email_field:
#         password_field = c
#         break

# if not password_field:
#     print("Password field not found.")
#     exit()

# print("Typing password...")
# password_field.click_input()
# password_field.type_keys(PASSWORD, with_spaces=True)

# time.sleep(1)
# password_field.type_keys("{ENTER}")

# print("Login automation completed.")



# import time
# from pywinauto.application import Application
# from pywinauto import Desktop

# ZOOM_PATH = r"C:\Users\Ujjwal Sharma\AppData\Roaming\Zoom\bin\Zoom.exe"
# EMAIL = "ujjwal.sharma@cctech.co.in"
# PASSWORD = "Bhole@3201"

# print("Launching Zoom...")
# app = Application(backend="uia").start(ZOOM_PATH)
# time.sleep(5)

# print("Detecting correct Zoom window...")

# zoom_window = None
# all_windows = Desktop(backend="uia").windows()

# for w in all_windows:
#     title = w.window_text().lower()
#     if "zoom" in title and w.element_info.control_type == "Window":
#         rect = w.rectangle()
#         if rect.width() > 300 and rect.height() > 300:
#             zoom_window = w
#             break

# if not zoom_window:
#     print("Error: Could not detect the Zoom window.")
#     exit()

# print(f"Selected Zoom window: {zoom_window.window_text()}")
# zoom_window.set_focus()
# time.sleep(1)

# # -------------------------
# # CLICK SIGN IN
# # -------------------------
# print("Searching for Sign In button...")

# sign_in_button = None
# for c in zoom_window.descendants():
#     if "sign in" in c.window_text().lower():
#         sign_in_button = c
#         break

# if sign_in_button:
#     print("Clicking Sign In...")
#     sign_in_button.click_input()
# else:
#     print("Sign In button not found.")
#     exit()

# time.sleep(4)

# # -------------------------
# # FIND EMAIL INPUT
# # -------------------------
# print("Searching for Email input field...")

# email_field = None
# for _ in range(20):
#     for c in zoom_window.descendants():
#         if c.element_info.control_type == "Edit":
#             email_field = c
#             break
#     if email_field:
#         break
#     time.sleep(1)

# if not email_field:
#     print("Error: Email field not found.")
#     exit()

# print("Typing email...")
# email_field.click_input()
# email_field.type_keys(EMAIL, with_spaces=True)
# time.sleep(1)

# # -------------------------
# # CLICK NEXT BUTTON
# # -------------------------
# print("Looking for NEXT button...")

# next_button = None
# for c in zoom_window.descendants():
#     if "next" in c.window_text().lower():
#         next_button = c
#         break

# if not next_button:
#     print("Next button not found!")
#     exit()

# print("Clicking Next...")
# next_button.click_input()
# time.sleep(4)

# # -------------------------
# # FIND PASSWORD FIELD
# # -------------------------
# print("Searching for Password field...")

# password_field = None
# for _ in range(15):
#     for c in zoom_window.descendants():
#         if c.element_info.control_type == "Edit" and "password" in c.legacy_properties().get("Value", "").lower():
#             password_field = c
#             break
#     if password_field:
#         break
#     time.sleep(1)

# if not password_field:
#     print("Password field not found.")
#     exit()

# print("Typing password...")
# password_field.click_input()
# password_field.type_keys(PASSWORD, with_spaces=True)

# time.sleep(1)
# password_field.type_keys("{ENTER}")

# print("Login automation completed successfully.")




from pywinauto.application import Application
from pywinauto import Desktop
import time
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
print("🎉 Login automation completed successfully!")


def logout_from_zoom(app):
    print("Trying to log out...")

    zoom = app.window(title_re=".*Zoom.*")
    zoom.set_focus()
    time.sleep(1)

    # Get window rectangle
    rect = zoom.rectangle()

    # Avatar button coordinates (top-right area)
    avatar_x = rect.right - 60   # adjust if needed
    avatar_y = rect.top + 40

    print(f"Clicking avatar at {avatar_x}, {avatar_y}")
    click(coords=(avatar_x, avatar_y))
    time.sleep(1)

    # Now click the "Sign out" option
    # Usually appears slightly below avatar menu
    signout_x = avatar_x - 50
    signout_y = avatar_y + 120

    print(f"Clicking Sign out at approx {signout_x}, {signout_y}")
    click(coords=(signout_x, signout_y))
    time.sleep(1)

    print("✔ Logout attempted. Checking confirmation...")

    # Optional: Confirm popup
    try:
        confirm_btn = zoom.child_window(title="Sign out", control_type="Button")
        confirm_btn.click_input()
        print("✔ Logout confirmed.")
    except:
        print("No confirmation popup.")

    print("🎉 Logout automation completed.")
