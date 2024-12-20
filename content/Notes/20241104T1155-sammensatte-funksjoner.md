---
id: 20241104T1155-sammensatte-funksjoner
aliases:
  - sammensatte funksjoner
  - komposisjon
tags: []
title: Sammensatte funksjoner
date: 2024-11-04
---

#matte [[20240616T1007-matte|matte]]

# sammensatte funksjoner

$$
f \left( x \right) = \sqrt[3]{3x^{3} - 3x}
$$

Dette er en sammensatt funksjon. Vi kan skrive innsiden av kvadratroten som $u \left( x \right)$.

$$
\begin{align}
    u \left( x \right) &= 3x^{3} - 3x \\
    f \left( x \right) &= \sqrt[3]{u \left( x \right)} \text{, når $u \left( x \right) = 3x^{3} - 3x$} \\
    g \left( u \right) &= \sqrt[3]{u} \\
    f \left( x \right) &= g \left( u \left( x \right) \right)
\end{align}
$$

Her er $u$ den indre funksjonen (også kalt kjerne), og $g$ er den ytre funksjonen. $\sqrt[3]{3x^{3} - 3x}$ er en komposisjon av to funksjoner.

Skrivemåte for funksjonskomposisjon: $\displaystyle g \circ u$
