---
id: 20241107T0750-objektorientert-programmering
aliases:
  - objektorientert programmering
  - oop
tags: []
title: objektorientert programmering
date: 2024-11-07
---

#it2 [[20240912T0621-it2|it2]]

# objektorientert programmering

- Objekt: inneholder metoder og attributter
- Klasse: oppskrift for hvordan objektene skal være
- Metoder: funksjoner i en klasse. Tar første parameter `self` i python
- Attributter: variabler i et objekt med tilordnede verdier
  Ulike instanser av en klasse har de samme attributtene, men kan ha ulike verdier
  To objekter med likt innhold i attributter er fortsatt to ulike objekter

## Klasser

Defineres i python med `class`-keyword. Har en **konstruktør** med navn `__init__`. Alle metoder tar et parameter `self`, som refererer til seg selv.

**Konstruktør**: funksjon som kjøres når en instans av en klasse initialiseres. Brukes til å sette variabler og lignende. Alt for initialiseringen gjøres på dette samme stedet.

Vi får modularitet ved å pakke data i form av attributter, og funksjonalitet i form av metoder sammen i klasser og objekter.

```py
class Person:
    def __init__(self, navn: str): # Konstruktør
        """Konstruktør"""
        self.navn = navn # Attributt
```

Klasser kan lagres hvor som helst: lister, ordbøker, variabler. Hvilken man bruker er avhengig av sammenhengen det brukes i, det er ingen som er den "beste".

```py
p1 = Person("Olai")
p2 = [Person("person1"), Person("person2")]
p3 = {
    "o": Person("Olai"),
    "p": Person("person3")
}
```

## Arv

Kan gjenbruke kode ved at ulike klasser har en superklasse.

```py
class Elev(Person):
    def __init__(self, navn: str, trinn: int):
        super().__init__(navn) # Initialisere parent-klassen først
        self.trinn = trinn

class Lærer(Person):
    def __init__(self, navn: str, fag: str[]):
        super().__init__(navn)
        self.fag = fag
```

Polyformi: metoder i ulike klasser som har samme navn, men ulik funksjonalitet. En superklasse til slike klasser kan ligne på en `Interface` i noen andre språk som java.

```py
class Dyr:
    def __init__(self, navn: str):
        self.navn = navn

    def hils(self):
        pass

class Hund(Dyr):
    ...
    def hils(self):
        print("Mjau")

class Katt(Dyr):
    ...
    def hils(self):
        print("Mjau")
```

## Tilgang og innkapsling

Noen språk har sylighetsmodifikatorer som `public`, `private` og `protected`. Det finnes ikke i python :(
I python gjør vi innkapsling ved å prefixe med understrek(er).

```py
class Dyr:
    def __init__(self, navn: str):
        self._navn = navn # Har ingen funksjon, men forteller utviklere at dette er privat
        self.__navn = navn # Endrer internt navnet til formen _Klassenavn__Variabelnavn, her _Dyr__navn
```

Begge disse to metodene fører til at det fortsatt er skrivbart, men forteller deg selv og andre utviklere at man ikke skal gjøre noe med dem.

### Getters / setters

Det er lurt å bruke funksjoner til å skrive og lese verdier, heller enn å gjøre det direkte. Der kan man håndtere verdier som kan være feil, eller på andre måter manipulere dataen. Man kan enten lage funksjoner som `getAge` og `setAge`, eller bruke decorators.

```py
class Person:
    def __init__(self, alder: int):
        self.__alder = alder

    @property
    def alder(self) -> int:
        """Getter"""
        return self.__alder

    @alder.setter
    def alder(self, alder: int):
        """Setter"""
        self.__alder = alder

p1 = Person(10)
print(person.alder) # vil kjøre getteren
person.alder = 5 # vil kjøre setteren
print(person._Person__alder) # vil lese verdien direkte
```

`@property` og `@attributtnavn.setter` er innebygget i python. Mer om decorators: https://realpython.com/primer-on-python-decorators/

## Abstraksjon

Man vil skjule unødvendige detaljer for brukeren; de bryr seg kun om _hva_ som skjer, ikke _hvordan_ det skjer.
Det vi gjør tilgjengelig for omverden kalles programmeringsgrensesnittet. (API / Application Programming Interface)
Med en API kan andre brukere / utviklere bruke andre sin kode i sine programmer. TV er et program -> Fjernkontroll er API.

## Klassevariabler

Attributter er objektvariabler. De er lokale til hver instans av klassen. Variabler koblet til selve klassen kaller vi **objektvariabler**. De er `static` i andre språk.

```py
class Gun:
    serial: int = 0

    def __init__(self):
        Gun.serial += 1
        self.serial = Gun.serial
```

## Klassemetoder

På samme måte som klassevariabler, gjelder klassemetoder for selve klassen, heller enn hver instans av klassen. De har tilgang til klassevariabler, men ikke til objektvariabler. De blir definert med decorator `@classmethod`.

```py
class Person:
    total_people = 0

    def __init__(self):
        Person.total_people += 1

    @classmethod
    def get_total_people():
        print(f"There are {Person.total_people} people in total")
```

## Slots

Slots sier hvilke attributter en klasse har. Det gjør at koden kjører pittelitt raskere, og lar deg ikke bruke noen attributter som ikke er i `__slots__`.

```py
class Person:
    __slots__ = ("alder", "navn")

    def __init__(self, alder, navn):
        self.alder = alder
        self.navn = navn
```
