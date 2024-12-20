---
id: 20240616T1007-produktregelen
aliases:
  - produktregelen
tags: []
title: Produktregelen
date: 2024-06-16
---

#matte [[20240616T1007-matte|matte]] [[20240616T1007-derivasjon|derivasjon]] [[20241028T1011-derivasjonsregler|derivasjonsregler]]

# Produktregelen

$$
\begin{align}
    f \left( x \right) &= \overbrace{e^{x}}^{u \left( x \right)} \cdot \overbrace{\ln{x}}^{v \left( x \right)} & \\
    f' \left( x \right) &= u'\left( x \right) \cdot v \left( x \right) + u \left( x \right) \cdot v' \left( x \right) & \\
    &= \boxed{u'v + uv'} & \\
    &= \left( e^{x} \right) \cdot \ln{x} + e^{x} \cdot \frac{1}{x} & \\
    &= \underline{\underline{e^{x} \left( \ln{x} + \frac{1}{x} \right)}} &
\end{align}
$$

Som oftest får vi et svar som kan faktoriseres i oppgaver som bruker produktregelen.

## Eksempel 1

$$
\begin{align}
    f \left( x \right) &= x^{2} \cdot \ln{x} & \\
    u &= x^{2}  \implies u' = 2x & \\
    v &= \ln{x}  \implies v' = \frac{1}{x} & \\
    f' \left( x \right) &= u'v + uv' & \\
    &= 2x \cdot \ln{x} + x^{2} + \frac{1}{x} & \\
    &= 2x\ln{x} + x & \\
    &= \underline{\underline{x \left( 2\ln{x} + 1 \right)}} &
\end{align}
$$

## Bevis

La $f$ er en funksjon som er produktet av to deriverbare funksjoner $u$ og $v$.

Da er $f \left( x \right) = u \left( x \right) \cdot v \left( x \right)$

Deriverer ved hjelp av [[20241028T1009-definisjonen-av-den-deriverte|definisjonen]]

$$
f' \left( x \right) = \lim_{\Delta x \to 0} \frac{\Delta f \left( x \right)}{\Delta x}
$$

Lar $h = \Delta x$ slik at vi får

$$
\begin{align}
    f' \left( x \right) &= \lim_{h \to 0} \frac{f \left( x + h \right) - f \left( x \right)}{h} & \\
    &=  \lim_{h \to 0} \frac{u \left( x+h \right) \cdot v \left( x + h \right) - u \left( x \right) \cdot v \left( x \right)}{h} & \\
    &=  \lim_{h \to 0} \frac{u \left( x+h \right) \cdot v \left( x + h \right) - u \left( x \right) \cdot v \left( x \right) + \overbrace{u \left( x \right) \cdot v \left( x + h \right) - u \left( x \right) \cdot v \left( x + h \right)}^{+0}}{h} & \\
    &= \lim_{h \to 0} \frac{u \left( x + h \right) \cdot v \left( x + h \right) - u \left( x \right) \cdot v \left( x + h \right) + u \left( x \right) \cdot v \left( x + h \right) - u \left( x \right) \cdot v \left( x \right)}{h} & \\
    &= \lim_{h \to 0} \frac{\left( u \left( x + h \right) - u \left( x \right) \right) \cdot v \left( x + h \right) + u \left( x \right) \cdot \left( v \left( x + h \right) - v \left( x \right) \right)}{h} & \\
    &= \lim_{h \to 0} \frac{\left( u \left( x + h \right) - u \left( x \right) \right) \cdot v \left( x + h \right)}{h} + \frac{u \left( x \right) \cdot \left( v \left( x + h \right) - v \left( x \right) \right)}{h} & \\
    &= \lim_{h \to 0} \frac{u \left( x + h \right) - u \left( x \right)}{h} \cdot v \left( x + h \right) + \lim_{h \to 0} u \left( x \right) \cdot \frac{v \left( x + h \right) - v \left( x \right)}{h} & \\
    &= \lim_{h \to 0} \frac{u \left( x + h \right) - u \left( x \right)}{h} \cdot \lim_{h \to 0} v \left( x + h \right) + \lim_{h \to 0} u \left( x \right) \cdot \lim_{h \to 0} \frac{v \left( x + h \right) - v \left( x \right)}{h} & \\
    f' \left( x \right) &= u' \left( x \right) \cdot v \left( x \right) + u \left( x \right) \cdot v' \left( x \right) &
\end{align}
$$
