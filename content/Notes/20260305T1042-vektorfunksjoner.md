---
id: 20260305T1042-vektorfunksjoner
aliases:
  - vektorfunksjoner
tags: []
date: "2026-03-05"
title: vektorfunksjoner
---

#matte [[20260122T1046-romgeometri|romgeometri]]

# vektorfunksjoner

Vektorfunksjoner viser punktet en vektor peker på fra origo. Det er i grunn mye det samme som en parameterfremstilling, men det er ofte enklere å jobbe med vektorfunksjoner når man skal gjøre blant annet derivasjon.

$$
\begin{align}
  l: \begin{cases}
    x &= x_{0} + at \\
    y &= y_{0} + bt^{2} \\
    z &= z_{0} + ct
  \end{cases}& \iff \vec{r}\left( t \right) = \left[ x_{0}+at, y_{0}+bt^{2}, z_{0}+ct \right] &
\end{align}
$$

Man har ofte behov for vektorfunksjoner da dette også beholder tiden.

---

Eksempel fra fysikk 2 der man har bevegelse i flere dimensjoner. I praksis er ikke $x$ og $y$ avhengige av hverandre. Her har vi gitt at $\vec{v} \left( 0 \right) = \left[ 5, 5 \cdot \sqrt{3} \right]$ og startpunktet er $\left( 0, 2 \right)$.

$$
\begin{align}
  \vec{v} \left( 0 \right) &= \left[ 5, 5 \sqrt{3} \right] & \\
  \vec{a} \left( t \right) &= \left[ 0, -9.81 \right] & \\
  \int \vec{a} \left( t \right) &= \int \vec{v}' \left( t \right) \,dx = \vec{v} \left( t \right) & \\
  \vec{v} \left( t \right) &= \int \vec{a} \left( t \right) \,dx = \left[ \int 0 \,dx, \int -9.81 \,dx \right] & \\
  \vec{v} \left( t \right) &= \left[ c_{x}, -9.81 t + c_{y} \right] & \\
  \vec{v} \left( t \right) &= \left[ 5, -9.81t + 5 \sqrt{3} \right] & \\
  \vec{r} \left( t \right) &= \int \vec{v} \left( t \right) = \left[ 5t + c, 5 \sqrt{3}t - \frac{1}{2} \cdot 9.81 t^{2} + c \right] & \\
  \vec{r} \left( t \right) &= \left[ 5t, 5 \sqrt{3}t - \frac{1}{2} \cdot 9.81 t^{2} + 2 \right] &
\end{align}
$$
