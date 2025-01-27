---
id: 20250108T0720-omvendte-funksjoner
aliases:
  - omvendte funksjoner
tags: []
date: "2025-01-08"
title: Omvendte funksjoner
---

#matte [[20240616T1007-matte|matte]] [[20240616T1007-funksjon|funksjoner]]

# omvendte funksjoner

En funksjon er noe som tar inn et tall, og gir ut et tall, for eksempel:

$$
\begin{align}
    g \left( x \right) & = & \\
    1 & \to 1 & \\
    2 & \to 4 & \\
    3 & \to 9 & \\
    4 & \to 16 &
\end{align}
$$

Her blir $f \left( x \right) = x^{2}$

Den omvendte funksjonen blir da en funksjon slik at

$$
\begin{align}
    g \left( x \right) & = & \\
    1 & \to 1 & \\
    4 & \to 2 & \\
    9 & \to 3 & \\
    16 & \to 4 &
\end{align}
$$

, altså at man får innverdiene fra $f \left( x \right)$, når man tar utverdien inn i $g \left( x \right)$

Her blir $g \left( x \right) = \sqrt{x}$

Her flytter man seg mellom de to domenene. Dette kan representeres som grafer, der de to aksene er de to domenene.

Verdimengden fra den funksjonen blir definisjonsmengden til den omvendte funksjonen, og definisjonsmengden til funksjonen blir verdimengden til den omvendte funksjonen.

![20250108T0832-omvendte-funksjoner-definisjonsmengde-verdimengde.png](Assets/20250108T0832-omvendte-funksjoner-definisjonsmengde-verdimengde.png)

![[20250108T0720-omvendte-funksjoner 2025-01-08 09.33.14.excalidraw]]

Det er ikke alle funksjoner som har omvendte funksjoner:

![[20250108T0720-omvendte-funksjoner 2025-01-08 09.37.30.excalidraw]]

Hvis det er flere utverdier med samme verdi, er det ikke mulig å lage en omvendt funksjon, da dette fører til at en innverdi har flere utverdier. Altså må hver innverdi kun ha en funksjonsverdi, og hver funksjonsverdi må ha kun en innverdi. Dette kalles at funksjonen er "en-entydig".

> [!NOTE] DVS.
> $x_1 \neq x_2 \implies f \left( x_1 \right) \neq f \left( x_2 \right)$

Funksjonen må være en-entydig for at det skal være mulig å finne en omvendt funksjon. Hvis den ikke er det ,må ma velge å kun se på en del av funksjonen.

Hvis en funksjon er [[20241121T1132-monotoniegenskaper|strengt monoton]] (voksende / avtakende), betyr det at den er en-entydig.

## Eksempel

Oppskrift på sjokoladekake

3 egg gir 1 kake
6 egg gir 2 kaker
9 egg gir 3 kaker

Denne funksjonen tar egg som input, kaker som output

$$
f \left( x \right) = \frac{x}{3}
$$

Den omvendte funksjonen blir da hvor mange egg man trenger til en kake. Den tar kaker som input, og egg som output.

$$
f^{-1} \left( x \right) = 3x
$$

Dette leses som "**f invers**" (den omvendte funksjonen til f)

![[20250108T0720-omvendte-funksjoner 2025-01-08 08.31.20.excalidraw]]

Funksjonene er speilvendt rundt $y = x$

![20250108T0745-omvendte-funksjoner-speilvendt-geogebra.png](Assets/20250108T0745-omvendte-funksjoner-speilvendt-geogebra.png)

### "Bevis at $f$ og $g$ er omvendte funksjoner"

$$
f \left( x \right) = \frac{x}{3} \land g \left( x \right) = 3x
$$

Har at

$$
f \left( g \left( x \right) \right) = \frac{3x}{3} = x
$$

Og

$$
g \left( f \left( x \right) \right) = 3 \cdot \frac{x}{3} = x
$$

Derfor er $f$ og $g$ omvendte funksjoner.

> To funksjoner $f$ og $g$ er omvendt av hverandre hvis
> $f \left( g \left( x \right) \right) = x$ for alle $x \in D_{g}$
> og $g \left( f \left( x \right) \right) = x$ for alle $x \in D_{f}$

> [!WARNING] OBS!
> $$\left( f \left( x \right) \right)^{-1} = \frac{1}{f \left( x \right)} \neq f^{-1} \left( x \right)$$

## Eksempel 2

$$
\begin{align}
    f \left( x \right) & = -1 + \ln \left( 2x \right) & \\
    y & = -1 + \ln \left( 2x \right) & \\
    \ln \left( 2x \right) & = y + 1 & \\
    e^{\ln \left( 2x \right)} & = e^{y + 1} & \\
    2x & = e^{y + 1} & \\
    x & = \frac{1}{2} e^{y + 1}
\end{align}
$$

For at dette skal bli en funksjon, skriver vi den om med samme uttrykk, men som en funksjon:

$$
f^{-1} \left( x \right) = \frac{1}{2} e^{x + 1}
$$

![20250108T0759-omvendte-funksjoner-2-geogebra-2.png](Assets/20250108T0759-omvendte-funksjoner-2-geogebra-2.png)

## Grafisk bevis på at omvendte funksjoner er symmetrisk rundt $y = x$

![[20250108T0720-omvendte-funksjoner 2025-01-08 09.07.19.excalidraw]]

## Eksempeloppgaver 3

Vis at funksjonene $f$ og $g$ er omvendte funksjoner

### a

$$
\begin{align}
    f \left( x \right) = 3x & \land g \left( x \right) = \frac{1}{3} x & \\
    f \left( g \left( x \right) \right) & = 3 \cdot \frac{1}{3} \cdot x = x & \\
    g \left( f \left( x \right) \right) & = \frac{1}{3} \cdot 3x = x &
\end{align}
$$

Dermed er $f$ og $g$ omvendte funksjoner.

### b

$$
\begin{align}
    f \left( x \right) = 2x + 6 & \land g \left( x \right) = \frac{1}{2}x - 3 & \\
    f \left( g \left( x \right) \right) & = 2 \left( \frac{1}{2} x - 3 \right) + 6 = x & \\
    g \left( f \left( x \right) \right) & = \frac{1}{2} \left( 2x + 6 \right) - 3 = x &
\end{align}
$$

Dermed er $f$ og $g$ omvendte funksjoner.

### c

$$
\begin{align}
    f \left( x \right) = 10^{x} & \land g \left( x \right) = \lg{x} & \\
    f \left( g \left( x \right) \right) & = 10^{\lg{x}} = x & \\
    g \left( f \left( x \right) \right) & = lg \left( 10^{x} \right) &
\end{align}
$$

Dermed er $f$ og $g$ omvendte funksjoner.

## Eksempeloppgaver 4

Undersøk om $f$ har en omvendt funksjon

### a

$$
\begin{align}
    f \left( x \right) & = x^{3} - 6x^{2} + 3 & D_{f} = \mathbb{R} \\
    f' \left( x \right) & = 3x^{2} - 12x & \\
    & = 3x \left( x - 4 \right) &
\end{align}
$$

![[20250108T0720-omvendte-funksjoner 2025-01-08 09.50.52.excalidraw]]

Denne funksjonen har ikke en omvendt funksjon, fordi den ikke er strengt monoton i hele definisjonsmengden.

For at funksjonen skal ha en omvendt funksjon, må jeg dele den opp i mindre biter ved å velge en definisjonsmengde $D_{f} \in \left\{ \left\langle \leftarrow, 0 \right], \left[ 0, 4 \right], \left[ 4, \rightarrow \right\rangle \right\}$

### b

$$
\begin{align}
    f \left( x \right) & = \frac{1}{3} x^{3} + \frac{1}{2} x^{2} + x + 2 & D_{f} = \mathbb{R} \\
    f' \left( x \right) & = x^{2} + x + 1 & \\
    x & = \frac{-1 \pm \sqrt{1 - 4}}{2} & \\
    & = \frac{-1 \pm \sqrt{-3}}{2} \notin \mathbb{R} &
\end{align}
$$

Andregradsleddet er positivt, så jeg vet at grafen er "smilende" (konveks).
($\forall$ betyr "for alle")
$f' \left( x \right) > 0 \forall x \in \mathbb{R}$

$f' \left( x \right)$ er strengt monoton.
$f \left( x \right)$ har en omvendt funksjon.

## Oppgaver 5

Oppgaver side 214-217 (5.2-5.9)

### 5.2

Funksjonen $f$ er gitt ved $f \left( x \right) = \sqrt{x + 2}$. Den omvendte funksjonen til $f$ er $g$.

#### a

Hva er definisjonsmengden og verdimengden til $g$?

$$
D_{f} = \left[ -2, \rightarrow \right\rangle \land V_f = \left[ 0, \rightarrow \right\rangle \implies \underline{\underline{D_g = \left[ 0, \rightarrow \right\rangle \land V_{g} = \left[ -2, \rightarrow \right\rangle}}
$$

#### b

Bestem $g \left( 4 \right)$

$$
\begin{align}
    f \left( x \right) = 4 \\
    \sqrt{x + 2} & = 4 & \\
    x + 2 & = \pm 16 & \\
    -16 & \notin D_{g} & \\
    \implies x + 2 & = 16 & \\
    x & = 14 & \\
    g \left( 4 \right) & = 14 &
\end{align}
$$

#### c

Tegn grafene til $f$ og $g$ i det samme koordinatsystemet

![20250108T0914-geogebra-oppg5-2-c.png](Assets/20250108T0914-geogebra-oppg5-2-c.png)

(her ble definisjonsmengden feil, burde stoppet på $x=0$, men GeoGebra skjønte det ikke)

### 5.3

Funksjonene $f$ og $g$ er omvendte funksjoner. Du får vite at $f \left( 3 \right) = 5$ og $f \left( -2 \right) = 8$.

#### a

Hva er $g \left( 5 \right)$?

$f \left( 3 \right) = 5 \implies \underline{\underline{g \left( 5 \right) = 3}}$

#### b

Hva er løsningen på likningen $g \left( x \right) = -2$?

$f \left( -2 \right) = 8 \implies g \left( 8 \right) = -2 \implies \underline{\underline{x = 8}}$

#### c

Skriv opp koordinatene til to punkter på grafen til $g$.

Fra de to forrige oppgavene:

$\left( 5, 3 \right)$ og $\left( 8, -2 \right)$

### 5.4

Den lineære funksjonen $f$ går gjennom punktene $\left( 2, -3 \right)$ og $\left( 4, 7 \right)$.
Tegn grafen til $f$ og graden til den omvendte funksjonen $g$ i det samme koordinatsystemet.
![[20250108T0720-omvendte-funksjoner 2025-01-08 10.26.03.excalidraw]]

## Eksempel - oppsummering / repetisjon

$f \left( x \right)$ og $g \left( x \right)$ er omvendte funksjoner hvis det er slik at $f \left( x \left( x \right) \right) = x$ og $g \left( f \left( x \right) \right) = x$

$g \left( f \left( x \right) \right) = x$
La $f \left( x \right) = y$
$g \left( y \right) = x$

### Oppgave 1

$$
f \left( x \right) = 2x - 8, D_{f} = \mathbb{R}
$$

Finn den omvendte funksjonen, g.

---

La $f \left( x \right) = y$. Finner x uttrykt ved y

$$
\begin{align}
    y &= 2x - 8 & \\
    y + 8 &= 2x & \\
    x &= \frac{1}{2}y + 4 & \\
    g \left( y \right) & = \frac{1}{2}y + 4 & \\
    g \left( x \right) & = \frac{1}{2}x + 4 &
\end{align}
$$

Den omvendte funksjonen: $g \left( x \right) = \frac{1}{2} x + 4, D_{g} = \mathbb{R} = V_{f}$

### Oppgave 2

$$
f \left( x \right) = 10^{x}, D_{f} = \mathbb{R}, V_{f} = \left\langle 0, \rightarrow \right\rangle
$$

$$
f^{-1} \left( x \right) = \lg{10}, D_{f} = \left\langle 0, \rightarrow \right\rangle, V_{f} = \mathbb{R}
$$

### Oppgave 3

$$
f \left( x \right) = 3 - \sqrt{x}, D_{f} = \left[ 0, \rightarrow \right\rangle
$$

$$
\begin{align}
    y & = 3 - \sqrt{x} & \\
    \sqrt{x} &= 3 - y & \\
    x &= \left( 3 - y \right)^{2} & \\
    x &= y^{2} - 6y + 9 & \\
    f^{-1} &= x^{2} - 6x + 9, D_{f^{-1}} = V_{f} = \left\langle \leftarrow, 3 \right] &
\end{align}
$$

3 er bunnpunktet til funksjonen. Dermed er $f^{-1}$ entydig, altså finnes den omvendte funksjonen.

### Oppgave 4

$f \left( x \right) = x^{2} - 4x$. Bestem $f^{-1}$ med størst mulig definisjonsmengde når du får oppgitt at $-1 \in V_{f^{-1}} = D_{f}$

$$
\begin{align}
    y & = x^{2} - 4x & \\
    x^{2} - 4x - y & = 0 & \\
    x & = \frac{4 \pm \sqrt{16 - 4y}}{2} & \\
    x & = \frac{4 \pm \sqrt{4 \left( 4 + y \right)}}{2} & \\
    x & = \frac{4 \pm \sqrt{4} \cdot \sqrt{4 + y}}{2} & \\
    x & = \frac{4 \pm 2 \cdot \sqrt{4 + y}}{2} & \\
    x & = 2 \pm \sqrt{4 + y} &
\end{align}
$$

---

$$
f \left( x \right) = x^{2} - 4x = x \left( x - 4 \right)
$$

Nullpunkt i $x=0$ og $x=4$. Symmetrisk om midtpunktet, dermed ekstremalpunkt i $\left( 2, f \left( 2 \right) \right) = \left( 2, -4 \right)$

Vet at funksjonen må være entydig, altså kan jeg kun velge $\left\langle \leftarrow, 2 \right]$, eller $\left[ 2, \rightarrow \right\rangle$

Kan også finne ved derivasjon, ved at $f' \left( x \right) = 2x - 4$.

Strengt avtakende i $\left\langle \leftarrow, 2 \right]$
Strengt voksende i $\left[ 2, \rightarrow \right\rangle$

Siden $-1 \in V_{f^{-1}} = D_{f}$, må vi bruke $D_{f} = \left\langle \leftarrow, 2 \right]$.

---

$$
x = 2 \pm \sqrt{4 + y}
$$

Velger den med minus.

$$
\begin{align}
    f^{-1} \left( y \right) & = 2 - \sqrt{4 + y} & \\
    f^{-1} \left( x \right) & = 2 - \sqrt{4 + y} & \\
    F_{f^{-1}} & = V_{f} = \left[ -4, \rightarrow \right\rangle &
\end{align}
$$

## Sammenheng med den deriverte

![20250113T1156-omvendt-funksjon-derivasjon.png](Assets/20250113T1156-omvendt-funksjon-derivasjon.png)

$n$ og $m$ er to linjer, symmetriske om linjen $y = x$ og ikke sammenfallende med koordinataksene.

Stigningstallet til $m$ er $\displaystyle a_{m} = \frac{y_{2} - y_{1}}{x_{2} - x_{1}}$.
Stigningstallet til $n$ er $\displaystyle a_{n} = \frac{x_{2} - x_{1}}{y_{2} - y_{1}}$.

$$
\boxed{a_{n} = \frac{1}{a_{m}}}
$$

$\displaystyle a_{n} \cdot a_{m} = 1 \frac{\left( y_{2} - y_{1} \right) \left( x_{2} - x_{1} \right)}{\left( x_{2} - x_{1} \right) \left( y_{2} - y_{1} \right)}$

---

Ex.

$$
f \left( x \right) = 3x - 2
$$

$$
f' \left( x \right) = 3 \implies {f^{-1}}' \left( x \right) = \frac{1}{3}
$$

Denne sammenhengen gjelder for alle deriverbare funksjoner som har en omvendt funksjon.

![20250113T1203-omvendt-funksjon-derivasjon-tangent.png](Assets/20250113T1203-omvendt-funksjon-derivasjon-tangent.png)

> [!NOTE] Definisjon
> La $f$ være en deriverbar funksjon., $f \left( x \right) = y$, der $g \left( y \right) = x$ er den omvendte funksjonen.
> Da er
>
> $$
> g' \left( y \right) = \frac{1}{f' \left( x \right)} \forall f' \left( x \right) \neq 0
> $$
