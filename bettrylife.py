import psutil
from threading import Timer
from plyer import notification
import pyttsx3

engine=pyttsx3.init()

def batteryStatus():
    # Get battery details
    battery = psutil.sensors_battery()
    if battery is None:  # Check if battery information is available (in case of desktops or no battery)
        print("No battery information available.")
        return

    plugged = battery.power_plugged
    percent = battery.percent
    
    # Check battery status
    plugged_status = "Plugged In" if plugged else "Not Plugged In"
    
    # Handle low battery notification
    if not plugged and percent < 40:
        output = f"{percent}% | {plugged_status}"
        print(output)
        print(f"Please plug in your charger. Battery life is only {percent}%")
        engine.say()
        engine.runAndWait()
        notification.notify(
            title="Battery Percentage",
            message=f"Battery life is {percent}% | {plugged_status}",
            timeout=10,
        )
    
    # Handle fully charged notification
    elif plugged and percent == 100:
        output = f"{percent}% | {plugged_status}"
        print(output)
        print("Please unplug the charger. Your battery is fully charged.")
        notification.notify(
            title="Battery Percentage",
            message=f"Battery is fully charged ({percent}%) | {plugged_status}",
            timeout=10,
        )
    
    # Schedule the next check in 60 seconds
    Timer(60.0, batteryStatus).start()

if __name__ == "__main__":
    batteryStatus()
