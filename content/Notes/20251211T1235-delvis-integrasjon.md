---
id: 20251211T1235-delvis-integrasjon
aliases:
  - delvis integrasjon
tags: []
date: "2025-12-11"
title: delvis integrasjon
---

#matte [[20251111T1105-integraler|integraler]]

# delvis integrasjon

Baserer seg på [[20240616T1007-produktregelen|Produktregelen]]:

$$
\begin{align}
  \left( u v \right)' &= u'v + uv' & \\
  u'v + uv' &= \left( uv \right)' & \\
  \int \left( u'v + uv' \right) \,dx &= uv + C & \\
  \int u'v\,dx + \int uv'\,dx &= uv + C &
\end{align}
$$

Trekker fra $\int uv'\,dx$ på begge sider og får formelen for delvis integrasjon:

$$
\int u' \cdot v \,dx = u \cdot v - \int u \cdot v' \,dx
$$

> (trenger ikke å ta med konstanten $C$, da dette inngår i det ubestemte integralet)

### Eksempel 15

Bestem integralene ved hjelp av delvis integrasjon:

**a**

$$
\int 2x \cdot \ln{x} \,dx
$$

Velger $u' = 2x$ og $v$ = $\ln{x}$. Frå da $u = x^{2}$ og $v' = \frac{1}{x}$:

$$
\begin{align}
  \int u'v\,dx &= uv - \int uv' \,dx & \\
  \int 2x \cdot \ln{x} \,dx &= x^{2} \cdot \ln{x} - \int x^{2} \cdot \frac{1}{x} \,dx & \\
  &= x^{2} \ln{x} - \int x \,dx & \\
  &= x^{2} \ln{x} - \left( \frac{1}{2} x^{2} + C_{1} \right) & \\
  &= x^{2} \ln{x} - \frac{1}{2}x^{2} + C &
\end{align}
$$

**b**

$$
\int \left( 2t - 1 \right) e^{-2t} \,dt
$$

Velger $u' = e^{-2t}$ og $v = 2t-1$. Får da $u = -\frac{1}{2}e^{-2t}$ og $v' = 2$.

$$
\begin{align}
  \int u'v\,dx &= uv - \int uv' \,dx & \\
  \int \left( 2t - 1 \right) \cdot e^{-2t} \,dt &= - \frac{1}{2} e^{-2t} \cdot \left( 2t - 1 \right) - \int - \frac{1}{2} e^{-2t} \cdot 2 \,dt &
\end{align}
$$

# Oppgaver

## Eksempeloppgave 1

$$
\begin{align}
  \int \underbrace{2x}_{u} &\cdot \underbrace{e^{x}}_{v'} \,dx & \\
  \int u \cdot v' \,dx &= u \cdot v - \int u' \cdot v \,dx & \\
  v &= \int v' \,dx = e^{x} & \\
  u' &= 2 & \\
  \int 2x \cdot e^{x} \,dx &= 2x \cdot e^{x} - \int 2 \cdot e^{x} \,dx & \\
  &= 2x \cdot e^{x} - 2e^{x} + C &
\end{align}
$$

## Eksempeloppgave 2

$$
\begin{align}
  \int \ln{x} \,dx &= \int \underbrace{1}_{u'} \cdot \underbrace{\ln{x}}_{v} \,dx & \\
  u' = 1 &\implies u = x & \\
  v = \ln{x} &\implies v' = \frac{1}{x} & \\
  &= x \cdot \ln{x} - \int x \cdot \frac{1}{x} \,dx & \\
  &= x \cdot \ln{x} - x + C &
\end{align}
$$

## Eksempeloppgave 3

$$
\begin{align}
  \int x^{2} \cdot e^{x} \,dx &= x^{2} \cdot e^{x} - \int 2x \cdot e^{x} \,dx & \\
  &= x^{2} \cdot e^{x} - \left( 2x \cdot e^{x} - \int 2 \cdot e^{x} \,dx \right) & \\
  &= x^{2} \cdot e^{x} - 2x \cdot e^{x} - 2 e^{x} + C &
\end{align}
$$

## 4.33 (s. 244)

Bestem integralene:

**a**

$$
\begin{align}
  \int \left( 2x + 1 \right) \cdot e^{x} \,dx &= \left( 2x + 1 \right) \cdot e^{x} - \int 2e^{x} \,dx & \\
  &= 2xe^{x} + e^{x} - 2e^{x} & \\
  &= 2xe^{x} - e^{x} + C &
\end{align}
$$

**b**

$$
\begin{align}
  \int 4x \cdot e^{2x} \,dx &= 4x \cdot \frac{1}{2}e^{2x} - \int 4 \cdot \frac{1}{2} e^{2x} \,dx & \\
  &= 2xe^{2x} - e^{2x} + C &
\end{align}
$$

## 4.34

Bestem integralene:

**a**

$$
\begin{align}
  \int x^{4} \ln{x} \,dx &= \frac{1}{5}x^{5} \cdot \ln{x} - \int \frac{1}{5}x^{5} \cdot \frac{1}{x} & \\
  &= \frac{1}{5}x^{5} \ln{x} - \int \frac{1}{5} x^{4} & \\
  &= \frac{1}{5}x^{5} \ln{x} - \frac{1}{25} x^{5} + C &
\end{align}
$$

**b**

$$
\begin{align}
  \int x \cdot e^{3x} \,dx &= x \cdot \frac{1}{3} e^{3x} - \int 1 \cdot \frac{1}{3}e^{3x} & \\
  &= \frac{1}{3}xe^{3x} - \frac{1}{9}e^{3x} + C &
\end{align}
$$

**c**

$$
\begin{align}
  \int x^{2} \cdot e^{x}\,dx &= x^{2}e^{x} - \int 2x \cdot e^{x} \,dx & \\
  &= x^{2}e^{x} - \left( 2xe^{x} - \int \left( 2e^{x} \right) \,dx \right) & \\
  &= x^{2}e^{x} - 2xe^{x} + 2e^{x} + C &
\end{align}
$$

## 4.36

Bestem integralene:

**a**

$$
\begin{align}
  \int x \sin{3x} \,dx &= - \frac{1}{3} x \cos{3x} - \int - \frac{1}{3} \cos{3x} \,dx & \\
  &= - \frac{1}{3} x \cos{3x} + \frac{1}{9} \sin{3x} + C &
\end{align}
$$

**b**

$$
\begin{align}
  \int x^{2} \sin{x} \,dx &= - x^{2} \cos{x} - \int -2x \cos{x} \,dx & \\
  &= -x^{2} \cos{x} - \left( -2x \sin{x} - \int -2 \sin{x} \,dx \right) & \\
  &= -x^{2}\cos{x} + 2x \sin{x} + 2 \cos{x} + C &
\end{align}
$$
