---
id: 20251030T1102-matematiske-bevis
aliases:
  - matematiske bevis
tags: []
date: "2025-10-30"
title: matematiske bevis
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# matematiske bevis

## Implikasjon

$$
a \implies b
$$

Hvis $a$, gjelder også $b$, men hvis $b$, gjelder ikke nødvendigvis $a$.

$$
\text{Det regner} \implies \text{Det er vått på bakken}
$$

## Ekvivalens

$$
\begin{align}
  2x &= 4 & \\
  &\Updownarrow & \\
  x &= 2 & \\
\end{align}
$$

## Direkte bevis

Dette er et direkte bevis. Man kan faktorisere ut $2$ og se at det passer med formelen for partall.

$$
\begin{align}
    n\,\text{er partall} &\implies n^{2} \,\text{er partall} \\
    n &= 2m  ,m \in \mathbb{Z} & \\
    n^{2} &= \left( 2m \right)^{2} = 4m^{2} = 2 \left( 2 \cdot m^{2} \right) &
\end{align}
$$

## Indirekte bevis

Kan prøve å bruke et direkte bevis som følger, men da kan man ikke komme noe videre fra dette.

$$
\begin{align}
  n^{2} \,\text{er partall} &\implies n \,\text{er partall} & \\
  n^{2} &= 2m, m \in \mathbb{Z} & \\
  n &= \sqrt{2m} &
\end{align}
$$

Ved indirekte bevis, antar man at påstanden er feil, og prøver å bevise det motsatte.

> $\text{Det regner} \implies \text{Det er vått på bakken}$
>
> $\text{Det er ikke vått på bakken} \implies \text{Det regner ikke}$

$$
\begin{align}
  n \,\text{er ikke partall} &\implies n^{2} \,\text{er ikke partall} & \\
  n &= \text{oddetall} & \\
  n &= 2m - 1 & \\
  n^{2} &= \left( 2m - 1 \right)^{2} & \\
  &= 4m^{2} - 4m + 1 & \\
  &= 2 \left( 2m^{2}  \right) - 2 \left( 2m \right) + 1 & \\
  n \,\text{oddetall} &\implies n^{2} \,\text{oddetall} &
\end{align}
$$

Har da indirekte bevist at den førstnevnte påstanden er sann.

---

$\sqrt{2}$ er irrasjonalt. Skal bevise dette ved hjelp av indirekte bevis:

> $\sqrt{2}$ kan skrives som brøk.

$$
\begin{align}
    \sqrt{2} &\in \mathbb{Q} & \\
  \sqrt{2} &= \frac{a}{b} &
\end{align}
$$

$a$ og $b$ er heltall, og $\frac{a}{b}$ er en maksimalt forkortet brøk.

$$
\begin{align}
  \frac{a^{2}}{b^{2}} &= 2 & \\
  a^{2} &= 2b^{2} & \\
  2b^{2} = \text{partall} \implies a^{2} &= \text{partall} \implies a = \text{partall} \\
  \left( 2m \right)^{2} &= 2b^{2} & \\
  2 \left( 2m \right)^{2} &= 2b^{2} & \\
  b^{2} &= 2m^{2} & \\
  b &= \text{partall} &
\end{align}
$$

Har funnet ut at både $a$ og $b$ er partall, og dette betyr at de skal kunne forkortes videre. Dette er en motsigelse til utgangspunktet der vi sier at det er en maksimalt forkortet brøk. Dermed er påstanden usann, og $\sqrt{2}$ kan ikke skrives som en brøk.

## Induksjonsbevis

$$
1^{2} + 2^{2} + 3^{2} + \dots + n^{2} = \frac{2n^{3} + 3n^{2} + n}{6}
$$

1. Vis at påstanden stemmer for en spesifikk verdi (vanligvis første)

$$
\begin{align}
  n &= 1 & \\
  1 &= \frac{2 \cdot 1 + 3 \cdot 1 + 1}{6} &
\end{align}
$$

2. Vis at om påstanden er sann for $n = k$, er den også sann for $n = k + 1$

$$
\begin{align}
    1^{2} + 2^{2} + 3^{2} + \dots + k^{2} &= \frac{2k^{3} + 3k^{2} + k}{b} & \\
1^{2} + 2^{2} + 3^{2} + \dots + k^{2} + \left( k + 1 \right)^{2} &= \frac{2 \left( k+1 \right)^{3} + 3 \left( k+1 \right)^{2} + \left( k + 1 \right)}{b} & \\
\frac{2k^{3} + 3k^{2} + k}{6} + \left( k+1 \right)^{2} &= \frac{2 \left( k + 1 \right)^{3} + 3 \left( k + 1 \right)^{2} + \left( k + 1 \right)}{6} & \\
  \frac{2k^{3} + 3k^{2} + k}{6} + \frac{6 \left( k + 1 \right)^{2}}{6} &= \frac{2 \left( k + 1 \right)^{3} + 3 \left( k + 1 \right)^{2} + k + 1}{6} & \\
  \frac{2k^{3} + 3k^{2} + k + 6k^{2} + 12k + 6}{6} &= \frac{2 \left( k^{3} + 3k^{2} + 3k + 1 \right) + 3 \left( k^{2} + 2k + 1 \right) + k + 1}{6} & \\
  \frac{2k^{3} + 9k^{2} + 13k + 6}{6} &= \frac{2k^{3} + 6k^{2} + 6k + 2 + 3k^{2} + 6k + 3 + k + 1}{6} & \\
  \frac{2k^{3} + 9k^{2} + 13k + 6}{6} &= \frac{2k^{3} + 9k^{2} + 13k + 6}{6} &
\end{align}
$$

# Oppgaver

## Eksempel 24

> Vis ved induksjon at $\left[ x^{n} \right]' = n \cdot x^{n - 1}$

$$
\begin{align}
  \left[ x^{1} \right] &= \left[ x^{0} \right]' = 1 & \\
  1 \cdot x^{1 - 1} & = x^{0} = 1 & \\
  \left[ x^{k} \right]' &= k \cdot x^{k - 1} & \\
  \left[ x^{k + 1} \right] &= \left[ x^{k} \cdot x \right]' & \\
  &= \left[ x^{k} \right]' \cdot x + x^{k} \cdot \left[ x \right]' & \\
  &= \left[ x^{k} \right]' \cdot x + x^{k} & \\
  &= k \cdot x^{k-1} \cdot x + x^{k} & \\
  &= kx^{k} + x^{k} & \\
  &= \left( x + 1 \right) \cdot x^{k} &
\end{align}
$$

Har nå ved hjelp av matematisk induksjon vist at formelen stemmer for alle $n \in \mathbb{N}$

## 3.95 (s. 196)

idk 😭

## 3.96

> Vis ved induksjon at summen av en aritmetisk rekke er gitt ved $\displaystyle \frac{a_{1} + a_{n}}{2} \cdot n$

$$
\begin{align}
  a_{1} + a_{2} + a_{3} + \dots + a_{n} &= \frac{a_{1} + a_{n}}{2} \cdot n & \\
  n = 1 \implies a_{1} &= \frac{a_{1} + a_{1}}{2} \cdot n = a_{1} & \\
  a_{1} + a_{2} + a_{3} + \dots + a_{k} &= \frac{a_{1} + a_{k}}{2} \cdot k & \\
  % a_{1} + a_{2} + a_{3} + \dots + a_{k} + a_{k+1} &= \frac{a_{1} + a_{k+1}}{2} \cdot \left( k+1 \right) & \\
  % \frac{a_{1} + a_{k}}{2} \cdot k + a_{k+1} &= \frac{a_{1} + a_{k+1}}{2} \cdot \left( k + 1 \right) & \\
  % \frac{k a_{1} + k a_{k}}{2} + \frac{2 a_{k+1}}{2} &= \frac{k a_{1} + a_{1} + k a_{k+1} + a_{k+1}}{2} & \\
  % \frac{ka_{1} + ka_{k} + 2a_{k+1}}{2} &= \frac{ka_{1} + a_{1} + ka_{k+1} + a_{k+1}}{2} & \\
  % \frac{ka_{1} + ka_{k} + 2a_{k} + 2d}{2} &= \frac{ka_{1} + a_{1} + ka_{k} + kd + a_{k} + d}{2} &
  %----------
  % a_{1} + a_{2} + a_{3} + \dots + a_{k} + a_{k+1} &= \frac{2a_{1} + d \left( k + 1 - 1 \right)}{2} & \\
  % \frac{2a_{1} + d \left( k - 1 \right)}{2} + a_{1} + dk &= \frac{2a_{1} + dk}{2} & \\
  % \frac{2a_{1} + dk - d}{2} + \frac{2a_{1}}{2} + \frac{2dk}{2} &= \frac{2a_{1} + dk}{2} & \\
  % \frac{4a_{1} + 3dk - d}{2} &= \frac{2a_{1} + dk}{2} &
  a_{1} + a_{2} + a_{3} + \dots + a_{k} &= \frac{2a_{1} + d \left( k - 1 \right)}{2} \cdot k & \\
  a_{1} + a_{2} + a_{3} + \dots + a_{k} + a_{k+1} &= \frac{2a_{1} + dk}{2} \cdot k & \\
  \frac{2a_{1} + d \left( k - 1 \right)}{2} \cdot k + a_{1} + dk &= \frac{2a_{1} + dk}{2} \cdot k & \\
  \frac{2ka_{1} + dk^{2} - dk}{2} + \frac{2a_{1}}{2} + \frac{2dk}{2} &= \frac{2ka_{1} + dk^{2}}{2} &
\end{align}
$$
