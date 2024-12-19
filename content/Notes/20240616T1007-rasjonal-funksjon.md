---
id: 20240616T1007-rasjonal-funksjon
aliases:
  - rasjonal funksjon
tags: []
---

Tags: #matte

## Rasjonale funksjoner

En rasjonal funksjon kan skrives som

$$
f(x)=\frac{p(x)}{q(x)}
$$

, der $p(x)$ og $q(x)$ er [[20240616T1007-polynom]]er.

Grafen til en rasjonal funksjon på formen

$$
h(x)=\frac{ax+b}{cx+d}
$$

hvor $a$, $b$, $c$ og $d$ er reelle tall, kaller vi en ==hyperbel==.

### Eksempel

$$
f(x)=\frac{2x+3}{x-7}
$$

```functionplot
---
title:
xLabel:
yLabel:
bounds: [-5,20,-15,15]
disableZoom: true
grid: true
---
f(x)=(2x+3)/(x-7)
g(x)=2
```

### Asymptoter

En hyperbel har

- Vertikal asymptote $\displaystyle x=-\frac{d}{c}$
- Horisontal asymptote $\displaystyle y=\frac{a}{c}$
  Den vertikale asymptoten er $x$-verdien til funksjonen når $f(x)$ nærmer seg $\infty$., altså at nevneren går mot null.
  $$
  \begin{align}
  \lim_{ \frac{ax+b}{cx+d} \to \infty } &\implies cx + d = 0 \\
  &\implies x+\frac{d}{c} = 0 \\
  &\implies x = \underline{\underline{-\frac{d}{c}}}
  \end{align}
  $$

Den horisontale asymptoten er $y$-verdien funksjonen nærmer seg når $x$ går mot $\infty$.

$$
\begin{align}
y &= \lim_{ x \to \infty } \frac{ax+b}{cx+d} \\
&= \lim_{ x \to \infty } \frac{a+\frac{b}{x}}{c+\frac{d}{x}} \\
&= \underline{\underline{\frac{a}{c}}}
\end{align}
$$

