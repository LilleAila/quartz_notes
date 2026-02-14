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
> jeg hadde ikke tid til å faktisk gjøre konkurransen lol men jeg tok notater fra møtet likevel

Antall frys av screenshare ila møtet: 14

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

Da får man tid $O \left( nv \log{nv} \right)$ i stedet for $O \left( n \log{n} \right)$ som ved vanlig dijkstra

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

Vi vil da holde styr på hvilke nodes som er brukt og hvilke som ikke er brukt. Dette kan være et binærtall. Hvir man for eksempel har besøkt nodes (1-indeksert) 1, 2, 3, 4 men ikke resten kan man ha 111000000. Tilstanden bryr seg ikke om hvordan man kom seg mellom nodes, bare hvilke som er brukt. Altså vil man få `dp[1111000000] = minste kostnad med disse nodes valgt`. Og så kan man forbinde to til og sette `dp[1111000011]` som gir et nytt utvalg og beregne det basert på den forrige state der man ikke hadde lagt til disse to nodes. (NOTE: ligner kanskje litt på knapsack?). Man vil da få $2^{n}$ ulike tilstander man kan være innom, worst case $2^{25}$. (i praksis blir vel dette å brute force alle kombinasjoner men med memoization da)

For eksempel kan man beregen `dp[11011011110]` ved å se på alle par av enerene. Hvis man da velger paret `2, 4` vil man se på `dp[10001011110]` (beste verdi uten disse) + `kostnad fra hønsehus -> node 2 -> node 4 -> hønsehus`.

Dette vil være en mulighet for å løse den, men kan bli ganske tregt med $O \left( n^{2} \right) \cdot O \left( 2^{n} \right)$ (der $n \leq 25$ men som likevel blir veldig mye)

---

Man kan optimalisere søket ved å se at rekkefølgen man gjør det i ikke har noe som helst å si (som jeg nevnte i starten).

Vi kan nå `11011` både ved å først besøke `11000` og å besøke først `00011`. Dette blir litt bortkastet da hvis man må beregne `11011` to ganger som blir samme resultat siden rekkefølgen på parene ikke har noe som helst å si. Så da ønsker vi å redusere states. Vi starter da ved å se på parene man kan lage med kun første bit.

Starter da med `DP[00000000] = 0` og tester alle parene vi kan lage med første bit, for eksempel `DP[10010000]`. Når vi gjør det i denne rekkefølgen har vi alltid en $1$ på første stilling og denne kan ikke lenger variere. Vi kan da ikke ha noen som helst stilling som starter med en $0$, altså finnes ikke lenger `DP[0010000]` siden denne ikke har en $1$-er på slutten. Vi fortsetter på samme måte ved å beregne de som har to 1-ere på starten. Så vi vil ha tilstanden `DP[1100101]`. Hvis vi fortsetter samme mønster vil vi da ikke kunne ha `DP[1101]` siden hver $1$-er i starten skal være paret med en annen. Altså har vi at minimum halvparten av $1$-erene MÅ være i starten.

Man får altså ikke lenger $2^{n}$ tilstander man må teste. Man trenger da ikke å se på hver eneste siden rekkefølgen ikke har noe og si og det da blir mer effektivt å alltid begynne med de i starten. Slik kan man drastisk redusere mange unødvendige tilstander som ikke følger dette mønsteret ved at alle $1$-ere må være i starten.

> Jeg er litt usikker på om tabulation eller memoization ville vært best her. Jeg tenker kanskje tabulation der man bygger opp etter det mønsteret jeg beskrev.

Adrian valgte å bruke memoization, altså top-down DP. `rec(11111)` vil da se på finne `min(rec(01101) + lengde med det valgte paret, rec(01111) + lengden av den gjenstående)`. Man vil bare bruke pytagoras 3 ganger for å finne lengdene.

## 5 - klassebilde

Man har personer stilt opp på en linje og ønsker å finne de personene som har størst gjennomsnittlig avstand i hvert bilde. Hvis man kun har én linje (ett klassebilde) vil dette da bli første og siste person på rekken. Vi har gitt at $n \leq 100 \,000$, så vi kan ikke teste alle kombinasjoner med $O \left( n^{2} \right)$ da dette ville tatt for lang tid.

`3 1 7 5 6 2 4` - Her vil 3 og 4 være lengst fra hverandre.
Legger til enda en linje:
`2 3 6 7 1 5 4`

Hvis vi har 5 og 6 som dette står og prøver å regne ut den totale avstanden mellom dem får vi 1 og -3 som blir 2 i avstand (abs), men vi kan reversere liste 2 sånn at vi får 4 i forskjell totalt som blir riktig. Altså vil vi snu listen slik at den samme alltid er lengst til venstre i paret. Hvis vi da summerer indeksen til hver av dem (uten å flippe)

```
0 1 2 3  4 5 6 <- INDEX
3 1 7 5  6 2 3 <- RAD 1
2 3 6 7  1 5 4 <- RAD 2

1 2 3 4  5 6 7 <- PERSON IDX
5 5 1 12 8 6 5 <- TOTAL INDEX
```

Hvis vi reverserer den nederste linjen får vi

```
0 1 2 3 4 5 6 <- INDEX
3 1 7 5 6 2 3 <- RAD 1
4 5 1 7 6 3 2 <- RAD 2 (flippet)

1 2 3 4 5 6 7 <- PERSON IDX
```

Hvis man har et par `a, b` og har for eksempel

```
a b
b a
b a
```

, vil man til slutt få

```
a b
a b
a b
```

Når vi prøver alle mulige permutasjoner av å flippe vil vi til slutt få en der paret er i samme rekkefølge i alle radene. Siden vi har gitt at antall bilder er $\leq 7$ kan man gjøre alle mulig flips og beregne gjennomsnittlig avstand for hver flip. Dette gir $O \left( 2^{K} N K \right)$.

Hver kombinasjon vil gi en avstand som er den maksimale. Vi velger det paret som har størst avstand mellom seg fra alle kombinasjonene. Så om vi kombinerer alle kombinasjonene av å reversere velger vi til slutt den maksimale. Så for hver konfigurasjon regner man ut summen av indeksene for hvert tall, og finner tallet med lavest sum av indeks og tallet med høyest sum av indeks. Vi lagrer denne differansen og gjør dette for hver eneste kombinasjon av flips for å finne størst total avstand. Strengt tatt vil vi kun trenge å sjekke $k-1$ kombinasjoner av flips siden den første bare kan stå som den er. (ellers ville man ha sjekket alle de samme kombinasjonene to ganger bare baklengs)

> [!NOTE]
> Disse for oppgave 5 ble litt rotete siden det tok meg litt lengre tid å forstå 😭

Ofte når det er lave tall som $k \leq 7$ i oppgaven betyr det at de vil at vi skal se på en løsning som er $2^{k}$ eller lignende.
