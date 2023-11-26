#Function to convert 12 hour time to 24 hour time
def convert_to_24_hour(hour, minute, period):
    # Checks if hour is in the range of 1 to 12
    if not (1 <= hour <= 12):
        raise ValueError("Hour must be in the range of 1 to 12")

    # Checks if minute is in the range of 0 to 59
    if not (0 <= minute <= 59):
        raise ValueError("Minute must be in the range of 0 to 59")

    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Format the hour and minute as two-digit strings
    change_hour = f"{hour:02d}"
    change_minute = f"{minute:02d}"

    # Combines the changed hour and minute
    time = f"{change_hour}{change_minute}"

    return time

print(convert_to_24_hour(9, 41, "am"))  

