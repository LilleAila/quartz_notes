---
id: 20240906T0732-naturfag-oppgaver-s67
aliases:
  - naturfag-oppgaver-s67
  - oppgaver-overføring-av-digital-informasjon
tags: []
---

#naturfag [[20240828T0840-naturfag|naturfag]] [[20240906T0737-oppgaver|oppgaver]] [[20240904T1208-trådløs-kommunikasjon|trådløs kommunikasjon]]

# Oppgaver s67

## Overføring av digital informasjon

2.7.1 - 2.8.5

> [!NOTE] Oppgave 2.7.1
> Hvilke fordeler har radiobølger i forhold til infrarød stråling?

Fordelene radiobølger har i forhold til infrarød stråling er at det kan gå mye lengre, med færre forstyrrelser, i motsetning til infrarød som ikke kan gå like langt og kan enkelt bli forstyrret.

> [!NOTE] Oppgave 2.7.2
> Hvilke egenskaper ved bærebølger kan vi forandre på for å overføre informasjon?

Vi kan enten forandre på frekvensen (FSK), eller endre på amplituden (ASK) på bølgen for å overføre informasjonen, der høyere amplitude eller frekvens tilsvarer 1 og lavere amplitude eller frekvens tilsvarer 0.

> [!NOTE] Oppgave 2.7.3
> Hvordan kan man skille mellom 0 og 1 for en frekvensskiftmodulert bølge?

En frekvensskiftmodulert bølge har alltid samme amplitude, men frekvensen endres. I områder med høyere frekvens er dette 1, og i områder med lavere frekvens er dette 0.

> [!NOTE] Oppgave 2.7.4
> Hvilket binært tall er representert ved FSK-bølgen nedenfor??

![20240906T0749-fsk-bølge-eksempel.png](Assets/20240906T0749-fsk-bølge-eksempel.png)

Tallet bølgen representerer er:
0100110
Jeg kan tolke det som at det er 0 på starten og det blir 00100110, som tilsvarer "&" i ASCII
Eller jeg kan tolke det som 01001100, som tilsvarer "L" i ASCII

> [!NOTE] Oppgave 2.7.5
> Tegn en ASK-bølge som representerer samme tall som FSK-bølgen i forrige oppgave

![[Drawing 2024-09-06 09.55.55.excalidraw]]

> [!NOTE] Oppgave 2.7.6
> Forklar prinsippene for kontaktløs betaling

Kontaktløs betaling bruker NFC. Near Field Communication bruker amplitudeskiftmodulerte radiobølger. EM-bølger fra kortleseren setter elektroner i kortet i bevegelse slik at kortet kan sende bølgene.

## Utvikling av nye kommunikasjonssystemer

> [!NOTE] Oppgave 2.8.1
> Hvordan kan en basestasjon skille én mobilsamtale fra en annen?

Ulike mobilsamtaler bruker bærebølger med ulike frekvenser. De bruker FSK-bølger, så de vil trenge litt rom til å endre frekvensen sin, men ulike samtaler vil gå over ulike frekvenser.

> [!NOTE] Oppgave 2.8.2
> Gi eksempler på hvordan uvedkommende kan overvåke mobilsamtaler eller annen informasjon du deler ved hjelp av mobiltelefonen din.

Alle signaler sendes ut i luften som radiobølger. Det betyr at det er potensielt mulig for noen uvedkommende å lese disse signalene for å finne ut hvilken data det er du sender og mottar. Bærebølger går over ulike frekvenser slik at hver person kun får for eksempel den mobilsamtalen den vil ha, men alle samtalene går likevel som signaler i luften som kan leses av hvem som helst. Noe som blir gjort for å unngå dette er å kryptere samtaler og all data som blir sendt rundt slik at det ikke gjør noe dersom noen uvedkommende får tilgang til denne dataen, fordi det ikke er mulig for dem å lese den.

> [!NOTE] Oppgave 2.8.3
> Hva menes med el-overfølsomhet?

El-overfølsomhet handler om at flere folk mener at de kan bli fysisk syke av EM-stråling fra mobiltelefoner, 5G og andre relaterte ting.
