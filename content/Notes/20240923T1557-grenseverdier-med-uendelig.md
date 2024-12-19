---
id: 20240923T1557-grenseverdier-med-uendelig
aliases:
  - grenseverdier med uendelig
tags: []
---

#matte [[20240616T1007-matte|matte]] [[20240916T0853-grenseverdi|grenseverdi]]

## Grenseverdier med uendelig

$$
f \left( x \right) = \frac{1}{x}
$$

$$
D_{f} = \mathbb{R} \setminus \left\{ 0 \right\}
$$

Hva skjer med $f \left( x \right)$ når $x \to 0^{+}$?

$$
f \left( 1 \right) = 1
$$

$$
f \left( \frac{1}{2} \right) = 2
$$

$$
f \left( 10^{-2} \right) = 10^{2}
$$

$$
f \left( 10^{-3} \right) = 10^{3}
$$

$$
f \left( 10^{-4} \right) = 10^{4}
$$

Jo nærmere vi kommer $0$, jo større blir $y$-verdien.

![20240923T0844-rational-function.png](Assets/20240923T0844-rational-function.png)

Det betyr at:

$$
\lim_{x \to 0^{+}} \frac{1}{x} = \infty
$$

Merk at $\infty$ (uendelig) er et symbol, IKKE et tall.

$$
f \left( x \right) \to \infty \text{ når } x \to 0^{+}
$$

Fordi uendelig ikke er et tall, betyr dette at grenseverdien ikke eksisterer. I tillegg er de to ensidige grenseverdiene ulike, så grenseverdien eksisterer ikke uansett.

Når $f \left( x \right)$ blir større og større når $x \to a$, eksisterer IKKE grenseverdien, men vi oppgir uendelig som svar.

Skrivemåte:

$$
\lim_{x \to a} f \left( x \right) = \infty
$$

- Vi kan få $f \left( x \right)$ så stor vi vil ved å velge $x$ nær nok $a$, men ikke lik $a$.

### Fortsettelse av oppgaven

$$
\lim_{x \to 0^{-}} f \left( x \right)
$$

$$
f \left( -10^{-1} \right) = -10^{1}
$$

$$
f \left( -10^{-2} \right) = -10^{2}
$$

$$
f \left( -10^{-3} \right) = -10^{3}
$$

![20240923T0852-rasjonal-funksjon-negativ.png](Assets/20240923T0852-rasjonal-funksjon-negativ.png)

$$
\underline{\underline{\lim_{x \to 0^{-}} f \left( x \right) = -\infty}}
$$

### Eksempel 1

$$
f \left( x \right) = \frac{1}{x}
$$

$$
\lim_{x \to \infty} f \left( x \right) = 0 \land \lim_{x \to -\infty} f \left( x \right) = 0
$$

$\displaystyle \lim_{x \to \infty} f(x) = b$ vil si at vi kan få $f(x)$ så nær b vi vil ved å velge stor nok $x$

$\displaystyle \lim_{x \to -\infty} f(x) = b$ vil si at vi kan få $f(x)$ så nær b vi vil ved å velge x som negativt tall med stor nok absoluttverdi

### Eksempel 2

$$
\lim_{x \to \infty} \frac{1}{x-3} = \lim{x \to \infty} \frac{1}{x} = \underline{\underline{0}}
$$

(Her trenger vi ikke å skrive det midterste leddet, man skjønner at man kan se bort fra $-3$ fordi den er negligerbar)

### Eksempel 3

$$
\lim_{x \to \infty} \left( \frac{1}{x} + 2 \right) = \lim_{x \to \infty} \frac{1}{x} + \lim{x \to \infty} 2 = 0 + 2 = 2
$$

(Same gjelder her, kan gå rett fra første til siste ledd)

### Eksempel 4

Dersom man har et polynomuttrykk i en brøk, kan man se bort fra alle leddene utenom det av høyeste grad. I praksis blir dette det samme som å gange med:

$$
\cdot \frac{ \frac{1}{x^{y}} }{ \frac{1}{x^{y}} }
$$

, der $y$ er graden av leddet med høyest grad.

$$
\lim_{x \to \infty} \frac{x^{2} + 1}{3x^{2} - 2x - 1} = \lim_{x \to \infty} \frac{\frac{x^{2}}{x^{2}} + \frac{1}{x^{2}}}{\frac{3x^{2}}{x^{2}} - \frac{2x}{x^{2}} - \frac{1}{x^{2}}} = \lim_{x \to \infty} \frac{1 + \frac{1}{x^{2}}}{3 - \frac{2}{x} - \frac{1}{x^{2}}} = \frac{1 + }{3 - 0 - 0} = \underline{\underline{\frac{1}{3}}}
$$

Her er ledd nr. 2 nødvendig å skrive, eller å forklare hvorfor jeg gikk rett fra 1 til svaret. Ledd 3 og 4 er ikke nødvendig på en innlevering, og er kun for å vise hva jeg gjør i eksempelet.

### Eksempel 5

$$
\lim_{x \to \infty} \frac{2x^{2} + 1}{4x^{2} - 3x + 1} = \lim_{x \to \infty} \frac{2\frac{x^{2}}{x^{2}} + \frac{1}{x^{2}}}{\frac{4x^{2}}{x^{2}} - \frac{3x}{x^{2}} + \frac{1}{x^{2}}} = \frac{2 + 0}{4 - 0 + 0} = \frac{2}{4} = \underline{\underline{\frac{1}{2}}}
$$

Steg 3 og 4 er unødvendig.

### Eksempel 6

Dersom man har en grenseverdi der funksjonen er en eksponentialfunksjon, kan man snu om på den:

$$
\lim_{x \to -\infty} e^{x} = \lim_{x \to \infty} \frac{1}{e^{x}} = \underline{\underline{0}}
$$
