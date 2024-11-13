# desktop-battery-status-alert-notification-system
desktop battery status alert notification system code written in python 

Battery Status Notifier
This Python script monitors the battery status of your device, providing notifications for low battery and fully charged battery states. It uses the psutil library to retrieve battery information and sends system notifications using plyer. Additionally, it uses pyttsx3 for text-to-speech alerts.

Features
Low Battery Notification: Notifies when battery is below 40% and not plugged in.
Full Charge Notification: Notifies when the battery is fully charged and plugged in.
Automatic Check: Runs every 60 seconds to update battery status.
Text-to-Speech Alert: Optionally announces notifications through speakers.
Requirements
To run this script, ensure the following Python libraries are installed:

psutil - For accessing battery information.
plyer - For cross-platform notifications.
pyttsx3 - For text-to-speech functionality.
You can install the required packages using:

bash
Copy code
pip install psutil plyer pyttsx3
Usage
Make sure your device has battery information available (e.g., laptops). This script may not function correctly on desktop computers without batteries.
Run the script:
bash
Copy code
python battery_notifier.py
The script will begin monitoring the battery status and will send notifications as necessary.
Code Explanation
Battery Status Check: The batteryStatus() function retrieves battery percentage and plugged-in status.
Notifications:
If the battery level falls below 40% and is not plugged in, a notification prompts you to charge the battery.
If the battery is fully charged (100%) and plugged in, a notification prompts you to unplug the charger.
Recurring Timer: The function re-calls itself every 60 seconds to continually check the battery status.
Notes
Notifications will appear on the system tray.
Text-to-speech might not be available or enabled on all systems, so please ensure your device supports it.
You can adjust the timer interval in the Timer(60.0, batteryStatus).start() line if you want to check more or less frequently.
This script provides a helpful way to manage battery usage, especially on laptops, ensuring you’re aware of both low and fully charged states.
