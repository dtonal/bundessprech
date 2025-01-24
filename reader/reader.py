from lxml import etree
from .redner import Redner, Name, Rolle

# Paths to the XML and DTD files
xml_file = "reader/testdata/20208.xml"
dtd_file = "reader/testdata/dbtplenarprotokoll.dtd"

# Parse the XML
with open(xml_file, "rb") as f:
    xml_data = f.read()

try:
    # Parse and validate against the DTD
    dtd = etree.DTD(dtd_file)
    root = etree.XML(xml_data)

    if dtd.validate(root):
        print("XML is valid according to the DTD.")
    else:
        print("XML is invalid.")
        print(dtd.error_log.filter_from_errors())

    # Print parsed data for testing
    for rede in root.findall(".//rede"):
        rede_id = rede.get("id")  # Get the "id" attribute of the "rede" element
        # Find the "name" element inside the "redner" tag
        redner = rede.find(".//redner")
        if redner is not None:
            # Extract the speaker's full name
            redner_id = redner.get("id")
            redner_name = rede.find(".//redner/name")
            vorname = redner_name.find("vorname").text if redner_name.find("vorname") is not None else ""
            nachname = redner_name.find("nachname").text if redner_name.find("nachname") is not None else ""
            fraktion = redner_name.find("fraktion").text if redner_name.find("fraktion") is not None else ""
            full_name = f"{vorname} {nachname}"
        else:
            full_name = "Unknown Speaker"
        print(f"Rede ID: {rede_id}, Speaker: {full_name} [{redner_id}] ({fraktion})")
        print("\n")
        # Iterate through all the paragraphs within the "rede" element
        # for paragraph in rede.findall("p"):
        #     # Check if the "klasse" attribute is "J", "J_1", or "O"
        #     klasse = paragraph.get("klasse")
        #     if klasse in ["J", "J_1", "O"]:
        #         # Extract the text of each paragraph (ignoring extra whitespace)
        #         paragraph_text = paragraph.text.strip() if paragraph.text else ""
                
        #         # Print each paragraph's text
        #         if paragraph_text:
        #             print(paragraph_text)
        # print("\n")

except Exception as e:
    print(f"Error reading or validating XML: {e}")
