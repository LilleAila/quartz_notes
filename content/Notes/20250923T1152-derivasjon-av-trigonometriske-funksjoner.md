---
id: 20250923T1152-derivasjon-av-trigonometriske-funksjoner
aliases:
  - derivasjon av trigonometriske funksjoner
tags: []
date: "2025-09-23"
title: derivasjon av trigonometriske funksjoner
---

# derivasjon av trigonometriske funksjoner

$$
\begin{align}
  f' \left( x \right) &= \lim_{\Delta x \to 0} \frac{f \left( x + \Delta x \right) - f \left( x \right)}{\Delta x} & \\
  &= \lim_{\Delta x \to 0} \frac{\sin{\left( x + \Delta x \right)} - \sin{\left( x \right)}}{\Delta x} & \\
  &= \lim_{\Delta x \to 0} \frac{\sin{x} \cdot \cos{\Delta x} + \cos{x} \cdot \sin{\Delta x} - \sin{x}}{\Delta x} & \\
  &= \lim_{\Delta x \to 0} \left( \frac{\cos{x} \cdot \sin{\Delta x}}{\Delta x} + \frac{\sin{x} \cdot \cos{\Delta x} - \sin{x}}{\Delta x} \right) & \\
  &= \lim_{\Delta x \to 0} \frac{\cos{x} \cdot \sin{\Delta x}}{\Delta x} + \lim_{\Delta x \to 0} \frac{\sin{x} \cdot \cos{\Delta x} - \sin{x}}{\Delta x} & \\
  &= \cos{x} \cdot \lim_{\Delta x \to 0} \frac{\sin{\Delta x}}{\Delta x} + \sin{x} \cdot \lim_{\Delta x \to 0} \frac{\cos{\Delta x} - 1}{\Delta x} &
\end{align}
$$

Her har vi to $\frac{0}{0}$-uttrykk, og har ikke mulighet til å verken faktorisere eller bruke l'hôpitals. Må derfor finne en annen løsning. Har gitt tre trekanter:

- Likebeint trekant med vinkel $u$ og sidelengder $1$.
- Sirkelsektor med vinkel $u$ og radius $1$. Har derfor buelengde $u$.
- Rettvinklet trekant der $h$ er høyden

![[20250923T1152-derivasjon-av-trigonometriske-funksjoner 2025-09-23 11.53.03.excalidraw.svg]]

$$
\begin{align}
  A_{1} &= \frac{1}{2} \cdot 1 \cdot 1 \cdot \sin{u} = \frac{1}{2} \sin{u} & \\
  A_{2} &= \pi r^{2} \cdot \frac{u}{2 \pi r} = \pi \cdot 1^{1} \cdot \frac{u}{2 \pi \cdot 1} = \frac{1}{2} u & \\
  A_{3} &= \frac{1}{2} g \cdot h = \frac{1}{2} \tan{u} &
\end{align}
$$

Vet fra figurene at

$$
A_{1} < A_{2} < A_{3}
$$

Og har at

$$
m < n \implies m \leq n
$$

, dermed

$$
\begin{align}
  A_{1} \leq A_{2} \leq A_{3} \\
  \frac{1}{2} \sin{u} \leq \frac{1}{2} u \leq \frac{1}{2} \tan{u} \\
  \sin{u} \leq u \leq \tan{u} = \frac{\sin{u}}{\cos{u}} \\
\end{align}
$$

Forutsetter $\sin{u} > 0$, deler på $\sin{u}$:

$$
1 \leq \frac{u}{\sin{u}} \leq \frac{1}{\cos{u}}
$$

Lar $u \to 0$:

$$
1 \leq \lim_{u \to 0} \frac{u}{\sin{u}} \leq 1
$$

Ser nå at den eneste muligheten for at det skal stemme er at $\displaystyle \lim_{u \to 0} = 1$, og derfor blir også $\displaystyle \lim_{u \to 0} \frac{\sin{u}}{u}$

Bruker enhetsformelen til å beregne den andre grenseverdien.

$$
\begin{align}
  \lim_{u \to 0} \frac{\cos{u} - 1}{u} &= \lim_{u \to 0} \frac{\left( \cos{u} - 1 \right)}{u} \cdot \frac{\left( \cos{u} + 1 \right)}{\left( \cos{u} + 1 \right)} & \\
  &= \lim_{u \to 0} \frac{\cos^{2}{u} - 1}{u \left( \cos{u} + 1 \right)} & \\
  &= \lim_{u \to 0} \frac{-\sin^{2}{u}}{u \left( \cos{u}  + 1 \right)} & \\
  &= \lim_{u \to 0} \frac{\sin{u}}{u} \cdot \frac{- \sin{u}}{\cos{u}  + 1} & \\
  &= 1 \cdot 0 & \\
  &= 0 &
\end{align}
$$

Kan sette dette inn i det originale uttrykket og få

$$
\begin{align}
  \left( \sin{x} \right)' &= \cos{x} \cdot \lim_{\Delta x \to 0} \frac{\sin{\Delta x}}{\Delta x} + \sin{x} \cdot \lim_{\Delta x \to 0} \frac{\cos{\Delta x} - 1}{\Delta x} & \\
  &= \cos{x} \cdot 1 + \sin{x} \cdot 0 & \\
  &= \boxed{\cos{x}} &
\end{align}
$$

Videre kan jeg bruke dette til å finne den deriverte av flere trigonometriske funksjoner:

---

$$
\begin{align}
  \left( \cos{x} \right)' &= \left( \sin{\left( \frac{\pi}{2} - x \right)} \right)' & \\
  &= \cos{\left( \frac{\pi}{2} - x \right)} \cdot \left( -1 \right) & \\
  &= - \sin{x} &
\end{align}
$$

---

$$
\begin{align}
  \left( \tan{x} \right)' &= \left( \frac{\sin{x}}{\cos{x}} \right)' & \\
  &= \frac{\cos{x} \cdot \cos{x} - \sin{x} \cdot \left( - \sin{x} \right)}{\cos^{2}{x}} & \\
  &= \frac{\cos^{2}{x} + \sin^{2}{x}}{\cos^{2}{x}} & \\
  &= \frac{1}{\cos^{2}{x}} = \tan^{2}{x} + 1 &
\end{align}
$$

# Oppgaver

## 2.29 (s. 109)

**a**

$$
\begin{align}
  f \left( x \right) &= 3 \sin{\left( 4x \right)} & \\
  f' \left( x \right) &= 12 \cos{4x} &
\end{align}
$$

**b**

$$
\begin{align}
  f \left( x \right) &= 2 \sin{3x} + 5 & \\
  f' \left( x \right) &= 6 \cos{3x} &
\end{align}
$$

**c**

$$
\begin{align}
  f \left( x \right) &= x^{2} \cdot \sin{x} & \\
  f' \left( x \right) &= 2x \cdot \sin{x} + x^{2} \cdot \cos{x} & \\
  &= x \left( 2 \sin{x} + x \cos{x} \right) &
\end{align}
$$

## 3.30

**a**

$$
\begin{align}
  f \left( x \right) &= x^{3} \cdot \cos{x} & \\
  f' \left( x \right) &= 3x \cos{x} - x^{3} \sin{x} &
\end{align}
$$

**b**

$$
\begin{align}
  f \left( x \right) &= 2 \sin{x} \cos{x} & \\
  &= \sin{2x} & \\
  f' \left( x \right) &= 2 \cos{2x} &
\end{align}
$$

---

$$
\begin{align}
  f \left( x \right) &= 2 \sin{x} \cos{x} & \\
  f' \left( x \right) &= 2 \left( \cos^{2}{x} - \sin^{2}{x} \right) & \\
  &= 2 \left( \cos^{2}{x} - \left( 1 - \cos^{2}{x} \right) \right) & \\
  &= 2 \left( 2 \cos^{2}{x} - 1 \right) & \\
  &= 4 \cos^{2}{x} - 2 &
\end{align}
$$

**c**

$$
\begin{align}
  f \left( x \right) &= \left( \cos{x} + 1 \right)^{3} & \\
  f' \left( x \right) &= - 3 \sin{x} \left( \cos{x} + 1 \right)^{2} &
\end{align}
$$

**d**

$$
\begin{align}
  f \left( x \right) &= \sqrt{\tan{x}} & \\
  f' \left( x \right) &= \frac{\tan^{2}{x} + 1}{2 \sqrt{\tan{x}}} & \\
  &= \frac{1}{2\cos^{2}{x} \sqrt{\tan{x}}} &
\end{align}
$$

**e**

$$
\begin{align}
  f \left( x \right) &= \ln{\left( \cos{x} \right)} & \\
  f' \left( x \right) &= - \frac{\sin{x}}{\cos{x}} & \\
  &= - \tan{x} &
\end{align}
$$

## 2.31

**a**

$$
\begin{align}
  f \left( x \right) &= x^{2} \cdot \sin{2x} & \\
  f' \left( x \right) &= 2x \sin{2x} + 2x^{2} \cos{2x} & \\
  &= 2x \left( \sin{2x} + x \cos{2x} \right) &
\end{align}
$$

**b**

$$
\begin{align}
  f \left( x \right) &= \sqrt{\cos{2x}} & \\
  f' \left( x \right) &= \frac{-2 \sin{2x}}{2 \sqrt{\cos{2x}}} & \\
  &= \frac{- \sin{2x}}{\sqrt{\cos{2x}}} &
\end{align}
$$

**c**

$$
\begin{align}
  f \left( x \right) &= 3 \cdot \left( \sin{x} - 2 \right)^{3} & \\
  f' \left( x \right) &= 9 \cos{x} \left( \sin{x} - 2 \right)^{2} & \\
\end{align}
$$

## 2.32

**a**

$$
\begin{align}
  f \left( x \right) &= 2 \cos{3x} & \\
  f' \left( x \right) &= -6 \sin{3x} &
\end{align}
$$

**b**

$$
\begin{align}
  f \left( x \right) &= \left( 2 \sin{x} + 3 \right)^{4} & \\
  f' \left( x \right) &= 8 \cos{x} \left( 2 \sin{x} + 3 \right)^{3} &
\end{align}
$$

**c**

$$
\begin{align}
  f \left( x \right) &= \sqrt{\tan{2x}} & \\
  f' \left( x \right) &= \frac{1}{\cos^{2}{2x} \sqrt{\tan{2x}}} &
\end{align}
$$
