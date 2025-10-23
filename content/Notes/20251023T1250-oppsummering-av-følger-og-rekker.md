---
id: 20251023T1250-oppsummering-av-følger-og-rekker
aliases:
  - oppsummering av følger og rekker
tags: []
date: "2025-10-23"
title: oppsummering av følger og rekker
---

#matte [[20250526T1040-matte-r2|Matte R2]] [[20250930T1107-følger|følger]] [[20251002T1037-rekker|rekker]]

# oppsummering av følger og rekker

## Aritmetiske følger og rekker

$$
\begin{align}
  a_{n} &= a_{n-1} + d & \\
  a_{n} &= a_{1} + d \left( n - 1 \right) & \\
  s_{n} &= \frac{n}{2} \left( a_{1} + a_{n} \right) &
\end{align}
$$

## Geometriske følger og rekker

$$
\begin{align}
  a_{n} &= k \cdot a_{n-1} & \\
  k &= \frac{a_{n}}{a_{n-1}} & \\
  a_{n} &= a_{1} \cdot k^{\left( n-1 \right)} & \\
  s_{n} &= a_{1} \frac{k^{n} - 1}{k - 1} & \\
\end{align}
$$

### Uendelige rekker

Rekken konvergerer mot en spesifikk verdi om $-1 < k < 1$, og divergerer om $-1 \geq k$ eller $k \geq 1$.

$$
\begin{align}
  -1 < k < 1 &\iff \left| k \right| < 1 \iff k^{2} < 1 & \\
  \lim_{n \to \infty} k^{n} = 0 &\implies s = \frac{a_{1}}{1 - k} &
\end{align}
$$
