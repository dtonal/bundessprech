import xml.etree.ElementTree as ET
from typing import List
from parliament import Sitzung, Redner, Rede, Name, Rolle

XML_FILE = "reader/testdata/20208.xml"

def parse_name(element) -> Name:
    """ Parse the 'name' element to create a Name object """
    titel = element.find("titel")
    vorname = element.find("vorname")
    nachname = element.find("nachname")
    namenszusatz = element.find("namenszusatz")
    ortszusatz = element.find("ortszusatz")
    fraktion = element.find("fraktion")
    rolle_lang = [role.text for role in element.findall("rolle/rolle_lang")]
    rolle_kurz = [role.text for role in element.findall("rolle/rolle_kurz")]

    return Name(
        titel=titel.text if titel is not None else None,
        vorname=vorname.text if vorname is not None else None,
        nachname=nachname.text if nachname is not None else None,
        namenszusatz=namenszusatz.text if namenszusatz is not None else None,
        ortszusatz=ortszusatz.text if ortszusatz is not None else None,
        fraktion=fraktion.text if fraktion is not None else None,
        rolle=Rolle(rolle_lang=rolle_lang, rolle_kurz=rolle_kurz)
    )


def parse_rede(element) -> Rede:
    """ Parse the 'rede' element to create a Rede object """
    rede_id = element.get("id")
    redner_element = element.find(".//redner")
    redner_id=redner_element.get("id")
    redner = Redner(redner_id, name=parse_name(element.find(".//redner/name")))
    rede_text = [p.text for p in element.findall(".//p")]

    return Rede(rede_id=rede_id, redner_id=redner_id, rede_text=rede_text)

def parse_sitzung(xml_string: str) -> Sitzung:
    """ Parse the XML string and return a Sitzung object """
    root = ET.fromstring(xml_string)

    # Extract session attributes
    wahlperiode = root.get("wahlperiode")
    sitzungsnummer = root.get("sitzung-nr")
    datum = root.get("sitzung-datum")

    # Create the Sitzung object
    sitzung = Sitzung(wahlperiode=wahlperiode, sitzungsnummer=sitzungsnummer, datum=datum)

    # Extract all rede (speeches) in the sitzungsverlauf
    for rede_element in root.findall(".//sitzungsverlauf/tagesordnungspunkt/rede"):
        rede = parse_rede(rede_element)
        sitzung.add_rede(rede)

    return sitzung

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

        # Print the result
        print(sitzung)

    except Exception as e:
        print(f"Error reading or validating XML: {e}")


if __name__ == "__main__":
    main()
