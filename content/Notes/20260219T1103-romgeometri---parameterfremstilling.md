---
id: 20260219T1103-romgeometri---parameterfremstilling
aliases:
  - Romgeometri - parameterfremstilling
tags: []
date: "2026-02-19"
title: Romgeometri - parameterfremstilling
---

#matte [[20260122T1046-romgeometri|romgeometri]]

# Romgeometri - parameterfremstilling

Fungerer i praksis nøyaktig det samme som [[20250312T0723-parameterframstilling|parameterframstilling]] i to dimensjoner. I det kartesiske koordinatsystemet kan man lage en parameterfremstilling som en linje ved

$$
\begin{align}
  &\begin{cases}
    x = x_{0} + at \\
    y = y_{0} + bt \\
    z = z_{0} + ct
  \end{cases} &
\end{align}
$$

Der man har et kjent punkt og en vektor. Man kan få en kurve hvis en av verdiene ikke er lineær, for eksempel en av

$$
\begin{align}
  &\begin{cases}
    x = x_{0} + \sin{t} \\
    y = y_{0} + at^{2} \\
    z = z_{0} + e^{t}
  \end{cases} &
\end{align}
$$

Generelt kaller vi alt som ikke er lineært en kurve.

$$
\begin{align}
  \text{Sirkel} &: \left( x - x_{0} \right)^{2} + \left( y-y_{0} \right)^{2} & \\
  \text{Enhetssirkelen} &: x^{2} + y^{2} = 1 & \\
  \text{Enhetssirkelen} &: \begin{cases}
    x = \cos{t} \\
    y = \sin{t}
  \end{cases}, t \in \left[ 0, 2 \pi \right] &
\end{align}
$$
