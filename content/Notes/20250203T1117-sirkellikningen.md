---
id: 20250203T1117-sirkellikningen
aliases:
  - sirkellikningen
tags: []
date: "2025-02-03"
title: Sirkellikningen
---

#matte [[20250115T0716-vektorer|vektorer]]

# sirkellikningen

![20250203T1118-sirkellikning.png](Assets/20250203T1118-sirkellikning.png)

$$
\begin{align}
  r &= \left| \vec{SP} \right| & \\
  &= \left| \left[ x - x_{0}, y - y_{0} \right] \right| & \\
  &= \sqrt{\left( x - x_{0} \right)^{2} + \left( y - y_{0} \right)^{2}} & \\
  r^{2} &= \left( x - x_{0} \right)^{2} + \left( y - y_{0} \right)^{2} &
\end{align}
$$

## Oppgave 1

> [!NOTE] Eksempel 22 (fra boken)
> En sirkel har sentrum i $\left( 2, -3 \right)$ og radius $5$.
> a. Finn likningen til sirkelen
> b. Undersøk om punktene $A \left( 5, 1 \right)$ og $B \left( -2, 3 \right)$ ligger på sirkelen.

$$
25 = \left( x - 2 \right)^{2} + \left( y + 3 \right)^{2}
$$

b.

Setter inn $x$ og $y$ for å sjekke om likningen går opp.

$$
\begin{align}
  25 &= \left( 5 - 2 \right)^{2} + \left( 1 + 3 \right)^{2} & \\
  &= 3^{2} + 4^{2} & \\
  &= 25 &
\end{align}
$$

Punkt $A$ ligger på sirkelen.

$$
\begin{align}
  25 &= \left( -2 - 2 \right)^{2} + \left( 3 + 3 \right)^{2} & \\
  &= \left( -4 \right)^{2} + 6^{2} & \\
  &= 52 \implies \text{nuh uh} &
\end{align}
$$

$25 \neq 52 \implies$ Punkt $B$ ligger ikke på sirkelen.

## Oppgave 2

Finn sentrum og radius i sirkelen gitt ved likningen $x^{2} + y^{2} - 4x + 6y = 12$

> [!NOTE]
> Bruker [[20240616T1007-fullstendig-kvadrat|Fullstendig kvadrat]] og [[20240616T1007-kvadratsetningene|Kvadratsetningene]]

$$
\begin{align}
  x^{2} + y^{2} - 4x + 6y &= 12 & \\
  x^{2} - 4x + 4 - 4 + y^{2} + 6y + 9 - 9 &= 12 & \\
  \left( x - 2 \right)^{2} - 4 + \left( y + 3 \right)^{2} - 9 &= 12 & \\
  \left( x - 2 \right)^{2} + \left( y + 3 \right)^{2} &= 25 & \\
  \left( x - 2 \right)^{2} + \left( y + 3 \right)^{2} &= 5^{2} &
\end{align}
$$

Vet dermed ut fra den generelle sirkellikningen $\displaystyle \left( x - x_{0} \right) + \left( y - y_{0} \right) = r^{2}$ at sirkelen har sentrum i $\left( 2, -3 \right)$ og radius $5$.

## 6.91

Finn sentrum og radius i sirkelen uten hjelpemidler.

### a

$$
\begin{align}
  x^{2} + y^{2} - 6x + 10y &= 15 & \\
  x^{2} - 6x + 9 - 9 + y^{2} + 10y + 25 - 25 &= 15 & \\
  \left( x-3 \right)^{2} + \left( y + 5 \right)^{2} &= 15 + 9 + 25 & \\
  \left( x - 3 \right)^{2} +  \left( y + 5 \right)^{2} &= 49 = 7^{2} &
\end{align}
$$

Sirkelen har sentrum i $\left( 3, -5 \right)$ og radius $7$.

### b

$$
\begin{align}
  x^{2} + y^{2} + 2x - 8y &= 64 & \\
  x^{2} + 2x + 1 - 1 + y^{2} - 8y + 16 - 16 &= 64 & \\
  \left( x + 1 \right)^{2} + \left( y - 4 \right)^{2} &= 64 + 1 + 16 & \\
  \left( x + 1 \right)^{2} + \left( y - 4 \right)^{2} &= 81 = 9^{2} &
\end{align}
$$

Sirkelen har sentrum i $\left( -1, 4 \right)$ og radius $9$.

### c

$$
\begin{align}
  x^{2} + y^{2} + 8x &= -11 & \\
  x^{2} + 8x + 16 - 16 + y^{2} + 0y + 0 &= -11 & \\
  \left( x + 4 \right)^{2} + \left( y + 0 \right)^{2} &= -11 + 16 & \\
  \left( x + 4 \right)^{2} + y^{2} &= 5 &
\end{align}
$$

Sirkelen har sentrum i $\left( -4, 0 \right)$ og radius $\sqrt{5}$.
