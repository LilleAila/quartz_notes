---
id: 20251218T1233-integrasjon-ved-delbrøkoppspalting
aliases:
  - integrasjon ved delbrøkoppspalting
tags: []
date: "2025-12-18"
title: integrasjon ved delbrøkoppspalting
---

#matte [[20251111T1105-integraler|integraler]]

# integrasjon ved delbrøkoppspalting

Dette er mer algebra enn en nødvendigvis en integrasjonsmetode. Man forkorter nevneren, setter det opp som et uttrykk med to ukjente $A$ og $B$, og setter $x$ slik at hver av dem blir $0$. Kan da dele det inn i flere brøker og integrere videre med [[20251218T1042-integrasjon-ved-substitusjon|substitusjon]] eller [[20251211T1235-delvis-integrasjon|delvis integrasjon]].

Noen ganger er det mulig å bruke substitusjon i stedet for delbrøkoppspalting. Vanligvis vil man bruke delbrøkoppspalting der nevner har høyere grad enn telleren. Om telleren har høyest grad kan det være nødvendig å gjøre polynomdivisjon.

$$
\begin{align}
  \int \frac{2x + 8}{x^{2} + 5x + 6} \,dx & & \\
  \frac{2x + 8}{\left( x + 3 \right) \left( x + 2 \right)} &= \frac{A}{\left( x + 3 \right)} + \frac{B}{\left( x + 2 \right)} & \\
  2x + 8 &= A \left( x + 2 \right) + B \left( x + 3 \right) & \\
  x = -3 & & \\
  2 \cdot \left( -3 \right) + 8 &= A \left( -3 + 2 \right) + B \left( -3 + 3 \right) & \\
  -6 + 8 &= A \cdot \left( -1 \right) & \\
  A &= -2 & \\
  x = -2 & & \\
  2 \cdot \left( -2 \right) + 8 &= A \left( -2 + 2 \right) + B \left( -2 + 3 \right) & \\
  B &= 4 & \\
  \frac{2x + 8}{\left( x + 3 \right) \left( x + 2 \right)} &= \frac{4}{\left( x + 2 \right)} - \frac{2}{\left( x + 3 \right)} & \\
  \int \frac{2x + 8}{x^{2} + 5x + 6} \,dx &=\int \frac{4}{x + 2} \,dx - \int \frac{2}{x + 3} \,dx & \\
  &= 4 \ln{\left| x + 2 \right|} - 2 \ln{\left| x + 3 \right|} + C &
\end{align}
$$

# Oppgaver

## Eksempel 21 (s. 253)

$$
\begin{align}
  \int \frac{8x - 4}{x^{2} - 4} \,dx &= \int \frac{8x - 4}{\left( x + 2 \right) \left( x - 2 \right)} & \\
  \frac{8x - 4}{\left( x + 2 \right) \left( x - 2 \right)} &= \frac{A}{x+2} + \frac{B}{x-2} & \\
  8x - 4 &= A \left( x-2 \right) + B \left( x+2 \right) & \\
  x = -2 & & \\
  8 \left( -2 \right) - 4 &= A \left( -2 - 2 \right) + B \left( -2 + 2 \right) & \\
  -20 &= -4A & \\
  A &= 5 & \\
  x = 2 & & \\
  8 \cdot 2 - 4 &= A \left( 2 - 2 \right) + B \left( 2 + 2 \right) & \\
  12 &= 4B & \\
  B &= 3 & \\
  \int \frac{5}{x+2} \,dx + \int \frac{3}{x - 2} \,dx &= 5 \ln{\left| x + 2 \right|} + 3 \ln{\left| x - 2 \right|} + C &
\end{align}
$$

## Eksempel 22

$$
\int \frac{x^{3} + 3x^{2} - 2x - 12}{x^{2} - 4} \,dx
$$

Telleren har høyere grad enn nevneren. Må derfor gjøre polynomdivisjon:

$$
\begin{array}{r r r r r l}
    (& x^{3} & +3x^{2} & - 2x &-12) &: \left( x^{2} - 4 \right) = x + 3 + \dfrac{2x}{x^{2} - 4} \\
    &-x^{3} & &+4x & & \\
    && 3x^{2} &+ 2x &- 12 & & \\
    && -3x^{3} & &+12 & & \\
    &&& 2x &&&
\end{array}
$$

I løsningsforslaget brukes delbrøkoppspalting, men jeg velger å heller gjøre integrasjon ved substitusjon.

$$
\begin{align}
  \int \frac{x^{3} + 3x^{2} - 2x - 12}{x^{2} - 4} \,dx &= \int \left( x + 3 + \frac{2x}{x^{2} - 4} \right) \,dx & \\
  &= \frac{1}{2}x^{2} + 3x + \int \frac{2x}{x^{2} - 4} \,dx & \\
  u &= x^{2} - 4 & \\
  \frac{du}{dx} &= 2x & \\
  dx &= \frac{du}{2x} & \\
  \int \frac{2x}{x^{2} - 4} \,dx &= \int \frac{2x}{u} \cdot \frac{du}{2x} & \\
  &= \int \frac{1}{u} \,du & \\
  &= \ln{\left| u \right|} + C & \\
  &= \ln{\left| x^{2} - 4 \right|} & \\
  \int \frac{x^{3} + 3x^{2} - 2x - 12}{x^{2} - 4} \,dx &= \frac{1}{2}x^{2} + 3x + \ln{\left| x^{2} - 4 \right|} + C & \\
  &= \frac{1}{2} x^{2} + 3x + \ln{\left| \left( x+2 \right) \left( x-2 \right) \right|} & \\
  &= \frac{1}{2} x^{2} + 3x + \ln{\left| x+2 \right|} + \ln{\left| x - 2 \right|} &
\end{align}
$$

## 4.50 (s. 257) TODO
