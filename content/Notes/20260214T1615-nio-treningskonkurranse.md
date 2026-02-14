---
id: 20260214T1615-nio-treningskonkurranse
aliases:
  - nio treningskonkurranse
tags: []
date: "2026-02-14"
title: nio treningskonkurranse
---

# nio treningskonkurranse

> Her er mine notater fra teams møtet

Antall frys: 10

---

Generelt sett ser jeg at det kan hjelpe ganske mye å bare tegne opp og skissere hvordan man ville gjort en simplifisert versjon (for eksempel en av eksempel casene) og så se om man kan finne et mønster eller en god løsningsmetode, altså starte med å skissere på papir i stedet for å skrive kode direkte.

## 1 - ekornfare

Fjerner alle som ingen ekorn kan gå til og der ekorn kan gå fra. Altså der et tre har minst en høyere nabo og ingen lavere naboer. (merk at om trær er like vil ikke ekornet gå mellom dem). Dette gjør man først en gang med alle trær, og så trenger man kun å legge til naboene til det som ble fjernet, og ikke å iterere over HELE listen igjen. Dermed får man lineær tid.

## 2 - brusskap

Jobbe med intervaller. Starter med intervallet (0, 0) og går videre. Når man ser at den neste transaksjonen vil føre til et ugyldig svar (ingen av bounds i intervallet er gyldige), vil vi sette intervallet til (0, k) der k er kapasiteten som vil tilsvare å legge til en ekstra transaksjon. Da vil antall slike bytter frem til slutten være riktig svar på oppgaven. Altså vil man for hver iterasjon fjerne de verdiene fra intervallet som ligger utenfor gyldighetsområdet, og om det ikke er en eneste gyldig verdi igjen i intervallet etter neste (NOTE: ikke denne men den neste, må ha en form for look ahead), blir man nødt til å "nullstille" intervallet som vil si å legge til en til transaksjon.

Man kan da gjøre dette i lineær tid ved å lage et nytt intervall for hver $n$ i listen. Man kunne bare brute forcet det med $O(n!)$ eller noe også lol

## 3 - togtur

Dette er et lavest total vekt grafproblem med en regel lagt til om at man har gratisbilletter tilgjengelig. Her vil man bruke dijkstras algoritme. Denne vil virke dersom man har ingen gratisbilletter.

Man kan enten gå den vanlige veien og betale normal pris. Alternativt kan man bruke opp en gratisbillett, men betale null i pris. Man ser altså på begge to mulighetene for hver kant. Man må da holde styr på antall gratisbilletter brukt. Hver node er da ikke bare en node, men man ser da også på hvor mange billetter det tok å komme seg dit. For en node lagrer man da `dp[n][k]` for en node i stedet for bare `dp[n]` som i vanlig dijkstra. Altså kan for eksempel

`dp[6][0] = 5` hvis man bruker ingen gratisbillett
`dp[6][1] = 2` hvis man bruker én gratisbillett
`dp[6][2] = 0` hvis man bruker to

Når man beregner `dp[6][2]` kan dette avhenge av `dp[3][1]`. Altså har man to måter å bruke en kant der en kant fra `3 -> 6` vil bli enten `dp[6][k] = dp[3] + vekt` eller `dp[6][k+1] = dp[3]`. Så i stedet for å se på hver node én gang, ser man på hver node `v` ganger (`v` er antall tilgjengelige gratisbilletter)

Da får man tid $O \left( nv \log_{nv} \right)$ i stedet for $O \left( n \log_{n} \right)$ som ved vanlig dijkstra

---

TODO: kanskje se en video på youtube for å forstå dijkstra litt bedre?

Det er ganske vanlig at en av de fem oppgavene inneholder en variant av et vektet grafproblem med noen ekstra regler lagt til. For eksempel ormehull oppgaven også fra finalen i fjor.

---

(før han sier den gode løsningen) jeg ville ha prøvd å legge til en tredje item i dijkstra tuplen for antall gratisbilletter igjen. i stedet for å legge kun til nabo-nodes i priority queuen

(total_kostnad, node)

ville jeg i stedet lagt til to elementer i køen:

(total_kostnad, gratisbilletter, node)
(kostnad_uten_neste_edge, gratisbilletter-1, node)

altså får køen format

(vekt, billetter, node)

> yooo jeg tenkte basicly det samme bare at han forklarte med en dp table men jeg tror at resultatet vil bli det samme på en måte

## 4 - reven

En rev kan bære to høns, og hvert gjemmested kan inneholde kun én høne før han må gå tilbake til hønsehuset. Man vil da forsøke å minimere avstanden. Merk at etter man har levert ut alle høns vil man ikke trenge å gå tilbake igjen. Man får gitt at $n$ er ganske liten her. I de andre oppgavene har man kunnet ha mer grådige algoritmer, men her må man tilsynelatende ha noe litt mer brute force-aktig.

Dette kan være et DP-problem. For hver tur vil man vanligvis gå fra hønsehus -> node 1 -> node 2 -> hønsehus. Det spiller ingen rolle om node 1 eller node 2 er først, og det spiller ikke noen rolle hvilken rekkefølge man tar parene i.

Vi vil da holde styr på hvilke nodes som er brukt og hvilke som ikke er brukt. Dette kan være et binærtall. Hvir man for eksempel har besøkt nodes (1-indeksert) 1, 2, 3, 4 men ikke resten kan man ha 111000000. Tilstanden bryr seg ikke om hvordan man kom seg mellom nodes, bare hvilke som er brukt. Altså vil man få `dp[1111000000] = minste kostnad med disse nodes valgt`. Og så kan man forbinde to til og sette `dp[1111000011]` som gir et nytt utvalg og beregne det basert på den forrige state der man ikke hadde lagt til disse to nodes. (NOTE: ligner litt på knapsack?). Man vil da få $2^{n}$ ulike tilstander man kan være innom, worst case $2^{25}$. (i praksis blir vel dette å brute force alle kombinasjoner men med memoization da)

For eksempel kan man beregen `dp[11011011110]` ved å se på alle par av enerene. Hvis man da velger paret `2, 4` vil man se på `dp[10001011110]` (beste verdi uten disse) + `kostnad fra hønsehus -> node 2 -> node 4 -> hønsehus`.

Dette vil være en mulighet for å løse den, men kan bli ganske tregt med $O \left( n^{2} \right) \cdot O \left( 2^{n} \right)$ (der $n \leq 25$ men som likevel blir veldig mye)

---

Man kan optimalisere søket ved å se at rekkefølgen man gjør det i ikke har noe som helst å si (som jeg nevnte i starten).

Vi kan nå `11011` både ved å først besøke `11000` og å besøke først `00011`. Dette blir litt bortkastet da hvis man må beregne `11011` to ganger som blir samme resultat siden rekkefølgen på parene ikke har noe som helst å si. Så da ønsker vi å redusere states.
