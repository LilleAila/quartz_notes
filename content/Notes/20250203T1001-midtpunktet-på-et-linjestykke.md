---
id: 20250203T1001-midtpunktet-på-et-linjestykke
aliases:
  - midtpunktet på et linjestykke
tags: []
date: "2025-02-03"
title: Midtpunktet på et linjestykke
---

#matte [[20250115T0716-vektorer|vektorer]]

# midtpunktet på et linjestykke

![20250203T1002-midtpunkt-linjestykke.png](Assets/20250203T1002-midtpunkt-linjestykke.png)

$$
\begin{align}
    \vec{OM} &= \vec{OA} + \vec{AM} = \vec{OA} + \frac{1}{2} \vec{AB} & \\
    &= \left[ x_{1}, y_{1} \right] = \frac{1}{2} \left[ x_{2} - x_{1}, y_{2} - y_{1} \right] & \\
    &= \left[ x_{1}, y_{1} \right] = \frac{1}{2} \left[ x_{2}, y_{2} \right] + \frac{1}{2} \left[ -x_{1}, -y_{2} \right] & \\
    &= \left[ x_{1}, y_{1} \right] + \left[ \frac{1}{2} x_{2}, \frac{1}{2} y_{2} \right] - \left[ \frac{1}{2} x_{1}, \frac{1}{2} y_{1} \right] & \\
    &= \left[ x_{1} - \frac{1}{2} x_{1} + \frac{1}{2} x_{2}, y_{1} - \frac{1}{2} y_{1} + \frac{1}{2} y_{2} \right] & \\
    &= \left[ \frac{1}{2} x_{1} + \frac{1}{2} x_{2}, \frac{1}{2} y_{1} + \frac{1}{2} y_{2} \right] & \\
    \vec{OM} &= \left[ \frac{x_{1} + x_{2}}{2}, \frac{y_{1} + y_{2}}{2} \right] & \\
    \text{Koordinater til $M$} &= \left( \frac{x_{1} + x_{2}}{2}, \frac{y_{1} + y_{2}}{2} \right) &
\end{align}
$$

## Oppgaver

### 6.85

Finn koordinatene til midtpunktet på linjestykket $AB$ når

#### a

$$
\begin{align}
    A \left( 4, 2 \right) & \land B \left( 10, 6 \right) & \\
    M &= \left( \frac{4+10}{2}, \frac{2+6}{2} \right) & \\
    &= \left( 7, 4 \right) &
\end{align}
$$

#### b

$$
\begin{align}
  A \left( 0, 2 \right) & \land B \left( 3, 8 \right) & \\
  M &= \left( \frac{0 + 3}{2}, \frac{2 + 8}{2} \right) & \\
  &= \left( \frac{3}{2}, 5 \right) &
\end{align}
$$

#### c

$$
\begin{align}
  A \left( -4, 2 \right) & \land B \left( 6, 2 \right) & \\
  M &= \left( \frac{-4 + 6}{2}, \frac{2 + 2}{2} \right) & \\
  &= \left( 1, 2 \right) &
\end{align}
$$
