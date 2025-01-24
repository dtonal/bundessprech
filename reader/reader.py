from lxml import etree

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
        redner = rede.find(".//redner/name")
        if redner is not None:
            # Extract the speaker's full name
            vorname = redner.find("vorname").text if redner.find("vorname") is not None else ""
            nachname = redner.find("nachname").text if redner.find("nachname") is not None else ""
            full_name = f"{vorname} {nachname}"
        else:
            full_name = "Unknown Speaker"
        print(f"Rede ID: {rede_id}, Speaker: {full_name}")
except Exception as e:
    print(f"Error reading or validating XML: {e}")
