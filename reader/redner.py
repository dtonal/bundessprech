# bundessprech_reader/redner.py

class Rolle:
    def __init__(self, rolle_lang=None, rolle_kurz=None):
        self.rolle_lang = rolle_lang or []
        self.rolle_kurz = rolle_kurz or []

    def __repr__(self):
        return f"Rolle(lang={self.rolle_lang}, kurz={self.rolle_kurz})"


class Name:
    def __init__(self, titel=None, vorname=None, nachname=None, namenszusatz=None,
                 ortszusatz=None, fraktion=None, rolle=None):
        self.titel = titel
        self.vorname = vorname
        self.nachname = nachname
        self.namenszusatz = namenszusatz
        self.ortszusatz = ortszusatz
        self.fraktion = fraktion
        self.rolle = rolle or Rolle()

    def __repr__(self):
        return f"Name(titel={self.titel}, vorname={self.vorname}, nachname={self.nachname}, " \
               f"namenszusatz={self.namenszusatz}, ortszusatz={self.ortszusatz}, " \
               f"fraktion={self.fraktion}, rolle={self.rolle})"


class Redner:
    def __init__(self, redner_id=None, name=None):
        self.redner_id = redner_id
        self.name = name or Name()

    def __repr__(self):
        return f"Redner(id={self.redner_id}, name={self.name})"
