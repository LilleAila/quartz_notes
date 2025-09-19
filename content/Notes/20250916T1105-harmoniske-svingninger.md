---
id: 20250916T1105-harmoniske-svingninger
aliases:
  - harmoniske svingninger
tags: []
date: "2025-09-16"
title: harmoniske svingninger
---

#matte [[20250911T1050-trigonometriske-funksjoner|trigonometriske funksjoner]]

# harmoniske svingninger

En funksjon der grafen varierer periodisk ut fra en likevektslinje på samme måte som grafen til $\sin{x}$ og $\cos{x}$ kalles en harmonisk svingning. Bruker funksjonen definert tidligere:

$$
f \left( x \right) = A \cdot \sin{\left( c \cdot x + \varphi \right)} + d
$$

- Grafen har samme form som grafen til $\sin{x}$
- Variabelen $A$ strekker grafen i $y$-retning (tilsvarer amplitude)
- Variabelen $c$ strekker grafen i $x$-retning (relaterer til funksjonens periode)
- Variebelen $\varphi$ forskyver grafen i $x$-retning
- Variabelen $d$ forskyver grafen i $y$-retning (tilsvarer likevektslinjen)

---

Amplituden til svingningen er det største utslaget fra likevektslinjen. Dette er avstanden fra et ekstremalpunkt til likevektslinjen. $\sin{x}$ har amplitude lik $1$.

---

En periode er avstanden mellom to toppunkter på grafen. Man kan løse følgende likning:

$$
\begin{align}
  \sin{\left( cx + \varphi \right)} &= 1 & \\
  cx + \varphi &= \frac{\pi }{2} + n \cdot 2 \pi  & \\
  cx &= -\varphi + \frac{\pi }{2} + n \cdot 2 \pi  & \\
  x &= - \frac{\varphi}{c} + \frac{\pi }{2c} + n \cdot \frac{2 \pi }{c} & \\
  x &= \frac{\pi - 2\varphi}{2c} + n \cdot \frac{2 \pi }{c} &
\end{align}
$$

Altså er perioden til grafen lik $\displaystyle \frac{2 \pi }{c}$.

---

Grafen til $f \left( x \right)$ skjærer likevektslinjen når $\sin{\left( cx + \varphi \right)} = 0$:

$$
\begin{align}
  A \sin{\left( cx + \varphi \right)} + d &= d & \\
  A \sin{\left( cx + \varphi \right)} &= 0 & \\
  \sin{\left( cx + \varphi \right)} &= 0 & \\
  cx + \varphi = n \cdot 2 \pi &\lor cx + \varphi = \pi + n \cdot 2 \pi  & \\
  cx = -\varphi + n \cdot 2 \pi &\lor cx = -\varphi + \pi + n \cdot 2 \pi  & \\
  x = - \frac{\varphi}{c} + n \cdot \frac{2 \pi }{c} &\lor x = - \frac{\varphi + \pi }{c} + n \cdot \frac{2 \pi }{c} &
\end{align}
$$

---

> [!NOTE]
> La $f$ være funksjonen $f \left( x \right) = A \sin{ \left( cx + \varphi \right)} + d$.
> Da gjelder:
>
> - Likevektslinjen er $y = d$
> - Amplituden er $A$
> - Perioden er $p = \frac{2 \pi }{c}$
> - Skjæringspunktet med likevektslinjen er $x = - \frac{\varphi}{c}$ (på vei opp), og $x = - \frac{\varphi + \pi }{c}$ (på vei ned).

## Uttrykk på formen

$$
a \cdot \sin{\left( cx \right)} + b \cdot \cos{\left( cx \right)}
$$

Kan skrives om på formen

$$
\begin{align}
  A \cdot \sin{\left( cx + \varphi \right)} & & \\
  A \cdot \left( \sin{\left( cx \right)} \cdot \cos{\varphi} + \sin{\varphi} \cdot \cos{\left( cx \right)} \right) & & \\
  \underbrace{A \cdot \cos{\varphi}}_{a} \cdot \sin{cx} + \underbrace{A \cdot \sin{\varphi}}_{b} \cdot \cos{cx} & &
\end{align}
$$

Kan representere som en rettvinklet trekant for å finne $A$.

$$
\begin{align}
  h^{2} &= a^{2} + b^{2} & \\
  h &= \sqrt{\left( A \cdot \cos{\varphi} \right)^{2} + \left( A \cdot \sin{\varphi} \right)^{2}} & \\
  h &= \sqrt{A^{2} \cdot \cos^{2}{\varphi} + A^{2} \cdot \sin^{2}{\varphi}} & \\
  h &= \sqrt{A^{2} \left( \cos^{2}{\varphi} + \sin^{2}{\varphi} \right)} & \\
  h &= \sqrt{A^{2}} & \\
  h &= A &
\end{align}
$$

![[20250916T1105-harmoniske-svingninger 2025-09-18 10.56.54.excalidraw.svg]]

Kan da finne at

$$
\frac{a}{A} = \cos{\varphi} \land \frac{b}{A} = \sin{\varphi}
$$

$$
\tan{\varphi} = \frac{\sin{\varphi}}{\cos{\varphi}} = \frac{b}{a}
$$

### Eksempel

$$
\begin{align}
  f \left( x \right) &= 4 \cdot \sin{\left( 3x \right)} - 4 \cdot \cos{\left( 3x \right)} - 1 & \\
  &= A \cdot \sin{\left( cx + \varphi \right)} + d & \\
  &= A \cdot \sin{\left( 3x + \varphi \right)} - 1 & \\
  A &= \sqrt{a^{2} + b^{2}} & \\
  &= \sqrt{9 + 16} & \\
  &= 5 & \\
  \sin{\varphi} &= \frac{-4}{5} \implies \varphi \in \left\{ 4.069, 5.356 \right\} & \\
  \cos{\varphi} &= \frac{3}{5} \implies \varphi \in \left\{ 0.927, 5.356 \right\} & \\
  \varphi &= 5.356 & \\
  f \left( x \right) &= 5 \sin{\left( 3x + 5.356 \right)} - 1 &
\end{align}
$$

Kan i CAS bruke `TrigKombiner(f, sin(x))`

### Eksempel 2

$$
\begin{align}
  -\cos{x} - \sqrt{3} \sin{x} &= 1, x \in \left[ 0, 2 \pi \right] & \\
  a = - \sqrt{3} &\land b = -1 & \\
  A &= \sqrt{a^{2} + b^{2}} & \\
  &= \sqrt{4} = 2 & \\
  \sin{\varphi} = - \frac{1}{2} &\land \cos{\varphi} = - \frac{\sqrt{3}}{2} & \\
  \varphi = - \frac{\pi}{6} + 2 \pi \cdot n \lor \varphi = \frac{7 \pi}{6} + 2 \pi \cdot n &\mathrel{\phantom{\lor}} \varphi = \frac{5 \pi}{6} + 2 \pi \cdot n \lor \frac{7 \pi}{6} + 2 \pi \cdot n & \\
  \varphi &= \frac{7 \pi}{6} & \\
  -\cos{x} - \sqrt{3} \sin{x} &= 1 & \\
  2 \sin{\left( x + \frac{7 \pi}{6} \right)} &= 1 & \\
  \sin{\left( x + \frac{7 \pi}{6} \right)} &= \frac{1}{2} & \\
  x + \frac{7 \pi}{6} = \frac{\pi}{6} + 2 \pi \cdot n &\lor x + \frac{7 \pi}{6} = \pi - \frac{\pi}{6} + 2 \pi \cdot n & \\
  x = \frac{\pi}{6} - \frac{7 \pi}{6} + 2 \pi \cdot n &\lor x = \pi - \frac{\pi}{6} - \frac{7 \pi}{6} + 2 \pi \cdot n & \\
  x = - \pi + 2 \pi \cdot n &\lor x = - \frac{\pi}{3} + 2 \pi \cdot n & \\
  x = \pi &\lor x = \frac{5 \pi}{3} &
\end{align}
$$

# Oppgaver

## Eksamen R2 V23 - Oppgave 6

$$
\begin{align}
    f \left( x \right) &= A \cdot \sin{\left( c \cdot x + \varphi \right)} + d & \\
    \text{Amplitude} = A &= \frac{f_{\text{max}} - f_{\text{min}}}{2} = \frac{6}{2} = 3 & \\
    \text{Likevektslinje} = d &= \frac{f_{\text{max}} + f_{\text{min}}}{2} = \frac{-2}{2} = -1 &
\end{align}
$$

Ser at en periode $P$ er lik $\frac{\pi }{2}$, da det samme utslaget forekommer på $x=0$ og $x= \frac{\pi }{2}$.

$$
\begin{align}
  P &= \frac{2\pi }{c} = \frac{\pi }{2} & \\
  \frac{2\pi }{c} &= \frac{\pi }{2} & \\
  2 \pi & = \frac{\pi }{2} \cdot c & \\
  2 &= \frac{1}{2} c & \\
  c &= 4 &
\end{align}
$$

$$
\begin{align}
    f \left( x \right) &= 3 \cdot \sin{\left( 4x + \varphi \right)} - 1 & \\
    \sin{\left( 4x + \varphi \right)} &= 0 & \\
    4x + \varphi = 0 + 2\pi \cdot n &\lor 4x + \varphi = \pi + 2\pi \cdot n & \\
    4x = -\varphi + 2\pi \cdot n &\lor 4x = \pi - \varphi + 2\pi \cdot n & \\
    x = \frac{- \varphi}{4} + \frac{\pi }{2} \cdot n &\lor x = \frac{\pi - \varphi}{4} + \frac{\pi }{2} \cdot n & \\
    \frac{\pi }{6} &= - \frac{\varphi}{4} & \\
    \frac{4\pi }{6} &= -\varphi & \\
    \varphi &= - \frac{4\pi }{6} &
\end{align}
$$

## Eksamen R2 V25 - Oppgave 4a

$$
\begin{align}
  f \left( x \right) &= s \cdot \sqrt{3} \cdot \sin{\left( 2x + \frac{\pi}{6} \right)} & \\
  f \left( x \right) &= A \cdot \sin{\left( cx + \varphi \right)} + d & \\
  \text{Amplitude} = A &= 2 \sqrt{3} & \\
  \text{Likevektslinje} = d &= 0 & \\
  \text{Periode} = P &= \frac{2 \pi}{k} = \frac{2\pi}{2} = \pi & \\
  \text{Faseforskyvning} &= - \frac{\varphi}{k} = - \frac{\frac{\pi}{6}}{2} = -\frac{\pi}{12} &
\end{align}
$$

## 2.19 (s. 97)

> Figuren viser grafen til en harmonisk funksjon $f \left( x \right)$. Bruk grafen til å finne et uttrykk for $f \left( x \right)$.

<!-- Lat som om det er et bilde her, jeg har ikke tilgang på digital boken 😔 -->

$$
\begin{align}
  f_{max} &= 3 & \\
  f_{min} &= -3 & \\
  A &= \frac{3 - \left( -3 \right)}{2} = \frac{6}{2} = 3 & \\
  d &= \frac{3 + \left( -3 \right)}{2} = \frac{0}{2} = 0 & \\
  P &= \pi & \\
  \text{Forskyvning} &= \frac{\pi}{8} &
\end{align}
$$

Leser av perioden fra grafen ved å sammenligne punktene $x=0$ og $x=\pi$. Ser at disse har samme utslag og at det da er en periode.

$$
\begin{align}
  \frac{2\pi}{c} &= \pi & \\
  2\pi &= c \cdot \pi & \\
  c &= 2 &
\end{align}
$$

Bruker negativ av forskyvningen, da den skal forskyves til høyre.

$$
\begin{align}
  \frac{\varphi}{2} &= - \frac{\pi}{8} & \\
  \varphi &= -\frac{\pi}{4} &
\end{align}
$$

Setter dette sammen og får

$$
f \left( x \right) = 3 \sin{\left( 2x - \frac{\pi}{4} \right)}
$$

## 2.23 (s. 104)

Funksjonen $f$ er gitt ved $f \left( x \right) = 3 \sin{2x} + 4 \cos{2x} - 1$.

**a**

> Bruk graftegner til å tegne grafen til $f$.

**b**

> Skriv $f$ på formen $f \left( x \right) = A \sin{\left( cx + \varphi \right)} + d$ ved å
>
> 1. Bruke grafen
> 2. Bruke funksjonsuttrykket til $f$

<!--
note: dette er feil todo
$$
\begin{align}
  a &= 3 & \\
  b &= 3 & \\
  A &= \sqrt{3^{2} + 4^{2}} = \sqrt{25} = 5 & \\
  \sin{\varphi} &= \frac{3}{5} & \\
  \varphi = 0.64 &\lor \varphi = 2.5 & \\
  \cos{\varphi} &= \frac{4}{5} & \\
  \varphi = 0.64 &\lor \varphi = 5.64 & \\
  f \left( x \right) &= 5 \sin{\left( 2x + 0.64 \right)} - 1 &
\end{align}
$$
-->
