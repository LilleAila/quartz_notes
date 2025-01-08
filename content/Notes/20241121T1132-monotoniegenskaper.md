---
id: 20241121T1132-monotoniegenskaper
aliases:
  - monotoniegenskaper
tags: []
date: "2024-11-21"
title: Monotoniegenskaper
---

#matte [[20240616T1007-matte|matte]] [[20240616T1007-derivasjon|derivasjon]]

# monotoniegenskaper

![20241121T1137-funksjon-eksempel.png](Assets/20241121T1137-funksjon-eksempel.png)

Funksjonen er strengt voksende i $\left[ a, c \right]$. Det betyr at den vokser gjennom hele intervallet.

$$
x_2 > x_1 \implies f \left( x_2 \right) > f \left( x_1 \right)
$$

Funksjonen er strengt avtakende i $\left\langle \leftarrow, a \right]$ og $\left[ c, \rightarrow \right\rangle$

$$
x_2 > x_1 \implies f \left( x_2 \right) < f \left( x_1 \right)
$$

Dette kalles monotoniegenskaper.

Hvis en funksjon er strengt voksende _eller_ strengt avtakende, kaller vi det strengt monoton.

> [!INFO] Monotoniegenskaper
> Gitt en funksjon $f$ og et intervall $I$ som er en del av eller lik $D_f$.
> \- $f$ er strengt voksende i $i$ hvis $x_2 > x_1 \implies f \left( x_2 \right) > f \left( x_1 \right)$ for alle $x_1, x_2 \in i$ > \- $f$ er strengt avtakende i $i$ hvis $x_2 > x_1 \implies f \left( x_2 \right) < f \left( x_1 \right)$ for alle $x_1, x_2 \in i$

## Oppgave

Hvorfor er det feil å si at $f$ er strengt avtakende i $\left\langle \leftarrow, a \right] \cup \left[ c, \rightarrow \right\rangle$

$f \left( c \right) > f \left( a \right) \land c > a \implies f$ er IKKE strengt avtakende i intervallet.

$f$ er strengt avtakende i $\left\langle \leftarrow, a \right]$ og i $\left[ c, \rightarrow \right\rangle$

## Fortegnslinje

- [ ] Insert bilde

![20241121T1202-fortegnslinje-monotoniegenskaper.png](Assets/20241121T1202-fortegnslinje-monotoniegenskaper.png)

$A$, $B$ og $C$ $\rightarrow$ Stasjonære punkt ($f' \left( x \right) = 0$ - horisontal tangent)

$A$ - bunnpunkt (går fra å avta til å vokse)
$B$ - terrassepunkt (vokser før og etter / avtar før og etter)
$C$ - toppunkt (går fra å vokse til å avta)

[[20240616T1007-ekstremalpunkt|Ekstremalpunkt]] og [[20240616T1007-terrassepunkt|terrassepunkt]] handler om hvordan monotoniegenskapene er før og etter punktene.

## Oppgave

$$
f \left( x \right) = e^{x} - 5x
$$

1. Finn monotoniegenskapene til $f$.
2. Finn koordinater til evt. stasjonære punkt.

### a)

$$
\begin{align}
    f' \left( x \right) &= e^{x} - 5 & \\
    e^{x} - 5 &= 0 & \\
    e^{x} &= 5 & \\
    x &= \ln{5} &
\end{align}
$$

Vet at $e^{x}$ er en strengt voksende funksjon. Den deriverte er negativ før $\ln{5}$, og voksende etter.

$$
\begin{align}
    \ln{6} \implies 6 - 5 &= 1 > 0 & \\
    \ln{4} \implies 4 - 5 &= -1 < 0 &
\end{align}
$$

$f$ er strengt avtakende i $\left\langle \leftarrow, \ln{5} \right]$.
$f$ er strengt voksende i $\left[ \ln{5}, \rightarrow \right\rangle$.

### b)

$x = \ln{5}$ gir $f' \left( x \right) = 0$ $\implies$ stasjonært punkt.
Monotoniegenskapene forteller at det er et bunnpunkt.

y-verdien:

$$
\begin{align}
    f \left( \ln{5} \right) &= e^{\ln{5}} - 5 \cdot \ln{5} & \\
    &= 5 - 5 \ln{5} & \\
    &= 5 \left( 1 - \ln{5} \right) &
\end{align}
$$

Bunnpunkt i $\left( \ln{5}, 5-5\ln{5} \right)$
