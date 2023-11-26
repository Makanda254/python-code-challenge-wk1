def convert_to_24_hour(hour, minute, period):
    # Check if hour is in the range of 1 to 12
    if not (1 <= hour <= 12):
        raise ValueError("Hour must be in the range of 1 to 12")

    # Check if minute is in the range of 0 to 59
    if not (0 <= minute <= 59):
        raise ValueError("Minute must be in the range of 0 to 59")

    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Format the hour and minute as two-digit strings
    formatted_hour = f"{hour:02d}"
    formatted_minute = f"{minute:02d}"

    # Combine the formatted hour and minute
    result = f"{formatted_hour}{formatted_minute}"

    return result

# Test cases
print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
print(convert_to_24_hour(1, 45, "pm"))  # Output: "1345"
print(convert_to_24_hour(12, 0, "am"))  # Output: "0000"
print(convert_to_24_hour(12, 30, "pm")) # Output: "1230"
