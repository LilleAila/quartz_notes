---
id: 20250203T1144-enhetsvektor
aliases:
  - enhetsvektor
tags: []
date: "2025-02-03"
title: Enhetsvektor
---

#matte [[20250115T0716-vektorer|vektorer]]

# enhetsvektor

En enhetsvektor er en vektor med lengde 1.

![20250203T1147-enhetsvektor.png](Assets/20250203T1147-enhetsvektor.png)

$$
\begin{align}
  \vec{e_{x}} &= \left[ 1, 0 \right] & \\
  \vec{e_{y}} &= \left[ 0, 1 \right] &
\end{align}
$$

> [!NOTE]
>
> $$
> \vec{e_{x}} \perp \vec{e_{y}}
> $$

Dermed blir

$$
\vec{u} = \left[ 2, 3 \right] = 2 \vec{e_{x}} + 3\vec{e_{y}}
$$

, eller mer generelt

$$
\left[ x, y \right] = x \cdot \vec{e_{x}} + y \cdot \vec{e_{y}}
$$

> [!NOTE]
> På høyere nivå skriver man heller:
>
> $$
> \begin{align}
>   \hat{\imath} &= \vec{e_{x}} & \\
>   \hat{\jmath} &= \vec{e_{y}} & \\
>   \hat{k} &= \vec{e_{z}} &
> \end{align}
> $$

## Vektorer på koordinatform

Ved hjelp av dette, kan man da skrive alle vektorer på koordinatform:

$$
\left[ x, y \right] = x \cdot \vec{e_{x}} + y \cdot \vec{e_{y}}
$$

Direkte som koordinater:
$$
\begin{align}
  \vec{p} = \left[ 1, 2 \right] &\land \vec{q} = \left[ 3, 1 \right] & \\
  \vec{p} + \vec{q} &= \left[ 1, 2 \right] + \left[ 3, 1 \right]  = \left[ 4, 3 \right] &
\end{align}
$$

I CAS:
![20250217T1001-cas-vektor-addisjon.png](Assets/20250217T1001-cas-vektor-addisjon.png)

Med enhetsvektorer:
$$
\begin{align}
  \left[ x_{1}, y_{1} \right] + \left[ x_{2}, y_{2} \right] &= \left( x_{1} \cdot \vec{e_{x}} + y_{1} \cdot \vec{e_{y}} \right) \left[ x_{2} \cdot \vec{e_{x}} + y_{2} \cdot \vec{e_{y}} \right] & \\
  &= \left[ x_{1} + x_{2}, y_{1} + y_{2} \right] &
\end{align}
$$

Subtraksjon gjøres på samme måte.

## Dekomponere vektorer

Hvis vi har en vekter $\vec{u}$ og to andre vektorer $\vec{a}$ og $\vec{b}$ der $\vec{a} \not\parallel \vec{b}$, kan vi altid skrive $\vec{u}$ som en sum av vektorer som er multipler av $\vec{a}$ og $\vec{b}$.

## Posisjonsvektor

> [!NOTE]
> Posisjonsvektor: En vektor fra origo til et punkt. For eksempel er $\vec{OP}$, posisjonsvektoren som går fra origo til punktet $P$, og viser altså hvor et punkt er i forhold til origo.
> Posisjonsvektoren til et punkt $\left( x, y \right)$ har koordinatene $\left[ x, y \right]$.

### Finne vektor mellom to punkter.

$$
\begin{align}
  A \left( x_{1}, y_{1} \right) &\land B \left( x_{2}, y_{2} \right) & \\
  \vec{AB} &= \left[ x_{2} - x_{1}, y_{2} - y_{1} \right] &
\end{align}
$$

## Ortogonale vektorer

$$
\begin{align}
  \vec{e_{x}} \cdot \vec{e_{x}} &= 1 & \\
  \vec{e_{y}} \cdot \vec{e_{y}} &= 1 & \\
  \vec{e_{x}} \cdot \vec{e_{y}} &= 0 & \\
  \left[ x_{1}, y_{1} \right] \cdot \left[ x_{2}, y_{2} \right] &= x_{1} \cdot x_{2} + y_{1} \cdot y_{2} &
\end{align}
$$

Generelt: to vektorer $\left[ x, y \right]$ og $\left[ y, -x \right]$ er ortogonal.

$$
\begin{align}
  \left[ x, y \right] \cdot \left[ y, -x \right] &= x \cdot y + y \cdot \left( -x \right) & \\
  &= x \cdot y - y \cdot x & \\
  &= 0 &
\end{align}
$$

## Lengde

Bruker pytagoras.

$$
\begin{align}
  \left| \left[ x, y \right] \right| &= \sqrt{x^{2 +} y^{2}} &
\end{align}
$$

## Avstand mellom punkter

Kan bruke begge de som er definert over.

Har punktene $A \left( x_{1}, y_{1} \right)$ og $B \left( x_{2}, y_{2} \right)$.

$$
\begin{align}
  A \left( x_{1}, y_{1} \right) & \land B \left( x_{2}, y_{2} \right) & \\
  \left| \vec{AB} \right| &= \left[ x_{2} - x_{1}, y_{2} - y_{1} \right] & \\
  &= \sqrt{\left( x_{2} - x_{1} \right)^{2} + \left( y_{2} - y_{1} \right)^{2}} &
\end{align}
$$

## Vinkel mellom vektorer på koordinatform

$$
\begin{align}
  \vec{p} \cdot \vec{q} &= \left| \vec{p} \right| \cdot \left| \vec{q} \right| \cdot \cos{\alpha} & \\
  \cos{\alpha} &= \frac{\vec{p} \cdot \vec{q}}{\left| \vec{p} \right| \cdot \left| \vec{q} \right|} & \\
  \alpha &= \cos^{-1} \left( \frac{\vec{p} \cdot \vec{q}}{\left| \vec{p} \right| \cdot \left| \vec{q} \right|} \right) &
\end{align}
$$

I GeoGebra kan man bruke `Vinkel(p, q)`.

## Beregne ulike størrelser i planet

### Midtpunktet på et linjestykke

Finne vektoren mellom punktene, halvvere den.

### Finne koordinatene til et punkt

Finne posisjonsvektoren til punktet

### Avstand fra punkt til en linje

Finne vektoren som står vinkelrett på linjen.

Korteste avstand fra et punkt til en linje.
Lengden av linjestykket, eller vektoren som går fra punktet og som står vinkelrett på linjen.

> [!NOTE]
> Tverrvektor
> To vektorer som står ortogonale på hverandre og som er like lange.
> $$
> \vec{u} \perp \vec{v} \land \left| \vec{u} \right| = \left| \vec{v} \right|
> $$
> Bruker det fra tidligere:
> $\vec{v} = \left[ a, b \right] \land \vec{u} = \left[ b, -a \right]$
