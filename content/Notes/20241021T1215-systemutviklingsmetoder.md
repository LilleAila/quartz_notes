---
id: 20241021T1215-systemutviklingsmetoder
aliases:
  - systemutviklingsmetoder
tags: []
title: systemutviklingsmetoder
date: 2024-10-21
---

#it2 [[20240912T0621-it2|it2]]

https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/2-objektorientert-programmering/2b-systemutvikling/systemutviklingsmetoder

# systemutviklingsmetoder

## Fossefallmetoden

Jobbe lineært. Hele prosjektet planlegges i forkant.

![20241021T1247-fossefallmetoden.png](Assets/20241021T1247-fossefallmetoden.png)

- Krav: Kravene til programvaren beskrives. Hvilke konkrete problemer skal programvaren løse?
- Design: Programvaren planlegges.
- Utvikling: Programvaren utvikles.
- Testing: Programvaren testes.
- Lansering: Programvaren er godkjent og kan lanseres.
- Vedlikehold: Programvaren vedlikeholdes. Feil rettes opp o.l.

Kan være nyttig for et forutsigbart prosjekt, men det kan være vanskelig å implementere endringer som kommer underveis.

## Smidig metodikk

![20241021T1251-smidig-metodikk.png](Assets/20241021T1251-smidig-metodikk.png)

Baserer seg på en syklus som gjentas igjen og igjen. Kalles ofte en "sprint", og varer i noen uker. Mindre steg enn i fossefallmetoden.

Starter med å beskrive krav, deretter planlegge sprinten ut fra hvilke krav og problemer som skal løses. Designer en løsning, lage den og implementere den. Til slutt oppsummeres sprinten, og resultatet presenteres og vurderes.

Produktet kan være "ferdig" etter første sprint, og kan forbedres og justeres i etterfølgende sprinter.

## Prosjektstyring

Plassere oppgaver i ulike kategorier:

- Ikke påbegynt
- Påbegynt
- Testes
- Godkjent

Underveis er det vanlig å ha møter, kalt "stand up"-møter eller "scrums".

## Versjonskontroll

Git - Lar mange folk samarbeide enklere, og lagrer endringer

GitHub - platform basert på git

## Parprogrammering

Jobber to og to, mens kun en får skrive kode av gangen. Den andre skal vurdere, kommentere og diskutere koden som skrives. (også forberedelse til muntlig eksamen)
