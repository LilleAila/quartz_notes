---
id: 20250825T1400-elektriske-kretser
aliases:
  - elektriske kretser
tags: []
date: "2025-08-25"
title: elektriske kretser
---

#tof1 [[20250821T0835-tof1|tof1 (teknologi og forskningslære)]]

# elektriske kretser

## Ladninger

Det finnes positive (+) og negative (-) ladninger. Gjenstander med ulik ladning tiltrekkes og gjenstander med samme ladning frastøter hverandre. Elektrisk ladning ($Q$) måles i columb ($C$). $Q_{\text{elektron}} = -6.02 \cdot 10^{-19} C$

## Strøm

Ladningen som passerer et bestemt område på en bestemt mengde tid $t$. Dette området er et tverrsnitt av en leder som for eksempel kobber. Har symbolet $I$ og måles i ampere ($A$).

$I = \frac{Q}{t}$. Det vil si at $1 A = 1 \frac{C}{s}$

Strømmen av elektroner går fra negativ pol til positiv pol, men strømretningen er definert som retningen fra positiv pol til negativ pol.

## Spenning

Spenningen mellom to punkter gjør at de elektriske ladningene strømmer gjennom lederen. Kan sammenlignes med en vannpumpe. I en elektrisk krets er spenningskilden ofte et batteri.

Når en elektrisk ladning $Q$ beveger seg i en ledning tilkoblet en spenningskilde, vil det virke en elektrisk kraft $F$ på ladningen. Kraften gjør et arbeid $W$ på ladningen, og dette vil overføre energi til den. Arbeid og energi måles i $J$. Spenning er definert som arbeidet per ladning.

$U = \frac{W}{Q}$

Symbolet for spenning er $U$, og enheten er $V$ (volt). $1 V = 1 \frac{J}{C}$

---

En spenningskilde som leverer konstant psenning kalles en likespenningskilde (DC). Batterier er eksempler på dette. Spenningns i strømnettet har vekselspenning, altså går det en vekselstrøm (AC) i kretsen. Strøm og spenning skifter retning med en frekvens på $50 Hz$ (svingninger per sekund), og spenningen er $230 V$ (dette er forholdet mellom fasene, og ikke en konstant spenning som i likespenning).

## Motstand

Motstand beskriver hvor lett ladningen kan strømme gjennom en leder. En tykk kobbertråd vil ha lavere motstand, enn en tynn kobbertråd. I tillegg til en lengre tråd ha høyere motstand enn en kortere tråd. Som mål for motstanden i et materiale, bruker vi resistans (symbol $R$, måles i $\Omega$).

$$
R = \frac{U}{I}
$$

Det vil si at $1 \Omega = 1 \frac{V}{A}$

En krets blir kortsluttet hvis man ikke har noe motstand mellom polene på spenningskilden. Dette er ikke ønskelig og vil skape mye varme og tømme batteriet for ladning. Man vil derfor ha en motstand i kretsen.

Motstand fargekodes slik:

![motstand](Assets/20250825T1415-motstand.png)

### Finne riktig resistans

> Skal finne riktig motstand til grønn diode

Bruker et datasheet for en generell grønn LED (light-emitting diode): https://www.farnell.com/datasheets/2724776.pdf
Det spiller ikke noen rolle nøyaktig hvilken.

![[Pasted image 20250904085940.png]]

Finner spenningstap (forward voltage, her $3.2\,\mathrm{V}$)
Finner strøm (her $20\,\mathrm{mA}$)

$$
\begin{align}
  V_{\text{total}} &= 9\,\mathrm{V} & \\
  V_{\text{motstand}} &= V_{\text{total} - V_{\text{LED}}} & \\
  &= 9\,\mathrm{V} - 3.2\,\mathrm{V} & \\
  &= 5.8\,\mathrm{V} &
\end{align}
$$

Vet da at det er $5.8\,\mathrm{V}$ igjen som må brukes i motstand. Bruker da ohms lov til å regne ut riktig resistans:

$$
\begin{align}
  U &= IR & \\
  R &= \frac{U}{I} & \\
  &= \frac{5.8\,\mathrm{V}}{20\,\mathrm{mA}} & \\
  &= \frac{5.8\,\mathrm{V}}{0.02\,\mathrm{A}} & \\
  &= 290 \,\Omega &
\end{align}
$$

> [!NOTE]
> Merk at uttrykket kan forenkles som følger:
>
> $$
> \frac{R_{\text{total}} - R_{\text{LED}}}{I}
> $$
>
> For den grønne dioden og et $9\,\mathrm{V}$ blir det:
>
> $$
> \frac{9\,\mathrm{V} - 3.2\,\mathrm{V}}{20\,\mathrm{mA}} = 290 \,\Omega
> $$

Man vil alltid heller ha for mye enn for lite motstand.

## Seriekobling

### Motstand

Motstanden i en seriekobling er lik summen av motstanden til de ulike komponentene.

$$
R = R_{1} + R_{2} + \dots + R_{n}
$$

## Parallellkobling

### Motstand

Motstanden i en parallellkobling er gitt ved formelen

$$
R = \left( \frac{1}{R_{1}} + \frac{1}{R_{2}} + \dots + \frac{1}{R_{n}} \right)^{-1}
$$

For eksempel, hvis man har to like motstander koblet parallelt, vil den totale motstanden være halvparten så mye som en enkelt motstand, fordi strømmen har dobbelt så mange veier å gå.

Totalresistansen $R$ i en parallellkobling er alltid mindre enn den minste av de tilkoblede resistansene.

---

I en krets med to parallellkoblede motstander på $220 \Omega$, vil den totale motstanden være

$$
\begin{align}
  R &= \left( \frac{1}{220\Omega} + \frac{1}{220 \Omega} \right)^{-1} & \\
  &= \left( \frac{2}{220\Omega} \right)^{-1} & \\
  &= \frac{220\Omega}{2} & \\
  &= 110\Omega &
\end{align}
$$

Bruker et batteri med en kjent spenning på $9V$. Kan da bruke ohms lov til å finne strømmen

$$
\begin{align}
  I &= \frac{U}{R} & \\
  &= \frac{9 V}{110 \Omega} & \\
  &\approx 0.081 A & \\
  &\approx 8 mA &
\end{align}
$$

## Ohms lov

Beskriver forholdet mellom strøm, spenning og motstand. Formelen for motstand utledes fra denne.

$$
U = I \cdot R
$$

### Strøm

Strømmen $I$ i en parallellkobling er lik summen av av alle strømmene. I et grenpunkt er summen av alle inngående strømmer lik summen av alle utgående strømmer.

### Spenning

Delspenningene i en parallellkobling er alltid lik hovedspenningen

## Koblingsbrett

Kolonnene merket $+$ og $-$ er forbundet med pluss og minus-polen til spenningskilden. De $5$ hullene på hver side av midten er forbundet.
