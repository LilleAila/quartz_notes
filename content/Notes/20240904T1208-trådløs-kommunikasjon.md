---
id: 20240904T1208-trådløs-kommunikasjon
aliases:
  - trådløs kommunikasjon
tags: []
title: trådløs kommunikasjon
date: 2024-09-04
---

# trådløs kommunikasjon

Bærebølger - en bølge med en frekvens som man kan bruke for å se at dette er "riktig" bølge.

![20240904T1225-bølgelengder.png](Assets/20240904T1225-bølgelengder.png)

Bølger med lavere bølgelengde, altså lavere frekvens, har mye høyere rekkevidde, men kan ikke ha så mye informasjon. Dette er det som brukes for radiobølger. Høyere frekvenser vil kunne transportere mer informasjon raskere, men vil ha lavere rekkevidde.

## Amplitudeskiftmodulasjon - ASK (amplitude shift keying)

Amplituden på bølgen endres slik at den representerer et digitalt signal der 1 er høy amplitude og 0 er lav amplitude. Denne typen signaler blir lett påvirket av støy, så den blir ikke brukt veldig mye

## Frekvensskiftmodulasjon - FSK (frequency shift keying)

- Frekvensen på bølgen endres i stedet for amplituden. Høyere frekvens på bølgen tilsvarer flere svingninger (Hz), og tilsvarer $1$, mens en lavere frekvens tilsvarer $0$

## Forskjellen mellom ASK og FSK -signaler

Her er et eksempel på hvordan et signal sendes som AM og som FM

![20240904T1238-am-fm-signaler.png](Assets/20240904T1238-am-fm-signaler.png)

## Trådløs optisk kommunikasjon

Informasjon kan også overføres ved hjelp av andre medium enn luft, for eksempel ved hjelp av lys, enten med ulike bølgelengder som analoge signaler, eller som av/på signaler ved å skru av og på lyset. Både bålbrenning og fyrlykter er eksempler på optisk kommunikasjon, men det kan også være nettverks-signaler i en nettverkskabel som også bruker lys til å overføre informasjon.

## Kommunikasjon via lyd

Lydsignaler kommer for eksempel fra at vi snakker sammen, eller for eksempel sonarer som bruker lyd for å få informasjon om ting som grunnforhold ved å sende ut lydsignaler som utfører seg forskjellig ut fra hvilken tetthet det er i materialene slik at de kan få informasjon om det.

## Oppgaver

1. Gi eksempler på hva vi bruker trådløs kommunikasjon til i hverdagen.
   Vi bruker trådløs kommunikasjon til alt mulig i hverdagen:

- Snakke med folk
- Gjøre skoleoppgaver på internett

Forskjellige typer trådløs kommunikasjon inkluderer

- Bluetooth
- WiFi
- RFID
- NFC
- Radio

2. Hva slags type stråling er radiobølger?
   Radiobølger er lavfrekvente elektromagnetiske bølger. Forskjellen mellom mekaniske og elektromagnetiske [[20240828T0840-bølger|bølger]] er at elektromagnetiske bølger ikke trenger et medium å bevege seg gjennom
3. Sammenlign bølgelengde og frekvens hos radiobølger med andre typer EM-stråling.
4. Hvilke bruksområder egner radiobølger seg til?
   Radiobølger egner seg til å sende enkle signaler (for eksempel lyd) over lange distanser, der alle skal motta det samme signalet heller enn med mobil der alle har ulike signaler de skal motta, som for eksempel i en bilradio.
5. Forklar hva som menes med bølgelengde og frekvens.
   Bølgelengen er distansen i meter mellom to bølgetopper. Frekvensen er hvor mange bølgetopper som passerer et punkt på ett sekund.

6. Hva er sammenhengen mellom frekvens og bølgelengde?
   Dersom både bølgelengden og bølgefarten økes, vil vi fortsatt ha samme frekvens. Hvis bølgelengden økes, men bølgefarten forblir den samme, vil bølgen ha høyere frekvens. Forholder mellom dette er:

   $$
   \text{bølgefart} = \text{frekvens} \cdot \text{bølgelengde}
   $$

   , eller uttrykt ved bokstaver:

   $$
   v = f \cdot \lambda
   $$

7. Hvordan kan vi overføre informasjon ved hjelp av radiosignaler?
   Radiobølger er et analogt signal, mens det man som oftest vil overføre er digitale signaler, altså signaler med 1100101 etc. Dette kan gjøres ved å kode det inn i bølgene enten ved å endre på amplituden, eller på frekvensen.

8. Hva er AM og FM? Hvorfor er det vanligere å bruke FM enn AM?
   AM står for Amplitudemodulering, som betyr at der man vil sende en høyere verdi, for eksempel når man vil sende signalet $1$, vil man øke amplituden, og for å sende $0$, vil man senke den. FM står for Frekvensmodulering. Der øker man heler frekvensen i stedet for amplituden. Dette gjør at det er mange færre forstyrrelser. Med AM kan det være mange kilder til forstyrrelse, for eksempel motorlyder.

9. Gi eksempler på ulike antennedesign. Hvilke fordeler og ulemper har de ulike antennedesignene?
   Antenner kan enten være direksjonelle, eller omnidireksjonelle. En direksjonell antenne vil kun sende signaler i en enkelt retning som den er laget for å sende signalene i, mens en omnidireksjonell antenne vil kunne sende signalene overalt rundt i rommet. Fordelen med en omnidireksjonell antenne er at den vil kunne sende signaler overalt i rommet, mens fordelen med en direksjonell antenne er at den vil kunne sende sterkere signaler, men kun i en retning.

10. Hvorfor regner vi med at radiobølger ikke er helsefarlige?
    De typene bølger vi regner som helsefarlige har veldig små bølgelengder som er mye høyere enn det synlige lyser, i motsetning til radiobølger som har veldig lang bølgelengde, som er mye større enn den lengste synlige bølgelengden.

11. Hva kan være problemet med bruk av radiobølger?
    Fordi radiobølger er så lavfrekvente, betyr dette at de ikke kan overføre like mye data som bølger med høyere frekvens. Derfor passer de bra til ting som bilradioer der man ikke trenger å overføre veldig mye informasjon, men har fordelen at de har stor rekkevidde slik at alle bilene kan høre det.

12. Hvorfor kan man ikke sende signaler på den frekvensen man selv vil?
    Ulike frekvenser er reservert til forskjellige ting. For eksempel går de fleste typene elektronikk man bruker med WiFi og Bluetooth på 2.4 eller 5 GHz. Dersom man bare bruker hvilken som helst frekvens man vil, betyr dette at det vil oppstå forstyrrelser mellom ulike signaler som sendes.

13. Gi noen eksempler på bruk av radiosignaler i ulike frekvensområder.

14. Hvorfor har radiobølgene fra den trådløse ruteren hjemme kortere bølgelengde og høyere frekvens enn signaler som brukes til DAB-radio?
    Signaler fra ruteren hjemme har ikke noe behov for å bevege seg like langt som radiobølger fra DAB-radio. Dette betyr at de kan bruke mye høyere frekvens (og lavere bølgelengde), slik at de kan overføre mer informasjon men over kortere lengde.

# Kilder

- [Trådløs kommunikasjon med radiobølger](https://ndla.no/nb/subject:1:f18b0daa-6507-4025-8998-b8a11c8ccc70/topic:5:dbc23651-7216-4610-bc38-dde58f013724/topic:3:fe851509-1f3c-4fef-9922-ae05ff1a4fba/resource:5edb583f-b7a9-4d04-8f3b-58100188e8ce)
- [Oppsummerende oppgaver - trådløs kommunikasjon](https://ndla.no/nb/subject:1:f18b0daa-6507-4025-8998-b8a11c8ccc70/topic:5:dbc23651-7216-4610-bc38-dde58f013724/topic:3:fe851509-1f3c-4fef-9922-ae05ff1a4fba/resource:fffdd2b6-1383-4d6a-91be-25629201dc94)
