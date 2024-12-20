---
id: 20241028T0959-derivasjon-av-logaritmer
aliases:
  - derivasjon av logaritmer
tags: []
title: Derivasjon av logaritmer
date: 2024-10-28
---

#matte [[20240616T1007-derivasjon|derivasjon]] [[20240821T0931-logaritmer|logaritmer]]

# derivasjon av logaritmer

$$
\left( \ln{x} \right)' = \frac{1}{x}
$$

## Skrive om som $\ln$

Man vil som oftest skrive uttrykk med $\lg$ om slik at alle logaritmer har $e$ som grunntall.

$$
x = 10^{\lg{x}}
$$

$$
\ln{x} = \ln{10^{\lg{x}}}
$$

$$
\ln{x} = \lg{x} \cdot \ln{10}
$$

$$
\frac{\ln{x}}{\ln{10}} = \lg{x}
$$

## Derivasjon

Finne den deriverte av $\left( \lg{x} \right)$.

$$
\left( \lg{x} \right)' = \left( \frac{1}{\ln{10}} \cdot \ln{x} \right)' = \frac{1}{\ln{10}} \cdot \frac{1}{x} = \underline{\underline{\frac{1}{x \ln{10}}}}
$$

Gjelder også for alle tall:

$$
\left( \log_{n}x \right)' = \frac{1}{x\ln{n}}
$$

## Bevis

Bevis for at $\left( \ln{x} \right)' = \frac{1}{x}$ ved hjelp av [[20241028T1009-definisjonen-av-den-deriverte|definisjonen av den deriverte]]:

$$
\begin{align}
    f \left( x \right) &= \ln{x} \\
    f' \left( x \right) &= \lim_{x \to 0} \frac{f \left( x + h \right) - f \left( x \right)}{h} \\
    &= \lim_{x \to 0} \frac{\ln{\left( x + h \right)} - \ln{x}}{h} \\
    &= \lim_{x \to 0} \frac{\ln{\left( \frac{x+h}{x} \right)}}{h} \\
    &= \lim_{x \to 0} \frac{\ln{\left( 1 + \frac{h}{x} \right)}}{h} \\
    &= \lim_{x \to 0} \frac{1}{h} \ln{\left( 1 + \frac{h}{x} \right)}
\end{align}
$$

La $\displaystyle n = \frac{x}{h}$. Da er $\displaystyle \frac{n}{x}=\frac{1}{h}$ og $\displaystyle \frac{hn}{x}=1 \implies \frac{h}{x} = \frac{1}{n}$
Ser at når $x \to 0$, vil $n \to \infty$

$$
\begin{align}
    &= \lim_{n \to \infty} \frac{n}{x} \ln{\left( 1 + \frac{1}{n} \right)} \\
    &= \lim_{n \to \infty} \frac{1}{x} \ln{\left( 1 + \frac{1}{n} \right)}^{n} \\
    &= \lim_{n \to \infty} \frac{1}{x} \cdot \lim_{n \to \infty} \ln{\left( 1 + \frac{1}{n} \right)}^{n} \\
    &= \frac{1}{x} \lim_{n \to \infty} \ln{\left( 1 + \frac{1}{n} \right)^{n}} \\
    &= \frac{1}{x} \ln{\lim_{n \to \infty}} \left( 1 + \frac{1}{n} \right)^{n}
\end{align}
$$

Vet at $\displaystyle \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^{n} = e$

$$
\begin{align}
    f' \left( x \right) &= \frac{1}{x} \ln{e} = \underline{\underline{ \frac{1}{x} }}
\end{align}
$$

## Oppgaver

### Eksempel 1

$$
\begin{align}
    f \left( x \right) &= 5x^{2} - 2\lg{x} \\
    f' \left( x \right) &= 10x - \frac{2}{x\ln{10}}
\end{align}
$$

### Eksempel 2

$$
\begin{align}
    g \left( x \right) &= \frac{1}{\ln{10}}\ln{x} - 2\lg{x} \\
    &= \lg{x} - 2\lg{x} \\
    &= -\lg{x} \\
    g' \left( x \right) &= -\frac{1}{x\ln{10}}
\end{align}
$$

$$
\begin{align}
    g \left( x \right) &= \frac{1}{\ln{10}}\ln{x} - 2\lg{x} \\
    g' \left( x \right) &= \frac{1}{\ln{10}} \cdot \frac{1}{x} - \frac{2}{x \cdot \ln{10}} \\
    g' \left( x \right) &= \frac{1}{x\ln{10}} - \frac{2}{x\ln{10}} = -\frac{1}{x\ln{10}}
\end{align}
$$
