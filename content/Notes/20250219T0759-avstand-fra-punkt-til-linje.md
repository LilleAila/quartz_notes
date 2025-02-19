---
id: 20250219T0759-avstand-fra-punkt-til-linje
aliases:
  - avstand fra punkt til linje
tags: []
date: "2025-02-19"
title: avstand fra punkt til linje
---

#matte [[20250115T0716-vektorer|vektorer]]

# avstand fra punkt til linje

Avstanden fra punkt $P$ til en linje $m$ er definert som den korteste avstanden fra $P$ til $m$. Denne avstanden måles langs normalen fra $P$ ned på $m$.

## Eksempel 24 (fra boken)

> [!NOTE]
> En linje $m$ går gjennom punktene $A \left( 1, -1 \right)$ og $B \left( 4, 8 \right)$. Finn avstanden fra punktet $P \left( 6, 4 \right)$ til linjen $m$.

![[20250219T0759-avstand-fra-punkt-til-linje 2025-02-19 09.02.06.excalidraw]]

Vet at vinkelen mellom $PQ$ og $AB$ er $90\degree$, altså er vektorene ortogonale og $\vec{PQ} \perp \vec{AB}$
Vet også at punktet $Q$ ligger på linjen m, altså er $\vec{AQ} \parallel \vec{AB}$, så man kan gange det med en konstant for å få $\vec{AB}$
Også er $\vec{PQ} = \vec{PA} + \vec{AQ}$

$$
\begin{align}
  \vec{PA} &= \left[ 1 - 6, -1 - 4 \right] = \left[ -5, -5 \right] & \\
  \vec{AB} &= \left[ 4 - 1, 8 - \left( -1 \right) \right] = \left[ 3, 9 \right] &
\end{align}
$$

Vet ut fra skissen at $k < 1$.

$$
\begin{align}
  \vec{PQ} &= \vec{PA} + \vec{AQ} & \\
  \vec{PQ} &= \vec{PA} + k \cdot \vec{AB} & \\
  \vec{PQ} \cdot \vec{AB} &= 0 & \\
  \left( \vec{PA} + k \cdot \vec{AB} \right) \cdot \vec{AB} &= 0 & \\
  \vec{PA} \cdot \vec{AB} + k \cdot \vec{AB}^{2} &= 0 & \\
  \left[ -5, -5 \right] \cdot \left[ 3, 9 \right] + k \cdot \left[ 3, 9 \right]^{2} &= 0 & \\
  -5 \cdot 3 - 5 \cdot 9 + k \cdot 3^{2} + 9^{2} &= 0 & \\
  -15 - 45 + 90k &= 0 & \\
  k &= \frac{2}{3} &
\end{align}
$$

$$
\begin{align}
  \vec{PQ} &= \vec{PA} + k \cdot \vec{AB} & \\
  &= \left[ -5, -5 \right] + \frac{2}{3} \cdot \left[ 3, 9 \right] & \\
  &= \left[ -5, -5 \right] + \left[ 2, 6 \right] & \\
  &= \left[ -3, 1 \right] & \\
  \left| \vec{PQ} \right| &= \sqrt{\left( -3 \right)^{2} + 1^{2}} & \\
  &= \sqrt{10} &
\end{align}
$$

Avstanden fra $P$ til $m$ er $\sqrt{10}$.

> [!NOTE]
> I GeoGebra kan man bruke funksjonen `Avstand( <Punkt>, <Objekt> )`.

### Oppgaver

#### 6.92

##### a

Finn avstanden mellom punktet $P \left( 2, 6 \right)$ og linjen $m$ gjennom $A \left( 1, 1 \right)$ og $B \left( 7, 5 \right)$.

![[20250219T0759-avstand-fra-punkt-til-linje 2025-02-19 09.29.20.excalidraw]]

$$
\begin{align}
  \vec{PA} &= \left[ 1-2, 1-6 \right] = \left[ -1, -5 \right] & \\
  \vec{AB} &= \left[ 7-1, 5-1 \right] = \left[ 6, 4 \right] & \\
  \vec{PQ} &= \vec{PA} + \vec{AQ} = \vec{PA} + k \cdot \vec{AB} &
\end{align}
$$

$$
\begin{align}
  \vec{PQ} \cdot \vec{AB} &= 0 & \\
  \left( \vec{PA} + k \cdot \vec{AB} \right) \cdot \vec{AB} &= 0 & \\
  \vec{PA} \cdot \vec{AB} + k \cdot \vec{AB}^{2} &= 0 & \\
  \left[ -1, -5 \right] \cdot \left[ 6, 4 \right] + k \cdot \left[ 6, 4 \right]^{2} &= 0 & \\
  -6 - 20 + k \cdot \left( 36 + 16 \right) &= 0 & \\
  52k &= 26 & \\
  k &= \frac{1}{2} &
\end{align}
$$

$$
\begin{align}
  \vec{PQ} &= \vec{PA} + \frac{1}{2} \vec{AB} & \\
  &= \left[ -1, -5 \right] + \frac{1}{2} \left[ 6, 4 \right] & \\
  &= \left[ -1, -5 \right] + \left[ 3, 2 \right] & \\
  &= \left[ 2, -3 \right] & \\
  \left| \vec{PQ} \right| &= \sqrt{2^{3} + \left( -3 \right)^{3}} = \sqrt{13} &
\end{align}
$$

> [!NOTE]
> Samsvarer ikke med skissen, men svaret ser rett ut (likt som fasit)

### 6.96

> Mellom $A$ og $B$ går det en rett vei. Fra $C$ skal kommunen lage en ny vei som gir forbindelse med veien $AB$. Koordinatene til punktene er gitt ved $A \left( 1, 2 \right)$, $B \left( 4, 8 \right)$, $C \left( 5, 4 \right)$.
> Alle lengdemål er i kilometer.
> Hvor må den nye veien treffe $AB$ for at den skal bli kortest mulig?

Jeg vil altså finne koordinatene til punktet $Q$, der $Q$ er punktet slik at $\left| \vec{CQ} \right|$ er lavest mulig.

$$
\begin{align}
  \vec{CA} &= \left[ 1 - 5, 2 - 4 \right] = \left[ -4, -3 \right] & \\
  \vec{AB} &= \left[ 4 - 1, 8 - 2 \right] = \left[ 3, 6 \right] & \\
  \vec{AQ} &= k \cdot \vec{AB} & \\
  \vec{CQ} &= \vec{CA} + k \cdot \vec{AB} &
\end{align}
$$

$$
\begin{align}
  \vec{CQ} \cdot \vec{AB} &= 0 & \\
  \left( \vec{CA} + k \cdot \vec{AB} \right) \cdot \vec{AB} &= 0 & \\
  \vec{CA} \cdot \vec{AB} + k \cdot \vec{AB}^{2} &= 0 & \\
  \left[ -4, -3 \right] \cdot \left[ 3, 6 \right] + k \cdot \left[ 3, 6 \right]^{2} &= 0 & \\
  -12 - 18 + k \cdot \left( 9 + 36 \right) &= 0 & \\
  45k &= 30 & \\
  k &= \frac{30}{45} = \frac{2}{3} &
\end{align}
$$

$$
\begin{align}
  \vec{CQ} &= \vec{CA} + k \cdot \vec{AB} & \\
  &= \left[ -4, -3 \right] + \frac{2}{3} \left[ 3, 6 \right] & \\
  &= \left[ -4, -3 \right] + \left[ 2, 4 \right] & \\
  &= \left[ -2, 1 \right] &
\end{align}
$$

$$
\begin{align}
  \vec{OQ} &= \vec{OC} + \vec{CQ} & \\
  &= \left[ 5, 4 \right] + \left[ -2, 1 \right] & \\
  &= \left[ 3, 5 \right] & \\
  \implies Q &= \left( 3, 5 \right) &
\end{align}
$$

Den nye veien må treffe $AB$ i punktet $\left( 3, 5 \right)$.

(dette er feil. fasit siser $\displaystyle \left( \frac{13}{5}, \frac{26}{5} \right)$

## Areal av trekant fra punkter

> [!NOTE]
> Punktene $A \left( 1, -1 \right)$, $P \left( 6, 4 \right)$ og $B \left( 4, 8 \right)$ er hjørnene i trekanten $APB$. Bestem arealet av $\triangle APB$

$$
A = \frac{1}{2} gh
$$

![[20250219T0759-avstand-fra-punkt-til-linje 2025-02-19 10.01.12.excalidraw]]

$$
\begin{align}
  \vec{AB} &= \left[ 4 - 1, u - \left( - 1 \right) \right] = \left[ 3, 9 \right] & \\
  g &= \left| \vec{AB} \right| & \\
  &= \left| \left[ 3, 9 \right] \right| & \\
  &= \sqrt{3^{2} + 9^{2}} & \\
  &= \sqrt{90} &
\end{align}
$$

Avstand fra $P$ til linjen gjennom $AB$ fant jeg i eksempel 24.

$$
h = \sqrt{10}
$$

$$
\begin{align}
  A &= \frac{1}{2} g \cdot h & \\
  &= \frac{1}{2} \sqrt{90} \cdot \sqrt{10} & \\
  &= \frac{1}{2} \sqrt{900} & \\
  &= \frac{1}{2} \cdot 30 & \\
  &= \underline{\underline{15}} &
\end{align}
$$

Arealet til trekanten $\triangle APB$ er $15$.

> [!NOTE]
> Kan sjekke svaret med GeoGebra. Tegne opp punktene, bruk mangekant-verktøyet, og bruk areal-verktøyet eller funksjonen `Areal( <Mangekant> )`.
>
> Under eksamen vil man få full pott for å bruke CAS til denne oppgaven i stedet for vektorer med mindre noe annet er spesifisert.

### Arealsetningen

En trekant er definert ved to vektorer $\vec{u}$ og $\vec{v}$ som starter i samme punkt. Arealet er ifølge arealsetningen lik

$$
\frac{1}{2} \cdot \left| \vec{u} \right| \cdot \left| \vec{v} \right| \cdot \sin{\alpha}
$$

![[20250219T0759-avstand-fra-punkt-til-linje 2025-02-19 10.13.55.excalidraw]]

Sinus til en vinkel er lik cosinus til komplementærvinkelen (forklares i R2). Dermed får vi

$$
\frac{1}{2} \cdot \left| \vec{u} \right| \cdot \left| \vec{v_{\perp}} \right| \cdot \cos{90\degree - \alpha}
$$

Dette er det samme som skalarproduktet, altså kan vi skrive:

$$
\frac{1}{2} \cdot \vec{u} \cdot \vec{v_{{\perp}}}
$$

Fordi skalarproduktet kan bli negativt, må vi ta absoluttverdien til slutt.

> [!NOTE] Definisjon
> Vektorene $\vec{u}$ og $\vec{v}$ definerer en trekant. Arealet av trekanten er da
> $$
> T = \frac{1}{2} \cdot \left| \vec{u} \cdot \vec{v_{\perp}} \right|
> $$
> der $\vec{v_{\perp}}$ er en tverrvektor til $\vec{v}$.

## Thalessetningen

En sirkel med sentrum $S$ og $AB$ som diameter, der $P$ er et vilkårlig punkt på sirkelen som ikke sammenfaller med $A$ eller $B$. Vil bevise at trekanten er rettvinklet, altså at $\vec{PA} \perp \vec{PB}$, altså at $\vec{PA} \cdot \vec{PB} = 0$.

- [ ] TODO: excalidraw, bevise med vektorer
