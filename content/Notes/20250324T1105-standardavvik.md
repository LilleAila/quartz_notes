---
id: 20250324T1105-standardavvik
aliases:
  - standardavvik
tags: []
date: "2025-03-24"
title: standardavvik
---

#matte [[20240616T1007-matte|Matte]]

# standardavvik

$$
s = \sqrt{\frac{1}{n-1} \left[ \left( y_{1} - \bar{y} \right)^{2} + \left( y_{2} - \bar{y} \right)^{2} + \dots + \left( y_{n} - \bar{y} \right)^{2} \right]}
$$

## Oppgave 7.38 - forsøk

På de foregående sidene har vi studert sammenhengen mellom hvor langt en klinkekule triller, og hvor lang tid den bruker. For alle forsøkene var hellingen av skråplanet den samme.
Et annet forsøk vi kan gjøre, er å endre hellingen av skråplanet og studere hvilken betydning det har for tiden kula bruker på å trille fra toppen av skråplanet.

1. La først den ene enden av skråplanet være 3 cm høyere enn den andre. Trill kula fem ganger fra toppen av skråplanet og mål hvor lang tid det tar. Regn ut gjennomsnitt, standardavvik og standardfeil.
2. Gjenta forsøket i oppgave a når den ene enden av skråplanet er 6 cm, 9 cm og 12 cm høyere enn den andre. Regn ut gjennomsnitt, standardavvik og standardfeil for hvert av de tre forsøkene.
3. Lag en figur som viser gjennomsnittstidene for forsøkene i oppgavene a og b med feilmarginer.
4. Undersøk om du kan bruke en regresjonsfunksjon til å beskrive hvordan tiden kula bruker, avhenger av hellingen til skråplanet.

---

3 cm på enden, langs hele.

4.43
3.96
4.03
3.68
4.31

6 cm på enden, langs hele

2.69
2.88
2.78
2.86
3.10

9 cm på enden, langs hele

2.38
2.28
2.44
2.21
2.51

12 cm på enden, langs hele

1.75
1.91
1.99
2.11
2.09

---

Måle vinkelen:

a = $3$ (høyde ved ende)
b = $\sqrt{120 ^{2} - 3^{2}} \approx 119.96$
c = $120$ (lengde på flate)

$$
\begin{align}
  a ^{2} &= b ^{2} + c ^{2} - 2 \cdot b \cdot c  \cdot \cos{A} & \\
  3^{2} &= 119.96^{2} + 120^{2} - 2 \cdot \sqrt{120^{2} - 3^{2}} \cdot 120 \cdot \cos{A} & \\
  -28782 &= 2 \cdot \sqrt{120^{2} - 3^{2}} \cdot 120 \cdot \cos{A} & \\
  -0.9996 &\approx \cos{A} & \\
  A &\approx 3.1\degree &
\end{align}
$$
