---
id: 20250925T1038-funksjonsdrøfting
aliases:
  - funksjonsdrøfting
tags: []
date: "2025-09-25"
title: funksjonsdrøfting
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# funksjonsdrøfting

Beskrive sentrale egenskaper ved funksjoner:

- [[20241121T1132-monotoniegenskaper|monotoniegenskaper]]
- [[20240616T1007-ekstremalpunkt|Ekstremalpunkt]], [[20241128T1012-kritiske-punkt|kritiske punkert]]
- [[20241128T1148-den-dobbelderiverte|krumming, vendepunkter]]
- Definisjonsmengde, verdimengde

## Harmonisk funksjon

Har at

$$
\begin{align}
  \left( \sin{x} \right)' &= \cos{x} & \\
  \left( \cos{x} \right)' &= - \sin{x} & \\
  \left( \tan{x} \right)' &= \frac{1}{\cos^{2}{x}} = \tan^{2}{x} + 1 &
\end{align}
$$

---

$$
f \left( x \right) = A \cdot \sin{\left( cx + \varphi \right)} + d
$$

Kan se bort fra alt utenfor $\sin{}$ hvis det kun forekommer $x$ inni, grunnet det vi vet om [[20250916T1105-harmoniske-svingninger|harmoniske svingninger]].

---

$$
\begin{align}
  g \left( x \right) &= \sin{x} + x & \\
  g' \left( x \right) &) \cos{x} + 1 & \\
  \cos{x} &= -1 & \\
  x &= \pi + 2 \pi \cdot n &
\end{align}
$$

# Oppgaver

## Eksempel 12 (s. 110)

Funksjonen $f$ er gitt ved $f \left( x \right) = x + 2 \sin{x}$, der $D_{f} = \left[ 0, 10 \right\rangle$. Bestem funksjonens monotoniegenskaper. Finn og beskriv eventuelle kritiske punkter.

$$
\begin{align}
  f' \left( x \right) &= 0 & \\
  2 \cos{x} + 1 &= 0 & \\
  \cos{x} &= - \frac{1}{2} & \\
  x &= \pm \frac{2\pi}{3} + 2\pi \cdot n & \\
  x &\in \left\{ \frac{2 \pi}{3}, \frac{4 \pi}{3}, \frac{8 \pi}{3} \right\} &
\end{align}
$$

Vet at $\cos{x}$ har toppunkt i $x=0$ om den ikke er forskjøvet. Dermed kan jeg se at $\cos{x}$ er positiv når $x \in \left[ 0, \frac{2\pi}{3} \right] \cup \left[ \frac{4\pi}{3}, \frac{8\pi}{3} \right]$ og negativ når $x \in \left\langle \frac{2\pi}{3}, \frac{4\pi}{3} \right\rangle \cup \left\langle \frac{8\pi}{3}, 10 \right\rangle$ innenfor definisjonsmengden. Får da:

- Toppunkt i $\displaystyle \left( \frac{2\pi}{3}, f \left( \frac{2\pi}{3} \right) \right) \approx \left( 2.09, 3.83 \right)$
- Bunnpunkt i $\displaystyle \left( \frac{4\pi}{3}, f \left( \frac{4\pi}{3} \right) \right) \approx \left( 4.19, 2.46 \right)$
- Toppunkt i $\displaystyle \left( \frac{8\pi}{3}, f \left( \frac{8\pi}{3} \right) \right) \approx \left( 8.38, 10.11 \right)$

Det er også et bunnpunkt i $\left( 0, 0 \right)$ i intervallet.

Monotoniegenskaper:

- Grafen til $f$ stiger i $x \in \left[ 0, 2.09 \right\rangle$ og $x \in \left[ 4.19 8.38 \right\rangle$
- Grafen til $f$ avtar i $x \in \left[ 2.09, 3.19 \right\rangle$ og $x \in \left[ 8.38, 10 \right\rangle$

## Eksempel 13

La $f$ være funksjonen

$$
f \left( x \right) = \cos^{2}{x} - \cos{x} - 1, c \in \left[ 0, 2 \pi \right\rangle
$$

Finn nullpunkter og ekstremalpunkter på grafen til $f$.

$$
\begin{align}
  f \left( x \right) &= 0 & \\
  \cos^{2}{x} - \cos{x} - 1 &= 0 & \\
  z^{2} - z - 1 &= 0 & \\
  z = \frac{\sqrt{5} + 1}{2} &\lor z = \frac{\sqrt{5} + 1}{2} & \\
  \cos{x} = -0.62 &\lor \cos{x} = 1.62 & \\
  x &= \pm 2.24 + n \cdot 2 \pi & \\
  x = 2.24 &\lor x = 4.04 &
\end{align}
$$

$$
\begin{align}
  f' \left( x \right) &= -2 \cos{x}\sin{x} + \sin{x} & \\
  -2 \cos{x} \sin{x} + \sin{x} &= 0 & \\
  \sin{x} \left( -2 \cos{x} + 1 \right) &= 0 & \\
  \sin{x} = 0 &\lor \cos{x} = \frac{1}{2} & \\
  x = \pi \cdot n &\lor x = \pm \frac{\pi}{3} + 2\pi \cdot n &
\end{align}
$$

Setter inn verdier av $n$ som gir resultater i intervallet $\left[ 0, 2 \pi \right\rangle$:

$$
x \in \left\{ 0, \frac{\pi}{3}, \pi, \frac{5\pi}{3} \right\}
$$

Finner den dobbeltderiverte

$$
\begin{align}
  f'' \left( x \right) &= -2 \cos^{2}{x} + 2\sin^{2}{x} + \cos{x}
\end{align}
$$

Ser at når $x=0$ er den dobbeltderiverte $f''(x) = -1$, altså synker den deriverte. Vet da at $f \left( x \right)$ synker i $\left[ 0, \frac{\pi}{3} \right\rangle$. Kan da finne funksjonsverdiene i de kritiske punktene og så finne ekstreemalpunktene.
