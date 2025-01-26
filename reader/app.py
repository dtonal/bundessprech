from parser import parse_sitzung
from db_access import store_sitzung
XML_FILE = "reader/testdata/20208.xml"


def clean_text(text):
    # Replace non-breaking spaces and other unwanted characters
    if text:
        return text.replace("\xa0", " ")  # Replacing non-breaking space with regular space
    return text


def main():
    # Parse the XML
    with open(XML_FILE, "r", encoding="utf-8") as file:
        xml_data = file.read()
        xml_data = clean_text(xml_data)

    try:
        # Parse the XML into a Sitzung object
        sitzung = parse_sitzung(xml_data)
        # Store the parsed Sitzung in DB
        store_sitzung(sitzung)
        # Print the result
        print(sitzung)

    except Exception as e:
        print(f"Error reading or validating XML: {e}")


if __name__ == "__main__":
    main()
