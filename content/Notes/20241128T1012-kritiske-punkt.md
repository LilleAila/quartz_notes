---
id: 20241128T1012-kritiske-punkt
aliases:
  - kritiske punkt
tags: []
---

#matte [[20240616T1007-matte|matte]] [[20240616T1007-derivasjon|derivasjon]]

# kritiske punkt

La f være en funksjon og $D_f = \left[ a, b \right]$
Evt kritiske punkt i

1. $c \in \left\langle a, b \right\rangle$ slik at $f' \left( x \right) = 0$
2. $c \in \left\langle a, b \right\rangle$ slik at $f$ ikke er deriverbar i $c$
3. Endepunktene $a$, $b$

Topp og bunnpunkt. Hvis den har det, er det som regel i de kritiske punktene.
Et endepunkt kan være et toppunkt.

## Oppgave

$$
f \left( x \right) = \begin{cases}
    x^{2} - 6x & \text{, } & -2 \leq x \leq 7 \\
    14 - x & \text{, } & 7 < x \leq 18
\end{cases}
$$

Kritiske punkt:

### Derivert lik 0

$$
f' \left( x \right) = \begin{cases}
    2x - 6 & \text{, } & -2 \leq x \leq 7 \\
    -1 & \text{, } & 7 < x \leq 18
\end{cases}
$$

$2x - 6 = 0 \implies x = 3 \implies f' \left( 3 \right) = 0$
$f' \left( 3 \right) = 3^{2}  6 \cdot 3 = 9 - 18 = -9$

$\left( 3, -9 \right)$ er et bunnpunkt fordi

- $f' \left( x \right) < 0$ før $x=3$
- $f' \left( x \right) > 0$ etter $x=3$

### Deriverbarhet

Se på $x=7$ (overgang mellom funksjonsuttrykk / bruddpunkt)

$f$ er ikke deriverbar $\implies x=7 \implies$ toppunkt, fordi positivt andregradsledd i f

$$
\lim_{x \to 7^-} f \left( x \right) = \lim_{x \to 7^-} x^{2} - 6x = 7
$$

$$
\lim_{x \to 7^-} f' \left( x \right) = \lim_{x \to 7^-} 2x - 6 = 8
$$

$$
\lim_{x \to 7^+} f \left( x \right) = \lim_{x \to 7^+} 14 - x = 7
$$

$$
\lim_{x \to 7^+} f' \left( x \right) = \lim_{x \to 7^+} -1 = -1
$$

Den deriverte vil ikke finnes i 7, vil være positiv før, og vil være negativ etter.

### Endene

$x=-2$, $f \left( x \right)$ synker $\implies$ toppunkt
$x=18$, $f \left( x \right)$ synker $\implies$ bunnpunkt
