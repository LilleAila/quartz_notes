---
id: 20250115T0851-skalarprodukt
aliases:
  - skalarprodukt
tags: []
date: "2025-01-15"
title: Skalarprodukt
---

#matte [[20240616T1007-matte|matte]] [[20250115T0716-vektorer|vektorer]]

# skalarprodukt

![[20250115T0851-skalarprodukt 2025-01-15 09.52.35.excalidraw.svg]]

Hvis vektorene er noenlunde i samme retning, blir cosinus-verdien positiv. Hvis de spriker fra hverandre, blir cosinus-verdien negativ.

- [ ] TODO: flytte dette inn i notat om sinus / cosinus

![[20250115T0851-skalarprodukt 2025-01-15 10.02.42.excalidraw.svg]]

![[20250115T0851-skalarprodukt 2025-01-15 10.04.44.excalidraw.svg]]

Gitt to vektorer $\vec{a}$ og $\vec{b}$
La $a$ være vinkelen mellom vektorene.
Skalarproduktet (eller prikkproduktet) mellom vektorene er da

$$
\vec{a} \cdot \vec{b} = \left| a \right| \cdot \left| b \right| \cdot \cos{\alpha}
$$

Resultatet er en skalar, ikke en vektor. Dette er et slags mål på hvor mye de peker i samme retning.

![[20250115T0851-skalarprodukt 2025-01-15 10.11.18.excalidraw.svg]]

Hvis vektorene står vinkelrette på hverandre, kaller vi dem ortogonale. Det vil si at $\alpha = 90 ^{\circ}$

$$
\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0 \land \left| \vec{a} \right| \neq 0 \land \left| \vec{b} \right| \neq 0
$$

## Regneregler

$$
\begin{align}
  \vec{a} \cdot \vec{b} & = \vec{b} \cdot \vec{a} & \\
  \vec{a} \cdot \left( \vec{b} + \vec{c} \right) & = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c} & \\
  \left( \vec{a} + \vec{b} \right) \cdot \left( \vec{c} + \vec{d} \right) & = \vec{a} \cdot \vec{c} + \vec{a} \cdot \vec{d} + \vec{b} \cdot \vec{c} + \vec{b} \cdot \vec{d} & \\
  \left( s \vec{a} \right) \cdot \left( t \vec{b} \right) & = \left( s \cdot t \right) \left( \vec{a} \cdot \vec{b} \right) &
\end{align}
$$

---

Oppfører seg stort sett som tall, og dermed kan vi også bruke kvadratsetningene.

$$
\begin{align}
  \left( \vec{a} + \vec{b} \right) ^{2} & = \vec{a} ^{2} + 2 \vec{a} \cdot \vec{b} + \vec{b} ^{2} & \\
  \left( \vec{a} - \vec{b} \right) ^{2} & = \vec{a} ^{2} - 2 \vec{a} \cdot \vec{b} + \vec{b} ^{2} & \\
  \left( \vec{a} + \vec{b} \right) \cdot \left( \vec{a} - \vec{b} \right) & = \vec{a} ^{2 -} \vec{b} ^{2} &
\end{align}
$$

---

$$
\begin{align}
  \vec{a} \cdot \vec{a} & = \left| \vec{a} \right| \cdot \left| \vec{a} \right| \cdot \cos{0} & \\
  & = \left| \vec{a} \right| \cdot \left| \vec{a} \right| \cdot 1 & \\
  \vec{a} ^{2} & = \left| \vec{a} \right| ^{2} & \\
  \left| \vec{a} \right| & = \sqrt{\vec{a} ^{2}} &
\end{align}
$$

## Geometrisk tolkning

![20250210T1014-skalarprodukt-geometrisk.png](Assets/20250210T1014-skalarprodukt-geometrisk.png)

Cosinussetningen:

$$
a^{2} = b^{2} + c^{2} - 2bc \cos{A}
$$

Med denne trekanten blir det:

$$
\begin{align}
  a &= \left| \vec{u} - \vec{v} \right| & \\
  b &= \left| \vec{u} \right| & \\
  c &= \left| \vec{v} \right| & \\
  A &= \alpha &
\end{align}
$$

$$
\left| \vec{u} - \vec{v} \right|^{2} = \left| \vec{u} \right|^{2} + \left| \vec{v} \right|^{2} - 2 \cdot \left| \vec{u} \right| \cdot \left| \vec{v} \right| \cdot \cos{\alpha}
$$

Vi kan skrive

$$
\begin{align}
    \left| \vec{u} - \vec{v} \right|^{2} &= \left( \vec{u} - \vec{v} \right)^{2} & \\
    &= \vec{u}^{2} - 2 \vec{u}\vec{v} + \vec{v}^{2} & \\
    &= \left| \vec{u} \right|^{2} - 2 \vec{u} \cdot \vec{v} + \left| \vec{v} \right|^{2} & \\
    &= \left| \vec{u} \right|^{2} + \left| \vec{v} \right|^{2} - 2 \cdot \vec{u} \cdot \vec{v} &
\end{align}
$$

Ser dermed at

$$
\left| \vec{u} \right| \cdot \left| \vec{v} \right| \cdot \cos{\alpha} = \vec{u} \cdot \vec{v}
$$

> [!NOTE]
> Skalarproduktet av $\vec{u}$ og $\vec{v}$ er
>
> $$
> \vec{u} \cdot \vec{v} = \left| \vec{u} \right| \cdot \left| \vec{v} \right| \cdot \cos{\alpha}
> $$

## Oppgaver

### 6.61

$$
\begin{align}
    \vec{u} = \left[ 6, 2 \right] &\land \vec{v} = \left[ 4, 3 \right] & \\
    \vec{u} \cdot \vec{v} &= 6 \cdot 4 + 2 \cdot 3 & \\
    &= 30 &
\end{align}
$$

$$
\begin{align}
  \vec{u} = \left[ -3, 5 \right] &\land \vec{v} = \left[ 5, 3 \right] & \\
  \vec{u} \cdot \vec{v} &= -3 \cdot 5 + 5 \cdot 3 & \\
  &= 0 &
\end{align}
$$

$$
\begin{align}
  \vec{u} = \left[ 4, 0 \right] &\land \vec{v} = \left[ 2, 7 \right] & \\
  \vec{u} \cdot \vec{v} &= 4 \cdot 2 + 0 \cdot 7 & \\
  &= 8 &
\end{align}
$$

### 6.62

![20250210T1008-6-62-a.png](Assets/20250210T1008-6-62-a.png)

![20250210T1009-6-62-b.png](Assets/20250210T1009-6-62-b.png)

### 6.63

#### a

$$
\begin{align}
  3 \left( \left[ 5, 2 \right] \cdot \left[ 3, -2 \right] \right) & = \left[ 5, 2 \right] \cdot 3 \left[ 3, -2 \right] & \\
  3 \left( \left[ 5, 2 \right] \cdot \left[ 3, -2 \right] \right) &= 3 \left( 5 \cdot 3 + 2 \cdot -2 \right) & \\
  &= 3 \left( 15 - 4 \right) & \\
  &= 33 & \\
  \left[ 5, 2 \right] \cdot 3 \left[ 3, -2 \right] &= 5 \cdot 9 + 2 \cdot -6 & \\
  &= 45 - 12 & \\
  &= 33 &
\end{align}
$$

#### b

$$
\begin{align}
  \left[ 2, 4 \right] \cdot \left[ -3, 2 \right] &= \left[ -3, 2 \right] \cdot \left[ 2, 4 \right] & \\
  \left[ 2, 4 \right] \cdot \left[ -3, 2 \right] &= 2 \cdot -3, 4 \cdot 2 & \\
  &= -6 + 8 & \\
  &= 2 & \\
  \left[ -3, 2 \right] \cdot \left[ 2, 4 \right] &= -3 \cdot 2 + 2 \cdot 4 & \\
  &= -6 + 8 & \\
  &= 2 &
\end{align}
$$

#### c

$$
\begin{align}
  \left[ 5, 2 \right] \cdot \left[ 5, 2 \right] &= \left| \left[ 5, 2 \right] \right|^{2} & \\
  \left[ 5, 2 \right] \cdot \left[ 5, 2 \right] &= 5 \cdot 5 + 2 \cdot 2 & \\
  &= 29 & \\
  \left| \left[ 5, 2 \right] \right|^{2} &= \left( \sqrt{5^{2} + 2^{2}} \right)^{2} & \\
  &= 5^{2} + 2^{2} & \\
  &= 29 &
\end{align}
$$

#### d

$$
\begin{align}
  \left[ 2, 3 \right] \cdot \left( \left[ -3, 1 \right] + \left[ 6, -2 \right] \right) &= \left[ 2, 3 \right] \cdot \left[ -3, 1 \right] + \left[ 2, 3 \right] \cdot \left[ 6, -2 \right] & \\
  \left[ 2, 3 \right] \cdot \left( \left[ -3, 1 \right] + \left[ 6, -2 \right] \right) &= \left[ 2, 3 \right] \cdot \left[ 3, -1 \right] & \\
  &= 2 \cdot 3 + 3 \cdot -1 & \\
  &= 3 & \\
  \left[ 2, 3 \right] \left[ -3, 1 \right] + \left[ 2, 3 \right] \cdot \left[ 6, -2 \right] &= 2 \cdot -3 + 3 \cdot 1 + 2 \cdot 6 + 3 \cdot -2 & \\
  &= 3 &
\end{align}
$$

### 6.64

#### a

$$
\begin{align}
  \vec{u} \cdot \vec{u} & = 49 & \\
  49 &= \left| \vec{u} \right| \cdot \left| \vec{u} \right| \cdot \cos{0} & \\
  \sqrt{49} &= \sqrt{\left| \vec{u} \right|^{2}} \cdot 1 & \\
  \left| \vec{u} \right| &= 7 &
\end{align}
$$

#### b

Ser fra forrige oppgave at $\vec{u}^{2} = \left| \vec{u} \right|^{2}$.

$$
\begin{align}
  \left| \vec{v} \right| &= 2 \sqrt{2} & \\
  \vec{v}^{2} &= \left| \vec{v} \right|^{2} = \left( 2 \sqrt{2} \right)^{2} & \\
  &= 4 \cdot 2 = 8 &
\end{align}
$$

### 6.65

#### a

$$
\begin{align}
  \left( \vec{u} + \vec{v} \right)^{2} &= \vec{u} \left( \vec{u} + \vec{v} \right) + \vec{v} \left( \vec{u} + \vec{v} \right) & \\
  &= \vec{u} \cdot \vec{u} + \vec{u} \cdot \vec{v} + \vec{v} \cdot \vec{u} + \vec{v} \cdot \vec{v} & \\
  &= \vec{u}^{2} + 2 \vec{u} + \vec{v} + \vec{v}^{2} &
\end{align}
$$

#### b

Skalarproduktet oppfører seg på samme måte som vanlige tall. Dermed gjelder alle de tre kvadratsetningene også for vektorer.

### 6.66

Du får vite at $\vec{u} \cdot \vec{v} = 5$, $\left| \vec{u} \right| = \sqrt{17}$ og $\left| \vec{v} \right| = \sqrt{13}$. Regn ut

### a

$$
\begin{align}
  2 \vec{v} \cdot \vec{u} + \vec{u} \cdot \left( 3 \vec{v} + \vec{u} \right) &= 2 \cdot \vec{v} \cdot \vec{u} + 3 \cdot \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{u} & \\
  &= 5 \cdot 5 + 17 = 22 &
\end{align}
$$

### 6.70

Avgjør om vektorene er ortogonale.

#### a

$$
\begin{align}
  \left[ 4, 1 \right] \perp \left[ -4, 16 \right] &\iff \left[ 4, 1 \right] \cdot \left[ -4, 16 \right] = 0 & \\
  4 \cdot -4 - 1 \cdot 16 = 0 & \implies \left[ 4, 1 \right] \perp \left[ -4, 16 \right] &
\end{align}
$$

Ingen av vektorene er nullvektorer, og skalarproduktet er lik 0. Dermed er vektorene ortogonale.

#### b

$$
\begin{align}
  \left[ -2, 5 \right] \cdot \left[ 14, 6 \right] &= -2 \cdot 14 + 5 \cdot 6 = 2 &
\end{align}
$$

Vektorene er ikke orgononale, siden skalarproduktet $\neq 0$

#### c

$$
\begin{align}
  \left[ \ln{2}, 2 \ln{2} \right] \cdot \left[ \ln{2}, -1 \right] & = \ln{2} \cdot \ln{2} + 2 \ln{2} \cdot -1 & \\
  & = \left( \ln{2} \right)^{2} - 2 \ln{2} &
\end{align}
$$

Vektorene er ikke orgononale, siden skalarproduktet $\neq 0$

### 6.71

Bestem $k$ slik at vektorene $\vec{u}$ og $\vec{v}$ er ortogonale uten hjelpemidler.

#### a

$$
\begin{align}
  \vec{u} = \left[ 2, 5 \right] &\land \vec{v} = \left[ k, 2 \right] & \\
  \vec{u} \cdot \vec{v} &= 2 \cdot k + 5 \cdot 2 = 2k + 10 & \\
  2k + 10 = 0 &\implies k = -5 &
\end{align}
$$

#### b

$$
\begin{align}
  \vec{u} = \left[ 2k, 4 \right] &\land \vec{v} = \left[ k, -2 \right] & \\
  \vec{u} \cdot \vec{v} &= 2k^{2} - 8 & \\
  k^{2} - 4 & = 0 & \\
  k^{2} & = 4 & \\
  k &= \pm 2 &
\end{align}
$$

### 6.68

Bestem skalarproduktet av $\vec{u}$ og $\vec{v}$ når $\left| \vec{u} \right| = 2$, $\left| \vec{v} \right| = 3 $ og vinkelen mellom vektorene er:

#### a: $0\degree$

$$
2 \cdot 3 \cdot \cos{0\degree} = 6 \cdot 1 = 6
$$

#### b: $30\degree$

$$
2 \cdot 3 \cdot \cos{30\degree} = 6 \cdot \frac{\sqrt{3}}{2}
$$

#### c: $45\degree$

$$
2 \cdot 3 \cdot \cos{45\degree} = 6 \cdot \frac{\sqrt{2}}{2}
$$

#### d: $60\degree$

$$
2 \cdot 3 \cdot \cos{60\degree} = 6 \cdot \frac{1}{2} = 3
$$

#### e: $90\degree$

$$
2 \cdot 3 \cdot \cos{90\degree} = 6 \cdot 0 = 0
$$

### 6.73

Finn vinkelen mellom vektorene ved å bruke skalarproduktet.

#### a

$$
\begin{align}
  \left[ 4, 1 \right] \cdot \left[ -4, 16 \right] &= -16 + 16 = 0 \implies \vec{u} \perp \vec{v} \implies \alpha = 0 &
\end{align}
$$

#### b

$$
\begin{align}
  & \left[ -2, 5 \right] \cdot \left[ 14, 6 \right] = -28 + 30 = 2 & \\
  \left| \left[ -2, 5 \right] \right| &= \sqrt{\left( -2 \right)^{2} + 5^{2}} = \sqrt{29} & \\
  \left| \left[ 14, 6 \right] \right| &= \sqrt{14^{2} + 6^{2}} = \sqrt{232} & \\
  \left[ -2, 5 \right] \cdot \left[ 14, 6 \right] &= \sqrt{29} \cdot \sqrt{232} \cdot \cos{\alpha} = \sqrt{6728} \cdot \cos\alpha & \\
  \sqrt{6728} \cdot \cos{\alpha} &= 2 &
\end{align}
$$
