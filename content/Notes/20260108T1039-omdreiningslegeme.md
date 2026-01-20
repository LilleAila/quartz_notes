---
id: 20260108T1039-omdreiningslegeme
aliases:
  - omdreiningslegeme
tags: []
date: "2026-01-08"
title: omdreiningslegeme
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# omdreiningslegeme

Man kan finne volumet til et tredimensjonalt objekt ved hjelp av omdreiningslegemet. Dette kan brukes så lenge radiusen til sirkelen kan representeres som en funksjon $f \left( x \right)$. Da har man at arealet av sirkelen med en gitt radius er $\pi \cdot r^{2}$. Basert på dette kan man finne volumet ved

$$
V = \pi \int_{a}^{b} f \left( x \right)^{2} \,dx
$$

---

Funksjonen $f \left( x \right)$ representerer radiusen til en sirkel på et gitt punkt i en kjegle.

$$
\begin{align}
  f \left( x \right) &= x & \\
  V &= \pi \int_{a}^{b} x^{2} \,dx & \\
  &= \pi \cdot \left[ \frac{1}{3}x^{3} \right]_{a}^{b} &
\end{align}
$$

---

Skal finne volumet av en kule. Må ta en halvsirkel pga $y^{2}$.

$$
\begin{align}
  x^{2} + y^{2} &= r^{2} & \\
  f \left( x \right) &= \sqrt{r^{2} - x^{2}} & \\
  V &= \pi \int_{-r}^{r} f \left( x \right)^{2} \,dx & \\
  &= \pi \int_{-r}^{r} \sqrt{r^{2} - x^{2}}^{2} \,dx & \\
  &= \pi \int_{-r}^{r} \left( r^{2} - x^{2} \right) \,dx & \\
  &= \pi \left[ r^{2}x - \frac{1}{3}x^{3} \right]_{-r}^{r} & \\
  &= \pi \left( \left( r^{3} - \frac{1}{3}r^{3} \right) - \left( -r^{3} + \frac{1}{3} r^{3} \right) \right) & \\
  &= \pi \left( 2r^{3} - \frac{2}{3} r^{3} \right) &  \\
  &= \pi \left( \frac{6 r^{3}}{3} - \frac{2r^{3}}{3} \right) & \\
  V &= \frac{4 \pi r^{3}}{3} &
\end{align}
$$

## Buelengde

![[20260108T1039-omdreiningslegeme 2026-01-13 11.05.48.excalidraw.svg]]

$$
\begin{align}
    \Delta s &= \sqrt{\left( \Delta x \right)^{2} + \left( \Delta y \right)^{2}} & \\
    &= \sqrt{\left( 1 + \left( \frac{\Delta y}{\Delta x} \right)^{2} \right) \cdot \left( \Delta x \right)^{2}} & \\
    &= \sqrt{1 + \left( \frac{\Delta y}{\Delta x} \right)^{2}} \cdot \Delta x& \\
    & \Delta x \to 0 & \\
    s &= \int_{a}^{b} \sqrt{1 + f' \left( x \right)^{2}} \,dx &
\end{align}
$$

## Overflate til omdreiningslegeme

$$
\begin{align}
  \text{Overflate} &= 2 \cdot \pi \cdot r \cdot \Delta s & \\
  O &= 2 \pi \int_{a}^{b} f \left( x \right) \cdot \sqrt{1 + f' \left( x \right)^{2}} \,dx &
\end{align}
$$

# Oppgaver [NDLA](https://ndla.no/r/matematikk-r2/volum-og-buelengde/60f5bcf9ee)

## Oppgave 1

$$
\begin{align}
  f \left( x \right) &= 2x & \\
  s &= \sqrt{\left( \Delta x \right)^{2} + \left( \Delta y \right)^{2}} & \\
  &= \sqrt{\left( 3 - 0 \right)^{2} + \left( 6 - 0 \right)^{2}} & \\
  &= \sqrt{45} & \\
  &= \sqrt{9} \sqrt{5} & \\
  &= 3 \sqrt{5} & \\
  s &= \int_{0}^{3} \left( \sqrt{1 + \left( f' \left( x \right) \right)^{2}} \right) \,dx & \\
  &= \int_{0}^{3} \left( \sqrt{1 + \left( 2 \right)^{2}} \right) \,dx & \\
  &= \int_{0}^{3} \left( \sqrt{5} \right) \,dx & \\
  &= \left[ \sqrt{5} x \right]_{0}^{3} & \\
  &= 3 \sqrt{5} &
\end{align}
$$
