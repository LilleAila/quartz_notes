---
id: 20240616T1007-innsettingsmetoden
aliases:
  - innsettingsmetoden
tags: []
date: "2024-06-16"
title: Innsettingsmetoden
---

#matte [[20240616T1007-likning|likning]] [[20240616T1007-likningssett|likningssett]]

# Innsettingsmetoden

Insettingsmetoden brukes for å løse [[20240616T1007-likningssett|likningssett]]. Den brukes ved å skrive om en av [[20240616T1007-likning|likningene]] slik at en av variablene skrives ved hjelp av de / den andre.

## Eksempel:

$$
\begin{align}
	&\begin{bmatrix}
		y - 3x &=& -4  \\[5pt]
		2y &=& -2x
	\end{bmatrix}&  \\[5pt]
	& y = -x &  \\[5pt]
	& -x -3x = -4 & \text{Setter inn i den første likningen}  \\[5pt]
	& -4x = -4 &  \\[5pt]
	& x = 1 &  \\[5pt]
	& 2y = -2 & \text{Setter verdien til $ x $ inn i likningen}  \\[5pt]
	& \underline{\underline{x = 1 \land y = -1}} &

\end{align}
$$

## Eksempel med høyere grad

$$
\begin{align}
&\begin{bmatrix}
	I: & 6x^{2}+y &=& 5  \\[5pt]
	II: & 2x + y &=& 2
\end{bmatrix}&
\end{align}
$$

Vi skriver om og benytter innsettingsmetoden:

$$
\begin{align}
&\begin{bmatrix}
	I: & x^{2}+y &=& 5  \\[5pt]
	II: & y &=& -2x+2
\end{bmatrix}&
\end{align}
$$

Setter vi $II$ inn i $I$, får vi:

$$
\begin{align}
& x^{2}+ \left(-2x+2\right) = 5 &
\end{align}
$$

som kan skrives om til

$$
\begin{align}
& x^{2}-2x-3=0 &
\end{align}
$$

Det er en [[20240616T1007-andregradslikning|andregradslikning]] som gir svarene $x=3\lor x=-1$. $y$-verdiene kan vi finne ved $II$. Da blir svaret:

$$
\begin{align}
& \underline{\underline{x = 3 \land y = -4 \lor x = -1 \land y = 4}} &
\end{align}
$$
