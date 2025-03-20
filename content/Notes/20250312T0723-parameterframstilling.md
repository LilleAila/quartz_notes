---
id: 20250312T0723-parameterframstilling
aliases:
  - parameterframstilling
tags: []
date: "2025-03-12"
title: Parameterframstilling
---

#matte [[20240616T1007-matte|matte]] [[20250115T0716-vektorer|vektorer]]

# parameterframstilling

En rett linje $\mathscr{l}$ som går gjennom to punkter, har en retningsvektor $\vec{r}$

Vil bestemme koordinatene til et vilkårlig punkt $P \left( x, y \right)$ på $\mathscr{l}$

Vi kan gå fra origo til $P$ via $A$.... Det gir et uttrykk for posisjonsvektoren til $P$.

$$
\vec{OP} = \vec{OA} + \vec{AP}
$$

$\vec{AP}$ er parallell med $\vec{r}$, derfor finnes det et tall $k$ slik at $\vec{AP} = k \cdot \vec{r}$.

$$
\vec{OP} = \vec{OA} + k \cdot \vec{r}
$$

$$
\begin{align}
  \left[ x, y \right] &= \left[ -1, 4 \right] + k \cdot \left[ 3, 2 \right] & \\
  \left[ x, y \right] &= \left[ -1 + 3k, 4 + 2k \right] &
\end{align}
$$

$$
x = -1 + 3k \land y = 4 + 2k
$$

, altså er koordinatene til $P$ $\left( -1 + 3k, 4 + 2k \right)$.

$$
\mathscr{l} = \begin{cases}
    x &= -1 + 3k & \\
    y &= 4 + 2k &
\end{cases}
$$

Parameteren står ofte for tid, og det er vanlig å bruke $t$ som navnet på parameteren:

$$
\mathscr{l} = \begin{cases}
    x &= -1 + 3t & \\
    y &= 4 + 2t &
\end{cases}
$$

## Oppgave

> [!NOTE] Oppgave
> En rett linje går gjennom punktet $\left( x_{0}, y_{0} \right)$ og har retningsvektoren $\left[ a, b \right]$.
> La $P \left( x, y \right)$ være et vilkårlig punkt på linjen.
> Utled en parameterfremstilling for linjen etter mønster av det vi gjorde ovenfor.

Jeg ser ovenfor at koordinatene til punktet $A$, i dette tilfellet $\left( x_{0}, y_{0} \right)$, blir konstantleddet i den resulterende parameterfremstillingen, og retningsvektoren blir stigningstallet. Dermed blir

$$
\mathscr{l} = \begin{cases}
    x &= x_{0} + ak & \\
    y &= y_{0} + bk &
\end{cases}
$$

> [!NOTE]
> En linje har uendelig mange punkter og retningsvektorer, og det finnes derfor uendelig mange ulike parameterframstillinger for en vilkårlig linje avhengig av hvilket punkt og retningsvektor vi tar utgangspunkt i.

$$
\begin{align}
  \vec{OP} &= \vec{OA} + \vec{AP} & \\
  \vec{OA} &= \left[ x_{0}, y_{0} \right] & \\
  \vec{AP} &= k \cdot \left[ a, b \right] & \\
  \vec{OP} &= \left[ x_{0}, y_{0} \right] + k \cdot \left[ a, b \right] & \\
  \vec{OP} &= \left[ x_{0}, y_{0} \right] + \left[ ka, kb \right] & \\
  \vec{OP} &= \left[ x_{0} + ka, y_{0} + kb \right] & \\
  \mathscr{l} &= \begin{cases}
    x &= x_{0} + at & \\
    y &= y_{0} + bt &
  \end{cases} &
\end{align}
$$

## Oppgave - Eksempel 1

> [!NOTE] Oppgave
> En linje $\mathscr{l}$ går gjennom punktene $A \left( 2, 1 \right)$ og $B \left( -3, 5 \right)$. Finn en parameterframstilling for $\mathscr{l}$

Vektoren fra $A$ til $B$ er en retningsvektor for linjen.

$$
\vec{r} = \vec{AB} = \left[ -3-2, 5-1 \right] = \left[ -5, 4 \right]
$$

Velger $A$ som et punkt på linjen og får

$$
\mathscr{l} = \begin{cases}
    x &= 2 - 5t & \\
    y &= 1 + 4t &
\end{cases}
$$

### I GeoGebra

Bruker verktøyet `Linje`. Høyreklikk og velge `Parametrisk form`.

![20250312T0855-parameterframstilling-geogebra.png](Assets/20250312T0855-parameterframstilling-geogebra.png)

## Oppgave - Eksempel 2

> [!NOTE] Oppgave
> En linje $m$ er gitt ver likningen $y = 3x + 4$.
> Finn en parameterframstilling for $m$.

Stigningstallet for linjen er $3$, så $\left[ 1, 3 \right]$ er en retningsvektor for $m$.
Konstantleddet for linjen er $4$, så $\left( 0, 4 \right)$ er et punkt på $m$.

$$
\mathscr{l} = \begin{cases}
    x &= t & \\
    y &= 3t + 4 &
\end{cases}
$$

## Oppgave - "Snakk" s. 301

### a

Forklar at disse parameterframstillingene gir den samme linjen

a:

$$
\begin{cases}
    x &=& 3 + 2t \\
    y &=& 1 + 5t
\end{cases}
$$

b:

$$
\begin{cases}
    x &=& 3 + 6t \\
    y &=& 1 + 15t
\end{cases}
$$

c:

$$
\begin{cases}
    x &=& 1 -2t \\
    y &=& -4 -5t
\end{cases}
$$

a og b gir den samme linjen, fordi $\left[ 2, 5 \right] \parallel \left[ 6, 15 \right]$.

I c er $\left[ -2, -5 \right] \parallel \left[ 2, 5 \right]$. Setter inn punktet $\left( 1, -4 \right)$ i a for å sjekke at punktet ligger på linjen.

$$
\begin{align}
  3 + 2t &= 1 \implies t = -1 & \\
  1 + 5t &= -4 \implies t = -1 &
\end{align}
$$

$-1 = -1 \implies$ alle parameterframstillingene gir den samme linjen.

---

Alternativ (bedre) løsning:

$$
\begin{align}
  3 + 2t &= 1 \implies t = -1 & \\
  1 + 5 \cdot -1 &= -4 &
\end{align}
$$

$y = -4$, som samsvarer med punktet $\left( 1, -4 \right)$

### b

Finn en retningsvektor for linjen $y = ax + b$

Bruker skjæringspunktet med y-aksen, og

$$
\begin{align}
  \vec{r} &= \left[ 1, a \right] & \\
  P &= \left( 0, b \right) &
\end{align}
$$

Da blir parameterfremstillingen:

$$
\mathscr{l} : \begin{cases}
    x &= 0 + 1t & \\
    y &= b + at &
\end{cases}
$$

### c

Hva er stigningstallet til linjen med retningsvektoren

$\left[ 1, 6 \right] \implies 6$
$\left[ -1, 6 \right] \implies -6$
$\left[ 2, 5 \right] \implies 3$
$\left[ a, b \right] \implies \dfrac{b}{a}$

Vil skrive om slik at x i vektoren blir lik 1, slik at y blir stigningstallet.

## Oppgaver s. 301

### 7.1

En linje $n$ er gitt ved parameterframstillingen

$$
\mathscr{l} = \begin{cases}
    x &= 3 + 2t & \\
    y &= 1 + 5t &
\end{cases}
$$

#### a. Les ut av parameterframstillingen

##### 1. Koordinatene til et punkt som linjen går gjennom

$$
\left( 3, 1 \right)
$$

##### 2. En retningsvektor for linjen

$$
\left[ 2, 5 \right]
$$

#### b. Skriv opp koordinatene til ytterligere to

##### 1. Punkter som linjen går gjennom

$$
\begin{align}
  \left( 5, 6 \right)& & \\
  \left( 7, 11 \right)& &
\end{align}
$$

##### 2. Retningsvektorer for linjen

$$
\begin{align}
  \left[ 4, 10 \right]& & \\
  \left[ 6, 15 \right]& &
\end{align}
$$

### 7.2

En linje $\mathscr{l}$ går gjennom punktet $\left( 2, 3 \right)$ og har retningsvektoren $\left[ -2, 1 \right]$.

#### a. Finn en parameterfrramstilling for $\mathscr{l}$

$$
\mathscr{l} : \begin{cases}
  x &=& 2 - 2t \\
  y &=& 3 + t
\end{cases}
$$

#### b. Tegn linjen i et koordinatsystem

![[20250312T0723-parameterframstilling 2025-03-12 09.07.46.excalidraw.svg]]

### 7.3

En linje $m$ går gjennom punktene $A\left( 0, -2 \right)$ og $B\left( 3, 4 \right)$.
Finn en parameterframstilling for $m$ uten å bruke hjelpemidler.

$$
\begin{align}
  \vec{AB} &= \vec{OB} - \vec{OA} & \\
  &= \left[ 3, 4 \right] - \left[ 0, -2 \right] & \\
  &= \left[ 3, 6 \right] &
\end{align}
$$

$$
\mathscr{l} : \begin{cases}
  x &=& 3 - 3t \\
  y &=& 4 + 6t
\end{cases}
$$

## Oppgave - Eksempel 3

En linje $\mathscr{l}$ er gitt ved parameterfremstillingen

$$
\mathscr{l} : \begin{cases}
  x &=& 10 - 2t \\
  y &=& -3 + t
\end{cases}
$$

Finn likningen til $\mathscr{l}$.

Finner et uttrykk for $t$:

$$
\begin{align}
  x &= 10 + 2t & \\
  x - 10 &= 2t & \\
  t &= \frac{1}{2}x - 5 &
\end{align}
$$

Setter dette inn i den andre likningen:

$$
\begin{align}
  y &= -3 - t & \\
  y &= -3 - \left( \frac{1}{2}x - 5 \right) & \\
  y &= - \frac{1}{2}x + 2 &
\end{align}
$$

Likningen til $\mathscr{l}$ er $y = - \frac{1}{2} x + 2$.

## Oppgave - Eksempel 4

Finn skjæringspunktene medkoordinataksene for linjen $m$ gitt ved

$$
\mathscr{l} : \begin{cases}
  x &=& 10 - 2t \\
  y &=& -3 + t
\end{cases}
$$

I skjæringspunktet med $x$-aksen er $y = 0$. Det gir $t = -3$.
Setter inn $-3$ for $t$ i den andre likningen og får $x = 4$.
Skjæringspunktet med $x$-aksen er $\left( 4, 0 \right)$

I skjæringspunktet med $y$-aksen er $x = 0$. Det gir $t = -5$
Setter inn $-5$ for $t$ i den andre likningen og får $y = 2$.
Skjæringspunktet med $y$-aksen er $\left( 0, 2 \right)$

## Oppgaver side 302-303

### 7.5

En linke $m$ er gitt ved parameterframstillingen

$$
m : \begin{cases}
  x &=& t - 2 & \\
  y &=& 3t + 5
\end{cases}
$$

#### a

Hvilke av disse punktene ligger på $m$?

---

$$
\begin{align}
  A \left( 5, 26 \right) & & \\
  x &= t - 2 & \\
  5 &= t - 2 & \\
  t &= 7 & \\
  y &= 3t + 5 & \\
  y &= 3 \cdot 7 + 5 & \\
  y &= 26 & .
\end{align}
$$

Punktet ligger på $m$.

---

$$
\begin{align}
  B \left( 0, 10 \right) & & \\
  0 &= t - 2 & \\
  t &= 2 & \\
  y &= 3 \cdot 2 + 5 & \\
  y &= 11 \neq 10 &
\end{align}
$$

Punktet ligger ikke på $m$.

---

$$
\begin{align}
  C \left( -4, -1 \right)& & \\
  -4 &= t - 2 & \\
  t &= -2 & \\
  y &= 3 \cdot -1 + 5 & \\
  y &= -1 &
\end{align}
$$

Punktet ligger på $m$.

---

$$
\begin{align}
  D \left( 1, 0 \right) & & \\
  1 &= t - 2 & \\
  t &= 3 & \\
  y &= 3 \cdot 3 + 5 & \\
  y &= 14 \neq 0 &
\end{align}
$$

Punktet ligger ikke på $m$.

#### b

Finn likningen til $m$.

$$
\begin{align}
  x &= t - 2 & \\
  t &= x + 2 & \\
  y &= 3 \left( x + 2 \right) + 5 & \\
  y &= 3x + 11 &
\end{align}
$$

#### c

Finn en parameterframstiling for en linje $n$ som er parallell med $m$ og som går gjennom punktet $\left( 4, 7 \right)$.

Bruker samme retningsvektor ($\left[ 1, 3 \right]$), men med punktet $\left( 4, 7 \right)$.

$$
m : \begin{cases}
  x &=& 3 + 1t & \\
  y &=& 7 + 3t
\end{cases}
$$

$$
m : \begin{cases}
  x &=& t + 3 & \\
  y &=& 3t + 7
\end{cases}
$$

### 7.6

Finn skjæringspunktet mellom koordinataksene og den rette linjen $m$ gitt ved

$$
m : \begin{cases}
  x &=& 1 + t & \\
  y &=& -3 + 2t
\end{cases}
$$

---

Skjæring med y-aksen:

$$
\begin{align}
  x &= 0 & \\
  0 &= 1 + t & \\
  t &= -1 & \\
  y &= -3 + 2t & \\
  y &= -5 &
\end{align}
$$

Linjen $m$ skjærer $y$-aksen i $\left( 0, -5 \right)$.

---

Skjæring med x-aksen:

$$
\begin{align}
  y &= 0 & \\
  0 &= -3 + 2t & \\
  t &= \frac{3}{2} & \\
  x &= 1 + t & \\
  x &= \frac{5}{2} &
\end{align}
$$

Linjen $m$ skjærer $x$-aksen i $\left( \frac{5}{2}, 0 \right)$.

### 7.7

Linjen $n$ skjærer koordinataksene for $x$-verdien $5$ og $y$-verdien $-2$. Finn en parameterframstilling for $n$.

Linjen $n$ går gjennom punkteen $A\left( 0, -2 \right)$ og $B\left( 5, 0 \right)$.

$$
\vec{r} = \vec{AB} = \vec{OB} - \vec{OA} = \left[ 5, 2 \right]
$$

$$
m : \begin{cases}
  x &=& 5 + 5t & \\
  y &=& 2t
\end{cases}
$$

## Oppgave - Eksempel 5, s. 304

Finn skjæringspunktet mellom linjene $a$ og $b$ gitt ved

$$
a : \begin{cases}
  x &=& 3t - 1 \\
  y &=& -2t + 4
\end{cases}
$$

$$
b : \begin{cases}
  x &=& 2t - 4 \\
  y &=& t - 1
\end{cases}
$$

Erstatter $t$ med $s$ i $b$, slik at det er enklere å se at det kan være ulike verdier.

$$
b : \begin{cases}
  x &=& 2s - 4 \\
  y &=& s - 1
\end{cases}
$$

Setter $x$-koordinatene lik hverandre og $y$-koordinatene lik hverandre.

$$
\begin{bmatrix}
  I & 3t - 1 &= 2s - 4 \\
  II &-2t + 4 &= s - 1
\end{bmatrix}
$$

Likning $II$ gir $s = -2t + 5$. Setter inn i $I$, og får:

$$
\begin{align}
  3t - 1 &= 2 \left( 2t + 5 \right) - 4 & \\
  3t &= -4t + 7 & \\
  t &= 1 &
\end{align}
$$

Setter dette inn i $t$ for parameterfremstillingen for $a$:

$$
a : \begin{cases}
  x &=& 3 \cdot 1 - 1 &= 2 \\
  y &=& -2 \cdot 1 + 4 &= 2
\end{cases}
$$

Skjæringspunktet mellom $a$ og $b$ er $\left( 2, 2 \right)$.

## Oppgave - Eksempel 6 s. 306

> To båter $A$ og $B$ følger hver sin kurs gitt ved parameterfremstillingene
>
> $$
> A: \begin{cases}
> x &=& 100t+300 \\
> y &=& 150t + 400
> \end{cases}
> $$
>
> $$
> B: \begin{cases}
> x &=& -50t + 2100 \\
> y &=& 200t
> \end{cases}
> $$
>
> Parameteren $t$ står for tid målt i minutter etter at de startet, og enheten langs aksene er meter.
> Undersøk om båtene kolliderer.

Setter $x$-verdiene lik hverandre:

$$
\begin{align}
  100t + 300 &= -50t + 2100 & \\
  150t &= 1800 & \\
  t &= 12 &
\end{align}
$$

Setter $y$-verdiene lik hverandre:

$$
\begin{align}
  150t + 400& = 200t & \\
  400 &= 50t & \\
  8 &= t &
\end{align}
$$

Båtene vil krysse gjennom samme punkt, men på ulik verdi av $t$. Dermed vil de ikke kollidere.
