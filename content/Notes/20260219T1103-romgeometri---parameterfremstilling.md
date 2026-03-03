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

Fungerer i praksis nøyaktig det samme som [[20250312T0723-parameterframstilling|parameterframstilling]] i to dimensjoner. I det kartesiske koordinatsystemet kan man lage en parameterfremstilling som en linje ved hjelp av et vilkårlig punkt på linjen og en vilkårlig retningsvektor.

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

## Vinkel mellom linjer

Man finner vinkelen mellom retningsvektorene. Det finnes to muligheter for resultatet. Man velger da den som er $\leq90\degree$. Det vil si at hvis vi får en vinkel over $90\degree$, må vi heller ta $180\degree - \angle u$. Altså har vi at vinkelem $\angle v$ mellom to linjer er

$$
\begin{align}
  u > 90\degree & \implies v = 180\degree - u & \\
  u \leq 90\degree &\implies v = u &
\end{align}
$$

## Vinkel mellom linje og plan

Man finner vinkelen mellom linjen og normalvektoren til planet. Altså vil vi ikke vinne $\angle u$, men vi må kompensere for at vi bruker normalvektoren i stedet for en retningevektor for en linje. Altså har vi at

$$
\begin{align}
  u < 90\degree &\implies v = 90\degree - u & \\
  u \geq 90\degree &\implies v = u - 90\degree &
\end{align}
$$

Eller generelt:

$$
v = \left| 90\degree - u \right|
$$

## Avstand fra punkt til linje

Vi har gitt en linnje $l$, og et punkt $P$. Vi lager et punkt $Q$ på linjen $l$ slik at vektoren $\vec{QP}$ står ortogonalt på linjen. Vi vet at $\vec{QP}$ er parallell med en normalvektor til linjen. Kan da sette opp en parameterfremstilling med kun én ukjent, t:

$$
Q = \begin{cases}
  x = x_{0} + at \\
  y = y_{0} + bt \\
  z = z_{0} + ct
\end{cases}
$$

---

Vi kan også definere en funksjon slik at $\left| \vec{QP} \right| = a \left( t \right)$, og bruke $a' \left( t \right) = 0$ for å finne den minste mulige lengden på $\vec{QP}$.
