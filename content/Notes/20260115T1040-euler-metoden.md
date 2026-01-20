---
id: 20260115T1040-euler-metoden
aliases:
  - euler metoden
tags: []
date: "2026-01-15"
title: euler metoden
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# euler metoden

Numerisk metode for å løse difflikninger.

$$
\Delta y = \Delta x \cdot y'
$$

Bruker formler fra fysikk som eksempler

---

$$
\begin{align}
  L &= k \cdot v & \\
  \sum F &= G - L = m \cdot a & \\
  mg - kv &= m a & \\
  \frac{mg - kv}{m} &= a & \\
  g - \frac{k}{m} v &= v' & \\
  \Delta v &= \Delta t \cdot v' & \\
  \Delta v &= \Delta t \cdot \left( g - \frac{k}{m} \cdot v \right) &
\end{align}
$$

---

$$
\begin{align}
  G &= \gamma \cdot \frac{Mm}{r^{2}} & \gamma = 6.67 \cdot 10^{-11} \,\mathrm{Nm^{2}kg^{-2}} \\
  m a &= \gamma \frac{Mm}{r^{2}} & \\
  a &= \gamma \frac{M}{r^{2}} &
\end{align}
$$

# Oppgaver

## 5.26 (s. 321)

$$
\begin{align}
  \frac{y'}{y - T} &= k & \\
  y' &= k \left( y - T \right) &
\end{align}
$$
