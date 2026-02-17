---
id: 20260212T1007-tof1-vårprosjekt-logg
aliases:
  - tof1-vårprosjekt-logg
tags: []
date: "2026-02-12"
title: tof1-vårprosjekt-logg
---

#tof1 [[20250904T0955-tof1-logg|tof1-logg]]

# tof1-vårprosjekt-logg

## 2025-02-05

Startet på vårprosjektet. Diskutert med Håvard hvilke sensorer som trengs og hva vi skal finne ut av. Vi komkluderte med at det kunne være interessant å undersøke hvordan støynivået på skolen henger sammen med ulike andre faktorer som for eksempel konsentrasjon.

Jeg begynte å se på hvordan man skal bruke DHT-22 og fått den til å lese inn data til seriell-konsollen. Jeg tror det vil være mulig å koble opp et SD kort direkte for å lagre dataen, jeg skal undersøke videre neste gang.

## 2025-02-09

Vi begynte å formulere noen kravspesifikasjoner til prosjektet. Jeg fant ut at det blir vanskelig å bruke SD-kort modulen med arduino uno, så vi måtte heller bytte til å bruke MKR NB 1500 fordi denne har en innebygget SD-kort leser. I praksis vil vi kunne gjøre det meste som fra før, og det blir faktisk enklere å gjøre mange ting fordi vi kan feste den direkte til et koblingsbrett. Vi ferdigstilte listen over hvilke sensorer som må kjøpes inn og begynte med å sette opp de komponentene vi har. Jeg koblet sammen arduinoen og sd kortet og testet at det var mulig å skrive til en fil.

Optimalt sett skulle vi opprettet nye filer for hver måling med navnet satt basert på RTC. Dette var ikke mulig med uno, men etter vi byttet til MKR NB 1500 har den en intern RTC modul som vi kan bruke. Jeg fant ut at vi har både DHT22 og BME280 tilgjengelig for å måle temperatur og luftfuktighet. Vi bestemte oss for å bruke sistnevnte i stedet da denne skal gi mer stabile målinger over tid.

Jeg opplevde noen problemer med SD-kortet og fikk det ikke til å virke helt. Det ble formatert korrekt fra linux, men arduinoen klarte likevel ikke å bruke det. Jeg prøvde både med det innebygde biblioteket og med `SdFat`-biblioteket, og ingen av dem klarte å oppfatte sd-kortet. Dette må jeg da jobbe videre med neste gang.

## 2025-02-12

Jeg fikk SD-kortet til å fungere denne gangen. Det viste seg at jeg brukte feil ting som jeg plugget SD-kortet inn i. Man måtte bruke en slik SD shield på arduino MKR NB 1500-en for at sd-kortet skulle fungere.

![20260212T1002-arduino-mkr-nb-1500-sd-shield.png](Assets/20260212T1002-arduino-mkr-nb-1500-sd-shield.png)

Videre skrev jeg en kode som skriver en CSV-datafil med økende navn (data_001.csv, data_002.csv etc). Jeg fikk ikke RTC til å fungere på en stabil måte, så jeg endte opp med å bare måtte bruke et tall for å identifisere filen. Dermed blir vi da nødt til å arkivere filen etter hver måling for å passe på at vi får riktig fil knyttet sammen med beskrivelsen. Dette blir nok ikke et stort problem da det sikkert er det vi ville gjort uansett.

I tillegg fikk vi BME280 til å fungere med en annen arduino:

![20260212T1007-bme280-arduino.png](Assets/20260212T1007-bme280-arduino.png)

Neste time vil vi kombinere de to programmene for å logge temperatur og fuktighet. Det som gjenstår nå handler om de sensorene som vi ikke har bestilt enda, så da blir det ikke så mye vi kan jobbe med fysisk. Da vil jeg heller fortsette å jobbe med å formulere kravspesifikasjonene.

## 2025-02-16

Vi har slått sammen de to programmene slik at det nå logges reell data til CSV-filen. Vi har nå i praksis skrevet alt grunnlaget vi trenger for å kunne utvide koden senere med flere sensorer, og må bare vente til disse kommer for å kunne implementere resten. Jeg har også begynt å lese litt i dokumentasjonen på hvordan jeg bruker TEMT6000 og KY07 (lys og lydsensorene).

Videre har vi sett litt på dataen fra testmålingene og jeg har tenkt på hva som kan være lurt å undersøke.
