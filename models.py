from gino import Gino
from pydantic import BaseModel


db = Gino()


class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer(), primary_key=True)
    birth_year = db.Column(db.String(), nullable=True)
    eye_color = db.Column(db.String(), nullable=True)
    films = db.Column(db.String(), nullable=True)
    gender = db.Column(db.String(), nullable=True)
    hair_color = db.Column(db.String(), nullable=True)
    height = db.Column(db.String(), nullable=True)
    homeworld = db.Column(db.String(), nullable=True)
    mass = db.Column(db.String(), nullable=True)
    name = db.Column(db.String(), nullable=True)
    skin_color = db.Column(db.String(), nullable=True)
    species = db.Column(db.String(), nullable=True)
    starships = db.Column(db.String(), nullable=True)
    vehicles = db.Column(db.String(), nullable=True)

    _idx1 = db.Index('app_characters_charactername', 'name', unique=True)


class CharacterValidationModel(BaseModel):
    birth_year: str
    eye_color: str
    films: str
    gender: str
    hair_color: str
    height: str
    homeworld: str
    mass: str
    name: str
    skin_color: str
    species: str
    starships: str
    vehicles: str