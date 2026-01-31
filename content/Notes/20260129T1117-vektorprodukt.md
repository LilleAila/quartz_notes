---
id: 20260129T1117-vektorprodukt
aliases:
  - vektorprodukt
tags: []
date: "2026-01-29"
title: vektorprodukt
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# vektorprodukt

Vektorproduktet er en måte å finne en vektor som står normalt på begge vektorene dene originerer på. I motsetning til skalarproduktet, gir dette en vektor i stedet for en skalar. Hvis man har et plan mellom to vektorer, vil vektorproduktet være en vektor som står normalt på planet.

$$
\overrightarrow{a \times b} \perp \vec{a} \land \overrightarrow{a \times b} \perp \vec{b}
$$

$$
\begin{align}
  \vec{a} \times \vec{b} \perp \vec{a} &\land \vec{a} \times \vec{b} \perp \vec{b} & \\
  \left| \vec{a} \times \vec{b} \right| &= \left| \vec{a} \right| \cdot \left| \vec{b} \right| \cdot \sin{\left( \angle \left( \vec{a}, \vec{b} \right) \right)} &
\end{align}
$$

Vektorproduktet må følge høyrehåndsregelen. I $\vec{a} \times \vec{b}$ vil $\vec{a}$ være pekefingeren, $\vec{b}$ er de fingrene som krummer og $\vec{a} \times \vec{b}$ vil være tommelfingeren som peker oppover.

![20260127T1241-right-hand-rule.png](Assets/20260127T1241-right-hand-rule.png)

Dette medfører følgende regler:

$$
\begin{align}
  \vec{a} \times \vec{b} &= - \vec{b} \times \vec{a} & \\
  \vec{a} \times \vec{a} &= \vec{0} & \\
  \vec{a} \times \left( \vec{b} + \vec{c} \right) &= \vec{a} \times \vec{b} + \vec{a} \times \vec{c} & \\
  k \cdot \left( \vec{a} \times \vec{b} \right) &= \left( k \vec{a} \right) \times \vec{b} = \vec{a} \times \left( k \vec{b} \right) &
\end{align}
$$

## Vektorprodukt med matriser

(vi har ikke egentlig lært om matriseregning enda)

For vektorproduktet bruker vi en $3 \times 3$ matrise.

$$
\begin{align}
  \begin{bmatrix}
        a & b & c \\
        d & e & f \\
        g & h & i
    \end{bmatrix}&&
\end{align}
$$

Man kan finne determinanten til en $2\times2$ matrise som følger:

$$
\det \begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix} = \left|\begin{matrix}
  a & b \\
  c & d
\end{matrix}\right| = a \cdot d - b \cdot c
$$

Man tar produkted nedover mot høyre og trekker fra produktet nedover til venstre. Dette tilsvarer arealet til et parallellogram.

![[20260122T1046-romgeometri 2026-01-29 11.13.19.excalidraw.svg]]

> [!NOTE]
> Man skriver vanligvis vektorer på matriseform i flere rader, men ikke med denne regelen for vektorprodukt.
>
> $$
> \vec{u} = \begin{bmatrix}
>   x \\ y \\ z
> \end{bmatrix}
> $$

Setter opp vektorene, og lager en $3 \times 3$-matrise. Når man regner ut $3\times3$-determinant, splitter man det først inn i $2 \times 2$-determinanter. Man "ignorerer" den raden og kolonnen man henter informasjon fra.

![[20260122T1046-romgeometri 2026-01-29 10.47.52.excalidraw.svg]]

All informasjonen for $x$-retning kommer fra $yz$-planet, siden det er da ortogonalt med det planet. Samme gjelder de andre planene. Man får da ett uttrykk for hver retning basert på de to andre retningene. Med todimensjonale vektorer ville man fått $x$ og $y$-komponentene lik $0$ og dermed kun en $z$-verdi.

$$
\begin{align}
  \vec{a} &= \left[ x_{1}, y_{1}, z_{1} \right] & \\
  \vec{b} &= \left[ x_{2}, y_{2}, z_{2} \right] & \\
  \vec{a} \times \vec{b} &= \left|\begin{matrix}
      \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
      x_{1} & y_{1} & z_{1} \\
      x_{2} & y_{2} & z_{2}
    \end{matrix}\right| & \\
  \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    x_{1} & y_{1} & z_{1} \\
    x_{2} & y_{2} & z_{2}
  \end{matrix}\right| &= \vec{e_{x}} \left|\begin{matrix}
    y_{1} & z_{1} \\
    y_{2} & z_{2}
  \end{matrix}\right| - \vec{e_{y}} \left|\begin{matrix}
    x_{1} & z_{1} \\
    x_{2} & z_{2}
  \end{matrix}\right| + \vec{e_{z}}  \left|\begin{matrix}
    x_{1} & y_{1} \\
    x_{2} & y_{2}
  \end{matrix}\right| & \\
  &= \vec{e_{x}} \left( y_{1} \cdot z_{2} - z_{1} \cdot y_{2} \right) - \vec{e_{y}} \left( x_{1} \cdot z_{2} - z_{1} \cdot x_{2} \right) + \vec{e_{z}} \left( x_{1} \cdot y_{2} - y_{2} \cdot x_{2} \right) \\
  \vec{a} \cdot \vec{b} &= \left[ y_{1} \cdot z_{2} - z_{1} \cdot y_{2}, - \left( x_{1} \cdot z_{2} - z_{1} \cdot x_{2} \right), x_{1} \cdot y_{2} - y_{1} \cdot x_{2} \right] &
\end{align}
$$

## Eksempel

$$
\begin{align}
  \vec{u} &= \left[ 3, 0, 1 \right] & \\
  \vec{v} &= \left[ 0, 1, 2 \right] & \\
  \vec{u} \times \vec{v} &= \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    3 & 0 & 1 \\
    0 & 1 & 2
  \end{matrix}\right| & \\
  &= e_{x} \left|\begin{matrix}
    0 & 1 \\
    1 & 2
  \end{matrix}\right| - \vec{e_{y}} \left|\begin{matrix}
    3 & 1 \\
    0 & 2
  \end{matrix}\right| + \vec{e_{z}} \left|\begin{matrix}
    3 & 0 \\
    0 & 1
  \end{matrix}\right| & \\
  &= \vec{e_{x}} \left( -1 \right) - \vec{e_{y}} \left( b \right) + \vec{e_{z}} \left( 3 \right) & \\
  &= \left[ -1, -6, 3 \right] &
\end{align}
$$

# Oppgaver

## Eksempel 15 (s. 373)

$$
\begin{align}
  \left[ 3, 0, 1 \right] \times \left[ 0, 1, 2 \right] &= \left( 3 \cdot \vec{e_{x}} + \cancel{0 \cdot \vec{e_{y}}} + 1 \cdot \vec{e_{z}} \right) \times \left( \cancel{0 \cdot \vec{e_{x}}} \cdot 1 \cdot \vec{e_{y}} + 2 \cdot \vec{e_{z}} \right) & \\
  &= 3 \cdot \underbrace{\vec{e_{x}} \times \vec{e_{y}}}_{\vec{e_{z}}} + 6 \cdot \underbrace{\vec{e_{x}} \times \vec{e_{z}}}_{-\vec{e_{y}}} + 1 \cdot \underbrace{-\vec{e_{z}} \times \vec{e_{y}}}_{\vec{e_{x}}} + \cancel{2 \cdot e_{z} \times \vec{e_{z}}} & \\
  &= 3 \vec{e_{z}} - 6 \vec{e_{y}} - 1 \cdot \vec{e_{x}} & \\
  &= \left[ 3, -6, -1 \right] &
\end{align}
$$

## 6.26 (s. 376)

$$
\begin{align}
  \left[ 3, 0, 4 \right] \times \left[ 0, 1, 0 \right] &= 3 e_{x} \times e_{y} + 4 e_{z} \times e_{y} & \\
  &= 3 e_{z} - 4 e_{x} & \\
  &= \left[ -4, 0, 3 \right] &
\end{align}
$$

Bruker definisjonen som følger:

$$
\begin{align}
  \left[ x, y, z \right] \cdot \vec{a} &= 0 & \\
  \left[ x, y, z \right] \cdot \vec{b} &= 0 & \\
  \sqrt{x^{2} + y^{2} + z^{2}} &= \left| \vec{a} \right| \cdot \left| \vec{b} \right| \cdot \sin{\angle \vec{a}, \vec{b}} & \\
  \cos{\left( \angle \vec{a}, \vec{b} \right)} &= \frac{\vec{a} \cdot \vec{b}}{\left| \vec{a} \right| \cdot \left| \vec{b} \right|} & \\
  \cos{\left( \angle \vec{a}, \vec{b} \right)} &= \frac{0}{\sqrt{3^{2} + 4^{2}} \cdot \sqrt{1^{2}}} & \\
  \cos{\left( \angle \vec{a}, \vec{b} \right)} &= \frac{0}{5} = 0 & \\
  \angle \vec{a}, \vec{b} &= 90 \degree & \\
  \left[ x, y, z \right] \cdot \left[ 0, 1, 0 \right] &= 0 & \\
  y &= 0 & \\
  \left[ x, y, z \right] \cdot \left[ 3, 0, 4 \right] &= 0 & \\
  3x + 4z &= 0 & \\
  3x &= -4z & \\
  x &= - \frac{4}{3}z & \\
  \sqrt{x^{2} + y^{2} + z^{2}} &= 5 & \\
  x^{2} + y^{2} + z^{2} &= 25 & \\
  \left( - \frac{4}{3} z \right)^{2} + 0^{2} + z^{2} &= 25 & \\
  \frac{16}{9} z^{2} + z^{2} &= 25 & \\
  \frac{25}{9} z^{2} &= 25 & \\
  z^{2} &= 9 & \\
  z &= \pm 3 & \\
  x &= - \frac{4}{3} z = \mp 4 & \\
  \vec{a} \times \vec{b} &= \left[ -4, 0, 3 \right] &
\end{align}
$$

Får to resultater. Velger det som oppfyller høyrehåndsregelen. Dette er en ekstremt tungvindt måte å gjøre det på, men som vi ser fører det til riktig svar.

## 6.26 (ulik metode)

**a**

$$
\begin{align}
  \left[ 3, 0, 4 \right] \times \left[ 0, 1, 0 \right] &= \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    3 & 0 & 4 \\
    0 & 1 & 0
  \end{matrix}\right| = \left[ -4, 0, 3 \right] &
\end{align}
$$

**b**

$$
\left[ 1, 0, 0 \right] \times \left[ \frac{1}{2}, \frac{1}{2}, 0 \right] = \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    1 & 0 & 0 \\
    \frac{1}{2} & \frac{1}{2} & 0
  \end{matrix}\right| = \left[ 0, 0, \frac{1}{2} \right]
$$

## 6.28

**a**

$$
\begin{align}
  \left[ 5, 2, 4 \right] \times \left[ 1, 3, 2 \right] &= \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    5 & 2 & 4 \\
    1 & 3 & 2
  \end{matrix}\right| = \left[ -8, -6, 13 \right] &
\end{align}
$$

**b**

$$
\begin{align}
  \left[ -3, 1, 1 \right] \times \left[ 10, -2, -4 \right] &= \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    -3 & 1 & 1 \\
    10 & -2 & -4
  \end{matrix}\right| = \left[ -2, -2, -4 \right] &
\end{align}
$$

**c**

$$
\begin{align}
  \left[ 5, 7, 6 \right] \times \left[ -1, 0, 2 \right] &= \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    5 & 7 & 6 \\
    -1 & 0 & 2
  \end{matrix}\right| = \left[ 8, -16, -7 \right] &
\end{align}
$$

**d**

$$
\begin{align}
  \left[ - \frac{1}{2}, -1, 0 \right] \times \left[ 0, 1, -3 \right] &= \left|\begin{matrix}
    \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
    - \frac{1}{2} & -1 & 0 \\
    0 & 1 & -3
  \end{matrix}\right| = \left[ 3, -\frac{3}{2}, - \frac{1}{2} \right] &
\end{align}
$$
