---
id: 20250317T1101-parameterframstilling-for-kurver
aliases:
  - parameterframstilling for kurver
tags: []
date: "2025-03-17"
title: parameterframstilling for kurver
---

#matte [[20250312T0723-parameterframstilling|parameterframstilling]]

# parameterframstilling for kurver

Man ser på et vilkårlig punkt $P \left( x, y \right)$ på linjen som går gjennom punktet $\left( x_{0}, y_{0} \right)$ og har retningsvektor $\left[ a, b \right]$. Dette punktet er gitt ved posisjonsvektoren

$$
\vec{OP} = \left[ x, y \right] = \left[ x_{0} + at, y_{0} + bt \right], t \in \mathbb{R}
$$

Hver verdi av parameteren $t$ gir en bestemt vektor $\vec{OP}$. $\vec{r}$ gitt ved $\vec{r} \left( t \right) = \vec{OP}$ er en _vektorfunksjon_ med parameteren $t$ som variabel. Man kan bruke uttrykk som ikke er lineære som koordinatene i vektorfunksjonen.

> [!NOTE]
> La $\vec{r} \left( t \right)$ være posisjonsvektoren til punktet $P \left( x \left( t \right), y \left( t \right) \right)$ på en kurve.
> Da er vektorfunksjonen $\vec{r}$ gitt ved $\vec{r} \left( t \right) = \left[ x \left( t \right), y \left( t \right) \right]$.

> Kan plotte i GeoGebra med `Kurve(<x-uttrykk>, <y-uttrykk>, <parameter>, <start>, <slutt>)`

## Oppgave

En spydkaster kaster spydet i en parabelbane gitt ved parameterfremstillingen

$$
s: \begin{cases}
    x &=& 20t \\
    y &=& 2 + 20t - 4.9t^{2}
\end{cases}
$$

Her er $t$ antall sekunder etter at spydet er kastet. $x$-aksen er langs bakken, og lengdene er målt i meter.

### a)

Tegn kurven som viser spydets bane.

Bruker GeoGebra, med `Kurve(20t, 2+20t-4.9t^2, t, 0, 5)`

![20250317T1121-geogebra-spyd-parameterfremstilling-kurve.png](Assets/20250317T1121-geogebra-spyd-parameterfremstilling-kurve.png)

### b)

Regn ut hvor lang tid det vil ta før spydet treffer bakken og lengden på kastet.

Vet at spydet treffer bakken når $y=0$:

$$
\begin{align}
  0 &= -4.9t^{2} + 20t + 2 & \\
  a &= -4.9 & \\
  b &= 20 & \\
  c &= 2 & \\
  x_{1}, x_{2} &= \frac{-20 \pm \sqrt{20^{2} - 4 \cdot -4.9 \cdot 2}}{2 \cdot -4.9} & \\
  x &= \frac{-20 + \sqrt{439.2}}{-9.8} & \\
  x &\approx 0.09766316693 &
\end{align}
$$

Forkaster den negative løsningen, da den ikke kan treffe bakken _før_ spydet blir kastet.

### c)

Finn når spydet er på sitt høyeste og hvor høyt det er da.

$$
\vec{r} \left( t \right) = \left[ x \left( t \right), y \left( t \right) \right] \implies \vec{r'} \left( t \right) = \left[ x' \left( t \right), y' \left( t \right) \right]
$$

Fart:

$$
s': \begin{cases}
    x &=& 20 \\
    y &=& 2 - 9.8 t
\end{cases}
$$

> [!NOTE] Note
> $9.8$ er omtrent gravitasjonsakselerasjonen på jorden

Setter da $y$-koordinaten av den deriverte lik $0$, og setter $t$ inn i uttrykket for $y$.

$$
\begin{align}
  2-9.8t &= 0 & \\
  t &= 2.04 & \\
  y &= 2 + 20 \cdot 2.04 - 4.9 \cdot 2.04^{2} & \\
  &= 22.41 &
\end{align}
$$

Spydet er på sitt høyeste etter $2.04$ sekunder, og er $22.41$ meter over bakken på dette tidspunktet.

### d)

Man finner akselerasjonen ved å derivere posisjonsvektoren to ganger og så regne ut lengden av denne vektoren. Finn akselerasjonen til spydet.

Akselerasjon:

$$
s'': \begin{cases}
    x &=& 0 \\
    y &=& -9.81
\end{cases}
$$

## Oppgave 7.14

Ulla står på et vannrett underlag og kaster en stein på skrå opp i luften. Steinen følger en del av kruven til vektorfunksjonen gitt ved

$$
\vec{r} \left( t \right) = \left[ 8.7t, -4.9t^{2} + 12t + 2 \right]
$$

Her er $t$ tiden målt i sekunder etter at steinen ble kastet. Koordinatsystemet har $x$-aksen langs bakken og $y$-aksen normalt på bakken der Ulla står. Enheten på aksene er meter.

### a)

> Tegn kurven til $\vec{r}$ for $t \in \left[ 0, 3 \right]$.

![20250317T1237-kurve.png](Assets/20250317T1237-kurve.png)

### b)

> Hvor er steinen når den forlater hånden?

$$
r: \begin{cases}
    x &=& 8.7t \\
    y &=& -4.9t^{2} + 12t + 2
\end{cases}
$$

Når steinen forlater hånden er $t=0$.

$$
\begin{align}
  x &= 8.7 \cdot 0 & \\
  &= 0 & \\
  y &= -4.9 \cdot 0^{2} + 12 \cdot 0 + 2 & \\
  &= 2 &
\end{align}
$$

Steinen forlater hånden i $\left( 0, 2 \right)$.

### c)

> Hvor lang tid tar det før steinen lander på bakken?

Løser likningen $y = 0$.

$$
\begin{align}
  -4.9t^{2} + 12t + 2 &= 0 & \\
  a &= -4.9 & \\
  b &= 12 & \\
  c &= 2 & \\
  t &= \frac{-12 \pm \sqrt{12^{2} - 4 \cdot -4.9 \cdot 2}}{2 \cdot -4.9} & \\
  t &= \frac{-12 \pm \sqrt{173.4}}{-9.8} & \\
  t_{0} \approx -0.1191983038 &\lor t_{1} \approx 2.568177896 &
\end{align}
$$

Tiden må være positiv, så kun den ene løsningen er gyldig. Det tar omtrent $2.6$ sekunder før steinen lander på bakken.

### d)

> Hvor langt er kastet?

Bruker verdien av $t$ fra forrige oppgave, og setter dette inn i funksjonen for $x$-verdien:

$$
\begin{align}
  t &\approx 2.6 & \\
  x &= 8.7 \cdot 2.6 & \\
  &= 22.62 &
\end{align}
$$

## 7.15

Alma fant et revespor. Hun fant ut at reven hadde fulgt kurven til vektorfunksjonen gitt ved

$$
\vec{r} \left( t \right) = \left[ t^{3} - t, 3t^{2} + 1 \right], -1.5 \leq t \leq 2.5
$$

Her står $t$ for tid målt i timer, $y$-aksen viser retning Nord og enheten langs aksene er kilometer.

### a)

> Tegn kurven til $\vec{r}$

![20250317T1305-kurve.png](Assets/20250317T1305-kurve.png)

### b)

> Bestem $\vec{r} \left( 0 \right)$. Hva forteller svaret?

$$
\begin{align}
  \vec{r} \left( 0 \right) &= \left[ 0 - 0, 3 \cdot 0 + 1 \right] & \\
  &= \left[ 0, 1 \right] &
\end{align}
$$

Dette forteller at $\vec{OP}$ etter 0 timer var $\left[ 0, 1 \right]$, som betyr at reven befant seg 1 kilometer nord.

### c)

> Bestem $\left| \vec{r} \left( 2 \right) \right|$. Hva forteller svaret?

$$
\begin{align}
  \vec{r} \left( 2 \right) &= \left[ 2^{3} - 2, 3 \cdot 2^{2} + 1 \right] & \\
  &= \left[ 6, 13 \right] & \\
  \left| \vec{r} \left( 2 \right) \right| &= \sqrt{6^{2} + 13^{2}} & \\
  &\approx 14.3 &
\end{align}
$$

Dette svaret forteller at etter 2 timer hadde reven beveget seg omtrent $14.3$ kilometer fra origo.

### d)

> Hvor langt fra startpunktet endte reven opp?

### e)

> Revesporet går to ganger gjennom det samme punktet.
> Bestem koordinatene til dette punktet og ved hvilke tidspunkter reven var der.
