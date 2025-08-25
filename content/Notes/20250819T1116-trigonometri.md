---
id: 20250819T1116-trigonometri
aliases:
  - trigonometri
tags: []
date: "2025-08-19"
title: trigonometri
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# trigonometri

![[20250819T1116-trigonometri 2025-08-19 11.19.13.excalidraw.svg]]

$$
\begin{align}
    \sin{u} &= \frac{\text{Motstående}}{\text{Hypotenus}} & \\
    \cos{u} &= \frac{\text{Hosliggende}}{\text{Hypotenus}} & \\
    \tan{u} &= \frac{\sin{u}}{\cos{u}} = \frac{\text{Motstående}}{\text{Hosliggende}} &
\end{align}
$$

## Viktige verdier

| $\angle u \degree$ | $\sin u$             | $\cos u$             | $\tan u$             |
| ------------------ | -------------------- | -------------------- | -------------------- |
| $0 \degree$        | $0$                  | $1$                  | $0$                  |
| $30 \degree$       | $\frac{1}{2}$        | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}}$ |
| $45 \degree$       | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$                  |
| $60 \degree$       | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$        | $\sqrt{3}$           |
| $90 \degree$       | $1$                  | $0$                  | udef                 |

> [!NOTE]
> Se s. 17 i læreboken

Huskeregel for $\sin$: $\frac{\sqrt{n}}{2}$ for $n$ i $\left\{ 0, 30, 45, 60, 90 \right\}$ der $n$ er indeks i listen fra $0$, altså $\left\{ 0, 1, 2, 3, 4 \right\}$.

Ut fra dette kan man også tenke seg frem til hva verdiene er for vinkler i de andre kvadrantene, ved hjelp av komplementær- og supplementærvinkler og reglene beskrevet under. Man bruker vanligvis $180 \degree$ som et referansepunkt og ser på differansen. Viktig å huske:

$$
\begin{align}
  \sin{\left( 180 \degree - u \right)} & = \sin u  & \\
  \cos{\left( 180 \degree - u \right)} & = -\cos u &
\end{align}
$$

## Enhetssirkelen

En sirkel med radius $1$. Dette betyr at en rettvinklet trekant i denne sirkelen vil alltid ha hypotenus med lengde $1$.

![[20250819T1116-trigonometri 2025-08-19 11.20.56.excalidraw.svg]]

En likning kan ha uendelig mange løsninger fordi verdiene av sin og cos vil være det samme med flere omdreininger. Med $-u$, vil $\cos$ være lik, og $\sin$ negativ.

$$
\begin{align}
  \cos{\left( -u \right)}& = \cos u & \\
  \sin{\left( -u \right)}& = - \sin u &
\end{align}
$$

Man kan gå i flere omløp rundt sirkelen. Hvis man ikke får en begrensning på området til x-verdien i en trigonometrisk likning, er det uendelig mange løsninger av å legge til eller trekke fra $360 \degree$ (eller $2\pi$). Med et normalt begrenset område til $x \in \left[ 0, 2\pi \right]$, vil man vanligvis ha to løsninger. Man vil finne samme løsning for $\sin$ i $180 \degree - u$, og for $\cos$ i $360 \degree - u$.

- I første kvadrant er $\sin$ og $\cos$ positiv. $\tan$ er positiv.
- I andre kvadrant er $\sin$ positiv og $\cos$ negativ. $\tan$ er negativ.
- I tredje kvadrant er $\sin$ og $\cos$ negativ. $\tan$ er positiv.
- I fjerde kvadrant er $\sin$ negativ og $\cos$ positiv. $\tan$ er negativ.

## Komplementvikler

Hvis $u+v = 90 \degree$, er vinklene komplementærvinkler.

![[20250819T1116-trigonometri 2025-08-19 11.32.02.excalidraw.svg]]

Oppfører seg som en [[20250108T0720-omvendte-funksjoner|omvendt funksjon]] hvis man tegner det som linjer.

$$
\begin{align}
  \cos {v} = \cos{\left( 90 \degree - u \right)} & = \sin{u} \\
  \sin {v} = \sin{\left( 90 \degree - u \right)} & = \cos{u} \\
\end{align}
$$

## Supplementvinkler

![[20250819T1116-trigonometri 2025-08-19 11.36.36.excalidraw.svg]]

En supplementvinkel er en vinkel slik at $u+v=180 \degree$

$$
\begin{align}
  \sin{u} &= \sin{v} & \\
  \cos{u} &= -\cos{u} &
\end{align}
$$

## Radianer

Grader gir lite mening og 360 er ikke basert på noe. Vi bruker heller $\pi$ som et mål på vinkler. Dette kalles radianer, og er basert på forholdet mellom $\pi$ og radius på en enhetssirkel. Det tilsvarer lengden på den delen av sirkelen som er innenfor vinkelen, altså blir $360 \degree = 2\pi$. Forholdet mellom buelengden og radius på sirkelen er absolutt vinkelmål.

$$
u = \frac{b}{r}
$$

Radianer er et enhetsløst tall uten enhet, da buelengden og radius måles i samme enhet. Derfor kalles dette absolutt vinkelmål. Radianer må ikke nødvendigvis inneholde $\pi$, men det er vanligvis det i eksakte løsninger. For å omgjøre til grader, erstatter man $\pi$ med $180 \degree$.

$$
\begin{align}
  0 \degree &= 0 & \\
  30 \degree &= \frac{\pi}{6} & \\
  45 \degree &= \frac{\pi}{4} & \\
  60 \degree &= \frac{\pi}{3} & \\
  90 \degree &= \frac{\pi}{2} & \\
  180 \degree &= \pi & \\
  360 \degree &= 2\pi &
\end{align}
$$

# Oppgaver (s. 60)

### 1.76

#### a.

$$
\begin{align}
  & \sin {30 \degree} \cdot \cos {30 \degree} + \cos{30 \degree} \cdot \sin{60 \degree} & \\
  & = \frac{1}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{3}}{2} & \\
  & = \frac{\sqrt{3}}{4} + \frac{3}{4} & \\
  & = \frac{3 + \sqrt{3}}{4} &
\end{align}
$$

#### b.

$$
\begin{align}
  & \cos {45 \degree} \cdot \cos {60 \degree} - \sin{45 \degree} \cdot \sin{60 \degree} & \\
  = & \frac{\sqrt{2}}{2} \cdot \frac{1}{2} - \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} & \\
  = & \frac{\sqrt{2}}{4} - \frac{\sqrt{6}}{4} & \\
  = & \frac{\sqrt{2} - \sqrt{6}}{4} &
\end{align}
$$

#### c.

$$
\begin{align}
  & \left( \cos{30 \degree} \right)^{2} + \left( \sin {30 \degree} \right)^{2} + \left( \tan {30 \degree} \right)^{2} & \\
  = & \left( \frac{\sqrt{3}}{2} \right)^{2} + \left( \frac{1}{2} \right)^{2} + \left( \frac{1}{\sqrt{3}} \right)^{2} & \\
  = & \frac{3}{4} + \frac{1}{4} + \frac{1}{3} & \\
  = & \frac{9}{12} + \frac{3}{12} + \frac{4}{12} & \\
  = & \frac{16}{12} & \\
  = & \frac{4}{3} &
\end{align}
$$

### 1.77

$$
\begin{align}
  \sin {139.46 \degree} & \approx 0.65  & \\
  \tan {59.39 \degree} & \approx \frac{0.65}{0.4} = 1.625 & \\
  \cos {315.57 \degree} & \approx 0.71 &
\end{align}
$$

### 1.78

$$
\begin{align}
  \cos {58 \degree} &= \sin{32 \degree} \approx 0.53 & \\
  \sin {58 \degree} &= \cos{32 \degree} \approx 0.848 & \\
  \sin {148 \degree} &= \sin{32 \degree} \approx 0.53 & \\
  \cos {148 \degree} &= -\cos{32 \degree} \approx -0.848 &
\end{align}
$$
