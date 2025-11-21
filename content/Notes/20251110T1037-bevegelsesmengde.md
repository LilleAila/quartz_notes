---
id: 20251110T1037-bevegelsesmengde
aliases:
  - bevegelsesmengde
tags: []
date: "2025-11-10"
title: bevegelsesmengde
---

#fysikk [[20250820T0820-fysikk-1|fysikk 1]] [[20250827T0824-bevegelse|bevegelse]] [[20250910T0834-krefter|krefter]]

# bevegelsesmengde

Bevegelsesmengden er en størrelse definert som

$$
\vec{p} = m \vec{v} \,\left[ \mathrm{kg \frac{m}{s}} \right]
$$

Bevegelsesmengde er alltid bevart, uavhengig av alle eksterne faktorer som blant annet friksjon, i motsetning til for eksempel mekanisk energi.

Newtons andre lov var opprinnelig formulert ved hjelp av bevegelsesmengde:

$$
\sum F = \frac{\Delta p}{\Delta t} = \frac{mv - mv_{0}}{t} = m \cdot \frac{v - v_{0}}{t} = m \cdot a
$$

Man kan også bruke dette som følger. Det kalles også "impuls" ($I$):

$$
\sum F \cdot \Delta t = \Delta p = I
$$

Man kan også si at

$$
\sum F = p' \left( t \right)
$$

## Støt

Et støt er elastisk hvis den totale kinetiske energien til systemet er bevart. Om den kinetiske energien bilr omgjort til andre energiformer i støtet, er det uelastisk.

# Oppgaver

## 5.05 (s. 151)

Kristoffer kaster en basketball fra høyden $1.8 \,\mathrm{m}$j over gulvet slik at den får farten $9.8 \,\mathrm{\frac{m}{s}}$ rett oppover. Ballen har massen $0.63 \,\mathrm{kg}$.

**a**

> Hva er bevegelsesmengden til balen idet den kastes?

$$
\begin{align}
  p &= m v & \\
  &= 0.63 \cdot 9.8 & \\
  &= 6.173 = 6.2 &
\end{align}
$$

**b**

> Hvor lang tid tar det før bevegelsesmengden til ballen er halvert?

$$
\begin{align}
  v &= a \cdot t + v_{0} & \\
  4.9 &= -9.81 t + 9.8 & \\
  t &= 0.49 &
\end{align}
$$

**c**

> Hva er bevegelsesmengden til ballen rett før den treffer bakken?

$$
\begin{align}
  2 \cdot -9.81 \cdot -1.8 &= v^{2} - 9.8^{2} & \\
  v &= \pm 11.461 & \\
  p &= m \cdot v = -7.2 &
\end{align}
$$

Setter negativ da jeg vet at den går nedover og satte positiv retning opp.

**d**

> Hvor stor er den totale endringen i bevegelsesmengden til ballen?

$$
\Delta p = 6.2 - \left( -7.2 \right) = 13.4 \,\mathrm{kg \frac{m}{s}}
$$

## 5.06

**a**

> Hvor stor er bevegelsesmengden før og etter kollisjonen?

$$
\begin{align}
  p_{0} &= 0.8 \cdot 0.35 = 0.28 & \\
  p_{1} &= -0.4 \cdot 0.35 = -0.14 &
\end{align}
$$

**b**

> Hvor stor var endringen i bevegelsesmengde i kollisjonen?

$$
\Delta p = -0.14 - 0.28 = -0.42
$$

## 5.07

**a**

> Utled Newtons 2. lov uttrykt ved bevegelsesmengde.

$$
\begin{align}
  \sum F &= \lim_{\Delta t \to 0} \frac{\Delta p}{\Delta t} & \\
  &= p' \left( t \right) & \\
  &= \left( m \left( t \right) \cdot v \left( t \right) \right) & \\
  &= m' \left( t \right) \cdot v \left( t \right) + m \left( t \right) \cdot v' \left( t \right) & \\
  & \text{Antar konstant masse:} & \\
  \sum F &= m \cdot a \left( t \right) &
\end{align}
$$

**b**

$$
\begin{align}
  \left[ \mathrm{N} \right] &= \left[ \mathrm{\frac{kg \frac{m}{s}}{s}} \right] & \\
  \left[ \mathrm{Ns} \right] &= \left[ \mathrm{kg \frac{m}{s}} \right] &
\end{align}
$$

**c**

> Uttrykk Newtons 1. lov med bevegelsesmengde

$$
\begin{align}
  v' \left( t \right) &= 0 & \\
  \sum F &= p' \left( t \right) & \\
  &= m \cdot 0 & \\
  &= 0 & \\
  v' \left( t \right) = 0 &\implies \sum F = 0 &
\end{align}
$$

## 5.08

Et legeme har massen $0.75 \,\mathrm{kg}$ og beveger seg med bevegelsesmengden $10 \,\mathrm{kg \frac{m}{s}}$ når det blir påvirket av kraftsummen $\sum F = 5.0 \,\mathrm{N}$ i bevegelsesretningen. Kraftsummen opphører etter $4.0 \,\mathrm{s}$.

**a**

> Hvor mye endres bevegelsesmengden totalt?

$$
\begin{align}
  \sum F &= \frac{\Delta p}{\Delta t} & \\
  5 \,\mathrm{N} &= \frac{\Delta p}{4 \,\mathrm{s}} & \\
  \Delta p &= 20 \,\mathrm{kg \frac{m}{s}} &
\end{align}
$$

**b**

> Hvor stor ble farten?

$$
\begin{align}
  p &= p_{0} + \Delta p & \\
  p &= 10 + 20 = 30 \,\mathrm{kg \frac{m}{s}} & \\
  p &= m v & \\
  v &= \frac{p}{m} & \\
  v &= \frac{30}{0.75} = 40 \,\mathrm{\frac{m}{s}} &
\end{align}
$$

**c**

> Hvor langt forflyttet legemet seg på de fire sekundene?

$$
\begin{align}
  s &= \frac{1}{2} \left( v + v_{0} \right)t & \\
  s &= \frac{1}{2} \left( 40 + \frac{10}{0.75} \right) \cdot 4 & \\
  s &= 106.6667 & \\
  &\approx 0.11 \cdot 10^{3} \,\mathrm{m} = 0.11 \,\mathrm{km} &
\end{align}
$$
