#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))
        filename = f"output_{idx}.txt"
        with open(filename, 'w') as f:
            f.write(content)

