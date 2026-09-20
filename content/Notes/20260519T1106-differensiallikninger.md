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

## Differensiallikninger av andre orden

$$
y'' + f \left( x \right) \cdot y' + g \left( x \right) \cdot y = h \left( x \right)
$$

En slik likning har ingen generell løsning.

$h \left( x \right) = 0 \iff \text{Homogen likning}$

$f \left( x \right)$ og $g \left( x \right)$ er konstanter $b$ og $c$ der $b \in \mathbb{R}$ og $c \in \mathbb{R}$. Altså har uttrykket konstante koeffisienter. Vi kan da forenkle til:

$$
y'' + b \cdot y' + c \cdot y = 0
$$

Dette er en homogen andreordens lineær differensiallikning med konstante koeffisienter, som har en generell løsning.

$$
\begin{align}
  y &= e^{rx} & \\
  y' &= r e^{rx} & \\
  y'' &= r^{2} e^{rx} & \\
  r^{2} \cdot e^{rx} + b \cdot r \cdot e^{rx} + c \cdot e^{rx} &= 0 & \\
  e^{rx} \left( r^{2} + b \cdot r + c \right) &= 0 & \\
  r^{2} + b \cdot r + c &= 0 &
\end{align}
$$

Dette er den karakteristiske likningen for en slik differensiallikning. Dette er en enkel andregradslikning der man kan finne $r$ og skrive dette inn i uttrykket for $y$. Man kan da finne 2, 1 eller 2 komplekse løsninger

### Eksempler

$$
y'' + y' - 6y = 0
$$

#### a)

> Vis at $r_{1} = -3$ og $r_{2} = 2$

$$
\begin{align}
  r^{2} + r - 6c &= 0 & \\
  \left( r - 2 \right) \left( r + 3 \right) &= 0 & \\
  r_{1} = -3 &\lor r_{2} = 2 &
\end{align}
$$

#### b)

> Vis at $y_{1} = e^{-3x}$ og $y_{2} = e^{2x}$

$$
\begin{align}
  y &= e^{rx} & \\
  y_{1} = e^{-3x} &\lor y_{2} = e^{2x} &
\end{align}
$$

#### c)

> Vis at $y = C_{1} e^{-3x} + C_{2} r^{2x}$ er en løsning for likningen.

$$
\begin{align}
  y &= C_{1} e^{r_{1}x} + C_{2} e^{r_{2}x} & \\
  y' &= C_{1} \cdot r_{1} \cdot e^{r_{1} x} + C_{2} \cdot r_{2} \cdot e^{r_{2}x} & \\
  y'' &= C_{1} \cdot r_{1}^{2} \cdot e^{r_{1}x} + C_{2} \cdot r_{2}^{2} \cdot e^{r_{2}x} & \\
  \left( C_{1} \cdot r_{1}^{2} \cdot e^{r_{1}x} + C_{2} \cdot r_{2}^{2} \cdot e^{r_{2}x} \right) + b \left( C_{1} \cdot r_{1} \cdot e^{r_{1}x} + C_{2} \cdot r_{2} \cdot e^{r_{2}x} \right) + c \left( C_{1}e^{r_{1}x} + C_{2}e^{r_{2}x} \right) &= 0 & \\
  \left( C_{1} \cdot \left( -3 \right)^{2} \cdot e^{-3x} + 2 \cdot 2^{2} \cdot e^{2x} \right) + C_{2} \cdot \left( -3 \right) \cdot e^{-3x} + C_{2} \cdot 2 \cdot e^{2x} - 6 \left( C_{1}e^{-3x} + C_{2}e^{2x} \right) &= 0 &
\end{align}
$$

Får til slutt at dette er sant, jeg gidder ikke å gjøre hele greien lol

### Generelt

Om $a \cdot y'' + b \cdot y' + c = 0$, har vi $a r^{2} + br + c = 0$.

Med to løsninger for den karakteristiske likningen, får man

$$
y = c_{1} \cdot e^{r_{1}x} + C_{2} \cdot e^{r_{2}x}
$$

Med én løsning for $r$, får man

$$
y = C_{1} \cdot x \cdot e^{rx} + C_{2} \cdot e^{rx}
$$

### Komplekse løsninger!

Vi har at

$$
i = \sqrt{-1} \implies i^{2} = -1
$$

Dette definerer komplekse tall. Vi kan da bruke:

$$
\begin{align}
  y'' - 6y' + 25y &= 0 & \\
  r^{2} - 6r + 25r &= 0 & \\
  r &= \frac{6 \pm \sqrt{36 - 100}}{2} & \\
  r &= \frac{6 \pm \sqrt{-64}}{2} & \\
  r &= \frac{6 \pm \sqrt{64} \sqrt{-1}}{2} & \\
  r &= \frac{6 \pm 8i}{2} & \\
  r &= 3 \pm 4i &
\end{align}
$$

Komplekse tall har en imaginær del og en reell del. Vi kan kalle den reelle delen $A$ og den imaginære delen for $B$. Man får da denne løsningen på differensiallikningen. Merk at denne løsningen er reell, selv om vi har fått en kompleks $r$ fra den karakteristiske likningen.

$$
y = e^{Ax} \left( C_{1} \cdot \sin{Bx} + C_{2} \cdot \cos{Bx} \right)
$$
