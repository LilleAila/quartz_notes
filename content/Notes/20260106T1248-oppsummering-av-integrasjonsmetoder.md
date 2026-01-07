---
id: 20260106T1248-oppsummering-av-integrasjonsmetoder
aliases:
  - oppsummering av integrasjonsmetoder
tags: []
date: "2026-01-06"
title: oppsummering av integrasjonsmetoder
---

#matte [[20251111T1105-integraler|integraler]]

# oppsummering av integrasjonsmetoder

## Valg av integrasjonsmetode

Substitusjon er vanligvis den enkleste metoden for integrasjon og er derfor foretrukket i tilfeller det det kan være mulig å bruke flere metoder. Delvis integrasjon vil man bruke der man har to uttrykk som er multiplisert. Delbrøkoppspalting brukes om man har en brøk der nevneren har høyere grad enn telleren. Det er også mulig å først gjøre polynomdivisjon for å få et slikt uttrykk og deretter bruke delbrøkoppspalting, men dette er ofte tungvindt hvis man heller kunne brukt substitusjon eller delvis integrasjon.

## [[20251211T1235-delvis-integrasjon|delvis integrasjon]]

$$
\begin{align}
  \int u' \cdot v \,dx &= u \cdot v - \int u \cdot v' \,dx & \\
  \int \sin{x} \cdot e^{x} \,dx &= - \cos{x} \cdot e^{x} + \int \cos{x} \cdot e^{x} \,dx & \\
  \int \sin{x} \cdot e^{x} \,dx &= - \cos{x} \cdot e^{x} + \sin{x} \cdot e^{x} - \int \sin{x} \cdot e^{x} \,dx & \\
  2 \int \sin{x} \cdot e^{x} \,dx &= \sin{x} \cdot e^{x} - \cos{x} \cdot e^{x} \\
  \int \sin{x} \cdot e^{x} \,dx &= \frac{e^{x}}{2} \left( \sin{x} - \cos{x} \right) + C &
\end{align}
$$

## [[20251218T1042-integrasjon-ved-substitusjon|integrasjon ved substitusjon / variabelskifte]]

$$
\begin{align}
  \int u \left( x \right) \,dx &= \int \frac{u \left( x \right)}{u' \left( x \right)} \,du & \\
  \int \sin{x} \cdot e^{\left( \cos{x} \right)} \,dx & & \\
  u &= \cos{x} & \\
  \frac{du}{dx} &= - \sin{x} & \\
  dx &= \frac{du}{- \sin{x}} & \\
  \int \sin{x} \cdot e^{\left( \cos{x} \right)} \,dx &= \int \sin{x} \cdot e^{u} \cdot \frac{du}{- \sin{x}} &
  &= \int -e^{u} \,du & \\
  &= - \int e^{u} \,du & \\
  &= - \int e^{\cos{x}} \,dx & \\
  &= -e^{\cos{x}} + C &
\end{align}
$$

## [[20251218T1233-integrasjon-ved-delbrøkoppspalting|integrasjon ved delbrøkoppspalting]]

$$
\begin{align}
  \int \frac{\dots}{\left( x+a \right) \left( x+b \right)} \,dx &= \int \left( \frac{A}{\left( x+a \right)} + \frac{B}{\left( x+b \right)} \right) \,dx & \\
  \int \frac{8x - 4}{x^{2} - 4} \,dx & & \\
  \frac{8x - 4}{x^{2} - 4} &= \frac{A}{\left( x+2 \right)} + \frac{B}{\left( x-2 \right)} & \\
  8x - 4 &= A \left( x-2 \right) + B \left( x+2 \right) & \\
  x = 2 &\implies B = 3 & \\
  x = -2&\implies A = 5 & \\
  \frac{8x - 4}{x^{2} - 4} &= \frac{5}{x+2} + \frac{3}{x-2} & \\
  \int \frac{8x - 4}{x^{2} - 4} \,dx &= \int \left( \frac{5}{x+2} + \frac{3}{x-2} \right) \,dx & \\
  &= 5 \ln{\left| x + 2 \right|} + 3 \ln{\left| x - 2 \right|} + C &
\end{align}
$$
