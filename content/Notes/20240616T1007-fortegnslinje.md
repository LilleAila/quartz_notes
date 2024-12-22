---
id: 20240616T1007-fortegnslinje
aliases:
  - fortegnslinje
tags: []
date: "2024-06-16"
title: Fortegnslinje
---

#matte [[20240616T1007-ulikhet|ulikhet]] [[20240616T1007-faktorisering|faktorisering]]

# Fortegnslinje

Fortegnslinjer er en måte å løse [[20240616T1007-ulikhet|ulikheter]]. Da skriver man opp alle faktorene i uttrykket på en linje, og ser hvor produktet deres blir et partall og et oddetall. I [[20240616T1007-intervall|intervallene]] der produktet er et oddetall, vil verdien være negativ, og andre steder positiv.

## Eksempel

Løs ulikheten:

$$
\begin{align}
\frac{x-4}{x^{2}-9} &\leq 0 \\
\text{Faktoriser:} \\
\frac{x-4}{(x+3)(x-3)} &\leq 0
\end{align}
$$

Nå har jeg et uttrykk der $0$ står alene på en side, og kan tegne opp en fortegnslinje:

```tikz
\usepackage{amsmath, amssymb}
\begin{document}
\begin{tikzpicture}[scale=1]

\node[anchor=south] at (-3, 0.5) { $ -3 $ };
\node[anchor=south] at (3, 0.5) { $ 3 $ };
\node[anchor=south] at (4, 0.5) { $ 4 $ };

\draw[gray] (-3, 0.5) -- (-3, -3);
\draw[gray] (3, 0.5) -- (3, -3);
\draw[gray] (4, 0.5) -- (4, -3);

\node[draw, anchor=east] at (-5.3,0) {$ x-4 $};
\draw[gray, thick, dotted] (-5, 0) -- (4, 0);
\draw[gray, thick] (4, 0) -- (5, 0);
\draw (4, 0) circle[radius=0.2];

\node[draw, anchor=east] at (-5.3,-1) {$ x-3 $};
\draw[gray, thick, dotted] (-5, -1) -- (3, -1);
\draw[gray, thick] (3, -1) -- (5, -1);
\draw (3, -1) circle[radius=0.2];

\node[draw, anchor=east] at (-5.3,-2) {$ x+3 $};
\draw[gray, thick, dotted] (-5, -2) -- (-3, -2);
\draw[gray, thick] (-3, -2) -- (5, -2);
\draw (-3, -2) circle[radius=0.2];

\node[draw, anchor=east] at (-5.3,-3) {$ \dfrac{x-4}{\left(x-3\right)\left(x+3\right)} $};
\draw[gray, thick, dotted] (-5, -3) -- (-3, -3);
\draw[gray, thick] (-3, -3) -- (3, -3);
\draw[gray, thick, dotted] (3, -3) -- (4, -3);
\draw[gray, thick] (4, -3) -- (5, -3);
\draw (-3, -3) circle[radius=0.2];
\draw (3, -3) circle[radius=0.2];
\draw (4, -3) circle[radius=0.2];

\end{tikzpicture}
\end{document}
```

Nederst har jeg tegnet fortegnslinjen for produktet av de tre andre funksjonene. Sirklene markerer nullpunktene til [[20240616T1007-funksjon|funksjonene]], og prikket linje symboliserer negativ funksjonsverdi. Ut fra om produktet til de tre øverste linjene er negativt eller positivt, finner jeg fortegnslinjen til hele uttrykket. Dette betyr at løsningen på ulikheten er:

$$
\frac{x-4}{(x-3)(x+3)} \leq 0 \implies \underline{\underline{x \in \langle\leftarrow, -3\rangle \cup \langle 3, 4]}}
$$

Grunnen til at $x=-3$ og $x=3$ ikke er inkludert i svaret, er fordi på disse punktene vil nevneren være lik $0$, som betyr at det ikke finnes noen funksjonsverdi på det punktet.
