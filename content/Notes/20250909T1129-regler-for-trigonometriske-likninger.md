---
id: 20250909T1129-regler-for-trigonometriske-likninger
aliases:
  - regler for trigonometriske likninger
tags: []
date: "2025-09-09"
title: regler for trigonometriske likninger
---

#matte [[20250819T1116-trigonometri|trigonometri]]

# regler for trigonometriske likninger

Oppsummering av trigonometri og de viktigste likningene.

## [[20250819T1116-trigonometri|Trigonometri]]

Verdier for $\sin{u}$ følger et system der $\sin{u} = \frac{\sqrt{n}}{2}$ der $n \in \left\{ 0, 1, 2, 3, 4 \right\}$ samsvarer med vinklene $\left\{ 0 \degree, 30 \degree, 45 \degree, 60 \degree, 90 \degree \right\}$. $\cos{u}$ følger samme systemet, men går nedover slik at det er "speilvendt" fra $\sin{u}$. Tangens kan utledes fra disse to verdiene ved $\frac{\sin{u}}{\cos{u}}$, og de gjenstående verdiene av $\sin{u}$ og $\cos{u}$ kan utledes ved hjelp av enhetssirkelen.

$$
\begin{align}
  \cos{u} &= \cos{\left( 2 \pi - u \right)} = \cos{\left( -u \right)} & \\
  \sin{u} &= \cos{\left( \pi - u \right)} & \\[1cm]
  -\cos{u} &= \cos{\left( \pi - u \right)} & \\
  -\sin{u} &= \sin{\left( 2\pi - u \right)} &
\end{align}
$$

## [[20250821T1057-trigonometriske-likninger|Trigonometriske likninger]]

$$
\begin{align}
  \sin{u} &= x & \\
  u = \sin^{-1}{x} + 2\pi \cdot n &\lor u = \pi - \sin^{-1}{x} + 2\pi \cdot n &, n \in \mathbb{Z} \\[1cm]
  \cos{u} &= x & \\
  u = \cos^{-1}{x} + 2\pi \cdot n &\lor u = - \cos^{-1}{x} + 2\pi \cdot n &, n \in \mathbb{Z} \\[1cm]
  \tan{u} &= x & \\
  u &= \tan^{-1}{x} + \pi \cdot n &, n \in \mathbb{Z}
\end{align}
$$

## [[20250902T1113-enhetsformelen|Enhetsformelen]]

$$
\begin{align}
  \sin^{2}{u} + \cos^{2}{u} &= 1 & \\
  \sin^{2}{u} &= 1 - \cos^{2}{u} & \\
  \cos^{2}{u} &= 1 - \sin^{2}{u} &
\end{align}
$$

## [[20250904T1054-sum-og-differanse-av-vinkler|Sum og differanse av vinkler]]

$$
\begin{align}
  \cos{\left( u \mp v \right)} &= \cos{u} \cdot \cos{v} \pm \sin{u} \cdot \sin{v} & \\
  \sin{\left( u \pm v \right)} &= \sin{u} \cdot \cos{v} \pm \cos{u} \cdot \sin{v} & \\[1cm]
  \sin{\left( 2u \right)} &= 2 \left( \sin{u} \cdot \cos{u} \right) & \\
  \cos{\left( 2u \right)} &= \cos^{2}{u} - \sin^{2}{u} & \\
  &= 1 - 2\sin^{2}{u} & \\
  &= 2 \cos^{2}{u} - 1 & \\
  \tan{\left( 2u \right)} &= \frac{2\tan{u}}{1 - \tan^{2}{u}} &
\end{align}
$$

## [[20250916T1105-harmoniske-svingninger|harmoniske svingninger]]

$$
\begin{align}
  f \left( x \right) &= a \cdot \sin{\left( cx \right)} + b \cdot \cos{\left( cx \right)} & \\
  &= A \cdot \sin{\left( cx + \varphi \right)} & \\
  A &= \sqrt{a^{2} + b^{2}} & \\
  \frac{a}{A} = \cos{\varphi} &\land \frac{b}{A} = \sin{\varphi} & \\
  \tan{\varphi} &= \frac{b}{a} &
\end{align}
$$
