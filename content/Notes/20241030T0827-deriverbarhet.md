---
id: 20241030T0827-deriverbarhet
aliases:
  - deriverbarhet
tags: []
title: Deriverbarhet
date: 2024-10-30
---

#matte [[20240616T1007-derivasjon|derivasjon]] [[20240925T0628-kontinuitet|kontinuitet]]

# deriverbarhet

[[20241028T1009-definisjonen-av-den-deriverte|definisjonen av den deriverte]]:

$$
f' \left( x \right) = \lim_{h \to 0} \frac{f \left( x + h \right) - f \left( x \right)}{h}
$$

$$
f' \left( x \right) = \lim_{x \to a} \frac{f \left( a + x - a \right) - f \left( a \right)}{}
$$

$h$ er avstanden mellom $a$ og $x$, så vi kan skrive det som:

$$
\lim_{x \to a} \frac{f \left( x \right) - f \left( a \right)}{x - a}
$$

![20241030T0850-deriverbarhet.png](Assets/20241030T0850-deriverbarhet.png)

I $-2$ er de ensidige grenseverdiene ulike, dermed har ikke den momentane vekstfarten en verdi i dette punktet. Det samme gjelder $2$, der man får to ulike tangenter i stedet for en.

Hvis vi ikke kan tegne **en** tangent i punktet $\left( a, f \left( a \right) \right)$ på grafen til en funksjon er ikke funksjonen deriverbar i $a$.

En funksjon er deriverbar hvis $\displaystyle \lim_{x \to a} \frac{r \left( x \right) - f \left( a \right)}{x - a}$ eksisterer.

Hvis en funksjon er deriverbar i $a$, er funksjonen også kontinuerlig i $a$.
Hvis en funksjon ikke er kontinuerlig i $a$, er den heller ikke deriverbar i $a$.

## Eksempel

$f \left( x \right) = \left| x \right|$. Bruk definisjonen av den deriverte for å sjekke om $f \left( x \right)$ er deriverbar i $x = 0$.

$$
f \left( x \right) = \begin{cases}
-x & \text{,} & x < 0 \\
x & \text{,} & x \geq 0
\end{cases}
$$

$$
\lim_{x \to 0^{-}} f \left( x \right) = \frac{f \left( x \right) - f \left( 0 \right)}{x - 0} = \lim_{x \to 0^{-}} \frac{-x - 0}{x - 0} = -1
$$

$$
\lim_{x \to 0^{+}} f \left( x \right) = \frac{f \left( x \right) - f \left( 0 \right)}{x - 0} = \lim_{x \to 0^{+}} \frac{x - 0}{x - 0} = 1
$$

De ensidige grenseverdiene er ulike, så grenseverdien eksisterer ikke. Vi kan tegne to tangenter i punktet, dermed er funksjonen ikke deriverbar i punktet $x = 0$..
