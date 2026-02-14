---
id: 20260210T1105-areal-og-volum
aliases:
  - areal og volum
tags: []
date: "2026-02-10"
title: areal og volum
---

#matte [[20260122T1046-romgeometri|romgeometri]] [[20260129T1117-vektorprodukt|vektorprodukt]]

# areal og volum

![[20260210T1105-areal-og-volum 2026-02-10 11.06.05.excalidraw.svg]]

$$
\begin{align}
  \sin{\theta} &= \frac{h}{\left| \vec{AD} \right|} & \\
  h &= \left| \vec{AD} \right| \cdot \sin{\theta} & \\
  A &= \left| \vec{AB} \right| \cdot h & \\
  A &= \left| \vec{AB} \right| \cdot \left| \vec{AD} \right| \cdot \sin{\theta} & \\
  A_{\text{parallellogram}} &= \left| \vec{AB} \times \vec{AD} \right| &
\end{align}
$$

Kan finne arealet ved hjelp av vektorproduktet, da arealet av parallellogrammet er lik lengden av vektorproduktet. Det samme konseptet kan man da bruke til å finne arealet av en vilkårlig figur ved å dele opp i trekanter.

$$
A_{\text{trekant}} = \frac{1}{2} \left| \vec{a} \times \vec{b} \right|
$$

## Volum

Skal finne volumet av et parallellepiped (parallellogram i tre dimensjoner)

![[20260210T1105-areal-og-volum 2026-02-10 11.16.25.excalidraw.svg]]

Bruker nesten samme fremgangsmåte her som med arealet over.

$$
\begin{align}
  V &= G \cdot h & \\
  V &= \left| \vec{a} \times \vec{b} \right| \cdot h & \\
  \cos{\theta} &= \frac{h}{\left| \vec{c} \right|} &  \\
  h &= \left| \vec{c} \right| \cdot \cos{\theta} & \\
  V &= \left| \vec{a} \times \vec{b} \right| \cdot \left| \vec{c} \right| \cdot \cos{\theta} & \\
  V_{\text{parallellepiped}} &= \left| \vec{a} \times \vec{b} \cdot \vec{c} \right| &
\end{align}
$$

Kan da basert på samme som for arealet finne

$$
\begin{align}
  V_{\text{prisme}} &= \frac{1}{2} \left| \vec{a} \times \vec{b} \cdot \vec{c} \right| & \\
  V_{\text{pyramide}} &= \frac{1}{3} \left| \vec{a} \times \vec{b} \cdot \vec{c} \right| & \\
  V_{\text{Tetraeder}} &= \frac{1}{6} \left| \vec{a} \times \vec{b} \cdot \vec{c} \right| &
\end{align}
$$

---

$$
\begin{align}
  \vec{a} \times \vec{b} &= \left|\begin{matrix}
      \vec{e_{x}} & \vec{e_{y}} & \vec{e_{z}} \\
      a_{x} & a_{y} & a_{z} \\
      b_{x} & b_{y} & b_{z}
    \end{matrix}\right| & \\
    &= \vec{e_{x}} \left| \begin{matrix}
        a_{y} & a_{z} \\
        b_{y} & b_{z}
    \end{matrix} \right| + \vec{e_{y}} \left| \begin{matrix}
        a_{x} & a_{z} \\
        b_{x} & b_{z}
    \end{matrix} \right| + \vec{e_{z}} \left| \begin{matrix}
        a_{x} & a_{y} \\
        b_{x} & b_{y}
    \end{matrix} \right| & \\
    \vec{a} \times \vec{b} \cdot \vec{c} &= \left[ \vec{e_{x}} \left| \begin{matrix}
            a_{y} & a_{z} \\
            b_{y} & b_{z}
        \end{matrix} \right| , \vec{e_{y}} \left| \begin{matrix}
            a_{x} & a_{z} \\
            b_{x} & b_{z}
        \end{matrix} \right| , \vec{e_{z}} \left| \begin{matrix}
            a_{x} & a_{y} \\
            b_{x} & b_{y}
        \end{matrix} \right| \right] \cdot \left[ c_{x}, c_{y}, c_{z} \right] & \\
    &= \vec{c_{x}} \left| \begin{matrix}
        a_{y} & a_{z} \\
        b_{y} & b_{z}
    \end{matrix} \right| + \vec{c_{y}} \left| \begin{matrix}
        a_{x} & a_{z} \\
        b_{x} & b_{z}
    \end{matrix} \right| + \vec{c_{z}} \left| \begin{matrix}
        a_{x} & a_{y} \\
        b_{x} & b_{y}
    \end{matrix} \right| & \\
    &= \left|\begin{matrix}
      \vec{c_{x}} & \vec{c_{y}} & \vec{c_{z}} \\
      a_{x} & a_{y} & a_{z} \\
      b_{x} & b_{y} & b_{z}
    \end{matrix}\right| & \\
    V_{\text{parallellepiped}} &= \left| \left|\begin{matrix}
      \vec{c_{x}} & \vec{c_{y}} & \vec{c_{z}} \\
      a_{x} & a_{y} & a_{z} \\
      b_{x} & b_{y} & b_{z}
    \end{matrix}\right| \right| &
\end{align}
$$

Man tar absoluttverdien til slutt siden volumet ikke kan være negativt. Man vil velge den øverste raden som vektoren med flest null-koordinater for å gjøre det lettest mulig.

# Oppgaver

## 6.34 (s. 384)

> Regn ut volumet av parallellepipedet utspent av vektorene $\vec{u}$, $\vec{v}$ og $\vec{w}$.

$$
\begin{align}
  \vec{u} &= \left[ 3, 2, 4 \right] & \\
  \vec{v} &= \left[ 4, 6, 1 \right] & \\
  \vec{w} &= \left[ 5, 1, 1 \right] & \\
  V &= \left| \left| \begin{matrix} 3 & 2 & 4 \\ 4 & 6 & 1 \\ 5 & 1 & 1 \end{matrix} \right| \right| & \\
  &= \left| 15 - \left( -2 \right) + \left( -104 \right) \right| & \\
  &= \left| -87 \right| & \\
  &= 87 &
\end{align}
$$

## 6.35

**a**

$$
\begin{align}
  \vec{AB} &= \left[ 5, 0, 0 \right] & \\
  \vec{BC} &= \left[ 4, 6, 0 \right] & \\
  A &= \left| \vec{AB} \times \vec{BC} \right| & \\
  &= \left| \left[ 0, 0, 30 \right] \right| & \\
  &= 30 &
\end{align}
$$

**b**

$$
\begin{align}
  h &= 4 & \\
  V &= G h & \\
  &= 4 \cdot 30 = 120 &
\end{align}
$$
