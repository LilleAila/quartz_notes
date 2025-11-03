---
id: 20251103T1302-fysikk-forsøk-energi
aliases:
  - fysikk forsøk energi
tags: []
date: "2025-11-03"
title: fysikk forsøk energi
---

#fysikk [[20250820T0820-fysikk-1|fysikk 1]] [[20251022T0820-energi|energi]]

# fysikk forsøk energi

## Utstyr

- Kule
- Bane for kulen til å trille
- Måleverktøy
- Mobilkamera
- PC med tracker installert

## Fremgangsmåte

Slipper kulen fra øverste punktet på banen, og filmer mens den ruller langs banen. Tar deretter denne videofilen og putter den inn i tracker, og lager en track som følger kulen. Kan videre bruke denne dataen i utregningene.

## Resultater

Målt data via tracker, brukt grafer for $y$-verdien og for farten $v$ mot tid og ekstrahert verdiene for noen få viktige punkter:

![20251103T1300-tracker-tracking-1.png](Assets/20251103T1300-tracker-tracking-1.png)

> [!NOTE]
> Tracker-filen kan lastes ned [her](Assets/potensiell-vs-kinetisk-energi-fysikk.trz)

$$
\begin{align}
  & \text{Toppen av banen} & \\
  h_{0} &= 0.526 \,\mathrm{m} & \\
  v_{0} &= 0 \,\mathrm{\frac{m}{s}} & \\[5mm]
  & \text{Før sirkelen} & \\
  h_{1} &= 0.09157 \,\mathrm{m} & \\
  v_{1} &= 3.059 \,\mathrm{\frac{m}{s}} & \\[5mm]
  & \text{Bunnen av sirkelen} & \\
  h_{2} &= 0.01923 \,\mathrm{m} & \\
  v_{2} &= 2.052 \,\mathrm{\frac{m}{s}} & \\[5mm]
  & \text{Slutten av banen} & \\
  h_{3} &= 0 \,\mathrm{m} & \\
  v_{3} &= 1.762 \,\mathrm{\frac{m}{s}} &
\end{align}
$$

$$
\begin{align}
  E_{P0} &= m \cdot 9.81 \cdot 0.526 & \\
  \frac{E_{P0}}{m} &= 5.51322 & \\
  E_{K0} &= \frac{1}{2} m \cdot 0^{2} & \\
  \frac{E_{K0}}{m} &= 0 & \\
  \frac{\sum E_{0}}{m} &= 5.513 & \\[10mm]
  E_{P1} &= m \cdot 9.81 \cdot 0.09157 \\
  \frac{E_{P1}}{m} &= 0.8983017 & \\
  E_{K1} &= \frac{1}{2} m \cdot 3.059^{2} & \\
  \frac{E_{K1}}{m} &= 4.6787405 & \\
  \frac{\sum E_{1}}{m} &= 5.577 & \\[10mm]
  E_{P2} &= m \cdot 9.81 \cdot 0.01923 & \\
  \frac{E_{P2}}{m} &= 0.1886463 & \\
  E_{K2} &= \frac{1}{2} m \cdot 2.052^{2} & \\
  \frac{E_{K2}}{m} &= 2.105352 & \\
  \frac{\sum E_{2}}{m} &= 2.294 & \\[10mm]
  E_{P3} &= m \cdot 9.81 \cdot 0 \\
  \frac{E_{P3}}{m} &= 0 & \\
  E_{K3} &= \frac{1}{2} m \cdot 1.762^{2} & \\
  \frac{E_{K3}}{m} &= 1.552322 & \\
  \frac{\sum E_{3}}{m} &= 1.552 &
\end{align}
$$

## Konklusjon

Ser basert på dette at energien er nesten helt bevart, innenfor måleusikkerheten, frem til sirkelen. Etter sirkelen kommer det med et energitap på over $70\%$ av $E_{P0}$. Før sirkelen er summen av $E_{P1}$ og $E_{K1}$ tilnærmet lik $E_{P0}$, som viser at energien er bevart.

Årsaken til det store energitapet fra sirkelen kan være både energitap i form av varme, lyd, etc, men jeg tror en stor del av dette skyldes feilkilder med målingene. Sannsynligvis er det noe med tracker som gjorde at den ga et dårlig svar for farten $v$ i sirkelen.
