# bundessprech_reader/parliament.py

from enum import Enum
from typing import Optional

class Sitzung:
    def __init__(self, wahlperiode, sitzungsnummer, datum, reden=None):
        self.wahlperiode = wahlperiode
        self.sitzungsnummer = sitzungsnummer
        self.datum = datum
        self.reden = reden or []  # Initialize an empty list if none is provided

    def add_rede(self, rede):
        self.reden.append(rede)

    def __repr__(self):
        return (
            f"Sitzung(wahlperiode={self.wahlperiode}, "
            f"sitzungsnummer={self.sitzungsnummer}, "
            f"datum={self.datum}, reden={len(self.reden)} speeches)"
        )


class Rolle:
    def __init__(self, rolle_lang=None, rolle_kurz=None):
        self.rolle_lang = rolle_lang or []
        self.rolle_kurz = rolle_kurz or []

    def __repr__(self):
        return f"Rolle(lang={self.rolle_lang}, kurz={self.rolle_kurz})"


class Name:
    def __init__(
        self,
        titel=None,
        vorname=None,
        nachname=None,
        namenszusatz=None,
        ortszusatz=None,
        fraktion=None,
        rolle=None,
    ):
        self.titel = titel
        self.vorname = vorname
        self.nachname = nachname
        self.namenszusatz = namenszusatz
        self.ortszusatz = ortszusatz
        self.fraktion = fraktion
        self.rolle = rolle or Rolle()

    def __repr__(self):
        return (
            f"Name(titel={self.titel}, vorname={self.vorname}, "
            f"nachname={self.nachname}, "
            f"namenszusatz={self.namenszusatz}, ortszusatz={self.ortszusatz}, "
            f"fraktion={self.fraktion}, rolle={self.rolle})"
        )


class Redner:
    def __init__(self, redner_id=None, name=None, fraktion=None):
        self.redner_id = redner_id
        self.name = name or Name()
        self.fraktion = fraktion or None

    def __repr__(self):
        return (
                f"Redner(id={self.redner_id}, name={self.name}, "
                f"fraktion={self.fraktion})"
        )


class Rede:
    def __init__(self, rede_id=None, redner=None, rede_text=None):
        self.rede_id = rede_id
        self.redner = redner or Redner()  # Redner is associated with Rede
        self.rede_text = rede_text or []

    def add_paragraph(self, paragraph):
        self.rede_text.append(paragraph)

    def __repr__(self):
        return (
            f"Rede(id={self.rede_id}, redner={self.redner}), "
            f"rede_text={self.rede_text})"
        )
