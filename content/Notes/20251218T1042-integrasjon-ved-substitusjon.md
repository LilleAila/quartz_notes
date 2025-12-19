---
id: 20251218T1042-integrasjon-ved-substitusjon
aliases:
  - integrasjon ved substitusjon
  - integrasjon ved substitusjon / variabelskifte
tags: []
date: "2025-12-18"
title: integrasjon ved substitusjon
---

#matte [[20251111T1105-integraler|integraler]]

# integrasjon ved substitusjon / variabelskifte

Dette kan sammenlignes med [[20241111T0941-kjerneregelen|kjerneregelen]] for derivasjon.

$$
\begin{align}
  \int x e^{x^{2}} \,dx & & \\
  u &= x^{2} & \\
  \frac{du}{dx} &= 2x & \\
  \frac{du}{2x} &= dx & \\
  \int x e^{u} \,\frac{du}{2x} &= \int \frac{x}{2x}e^{u} \,du & \\
  &= \int \frac{1}{2} e^{u} \,du &
\end{align}
$$

---

$$
\begin{align}
  \int x^{2}& \cdot e^{x^{2}} \,dx & \\
  u &= x^{2} &  \\
  \frac{du}{dx} &= 2x & \\
  \frac{du}{2x} &= dx & \\
  \int x^{2} \cdot e^{x^{2}} \,dx &= u \cdot e^{u} \,\frac{du}{2x} &
\end{align}
$$

Kan ikke fortsette herfra fordi man fortsatt har en $x$. Integrasjon ved substitusjon fungerer kun hvis man kan erstatte alle instanser av $x$ med $u$.

---

$$
\begin{align}
  \int \frac{2x}{x^{2} + 1}\,dx & & \\
  u &= x^{2} + 1 & \\
  \frac{du}{dx} &= 2x & \\
  dx &= \frac{du}{2x} & \\
  \int \frac{2x}{x^{2} + 1}\,dx &= \int \frac{2x}{u} \, \frac{du}{2x} & \\
  &= \int \frac{1}{u} \,du & \\
  &= \ln{\left| u \right|} & \\
  &= \ln{\left| x^{2} + 1 \right|} &
\end{align}
$$

# Oppgaver

## Eksempel s. 247

$$
\begin{align}
  \int 2xe^{x^{2}}\,dx & & \\
  u &= x^{2} & \\
  u' &= 2x & \\
  \int 2xe^{x^{2}} \,dx &= \int u' \cdot e^{u} \frac{du}{u'} & \\
  &= \int e^{u} \,du & \\
  &= e^{u} + C & \\
  &= e^{x^{2}} + C &
\end{align}
$$

## Eksempel 17

$$
\begin{align}
  \int \sin{\left( 4x + 5 \right)} \,dx & & \\
  u &= 4x + 5 & \\
  \frac{du}{dx} &= 4 & \\
  dx &= \frac{du}{4} & \\
  \int \sin{\left( 4x + 5 \right)} \,dx &= \int \sin{u} \cdot \frac{du}{4} & \\
  &= \int \frac{\sin{u}}{4} \,du & \\
  &= -\frac{1}{4} \cos{u} + C & \\
  &= -\frac{1}{4} \cos{\left( 4x + 5 \right)} + C &
\end{align}
$$
