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

## Definisjon ved skalarprodukt

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
