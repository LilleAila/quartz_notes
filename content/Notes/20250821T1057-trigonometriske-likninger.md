---
id: 20250821T1057-trigonometriske-likninger
aliases:
  - trigonometriske likninger
tags: []
date: "2025-08-21"
title: trigonometriske likninger
---
o
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
