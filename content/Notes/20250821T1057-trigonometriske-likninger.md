---
id: 20250821T1057-trigonometriske-likninger
aliases:
  - trigonometriske likninger
tags: []
date: "2025-08-21"
title: trigonometriske likninger
---

#matte [[20250819T1116-trigonometri|trigonometri]] [[20240616T1007-likning|Likninger]]

# trigonometriske likninger

## Sinus

Ønsker å løse likningen $\sin u = b$. Vet at for alle vinkler $u$, vil supplementvinkelen $180 - u$ ha samme verdi av sinus. Det vil også være uendelig mange løsninger på formen $360 \degree \cdot a + u$, der $a \in \mathbb{Z}$. Noen ganger skal man finne løsninger til likningen i første omløp. Det vil si at $\angle u \in \left[ 0 \degree, 360 \degree \right\rangle$, altså at $\angle u \in \left[ 0, 2 \pi \right\rangle$ i radianer.

> [!NOTE] Eksempel 7
> Finn løsningene av likningen $\sin v = \frac{\sqrt{3}}{2}$ for vinkler mellom $0 \degree$ og $360 \degree$.

Vet at $\sin 60 \degree = \frac{\sqrt{3}}{2}$, og dermed er $v = 60 \degree$ en løsning. Supplementvinkelen har samme sinusverdi:

$$
\begin{align}
  180 \degree - 60 \degree &= 120 \degree & \\
  L &= \left\{ 60 \degree, 120 \degree \right\} & \\
  v = 60 \degree &\lor v = 120 \degree &
\end{align}
$$

Kan også løse dette grafisk ved å finne skjæringen mellom `Sirkel((0, 0), 1)` og $y = \frac{\sqrt{3}}{2}$ med GeoGebra.

Kan løse i CAS med $\text{Løs} \left( \left\{ \sin \left( v \degree \right) = \frac{\sqrt{3}}{2}, v \geq 0, v < 360 \right\} \right)$. For å få svaret i radianer, kan man i stedet bruke $\text{Løs} \left( \left\{ \sin \left( v \right) = \frac{\sqrt{3}}{2}, v \geq 0, v < 2\pi \right\} \right)$.

Altså har vi den generelle løsningen

$$
\begin{align}
  u &= \begin{cases}\begin{aligned}
    & u_{0} + n \cdot 360 \\
    180 \degree - & u_{0} + n \cdot 360 \degree
  \end{aligned}\end{cases} &
\end{align}
$$

, eller for radianer:

$$
\begin{align}
  u &= \begin{cases}\begin{aligned}
    & u_{0} + n \cdot 2 \pi \\
    \pi - & u_{0} + n \cdot 2 \pi
  \end{aligned}\end{cases} &
\end{align}
$$

, der $n \in \mathbb{Z}$. Hvis man får oppgitt et intervall som løsningene skal ligge i, setter man inn ulike verdier av $n$ slik at vi finner alle løsningene i intervallet.

> [!NOTE] Eksempel 8
> Vi har gitt likningen $\sin v = \frac{1}{2}$.
>
> 1. Finn den generelle løsningen av likningen
> 2. Finn løsningene når $v \in \left[ 0, 4 \pi \right\rangle$

1. Ettersom $\sin \frac{\pi}{6} = \frac{1}{2}$, er løsningene i første omløp:

$$
v = \frac{\pi}{6} \lor v = \pi - \frac{\pi}{6} = \frac{5\pi}{6}
$$

Man får flere løsninger for hvert omløp. Den generelle løsningen er

$$
v = \frac{\pi}{6} + n \cdot 2 \pi \lor v = \frac{5 \pi}{6} + n \cdot 2 \pi, n \in \mathbb{Z}
$$

2. Setter inn verdier av $n$ som gir resultater i første og andre omløp:

$$
\begin{align}
  n = 0 &\implies v = \frac{\pi}{6} + 0 \cdot 2 \pi &= \frac{\pi}{6} \\
  n = 1 &\implies v = \frac{\pi}{6} + 1 \cdot 2 \pi &= \frac{13\pi}{6}
\end{align}
$$

$$
\begin{align}
  n = 0 &\implies v = \frac{5\pi}{6} + 0 \cdot 2 \pi &= \frac{5\pi}{6} \\
  n = 1 &\implies v = \frac{5\pi}{6} + 1 \cdot 2 \pi &= \frac{17\pi}{6}
\end{align}
$$

Løsningene blir

$$
v = \frac{\pi}{6} \lor v = \frac{5\pi}{6} \lor v = \frac{13\pi}{6} \lor v = \frac{17\pi}{6}
$$

## Cosinus

Har gitt likningen $\cos{u} = a$. Vet at generelt er $\cos{u} = \cos{-u}$. Har dermed fra samme logikk som sinus at

$$
\begin{align}
  u &= \begin{cases}\begin{aligned}
    & u_{0} + n \cdot 360 \\
    - & u_{0} + n \cdot 360 \degree
  \end{aligned}\end{cases} &
\end{align}
$$

, eller for radianer:

$$
\begin{align}
  u &= \begin{cases}\begin{aligned}
    & u_{0} + n \cdot 2 \pi \\
    - & u_{0} + n \cdot 2 \pi
  \end{aligned}\end{cases} &
\end{align}
$$

, der $n \in \mathbb{Z}$

> [!NOTE] Eksempel 9
> Løs likningen:
>
> $$
> 2 \cos{v} - \sqrt{2} = 0, v \in \left[ 0 \degree, 360 \degree \right\rangle
> $$

$$
\begin{align}
  2 \cos{v} - \sqrt{2} &= 0 & \\
  2 \cos{v} &= \sqrt{2} & \\
  \cos{v} &= \frac{\sqrt{2}}{2} &
\end{align}
$$

Vet at $\cos{45 \degree} = \frac{\sqrt{2}}{2}$, og får den generelle løsningen

$$
v = 45 \degree + n \cdot 360 \degree \lor v = -45 \degree + n \cdot 360 \degree
$$

Setter inn verdier av $n$ for å finne vinklene.

> [!NOTE]
> Merk at med enkle likninger som dette, vil $n$ tilsvare ett omløp, men hvis man for eksempel har $\cos{2v}$, vil man måtte prøve flere verdier av $n$.

$$
\begin{align}
  n=0 &\implies v = 45 \degree + 0 \cdot 360 \degree = 45 \degree & \\
  n=1 &\implies v = 45 \degree + 1 \cdot 360 \degree = 405 \degree &
\end{align}
$$

$$
\begin{align}
  n=0 &\implies v = -45 \degree + 0 \cdot 360 \degree = -45 \degree & \\
  n=1 &\implies v = -45 \degree + 1 \cdot 360 \degree = 315 \degree &
\end{align}
$$

Løsningene i intervallet $\left[ 0 \degree, 360 \degree \right\rangle$ er $v = 45 \degree \lor v = 315 \degree$.

## Tangens

Gjøres på samme måte som de andre. Hvis man har en løsning for tangens i første kvadrant, vil man også ha en løsning i tredje kvadrant ($\pi + u$). Dette er på grunn av definisjonen $\displaystyle \frac{\sin{u}}{\cos{u}}$.

Tangens kan også defineres som $\displaystyle \frac{\text{motstående}}{\text{hosliggende}}$ i trekanter. Hvis vi da lager en trekant slik at den hosliggende kateten er lik $1$, kan vi lese av $\tan{u}$ som $y$-koordinaten:

![[20250821T1057-trigonometriske-likninger 2025-08-28 10.42.12.excalidraw.svg]]

Noen ganger kan andre likninger skrives om til tangenslikninger:

$$
\begin{align}
  \sin{u} + \cos{u} &= 0 & \\
  \frac{\sin{u}}{\cos{u}} &= \frac{- \cos{u}}{\cos{u}} & \\
  \tan{u} &= -1 &
\end{align}
$$

Man trenger kun én generell løsning med $+ 180 \degree \cdot n$ (eller $+ pi \cdot n$), i stedet for to slik som med $\sin$ og $\cos$:

$$
\begin{align}
  \tan{u} &= 1 & \\
  u &= \tan^{-1}{\left( 1 \right)} & \\
  u &= 45 \degree + 180 \degree \cdot n & \\
  &= \frac{\pi}{4} + \pi \cdot n &
\end{align}
$$

## Andre uttrykk inne i funksjonen

(merk at mengden $\left[ 0, 4 \right]$ er oppgitt i radianer, selv om det ikke inneholder $\pi$)

$$
\begin{align}
  \sin{\left( \pi x \right)} &= \frac{1}{2}, x \in \left[ 0, 4 \right] & \\
  \pi x &= \sin^{-1}{\frac{1}{2}} & \\
  \pi x = \frac{\pi}{6} + 2 \pi \cdot n &\lor \pi x = \frac{5\pi}{6} + 2 \pi \cdot n & \\
  x = \frac{1}{6 + 2n} &\lor x = \frac{5}{6 + 2n} &
\end{align}
$$

## Sammensatte likninger

$$
\begin{align}
  \sin^{2}{x} - \frac{3}{2} \sin{x} - 1 &= 0 & \\
  z &= \sin{x} & \\
  z^{2} - \frac{3}{2} z - 1 &= 0 & \\
  \left( z - 2 \right) \left( z + \frac{1}{2} \right) &= 0 & \\
  \sin{x} &= 2 & \text{sin kan ikke være > 1} \\
  \sin{x} &= - \frac{1}{2} & \\
  x = 210 \degree &\lor x = 330 \degree & \text{(innenfor første omløp)}
\end{align}
$$

---

"Veien om tangens". Forutsetter at både $\sin{}$ og $\cos{}$ er med samme vinkel.

$$
\begin{align}
  \sqrt{3} \sin{\left( 2x \right)} + 3 \cos{\left( 2x \right)} &= 0 & \\
  \sin{\left( 2x \right)} &= - \frac{3}{\sqrt{3}} \cos{\left( 2x \right)} & \\
  \frac{\sin{\left( 2x \right)}}{\cos{\left( 2x \right)}} &= - \frac{3}{\sqrt{3}} \frac{\cos{\left( 2x \right)}}{\cos{\left( 2x \right)}} & \\
  \tan{\left( 2x \right)} &= - \frac{3}{\sqrt{3}} = - \sqrt{3} & \\
  2x &= - \frac{\pi}{3} + \pi \cdot n & \\
  x &= - \frac{\pi}{6} + \frac{\pi}{2} \cdot n &
\end{align}
$$

---

Bruker [[20250902T1113-enhetsformelen|enhetsformelen]]

$$
\begin{align}
  3 \sin^{2}{x} - 5 \sin{x} \cos{x} + 6 \cos^{2}{x} &= 2 & \\
  3 \sin^{2}{x} - 5 \sin{x} \cos{x} + 6 \cos^{2}{x} &= 2 \sin^{2}{x} + 2\cos^{2}{x} & \\
  \sin^{2}{x} - 5 \sin{x} \cos{x} + 4 \cos^{2}{x} &= 0 & \\
  \frac{\sin^{2}{x}}{\cos^{2}{x}} - \frac{5\sin{x}\cos{x}}{\cos^{2}{x}} + \frac{4\cos^{2}{x}}{\cos^{2}{x}} &= 0 & \\
  \tan^{2}{x} - 5\tan{x} + 4 &= 0 &
\end{align}
$$

---

Ulike vinkler? Kan bruke [[20250904T1054-sum-og-differanse-av-vinkler|sum og differanse av vinkler]] og så [[20250902T1113-enhetsformelen|enhetsformelen]]. Man kan ikke bruke veien om tangens med to ulike vinkler.

$$
\begin{align}
  \sin{\left( x \right)} - \cos{\left( 2x \right)} &= 0 & \\
  \sin{\left( x \right)} - \cos{\left( x + x \right)} &= 0 & \\
  \sin{\left( x \right)} - \left( \cos{x} \cdot \cos{x} - \sin{x} \cdot \sin{x} \right) &= 0 & \\
  \sin{\left( x \right)} - \cos^{2}{x} + \sin^{2}{x} &= 0 & \\
  \sin{x} - \left( 1 - \sin^{2}{x} \right) + \sin^{2}{x} &= 0 & \\
  2\sin^{2}{x} + \sin{x} - 1 &= 0 &
\end{align}
$$

# Oppgaver (s. 32)

## 1.19

Løs likningene når du får vite at vinklene ligger i første omløp. Oppgi svaret i grader.

**a**

$$
\begin{align}
  \sin{u} &= \frac{\sqrt{2}}{2} & \\
  u &= \sin^{-1} \left( \frac{\sqrt{2}}{2} \right) & \leftarrow \text{denne linjen er ikke nødvendig for enkle uttrykk} \\
  u = \frac{\pi}{4} + 2 \pi \cdot n &\lor u = \frac{3 \pi}{4} + 2 \pi \cdot n & \\
  u < 2 \pi \implies & \underline{\underline{u = \frac{\pi}{4} \lor u = \frac{3 \pi}{4}}} & \text{oops jeg glemte i grader}
\end{align}
$$

**b**

$$
\begin{align}
  \sin{u} &= - \frac{1}{2} & \\
  u &= \sin^{-1} \left( \frac{1}{2} \right) & \\
  u = 210 \degree + 360 \degree \cdot n &\lor u = 330 \degree + 360 \degree \cdot n & \\
  u < 360 \degree \implies & \underline{\underline{u = 210 \degree \lor u = 330 \degree}} &
\end{align}
$$

**c**

$$
\begin{align}
  \sin{u} &= 1 & \\
  u &= 90 \degree + 360 \degree \cdot n & \\
  u < 360 \degree \implies & \underline{\underline{u = 90 \degree}} &
\end{align}
$$

## 1.20

Løs likningene:

**a**

$$
\begin{align}
  2 \sin{v} + \sqrt{2} &= 0, v \in \left[ 0, 2 \pi \right\rangle & \\
  \sin{v} &= - \frac{\sqrt{2}}{2} & \\
  v = \frac{5\pi}{4} + 2\pi \cdot n &\lor v = \frac{7\pi}{4} + 2\pi \cdot n & \\
  v \in \left[ 0, 2\pi \right\rangle \implies & v = \frac{5\pi}{4} \lor v = \frac{7\pi}{4} &
\end{align}
$$

**b**

$$
\begin{align}
  \sin{v} &= - \frac{\sqrt{3}}{2}, v \in \left[ 0 \degree, 360 \degree \right\rangle & \\
  v = 150 \degree + 360 \degree \cdot n &\lor v = 300 \degree + 360 \degree \cdot n & \\
  v \in \left[ 0 \degree, 360 \degree \right\rangle \implies & \underline{\underline{v = 150 \degree \lor v = 300 \degree}} &
\end{align}
$$

**c**

$$
\begin{align}
  3 \sin{v} + 3 &= 0, v \in \left[ 0, 2 \pi \right\rangle & \\
  \sin{v} &= 1 & \\
  v &= \frac{\pi}{2} + 2\pi \cdot n & \\
  v \in \left[ 0, 2 \pi \right\rangle \implies & \underline{\underline{v = \frac{\pi}{2}}} &
\end{align}
$$

## 1.21

**a**

Grafisk: Bruker GeoGebra. Tegner opp en enhetssirkel (`Sirkel((0, 0), 1)`) og finner skjæringspunkter mellom $y=0.32$ og sirkelen. Finner deretter vinkelen med vinkel-verktøyet. Merk at resultatet blir i grader og må konverteres hvis svaret skal være i radianer. Dette kan gjøres globalt under "Algebra"-seksjonen i innstillinger.
CAS: Løser likningssettet `sin(u)=0.32` og `u<2pi`

**b**

Grafisk: samme som forrige
CAS: Samme som forrige, men konverterer til grader med å dele på `°` (alt+o)

**c**

Grafisk: samme som forrige. Merk at vinkelen skal måles slik at man velger punktene mot klokken.
CAS: Samme som første

**d**

Grafisk: Ser at $3 \sin{u} = \frac{7}{2} \implies \sin{u} = \frac{7}{6}$. Vet at dette ikke vil gi noe gyldig svar, da verdien av $\sin{u}$ må være $\leq 1$. Hvis jeg fortsetter med å prøve å tegne en linje og finne skjæringspunkter, ser jeg at det ikke finnes noen løsning.
CAS: Får ingen løsninger med `Løs({$1, $2})`

## 1.22

Tabellen viser tilnærmingsverdier for sinus til noen utvalgte vinkler. Vi bruker av $\pi \approx 3.14$.

| $v$ (i grader) | $v$ (i radianer) | $\sin{v}$ |
| -------------- | ---------------- | --------- |
| $40 \degree$   | $0.70$           | $0.64$    |
| $53 \degree$   | $0.93$           | $0.80$    |
| $74 \degree$   | $1.29$           | $0.96$    |

**a**

$$
\begin{align}
  \sin{v} &= 0.8, v \in \left[ 0 \degree, 360 \degree \right\rangle & \\
  v = 53 \degree &\lor v = 127 \degree &
\end{align}
$$

**b**

$$
\begin{align}
  \sin{v} &= 0.64, v \in \left[ 0 \degree, 360 \degree \right\rangle & \\
  v = 40 \degree &\lor v = 140 \degree &
\end{align}
$$

**c**

$$
\begin{align}
  \sin{v} &= 0.96, v \in \left[ 0 \degree, 720 \degree \right\rangle & \\
  v = 74 \degree \lor v = 106 \degree &\lor v = 434 \degree \lor v = 466 &
\end{align}
$$

**d**

$$
\begin{align}
  \sin{v} &= 0.8, v \in \left[ 0, 2 \pi \right\rangle & \\
  v = 0.93 &\lor v = 2.21 &
\end{align}
$$

**e**

$$
\begin{align}
  \sin{v} &= 0.64, v \in \left[ -2 \pi, 0 \right\rangle & \\
  v = -5.58 &\lor v = -3.84 &
\end{align}
$$

**f**

$$
\begin{align}
  \sin{v} &= 0.96, v \in \left[ 0, 2\pi \right] & \\
  v = 1.29 &\lor v = 1.85 &
\end{align}
$$

## 1.23

Løs likningene

**a**

$$
\begin{align}
  \cos{u} &= \frac{\sqrt{3}}{2} & \\
  u = \frac{\pi}{6} + 2\pi \cdot n &\lor u = \frac{11\pi}{6} + 2\pi \cdot n & \\
  v \in \left[ 0, 2\pi \right] \implies &u = \frac{\pi}{6} \lor u = \frac{11\pi}{6} &
\end{align}
$$

**b**

$$
\begin{align}
  \sqrt{2} \cos{u} + 2 &= 1, u \in \left[ 0 \degree, 360 \degree \right\rangle & \\
  \cos{u} &= - \frac{\sqrt{2}}{2} & \\
  u = 225 \degree &\lor u = 135 \degree &
\end{align}
$$

**c**

$$
\begin{align}
  2 \cos{u} - 1 &= 0, u \in \left[ 0, 2 \pi \right\rangle & \\
  \cos{u} &= \frac{1}{2} & \\
  u = \frac{\pi}{3} &\lor u = \frac{5\pi}{3} &
\end{align}
$$

## 1.27

Vi har gitt likningen $\tan{v}=1$. Løs likningen når

**a**

$v \in \mathbb{R}$

$$
\begin{align}
  \tan{v} &= 1 & \\
  v &= \tan^{-1}{v} & \\
  v &= \frac{\pi}{4} + \pi \cdot n = 45 \degree + 180 \degree \cdot n &
\end{align}
$$

**b**

$v \in \left[ 0 \degree, 360 \degree \right\rangle$

Bruker verdiene av $n$ der resultatet blir $< 360 \degree$:

$$
v = 45 \degree \lor v = 225 \degree
$$

**c**

$v \in \left[ 0, 2 \pi \right\rangle$

Samme som forrige, men i radianer.

$$
v = \frac{\pi}{4} \lor v = \frac{5 \pi}{4}
$$

## 1.28

Løs likningene

**a**

$$
\begin{align}
  3 \tan{v} &= \sqrt{3}, v \in \left[ 0 \degree, 360 \degree \right\rangle & \\
  \tan{v} &= \frac{\sqrt{3}}{3} = \frac{1}{\sqrt{3}} & \\
  v &= 30 \degree + 180 \degree \cdot n & \\
  v &= 30 \degree \lor v = 210 \degree &
\end{align}
$$

**b**

$$
\begin{align}
  \sqrt{3} \tan{v} &= -3, v \in \left[ - \pi, \pi \right\rangle & \\
  \tan{v} &= - \frac{\sqrt{3}}{3} = - \sqrt{3} & \\
  v &= \frac{2\pi}{3} + \pi \cdot n, n \in \mathbb{Z} & \leftarrow \text{den siste delen der er ikke egentlig nødvendig} \\
  v &= \frac{-\pi}{3} \lor v = \frac{2\pi}{3} &
\end{align}
$$

**c**

$$
\begin{align}
  \tan{v} &= 0, v \in \left[ -180 \degree, 180 \degree \right\rangle & \\
  v &= 0 \degree + 180 \degree \cdot n & \\
  v &= -180 \degree \lor v = 0 \degree &
\end{align}
$$

## 1.29

**a**

$$
\begin{align}
  \tan{v} &= 0.5, v \in \left[ 0, 2\pi \right\rangle & \\
  v &= \tan^{-1}{\left( 0.5 \right)} \approx 0.463 + \pi \cdot n & \\
  v &\approx 0.463 \lor v \approx 3.605 &
\end{align}
$$

**b**

$$
\begin{align}
  3 \tan{v} &= -2, v \in \left[ 0 \degree, 360 \degree \right] & \\
  \tan{v} &= - \frac{2}{3} & \\
  v &\approx 33.69 \degree + 180 \degree \cdot n & \\
  v &\approx 33.69 \degree \lor v \approx 213.69 &
\end{align}
$$

**c**

$$
\begin{align}
  5 \tan{v} &= 7, v \in \left[ - \pi, \pi \right\rangle & \\
  \tan{v} &= \frac{7}{5} & \\
  v &\approx 0.95 + \pi \cdot n & \\
  v &\approx -2.19 \lor v \approx 0.95 &
\end{align}
$$

**d**

$$
\begin{align}
  \tan{v} &= 0.36, v \in \left[ -180 \degree, 180 \degree \right\rangle & \\
  v &\approx 19.79 \degree + 180 \degree \cdot n & \\
  v &\approx -160.21 \degree \lor v \approx 19.79 \degree &
\end{align}
$$

## 1.98

Vi har gitt likningen $\tan{v} = -1$. Løs likningen når

**a**

$v \in \mathbb{R}$

$$
\begin{align}
  \tan{v} &= -1 & \\
  v &= \frac{3\pi}{4} + \pi \cdot n &
\end{align}
$$

**b**

$v \in \left[ 0 \degree, 360 \degree \right\rangle$

$$
\begin{align}
  v &= 135 \degree + 180 \degree \cdot n & \\
  v &= 135 \degree \lor v = 315 \degree &
\end{align}
$$

**c**

$v \in \left[ 0, 2 \pi \right\rangle$

$$
\begin{align}
  v &= \frac{3\pi}{4} + \pi \cdot n & \\
  v &= \frac{3\pi}{4} \lor v = \frac{7\pi}{4} &
\end{align}
$$

## 1.99

Løs likningene:

**a**

$$
\begin{align}
  \tan{v} &= \frac{\sqrt{3}}{3}, v \in \left[ 0, 2\pi \right\rangle & \\
  \tan{v} &= \frac{1}{\sqrt{3}} & \\
  v &= \frac{\pi}{6} + \pi \cdot n & \\
  v &= \frac{\pi}{6} \lor v = \frac{7\pi}{6} &
\end{align}
$$

**b**

$$
\begin{align}
  \sqrt{3} \tan{v} - 3 &= 0, v \in \left[ -360 \degree, 0 \degree \right\rangle & \\
  \tan{v} &= \frac{3}{\sqrt{3}} = \sqrt{3} & \\
  v &= 60 \degree + 180 \degree \cdot n & \\
  v &= -300 \degree \lor v = -120 \degree &
\end{align}
$$

## 1.100

Løs likningene:

**a**

$$
\begin{align}
  3 \sin{\left( 2x \right)} &= 2, x \in \left[ -\pi, \pi \right\rangle & \\
  \sin{\left( 2x \right)} &= \frac{2}{3} & \\
  2x &= \sin^{-1}{\frac{2}{3}} & \\
  2x \approx 0.7 + \pi \cdot n &\lor 2x \approx 2.4 + \pi \cdot n & \\
  x \approx 0.35 + \frac{\pi}{2} \cdot n &\lor x \approx 1.2 + \frac{\pi}{2} \cdot n & \\
  x \approx -2.79 \lor x \approx -1.22 &\lor x \approx 0.35 \lor x \approx 1.92 &
  % 2x &\approx 41.8 \degree + 360 \degree \cdot n \lor 2x \approx 138.2 \degree + 360 \degree \cdot n & \\
  % x &\approx 20.9 \degree + 180 \degree \cdot n \lor x \approx 69.1 \degree + 180 \degree \cdot n & \\
\end{align}
$$

**b**

$$
\begin{align}
  2 \cos{x} - 1 &= \frac{1}{4}, x \in \left[ 0 \degree, 360 \degree \right\rangle & \\
  \cos{x} &= \frac{5}{8} & \\
  x \approx 51.3 \degree + 360 \degree \cdot n &\lor x \approx 308.7 \degree + 360 \degree \cdot n & \\
  x \approx 51.3 &\lor x \approx 308.7 &
\end{align}
$$

**c**

$$
\begin{align}
  \tan{x} &= 3.47, x \in \left[ 0, 2 \pi \right\rangle & \\
  x &\approx 1.29 + \pi \cdot n & \\
  x &\approx 1.29 \lor x \approx 4.43 &
\end{align}
$$

## 1.101

Finn en generell løsning av likningene:

**a**

$$
\begin{align}
  2 \sin{\left( \frac{\pi}{8}x \right)} &= \sqrt{3} & \\
  \sin{\left( \frac{\pi}{8}x \right)} &= \frac{\sqrt{3}}{2} & \\
  \frac{\pi}{8}x = \frac{\pi}{3} + 2\pi \cdot n &\lor \frac{\pi}{8}x = \frac{2\pi}{3} + 2\pi \cdot n & \\
  \pi x = \frac{8\pi}{3} + 16\pi \cdot n &\lor \pi x = \frac{16\pi}{3} + 16\pi \cdot n & \\
  x = \frac{8}{3} + 16n &\lor x = \frac{16}{3} + 16n &
\end{align}
$$

**b**

$$
\begin{align}
  \cos{\left( 2x + \frac{\pi}{3} \right)} &= \frac{\sqrt{2}}{2} & \\
  2x + \frac{\pi}{3} = \frac{\pi}{4} + 2\pi \cdot n &\lor 2x + \frac{\pi}{3} = \frac{7\pi}{4} + 2\pi \cdot n & \\
  2x + \frac{4\pi}{12} = \frac{3\pi}{12} + 2\pi \cdot n &\lor 2x + \frac{4\pi}{12} = \frac{21\pi}{12} + 2\pi \cdot n & \\
  2x = - \frac{\pi}{12} + 2\pi \cdot n &\lor 2x = \frac{17\pi}{12} + 2\pi \cdot n & \\
  x = - \frac{\pi}{24} + \pi \cdot n &\lor x = \frac{17\pi}{24} + \pi \cdot n &
\end{align}
$$

**c**

$$
\begin{align}
  \sin{\left( 3x - \frac{\pi}{4} \right)} &= - \frac{1}{2} & \\
  3x - \frac{\pi}{4} &= \sin^{-1}{\left( - \frac{1}{2} \right)} & \\
  3x - \frac{\pi}{4} &= -\sin^{-1}{\left( \frac{1}{2} \right)} & \\
  3x - \frac{\pi}{4} = - \frac{\pi}{6} + 2\pi \cdot n &\lor 3x - \frac{\pi}{4} = - \frac{5\pi}{6} + 2\pi \cdot n & \\
  3x - \frac{3\pi}{12} = - \frac{2\pi}{12} + 2\pi \cdot n &\lor 3x - \frac{3\pi}{12} = - \frac{10\pi}{12} + 2\pi \cdot n & \\
  3x = \frac{\pi}{12} + 2\pi \cdot n &\lor 3x = - \frac{7\pi}{12} + 2\pi \cdot n & \\
  x = \frac{\pi}{36} + \frac{2}{3} \pi \cdot n &\lor x = - \frac{7\pi}{36} + \frac{2}{3} \pi \cdot n &
\end{align}
$$

## 1.102

Hvor mange løsninger kan likningen under maksimalt ha?

$$
\tan{\left( 3u + \frac{\pi}{6} \right)} = 0.6, u \in \left[ 0, 20\pi \right\rangle
$$

$2\pi$ tilsvarer ett omløp, altså er $20\pi$ lik $10$ omløp. En likning på formen $\tan{x} = y$ kan ha to løsninger i hvert omløp. Her er $u$ multiplisert med $3$, så det finnes tre ganger så mange løsninger.

$$
10 \cdot 2 \cdot 3 = 60
$$

Likningen kan maksimalt ha $60$ løsninger.
