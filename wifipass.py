import subprocess

profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
profile_names = [line.split(":")[1].strip() for line in profiles_data.split('\n') if "All User Profile" in line]

wifi_profiles = {}

for profile_name in profile_names:
    try:
        profile_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8')
        password_line = [line.split(":")[1].strip() for line in profile_data.split('\n') if "Key Content" in line][0]
        wifi_profiles[profile_name] = password_line
    except Exception as e:
        wifi_profiles[profile_name] = "No password available"

for profile_name, password in wifi_profiles.items():
    print(f"Profile: {profile_name}\nPassword: {password}\n")
