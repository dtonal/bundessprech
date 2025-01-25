# bundessprech_reader/parliament.py

from enum import Enum
from typing import Optional
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Base-Klasse für SQLAlchemy-Modelle
Base = declarative_base()

class Sitzung(Base):
    __tablename__ = "sitzung"

    id = Column(Integer, primary_key=True)
    wahlperiode = Column(Integer, nullable=False)
    sitzungsnummer = Column(Integer, nullable=False)
    datum = Column(Date, nullable=False)
    reden = relationship("Rede", back_populates="sitzung")  # Beziehung zu Rede

    def __init__(self, wahlperiode, sitzungsnummer, datum, reden=None):
        self.wahlperiode = wahlperiode
        self.sitzungsnummer = sitzungsnummer
        self.datum = datum
        self.reden = reden or []

    def add_rede(self, rede):
        self.reden.append(rede)

    def __repr__(self):
        return (
            f"Sitzung(wahlperiode={self.wahlperiode}, "
            f"sitzungsnummer={self.sitzungsnummer}, "
            f"datum={self.datum}, reden={len(self.reden)} speeches)"
        )


class Rede(Base):
    __tablename__ = "rede"

    id = Column(Integer, primary_key=True)
    rede_id = Column(String, unique=True, nullable=False)
    sitzung_id = Column(Integer, ForeignKey("sitzung.id"))
    rede_text = Column(String)  # Redetext wird als langer String gespeichert
    redner_id = Column(Integer, ForeignKey("redner.id"))
    sitzung = relationship("Sitzung", back_populates="reden")
    redner = relationship("Redner", back_populates="reden")

    def __init__(self, rede_id, redner_id, rede_text=None):
        self.rede_id = rede_id
        self.rede_text = rede_text or []

    def add_paragraph(self, paragraph):
        self.rede_text.append(paragraph)

    def __repr__(self):
        return (
            f"Rede(id={self.rede_id}, text={self.rede_text[:30]}...)"
        )

class Redner(Base):
    __tablename__ = "redner"

    id = Column(Integer, primary_key=True)
    redner_id = Column(String, unique=True, nullable=False)
    name_id = Column(Integer, ForeignKey("name.id"))
    fraktion = Column(String, nullable=True)
    name = relationship("Name", back_populates="redner")
    reden = relationship("Rede", back_populates="redner")  # Beziehung zu Rede

    def __init__(self, redner_id=None, name=None, fraktion=None):
        self.redner_id = redner_id
        self.name = name
        self.fraktion = fraktion

    def __repr__(self):
        return (
            f"Redner(id={self.redner_id}, name={self.name}, "
            f"fraktion={self.fraktion})"
        )


class Name(Base):
    __tablename__ = "name"

    id = Column(Integer, primary_key=True)
    titel = Column(String, nullable=True)
    vorname = Column(String, nullable=True)
    nachname = Column(String, nullable=True)
    namenszusatz = Column(String, nullable=True)
    ortszusatz = Column(String, nullable=True)
    fraktion = Column(String, nullable=True)
    rolle_id = Column(Integer, ForeignKey("rolle.id"))
    rolle = relationship("Rolle", back_populates="namen")  # Beziehung zu Rolle
    redner = relationship("Redner", back_populates="name")  # Beziehung zu Redner

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
        self.rolle = rolle

    def __repr__(self):
        return (
            f"Name(titel={self.titel}, vorname={self.vorname}, "
            f"nachname={self.nachname}, "
            f"namenszusatz={self.namenszusatz}, ortszusatz={self.ortszusatz}, "
            f"fraktion={self.fraktion}, rolle={self.rolle})"
        )


class Rolle(Base):
    __tablename__ = "rolle"

    id = Column(Integer, primary_key=True)
    rolle_lang = Column(String, nullable=True)
    rolle_kurz = Column(String, nullable=True)
    namen = relationship("Name", back_populates="rolle")  # Beziehung zu Name

    def __init__(self, rolle_lang=None, rolle_kurz=None):
        self.rolle_lang = rolle_lang
        self.rolle_kurz = rolle_kurz

    def __repr__(self):
        return f"Rolle(lang={self.rolle_lang}, kurz={self.rolle_kurz})"
