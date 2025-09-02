---
id: 20250902T1113-enhetsformelen
aliases:
  - enhetsformelen
tags: []
date: "2025-09-02"
title: enhetsformelen
---

#matte [[20250819T1116-trigonometri|trigonometri]] [[20250821T1057-trigonometriske-likninger|trigonometriske likninger]]

# enhetsformelen

![[20250819T1116-trigonometri 2025-09-02 11.04.09.excalidraw.svg]]

Uttrykker dette som vektorer og finner lengden. Får da at

$$
\begin{align}
  \vec{OP} &= \left[ \cos{u}, \sin{u} \right] & \\
  \left| \vec{OP} \right| &= 1 & \\
  \left| \vec{OP} \right| &= \sqrt{\left( \cos{u} \right)^{2} + \left( \sin{u} \right)^{2}} & \\
  \sqrt{\cos^{2}{u} + \sin^{2}{u}} &= 1^{2} & \\
  \cos^{2}{u} + \sin^{2}{u} &= 1 &
\end{align}
$$

Altså har vi at

$$
\cos^{2}{u} + \sin^{2}{u} = 1
$$

---

$$
\begin{align}
  & \frac{\cos^{2}{x} - 3 - \left( \sin^{2}{x} - 2 \right)}{\sin{x}} & \\
  &= \frac{1 - \sin^{2}{x} - 3 - \sin^{2}{x} + 2}{\sin{x}} & \\
  &= \frac{-2 \sin^{2}{x}}{\sin{x}} & \\
  &= -2 \sin{x} &
\end{align}
$$

---

$$
\begin{align}
  \sin^{2}{x} + 3 \cos^{2}{x} &= 1 & \\
  \sin^{2}{x} + 3 \cos^{2}{x} &= \cos^{2}x + \sin^{2}{x} & \\
  2 \cos^{2}{x} &= 0 &
\end{align}
$$

---

$$
\begin{align}
  \sin{u} &= \frac{3}{5} & \text{$u$ er i første kvadrant} \\
  \sin^{2}{u} &= \frac{9}{25} & \\
  1 - \cos^{2}{u} &= \frac{9}{25} & \\
  -\cos^{2}{u} &= \frac{9}{25} - \frac{25}{25} & \\
  \cos^{2}{u} &= \frac{16}{25} & \\
  \cos{u} &= \pm \frac{4}{5} & \\
  \cos{u} &= \frac{4}{5} & \text{fordi $u$ er i første kvadrant}
\end{align}
$$

# Oppgaver (s. 44)

## 1.35

Du får vite at vinkel $u$ ligger i andre kvadrant, og at $\sin{u} = \frac{1}{4}$.

**a**

> Bestem den eksakte verdien til $\cos{u}$.

$$
\begin{align}
  \sin{u} &= \frac{1}{4} & \\
  \sin^{2}{u} &= \frac{1}{16} & \\
  1 - \cos^{2}{u} &= \frac{1}{16} & \\
  -\cos^{2}{u} &= -\frac{15}{16} & \\
  \cos^{2}{u} &= \frac{15}{16} & \\
  \cos{u} &= - \frac{\sqrt{15}}{4} &
\end{align}
$$

**b**

> Bestem den eksakte verdien til $\tan{u}$

$$
\begin{align}
  \tan{u} &= \frac{\sin{u}}{\cos{u}} & \\
  &= \frac{\frac{1}{4}}{\frac{- \sqrt{15}}{4}} & \\
  &= \frac{1}{4} \cdot \frac{4}{- \sqrt{15}} & \\
  &= \frac{4}{-4 \cdot \sqrt{15}} & \\
  &= - \frac{1}{\sqrt{15}} & \\
  &= - \frac{\sqrt{15}}{15} &
\end{align}
$$

## 1.36

Du får vite at $\cos{x} = \frac{5}{7}$. Bestem $\sin{x}$ og $\tan{x}$ når du får vite at vinkelen $x$ ligger i fjerde kvadrant.

**sin**

$$
\begin{align}
  \cos{x} &= \frac{5}{7} & \\
  \cos^{2}{x} &= \frac{25}{49} & \\
  1 - \sin^{2}{x} &= \frac{25}{49} & \\
  -\sin^{2}{x} &= -\frac{24}{49} & \\
  \sin^{2}{x} &= \frac{24}{49} & \\
  \sin{x} &= - \frac{\sqrt{24}}{7} & \\
  \sin{x} &= - \frac{2\sqrt{6}}{7} &
\end{align}
$$

**tan**

$$
\begin{align}
  \tan{x} &= \frac{\sin{x}}{\cos{x}} & \\
  &= \frac{\frac{-2\sqrt{6}}{7}}{\frac{5}{7}} & \\
  &= \frac{-2\sqrt{6}}{7} \cdot \frac{7}{5} & \\
  &= - \frac{2\sqrt{6}}{5} &
\end{align}
$$

## 1.37

Figuren viser vinklene $u$ og $v$ i enhetssirkelen.

<!-- Paste image virker ikke men bare lat som om figuren fra side 44 er her 😭 -->

**a**

> Bruk figuren til å finne eksakte verdier for $\sin{u}$, $\cos{u}$, $\tan{u}$, $\cos{v}$, $\sin{v}$ og $\tan{v}$.

Leser fra figuren at $\sin{u} = \frac{2}{5}$. Bruker enhetsformelen videre:

---

$$
\begin{align}
  \sin{u} &= \frac{2}{5} & \\
  \sin^{2}{u} &= \frac{4}{25} & \\
  1 - \cos^{2}{u} &= \frac{4}{25} & \\
  \cos^{2}{u} &= \frac{21}{25} & \\
  \cos{u} &= \frac{\sqrt{21}}{5} &
\end{align}
$$

---

$$
\begin{align}
  \tan{u} &= \frac{\sin{u}}{\cos{u}} & \\
  &= \frac{\frac{2}{5}}{\frac{\sqrt{21}}{5}} & \\
  &= \frac{2}{\sqrt{21}} & \\
  &= \frac{2 \sqrt{21}}{21} &
\end{align}
$$

---

Leser fra figuren at $\cos{v} = - \frac{2}{3}$. Bruker enhetsformelen videre:

---

$$
\begin{align}
  \cos{v} &= - \frac{2}{3} & \\
  \cos^{2}{v} &= \frac{4}{9} & \\
  \sin^{2}{v} &= \frac{5}{9} & \\
  \sin{v} &= - \frac{\sqrt{5}}{3} &
\end{align}
$$

---

$$
\begin{align}
  \tan{v} &= \frac{-\frac{\sqrt{5}}{3}}{-\frac{2}{3}} & \\
  &= \frac{\sqrt{5}}{2} &
\end{align}
$$

**b**

> Bruk digitalt verktøy til å finne $\angle u$ og $\angle v$. Kontroller at de trigonometriske verdiene du har funnet i a, stemmer.

$$
\angle u \approx 0.41 \land \angle v \approx 3.98
$$

> [!NOTE]
> Pass på å bruke symbolsk utregning i CAS
> Merk at CAS gir alltid den laveste vinkelen, så man må sette `v := 2pi - acos(-2/3)` for å få den riktige vinkelen, da denne har samme $\cos$-verdi. Legg merke til delen med `2pi -`

![[Pasted image 20250902120251.png]]