---
id: 20260519T1106-differensiallikninger
aliases:
  - differensiallikninger
tags: []
date: "2026-05-19"
title: differensiallikninger
---

#matte [[20250526T1040-matte-r2|Matte R2]]

# differensiallikninger

Eksempel:

$$
f' \left( x \right) + 2 \cdot f \left( x \right) = 2
$$

I kontrast til en vanlig likning, er målet i en difflikning å finne et uttrykk for $f \left( x \right)$, uttrykt med $x$. Man skriver det ofte enklere med $y$ i stedet for $f \left( x \right)$.

$$
y' + 2y = 2
$$

Difflikninger er av første orden når den høyeste deriverte er den førstederiverte. En difflikning som $y'' + y = 0$ er av andre orden. Den enkleste formen for difflikninger, som vi allerede har løst, er en likning på formen

$$
\begin{align}
  y' &= g \left( x \right) & \\
  \int f' \left( x \right) \,dx &= \int g \left( x \right) \,dx & \\
  f \left( x \right) &= \int g \left( x \right) \,dx &
\end{align}
$$

Man kan gjøre det samme for en tilsvarende andreordens difflikning:

$$
\begin{align}
  y'' &= g \left( x \right) & \\
  y' &= \int 8x \,dx = 4x^{2} + C & \\
  y &= \int \left( 4x^{2} + C \right) \,dx & \\
  y &= \frac{4}{3} x^{3} + C_{1}x + C_{2}
\end{align}
$$

## Separable difflikninger

En separabel difflikning er en likning som kan skrives på formen

$$
P \left( y \right) \cdot y' = g \left( x \right)
$$

Eksempler:

$$
\begin{align}
  y' &= y \cdot \cos{x} & \\
  \frac{y'}{y} &= \cos{x} & \\
  \frac{1}{y} \cdot y' &= \cos{x} &
\end{align}
$$

$$
\begin{align}
  y' + x^{2} y' - x y &= 0 & \\
  y' + x^{2} y' &= x y & \\
  y' \left( 1 + x^{2} \right) &= x y & \\
  \frac{y'}{y} &= \frac{x}{1 + x^{2}} & \\
  \frac{1}{y} \cdot y' &= \frac{x}{1 + x^{2}} &
\end{align}
$$

---

Man har at

$$
\begin{align}
  P \left( y \right) \cdot y' &= g \left( x \right) & \\
  P \left( y \right) \cdot \frac{dy}{dx} &= g \left( x \right) & \\
  \int P \left( y \right) \frac{dy}{dx} \,dx &= \int g \left( x \right) \,dx & \\
  \int P \left( y \right) \,dy &= \int g \left( x \right) \,dx &
\end{align}
$$

Kan bruke dette med en likning:

$$
\begin{align}
  \frac{1}{y} \cdot y' &= \cos{x} & \\
  \int \frac{1}{y} \,dy &= \int \cos{x} \,dx & \\
  \ln{\left| y \right|} &= \sin{x} + C & \\
  e^{\ln{\left| y \right|}} &= e^{\left( \sin{x} + C \right)} & \\
  \left| y \right| &= e^{\sin{x}} \cdot e^{C_{1}} & \\
  y &= C \cdot e^{\sin{x}} &
\end{align}
$$

## Lineære differensiallikninger (av første orden)

Mens separable difflikninger er et produkt av $y'$ og en funksjon $P \left( y \right)$, mens lineære differensiallikninger er en sum og skrives på formen:

$$
y' + f \left( x \right) \cdot y = g \left( x \right)
$$

Her er $y$ og $y'$ i ulike ledd, som gjør at de ikke kan kombineres trivielt.

Hvis vi setter $g \left( x \right) = 0$, kaller vi dette en homogen difflikning. Dette blir den enkleste å løse. Hvis $g \left( x \right) \neq 0$, er dette en inhomogen difflikning, og dette er litt vanskeligere.

Den generelle løsningen tar utgangspunkt i produktregelen for derivasjon.

$$
\begin{align}
  \left( u \cdot y \right)' &= u' \cdot y + u \cdot y' &
\end{align}
$$

Her har vi et uttrykk der et ledd inneholder $y$ og et inneholder $y'$, men vi må ha faktorisert noe i det opprinnelige uttrykket for at denne skal passe inn.

$$
\begin{align}
  e^{F \left( x \right)} & & \\
  F \left( x \right) &= \int f \left( x \right) \,dx & \\
  \left( e^{F \left( x \right)} \right)' &= f \left( x \right) \cdot e^{F \left( x \right)} & \\
  y' + f \left( x \right) \cdot y &= g \left( x \right) & \cdot e^{F \left( x \right)}, F \left( x \right) = \int f \left( x \right) \,dx \\
  e^{F \left( x \right)} \cdot y' + f \left( x \right) \cdot e^{F \left( x \right)} \cdot y &= g \left( x \right) \cdot e^{F \left( x \right)} & \\
  \left( e^{F \left( x \right)} \cdot y \right)' &= g \left( x \right) \cdot e^{F \left( x \right)} & \\
  \int \left( e^{F \left( x \right)} \cdot y \right)' \,dx &= \int g \left( x \right) \cdot e^{F \left( x \right)} \,dx & \\
  e^{F \left( x \right)} \cdot y &= \int g \left( x \right) \cdot e^{F \left( x \right)} \,dx & \\
  y &= e^{-F \left( x \right)} \int g \left( x \right) \cdot e^{F \left( x \right)} \,dx &
\end{align}
$$
