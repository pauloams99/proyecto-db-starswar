from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

association_person_film = Table(
    "association_person_film",
    db.metadata,
    Column("person_id", ForeignKey("person.id"), primary_key=True),
    Column("film_id", ForeignKey("films.id"), primary_key=True),
)

association_planet_film = Table(
    "association_planet_film",
    db.metadata,
    Column("planet_id", ForeignKey("planet.id"), primary_key=True),
    Column("film_id", ForeignKey("films.id"), primary_key=True),
)

class Person(db.Model):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    species_id: Mapped[int] = mapped_column(ForeignKey("species.id"))

    planet: Mapped["Planet"] = relationship(back_populates="people")
    species: Mapped["Species"] = relationship(back_populates="people")
    films: Mapped[List["Films"]] = relationship(
        secondary=association_person_film, back_populates="characters"
    )

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    people: Mapped[List["Person"]] = relationship(back_populates="planet")
    species: Mapped[List["Species"]] = relationship(back_populates="homeworld")

    films: Mapped[List["Films"]] = relationship(
        secondary=association_planet_film, back_populates="planets"
    )

class Species(db.Model):
    __tablename__ = 'species'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    homeworld_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    homeworld: Mapped["Planet"] = relationship(back_populates="species")
    people: Mapped[List["Person"]] = relationship(back_populates="species")


class Films(db.Model):
    __tablename__ = 'films'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    year: Mapped[int] = mapped_column(nullable=True)
    director: Mapped[str] = mapped_column(String(100), nullable=False)

    characters: Mapped[List["Person"]] = relationship(
        secondary=association_person_film, back_populates="films"
    )
    planets: Mapped[List["Planet"]] = relationship(
        secondary=association_planet_film, back_populates="films"
    )