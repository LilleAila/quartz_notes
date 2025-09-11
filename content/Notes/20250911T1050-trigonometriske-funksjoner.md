---
id: 20250911T1050-trigonometriske-funksjoner
aliases:
  - trigonometriske funksjoner
tags: []
date: "2025-09-11"
title: trigonometriske funksjoner
---

#matte [[20250526T1040-matte-r2|Matte R2]] [[20250819T1116-trigonometri|trigonometri]]

# trigonometriske funksjoner

Grafen til $f \left( x \right) = \sin{x}$ ser slik ut når man tegner den for alle omløp:

![[Pasted image 20250911105102.png]]

Vet at funksjonen har en verdimengde $V_{f} = \left[ -1, 1 \right]$, da sinusverdien alltid ligger i dette området. Man kan finne ekstremalpunktene ved å løse likningene $f \left( x \right) = 1$ og $f \left( x \right) = -1$.

$$
\begin{align}
  \sin{x} &= 1 & \\
  x = \frac{\pi }{2} + n \cdot 2 \pi &\lor x = \pi - \frac{\pi }{2} + n \cdot 2 \pi  & \\
  x &= \frac{\pi }{2} + n \cdot 2 \pi  &
\end{align}
$$

$$
\begin{align}
  \sin{x} &= -1 & \\
  x = \frac{3 \pi }{2} + n \cdot 2 \pi &\lor x = \pi - \frac{3 \pi }{2} + n \cdot 2 \pi  & \\
  x = \frac{3 \pi }{2} + n \cdot 2 \pi &\lor x = - \frac{\pi }{2} + n \cdot 2 \pi  & \\
  x &= \frac{3 \pi }{2} + n \cdot 2 \pi &
\end{align}
$$

Videre kan vi løse likningen $\sin{x} = 0$ for å finne nullpunkter. Får da $x = n \cdot \pi$.

Grafen til funksjonen gjentar seg. Et omløp på $2 \pi$ tilsvarer en repetisjon, altså har funksjonen periode $2 \pi$. Grafen svinger opp og ned rundt linjen $y=0$, og denn elinjen kalles likevektslinjen.

---

Grafen til $g \left( x \right) = \cos{x}$ har akkurat de samme egenskapene, men har blitt horisontalt forskjøvet med $\pi$, slik at toppunktene forekommer på $x = 2 \cdot \pi$, bunnpunktene på $x = \pi + n \cdot 2 \pi$, og nullpunkter i $x = \frac{\pi }{2} + n \cdot \pi$. Derfor er $\cos{x} = \sin{\left( \frac{\pi }{2} - x \right)}$.

---

$$
f \left( x \right) = A \cdot \sin{\left( c \cdot x + \varphi \right) + d}
$$

Når man endrer $d$, blir grafen forskjøvet vertikalt med $d$ enheter oppover langs $y$-aksen.
Når man endrer $\varphi$, blir grafen forskjøvet horisontalt med $-\varphi$ enheter langs $x$-aksen (altså $\varphi$ enheter mot venstre).

> [!NOTE]
> La $f$ være en funksjon.
> Grafen til $f \left( x + k \right)$ er forskjøvet med $k$ enheter mot venstre i forhold til grafen $f$.
> Grafen til $f \left( x \right) + k$ er forskjøvet med $k$ enheter oppover i forhold til grafen $f$.

Når man endrer på $A$, blir grafen vertikalt strukket med en faktor $A$ i $y$-retning.
Når man endrer på $c$, blir grafen strukket i $x$-retning.

> [!NOTE]
> La $f$ være en funksjon.
> Når $k > 1$: Grafen til $g \left( x \right) = f \left( k \cdot x \right)$ er komprimert med en faktor $k$ i $x$-retning.
> Når $k < 1$: Grafen til $g \left( x \right) = f \left( x \cdot x \right)$ er strukket ut med en faktor $k$ i $x$-retning.
> Når $k > 1$: Grafen til $g \left( x  \right) = k \cdot f \left( x \right)$ er strukket ut med en faktor $k$ i $y$-retning.
> Når $k < 1$: Grafen til $g \left( x \right) = k \cdot f \left( x \right)$ er komprimert med en faktor $k$ i $y$-retning.

## Harmoniske svingninger

En funksjon der grafen varierer periodisk ut fra en likevektslinje på samme måte som grafen til $\sin{x}$ og $\cos{x}$ kalles en harmonisk svingning. Bruker funksjonen definert tidligere:

$$
f \left( x \right) = A \cdot \sin{\left( c \cdot x + \varphi \right)} + d
$$

- Grafen har samme form som grafen til $\sin{x}$
- Variabelen $A$ strekker grafen i $y$-retning
- Variabelen $d$ forskyver grafen i $y$-retning
- Variabelen $c$ strekker grafen i $x$-retning
- Variebelen $\varphi$ forskyver grafen i $x$-retning

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

Altså er perioden til grafen lik $\frac{2 \pi }{c}$.

---

Grafen til $f \left( x \right)$ skjører likevektslinjen når $\sin{\left( cx + \varphi \right)} = 0$:

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

