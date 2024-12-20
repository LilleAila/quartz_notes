---
id: 20241028T1009-definisjonen-av-den-deriverte
aliases:
  - definisjonen av den deriverte
tags: []
title: definisjonen av den deriverte
date: 2024-10-28
---

#matte [[20240616T1007-derivasjon|derivasjon]]

# definisjonen av den deriverte

$$
f' \left( x \right) = \lim_{\Delta x \to 0} \frac{\Delta f \left( x \right)}{\Delta x} = \lim_{\Delta x \to 0} \frac{f \left( x + \Delta x \right) - f \left( x \right)}{\Delta x}
$$

Enklere skrevet ($h = \Delta x$)

$$
\lim_{ h \to 0 } \frac{f(x+h)-f(x)}{h}
$$

Den kan brukes til å utlede ulike derivasjonsregler algebraisk.

## Eksempel 1

$$
\begin{align}
    f \left( x \right) &= 3x + 1 \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{3 \left( x + h \right) + 1 - 3x - 1}{h} \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{3h}{h} = \underline{\underline{3}}
\end{align}
$$

## Eksempel 2

$$
\begin{align}
    f \left( x \right) &= x^{2} \\
    f \left( x + h \right) &= \left( x + h \right)^{2} = x^{2} + 2xh + h^{2} \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{\left( x^{2} + 2xh + h^{2} \right) - x^{2}}{h} \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{ 2xh + h^{2}}{h} \\
    f' \left( x \right) &= \lim_{x \to 0} 2x + h = \underline{\underline{2x}}
\end{align}
$$

## Eksempel 3

$$
f \left( x \right) = x^{2} + 4x + 5
$$

Bruk definisjonen av den deriverte og finn $f' \left( x \right)$.

$$
\begin{align}
    f \left( x + h \right) &= \left( x+h \right)^{2} + 4 \left( x+h \right) + 5 \\
    f \left( x + h \right) &= x^{2} + 2xh + h^{2} + 4x + 4h + 5 \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{x^{2} + 2xh + h^{2} + 4x + 4h + 5 - x^{2} - 4x - 5}{h} \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{2xh + h^{2} + 4h}{h} \\
    f' \left( x \right) &= 2x + 4
\end{align}
$$

## Eksempel 3

$$
\begin{align}
    f \left( x \right) &= x^{3} + 1 \\
    f \left( x + h \right) &= \left( x+h \right)^{3} + 1 \\
    &= x \left( x+h \right)^{2} + h \left( x+h \right)^{2} \\
    &= x \left( x^{2} + 2xh + h^{2} \right) + h \left( x^{2} + 2xh + h^{2} \right) \\
    &= x^{3} + 2x^{2}h + xh^{2} + hx^{2} + 2xh^{2} + h^{3} \\
    &= x^{3} + 3x^{2}h + 3xh^{2} + h^{3}
\end{align}
$$

- [ ] TODO (og skrive den pyramide greien)

## Eksempel 4

Kan bruke konjugatsetningen:

$$
\begin{align}
    f \left( x \right) &= \sqrt{x} \\
    f \left( x + h \right) &= \sqrt{x + h} \\
    f' \left( x \right) &= \lim_{h \to 0} \frac{\sqrt{x+h} - \sqrt{x}}{h} \\
    &= \lim_{h \to 0} \frac{\sqrt{x+h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} \\
    &= \lim_{h \to 0} \frac{\left( \sqrt{x+h} \right)^{2}-\left( \sqrt{x} \right)^{2}}{h \left( \sqrt{x+h} + \sqrt{x} \right)} \\
    &= \lim_{h \to 0} \frac{x + h - x}{h \left( \sqrt{x+h} + \sqrt{x} \right)} \\
    &= \lim_{h \to 0} \frac{1}{\sqrt{x + h} + \sqrt{x}} \\
    &= \frac{1}{2 \sqrt{x}}
\end{align}
$$

Med [[20241028T1011-derivasjonsregler|derivasjonsregler]]:

$$
\begin{align}
    f \left( x \right) &= \sqrt{x} = x^{\frac{1}{2}} \\
    f' \left( x \right) &= \frac{1}{2} x^{-\frac{1}{2}} \\
    &= \frac{1}{2x^{-\frac{1}{2}}} \\
    &= \frac{1}{2 \sqrt{x}}
\end{align}
$$
