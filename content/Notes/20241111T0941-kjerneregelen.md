---
id: 20241111T0941-kjerneregelen
aliases:
  - kjerneregelen
tags: []
title: kjerneregelen
date: 2024-11-11
---

#matte [[20240616T1007-matte|matte]] [[20241104T1155-sammensatte-funksjoner|sammensatte funksjoner]] [[20240616T1007-derivasjon|derivasjon]] [[20241028T1011-derivasjonsregler|derivasjonsregler]]

# kjerneregelen

- [ ] TODO: snippets for ulike formler, og for oppsettet av de ulike oppgavetypene, for eksempel kjerneregelen

La $f$ være en sammensatt funksjon med $g$ som ytre funksjon og $u$ som kjerne.

$$
\LARGE f \left( x \right) = g \left( u \left( x \right) \right) \implies f' \left( x \right) = g' \left( u \left( x \right) \right) \cdot u' \left( x \right)
$$

Derivere den ytre funksjonen, og gange med den deriverte av kjernen. Vi skriver ofte bare $u$, i stedet for $u \left( x \right)$.

## Eksempel 1

$$
\begin{align}
    f \left( x \right) &= \left( x^{3} + 2x \right)^{3} & \\
    g \left( u \right) &= u^{3} & u \left( x \right) &= x^{3} + 2x \\
    g' \left( u \right) &= 3u^{2} & u' \left( x \right) &= 3x^{2} + 2 \\
    f' \left( x \right) &= g' \left( u \right) \cdot u' & \\
    &= \underline{\underline{3 \left( x^{3} + 2x \right)^{2} \cdot \left( 3x^{2} + 2 \right)}} &
\end{align}
$$

## Eksempel 2

$$
\begin{align}
    f \left( x \right) &= \left( 2x - 1 \right)^{4} & \\
    g \left( u \right) &= u^{4} & u \left( x \right) &= 2x-1 \\
    g' \left( u \right) &= 4u^{3} & u' \left( x \right) &= 2 \\
    f' \left( x \right) &= g' \left( u \right) \cdot u' & \\
    &= \underline{\underline{8 \left( 2x - 1 \right)^{3}}}
\end{align}
$$

## Eksempel 3

$$
\begin{align}
    f \left( x \right) = e^{3x} \\
    g \left( u \right) &= e^{u} & u \left( x \right) &= 3x & \\
    g' \left( x \right) &= e^{u} & u' \left( x \right) &= 3 & \\
    g' \left( u \right) \cdot u' &= \underline{\underline{3e^{3x}}} &
\end{align}
$$

For lineære eksponenter, ser det alltid veldig likt ut som den vanlige regelen for konstante eksponenter, men uten å redusere eksponenten.

$$
\boxed{\left( e^{kx} \right)' = ke^{kx}}
$$

## Eksempel 4

$$
\begin{align}
    g \left( x \right) &= \ln{4x} & \\
    g \left( x \right) &= \left( \ln{u} \right)' \cdot u' &  \\
    &= \frac{1}{u} 4 & \\
    &= \frac{1}{4x} \cdot 4 & \\
    &= \underline{\underline{\frac{1}{x}}} &
\end{align}
$$

Den deriverte blir alltid lik $\frac{1}{x}$, uansett hva $k$ er.

$$
\boxed{\left( \ln{kx} \right)' = \frac{1}{x}}
$$
