---
id: 20250106T0943-lhopitals-regel
aliases:
  - l'hôpitals regel
tags: []
date: "2025-01-06"
title: L'Hôpitals regel
---

#matte [[20240616T1007-matte|matte]] [[20240916T0853-grenseverdi|grenseverdi]]

# L'Hôpitals regel

Hvis grenseverdien til teller og nevner begge går mot 0 eller uendelig

, kan vi se på [[20240616T1007-derivasjon|den deriverte]]til teller og nevner for å finne grenseverdien.

---

Dersom $\displaystyle \lim_{x \to a} f \left( x \right) = 0 \land \lim_{x \to a} g \left( x \right) = 0$ eller dersom $\displaystyle \lim_{x \to a} f \left( x \right) = \infty \land \lim_{x \to a} g \left( x \right) = \infty$, har vi at

$$
\lim_{x \to a} \frac{f \left( x \right)}{g \left( x \right)} = \lim_{x \to a} \frac{f' \left( x \right)}{g' \left( x \right)}
$$

Dersom $\displaystyle \lim_{x \to a} \frac{f' \left( x \right)}{g' \left( x \right)}$ eksisterer eller er lik $\pm \infty$.

## Eksempel

$$
\lim_{x \to 0} \frac{e^{2x} - 1}{x}
$$

(dette er et "$\frac{0}{0}$"-uttrykk, bruker L'Hôpital)

$$
\lim_{x \to 0} \frac{e^{2x} - 1}{x} = \lim_{x \to 0} \frac{\left( e^{2x} - 1 \right)'}{x'} = \lim_{x \to 0} \frac{2e^{2x}}{1} = 2e^{2 \cdot 0} = \underline{\underline{2}}
$$

## Eksempel 2

$$
\lim_{x \to \infty} \frac{x^{2}}{e^{3x}}
$$

(dette er et "$\frac{\infty}{\infty}$"-uttrykk, bruker L'Hôpital)

$$
\lim_{x \to \infty} \frac{x^{2}}{e^{3x}} = \lim_{x \to \infty} \frac{\left( x^{2} \right)'}{\left( e^{3x} \right)'} = \lim_{x \to \infty} \frac{2x}{3e^{3x}} = \lim_{x \to \infty} \frac{\left( 2x \right)'}{\left( 3e^{3x} \right)'} = \lim_{x \to \infty} \frac{2}{9e^{3x}} = 0
$$

## Eksempel 3

$$
\lim_{x \to 3} \frac{x-3}{x^{2} + x - 12}
$$

Dette er et $\frac{0}{0}$-uttrykk, og det kan enten løses ved L'Hôpitals eller ved faktorisering.

### L'Hôpitals

$$
\lim_{x \to 3} \frac{1}{2x + 1} = \underline{\underline{\frac{1}{7}}}
$$

### Faktorisering

$$
\lim_{x \to 3} \frac{x - 3}{x^{2} + x - 12} = \lim_{x \to 3} \frac{x - 3}{\left( x - 3 \right) \left( x + 4 \right)} = \lim_{x \to 3} \frac{1}{x + 4} = \underline{\underline{\frac{1}{7}}}
$$

(Sum-produkt-metoden. $4-3=1$ og $4 \cdot -3=-12$)
