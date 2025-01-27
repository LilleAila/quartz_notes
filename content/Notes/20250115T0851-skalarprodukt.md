---
id: 20250115T0851-skalarprodukt
aliases:
  - skalarprodukt
tags: []
date: "2025-01-15"
title: Skalarprodukt
---

#matte [[20240616T1007-matte|matte]] [[20250115T0716-vektorer|vektorer]]

# skalarprodukt

![[20250115T0851-skalarprodukt 2025-01-15 09.52.35.excalidraw]]

Hvis vektorene er noenlunde i samme retning, blir cosinus-verdien positiv. Hvis de spriker fra hverandre, blir cosinus-verdien negativ.

- [ ] TODO: flytte dette inn i notat om sinus / cosinus

![[20250115T0851-skalarprodukt 2025-01-15 10.02.42.excalidraw]]

![[20250115T0851-skalarprodukt 2025-01-15 10.04.44.excalidraw]]

Gitt to vektorer $\vec{a}$ og $\vec{b}$
La $a$ være vinkelen mellom vektorene.
Skalarproduktet (eller prikkproduktet) mellom vektorene er da

$$
\vec{a} \cdot \vec{b} = \left| a \right| \cdot \left| b \right| \cdot \cos{\alpha}
$$

Resultatet er en skalar, ikke en vektor. Dette er et slags mål på hvor mye de peker i samme retning.

![[20250115T0851-skalarprodukt 2025-01-15 10.11.18.excalidraw]]

Hvis vektorene står vinkelrette på hverandre, kaller vi dem ortogonale. Det vil si at $\alpha = 90 ^{\circ}$

$$
\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0
$$

## Regneregler

$$
\begin{align}
  \vec{a} \cdot \vec{b} & = \vec{b} \cdot \vec{a} & \\
  \vec{a} \cdot \left( \vec{b} + \vec{c} \right) & = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c} & \\
  \left( \vec{a} + \vec{b} \right) \cdot \left( \vec{c} + \vec{d} \right) & = \vec{a} \cdot \vec{c} + \vec{a} \cdot \vec{d} + \vec{b} \cdot \vec{c} + \vec{b} \cdot \vec{d} & \\
  \left( s \vec{a} \right) \cdot \left( t \vec{b} \right) & = \left( s \cdot t \right) \left( \vec{a} \cdot \vec{b} \right) & 
\end{align}
$$

---

Oppfører seg stort sett som tall, og dermed kan vi også bruke kvadratsetningene.

$$
\begin{align}
  \left( \vec{a} + \vec{b} \right) ^{2} & = \vec{a} ^{2} + 2 \vec{a} \cdot \vec{b} + \vec{b} ^{2} & \\
  \left( \vec{a} - \vec{b} \right) ^{2} & = \vec{a} ^{2} - 2 \vec{a} \cdot \vec{b} + \vec{b} ^{2} & \\
  \left( \vec{a} + \vec{b} \right) \cdot \left( \vec{a} - \vec{b} \right) & = \vec{a} ^{2 -} \vec{b} ^{2} & 
\end{align}
$$

---

$$
\begin{align}
  \vec{a} \cdot \vec{a} & = \left| \vec{a} \right| \cdot \left| \vec{a} \right| \cdot \cos{0} & \\
  & = \left| \vec{a} \right| \cdot \left| \vec{a} \right| \cdot 1 & \\
  \vec{a} ^{2} & = \left| \vec{a} \right| ^{2} & \\
  \left| \vec{a} \right| & = \sqrt{\vec{a} ^{2}} & 
\end{align}
$$
