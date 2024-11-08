"""
Module to create a Pythoin function
that generate  personalized invitation files
"""

import os


def generate_invitations(template, attendees):
    """ Generate  personalized invitation"""

    try:
        if not isinstance(template, str):

            raise TypeError("Template is not a string.")

        if not isinstance(attendees, list) or not\
                all(isinstance(attendee, dict) for attendee in attendees):

            raise TypeError("Attendees should be a list of dictionaries.")

    except TypeError as e:
        print(f"Error: {e}")
        return e

    try:
        if not template.strip():

            raise ValueError("Template is empty, no output files generated.")

        if not attendees:

            raise ValueError("No data provided, no output files generated.")

    except ValueError as e:
        print(f"Error: {e}")
        return e

    for index, attendee in enumerate(attendees, start=1):
        output_content = template
         
        for key in ["name", "event_title", "event_date", "event_location"]:

            placeholder = "{" + key + "}"
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            output_content = output_content.replace(placeholder, value)
        filename = f"output_{index}.txt"

        if os.path.exists(filename):
            print(f"Warning: {filename} already exists.")
            continue

        with open(filename, 'w') as new_file:
            new_file.write(output_content)
