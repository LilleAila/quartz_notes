---
id: 20250904T1054-sum-og-differanse-av-vinkler
aliases:
  - sum og differanse av vinkler
tags: []
date: "2025-09-04"
title: sum og differanse av vinkler
---

#matte [[20250526T1040-matte-r2|Matte R2]] [[20250819T1116-trigonometri|trigonometri]]

# sum og differanse av vinkler

Tegner opp en enhetssirkel med to vinkler som vektorer fra $O$ til et punkt på sirkellinjen.

![[2025-09-04 2025-09-04 10.40.06.excalidraw.svg]]

$$
\begin{align}
  \vec{OP} \cdot \vec{OQ} &= \underbrace{\left| \vec{OP} \right|}_{=1} \cdot \underbrace{\left| \vec{OQ} \right|}_{=1} \cdot \cos{\left( u - v \right)} & \\
  &= \cos{\left( u - v \right)} & \\
  \vec{OP} &= \left[ \cos{u}, \sin{u} \right] & \\
  \vec{OQ} &= \left[ \cos{v}, \sin{v} \right] & \\
  \vec{OP} \cdot \vec{OQ} &= \cos{u} \cdot \cos{v} + \sin{u} \cdot \sin{v} & \\
  \cos{\left( u - v \right)} &= \cos{u} \cdot \cos{v} + \sin{u} \cdot \sin{v} &
\end{align}
$$

---

Eksempel:

$$
\begin{align}
  \cos{\left( 15 \degree \right)} &= \cos{\left( 45 \degree - 30 \degree \right)} & \\
  &= \cos{45\degree} + \cos{30 \degree} + \sin{45\degree} \cdot \sin{30\degree} & \\
  &= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} & \\
  &= \frac{\sqrt{6} + \sqrt{2}}{2} &
\end{align}
$$

### Addisjon

$$
\begin{align}
  \cos{\left( u + v \right)} &= \cos{\left( u - \left( -v \right) \right)} & \\
  &= \cos{\left( u \right)} \cdot \cos{\left( -v \right)} + \sin{\left( u \right)} \cdot \sin{\left( -v \right)} & \\
  &= \cos{u} \cdot \cos{v} - \sin{u} \cdot \sin{v} &
\end{align}
$$

### Sinus

Bruker det at sinus og cosinus er forskjøvet med $90 \degree$ for å omformulere uttrykket:

$$
\begin{align}
  \sin{\left( u + v \right)} &= \cos{\left( 90 \degree - \left( u + v \right) \right)} & \\
  % &= \cos{\left( 90\degree \right)} \cdot \cos{\left( u + v \right)} + \sin{\left( 90\degree \right)} \cdot \sin{\left( u + v \right)} &
  &= \cos{\left( 90\degree - u - v \right)} & \\
  &= \cos{\left( \left( 90 \degree - u \right) - v \right)} & \\
  &= \cos{\left( 90 \degree - u \right)} \cdot \cos{\left( v \right)} + \sin{\left( 90\degree - u \right)} \cdot \sin{\left( v \right)} & \\
  &= \sin{u} \cdot \cos{v} + \cos{u} \cdot \sin{v} &
\end{align}
$$

### Oppsummering

> [!NOTE] Likninger for sum og differanse av vinkler
>
> $$
> \begin{align}
>   \cos{\left( u \mp v \right)} &= \cos{u} \cdot \cos{v} \pm \sin{u} \cdot \sin{v} & \\
>   \sin{\left( u \pm v \right)} &= \sin{u} \cdot \cos{v} \pm \cos{u} \cdot \sin{v} &
> \end{align}
> $$

Ut fra dette kan man også utlede definisjoner for $2u$:

$$
\begin{align}
  \sin{\left( 2 u \right)} &= \sin{\left( u + u \right)} & \\
  &= \sin{u} \cdot \cos{u} + \cos{u} \cdot \sin{u} & \\
  \sin{\left( 2u \right)} &= 2 \left( \sin{u} \cdot \cos{u} \right) &
\end{align}
$$

---

$$
\begin{align}
  \cos{\left( 2u \right)} &= \cos{\left( u + u \right)} & \\
  &= \cos{u} \cdot \cos{u} - \sin{u} \cdot \sin{u} & \\
  &= \cos^{2}{u} - \sin^{2}{u} &
\end{align}
$$

Kan nå bruke [[20250902T1113-enhetsformelen|enhetsformelen]] til å skrive det om:

$$
\begin{align}
  \cos{\left( 2u \right)} &= \cos^{2}{u} - \left( 1 - \cos^{2}{u} \right) & \\
  &= 2 \cos^{2}{u} - 1 & \\
  \cos{\left( 2u \right)} &= \left( 1 - \sin^{2}{u} \right) - \sin^{2}{u} & \\
  &= 1 - 2 \sin^{2}{u} &
\end{align}
$$

# Oppgaver (s. 50)

## 1.45

> Bestem eksakte verdier for

**a**

> $\sin{75\degree}$

$$
\begin{align}
  \sin{75\degree} &= \sin{\left( 45 \degree + 30 \degree \right)} & \\
  &= \sin{45\degree} \cdot \cos{30 \degree} + \cos{45 \degree} \cdot \sin{30 \degree} & \\
  &= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} & \\
  &= \frac{\sqrt{6} + \sqrt{2}}{4} &
\end{align}
$$

**b**

> $\cos{75 \degree}$

$$
\begin{align}
  \cos{75\degree} &= \cos{\left( 45\degree + 30 \degree \right)} & \\
  &= \cos{45\degree} \cdot \cos{30\degree} - \sin{45\degree} \cdot \sin{30\degree} & \\
  &= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2} & \\
  &= \frac{\sqrt{6} - \sqrt{2}}{4} &
\end{align}
$$

**c**

> $\tan{75 \degree}$

$$
\begin{align}
  \tan{75 \degree} &= \frac{\sin{75 \degree}}{\cos{75\degree}} & \\
  &= \frac{\frac{\sqrt{6} + \sqrt{2}}{4}}{\frac{\sqrt{6} - \sqrt{2}}{4}} & \\
  &= \frac{\sqrt{6} + \sqrt{2}}{\sqrt{6} - \sqrt{2}} & \\
  &= \frac{\left( \sqrt{6} + \sqrt{2} \right)^{2}}{\sqrt{6}^{2} - \sqrt{2}^{2}} & \\
  &= \frac{6 + 2 \sqrt{12} + 2}{4} & \\
  &= 2 + \frac{\sqrt{12}}{4} & \\
  &= 2 + \sqrt{3} &
\end{align}
$$

## 1.46

> Bestem eksakte verdier for

**a**

> $\sin{105 \degree}$

$$
\begin{align}
  \sin{105 \degree} &= \sin{45 \degree + 60 \degree} & \\
  &= \sin{45 \degree} \cdot \cos{60 \degree} + \cos{45 \degree} \cdot \sin{60 \degree} & \\
  &= \frac{\sqrt{2}}{2} \cdot \frac{1}{2} + \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} & \\
  &= \frac{\sqrt{2} + \sqrt{6}}{4} &
\end{align}
$$

**b**

> $\cos{105 \degree}$

$$
\begin{align}
  \cos{105 \degree} &= \cos{45 \degree + 60 \degree} & \\
  &= \cos{45 \degree} \cdot \cos{60 \degree} - \sin{45 \degree} \cdot \sin{60 \degree} & \\
  &= \frac{\sqrt{2}}{2} \cdot \frac{1}{2} - \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} & \\
  &= \frac{\sqrt{2} - \sqrt{6}}{4} &
\end{align}
$$

**c**

> $\tan{105 \degree}$

$$
\begin{align}
  \tan{105 \degree} &= \frac{\sin{105 \degree}}{\cos{105 \degree}} & \\
  &= \frac{\frac{\sqrt{2} + \sqrt{6}}{4}}{\frac{\sqrt{2} - \sqrt{6}}{4}} & \\
  &= \frac{\sqrt{2} + \sqrt{6}}{\sqrt{2} - \sqrt{6}} & \\
  &= \frac{2 + 2 \sqrt{12} + 6}{-4} & \\
  &= -2 - \sqrt{3} &
\end{align}
$$

## 1.47

> Forenkle uttrykkene

**a**

$$
\begin{align}
  \sin{\left( v + 60 \degree \right)} + \cos{\left( v + 30 \degree \right)} &= \sin{v} \cdot \cos{60 \degree} + \cos{v} \cdot \sin{60\degree} + \cos{v} \cdot \cos{30\degree} - \sin{v} \cdot \sin{30\degree} & \\
  &= \sin{v} \cdot \frac{1}{2} + \cos{v} \cdot \frac{\sqrt{3}}{2} + \cos{v} \cdot \frac{\sqrt{3}}{2} - \sin{v} \cdot \frac{1}{2} & \\
  &= \sqrt{3} \cos{v} &
\end{align}
$$

**b**

$$
\begin{align}
  \sin{\left( v + \frac{\pi }{4} \right)} - \cos{\left( v - \frac{\pi }{4} \right)} &= \sin{v} \cdot \cos{\frac{\pi }{4}} + \cos{v} \cdot \sin{\frac{\pi }{4}} - \left( \cos{v} \cdot \cos{\frac{\pi }{4}} + \sin{v} \cdot \sin{\frac{\pi }{4}} \right) & \\
  &= \sin{v} \cdot \frac{\sqrt{2}}{2} + \cos{v} \cdot \frac{\sqrt{2}}{2} - \cos{v} \cdot \frac{\sqrt{2}}{2} - \sin{v} \cdot \frac{\sqrt{2}}{2} & \\
  &= 0 &
\end{align}
$$

## 1.48
