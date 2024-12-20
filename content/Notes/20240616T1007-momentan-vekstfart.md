---
id: 20240616T1007-momentan-vekstfart
aliases:
  - momentan vekstfart
tags: []
title: Momentan vekstfart
date: 2024-06-16
---

#matte [[20240616T1007-derivasjon|derivasjon]] [[20240616T1007-tangent|tangent]]

# Momentan vekstfart

GeoGebra: `Momentan-Vekstfart`

Når man tegner sporet til $(x, y)$ der y er den momentane vekstfarten til $f \left( x \right)$ i $x$, der man endrer x, får man [[20240616T1007-derivasjon|den deriverte]] av $f \left( x \right)$. Denne funksjonen vil alltid ha en grad mindre enn $f \left( x \right)$.

![20241014T0900-momentan-vekstfart.png](Assets/20241014T0900-momentan-vekstfart.png)
Vi kan se fra den deriverte hvorfor den har en grad lavere, fordi $f' \left( x \right)$ er positiv når $f \left( x \right)$ øker, negativ når $f \left( x \right)$ synker, og null når $f \left( x \right)$ har et ekstremalpunkt. Fordi $f \left( x \right)$ har to ekstremalpunkt, vil $f' \left( x \right)$ ha to nullpunkter, altså er det en andregradsfunksjon.

Den momentane vekstfarten til funksjonen $f$ i $x=x_{1}$, er lik stigningstallet av [[20240616T1007-tangent|tangenten]] til $f$ i punktet $(x_{1}, f(x_{1}))$ og forteller hvor mye funksjonen endrer seg i akkurat dette punktet.

Fortegnet til den momentane vekstfarten kan fortelle oss noe om hvordan funksjonen ser ut. Hvis

- $f$ vokser mot høyre, er den momentane vekstfarten positiv
- $f$ avtar mot høyre, er den momentane vekstfarten negativ
- $f$ har et stasjonært punkt ([[20240616T1007-ekstremalpunkt|ekstremalpunkt]] eller [[20240616T1007-terrassepunkt|terrassepunkt]]), er den momentane vekstfarten lik null

## Eksempel 1

Vi har $\left( x, f \left( x \right) \right)$ og $a = f' \left( x \right)$. Finn likningen til tangenten.

Kan bruke ettpunktsformelen:

$$
y - y_1 = a (x - x_1)
$$

$$
y_1 = f \left( x \right)
$$

$$
x_1 = x
$$

$$
a = f' \left( x \right)
$$

## Eksempel 2

Punkt: $\left( 2, 3 \right)$
Stigningstall: $4$

$$
y - y_1 = a \left( x - x_1 \right)
$$

$$
y - 3 = 4 \left( x - 2 \right)
$$

$$
y - 3 = 4x - 8
$$

$$
\underline{\underline{y = 4x - 5}}
$$

## Eksempel 3

Funksjon $f \left( x \right)$. Vet at $f' \left( x \right) = 2e^{2x}$.

1. Finn likningen til tangenten som går gjennom $\left( \ln{3}, 9 \right)$.

Bruker $f' \left( x \right)$ til å finne stigningstallet $a$:

$$
a = f' \left( \ln{3} \right) = 2e^{2 \cdot \ln{3}} = 2e^{\ln{9}} = 18
$$

Kunne også brukt potensregler: $2e^{2 \cdot \ln{3}} = 2 \left( e^{\ln{3}} \right)^{2} = 2 \cdot 3^{2} = 18$

Finner likningen ved ettpunktfsormelen.

$$
y - f \left( a \right) = f' \left( a \right) \left( x - a \right)
$$

$$
y - 9 = 18 \left( x - \ln{3} \right)
$$

$$
y = 18x - 18\ln{3} + 9 = 9 \left( 2x - 2\ln{3} + 1 \right) = 9 \left( 2x - \ln{9} + 1 \right)
$$

## Eksempel 4

$$
f \left( x \right) = 2\ln{x}
$$

1. Finn tangent:

$$
\left( 1, f \left( 1 \right) \right)
$$

2. Bestem $a$ slik at tangenten i punkt $\left( a, f \left( a \right) \right)$ får stigningstall 3.

Løst i GeoGebra:

![20241014T1028-geogebra-tangent-oppgave.png](Assets/20241014T1028-geogebra-tangent-oppgave.png)

## Eksempel 5

Funksjonen $g$ er gitt ved $g \left( x \right)$ = $3e^{\frac{3}{2}}$. Finn likningen til tangenten i punktet $\left( 0, f \left( 0 \right) \right)$

Bruker derivasjonsregel for uttrykk med $e^{x}$

$$
g' \left( x \right) = \frac{3}{2} e^{\frac{x}{2}}
$$

$$
y - g \left( 0 \right) = g' \left( 0 \right) \left( x - 0 \right)
$$

$$
y - 3 = \frac{3}{2}x
$$

$$
\underline{\underline{y = \frac{3}{2}x + 3}}
$$

Sjekket svaret med GeoGebra; fikk samme svar, men ganger med $\ln{e}$ av en eller annen grunn. Dette bør jeg nevne i vurderinger at den tuller seg, men jeg forstår svaret den gir meg.

![20241014T1102-geogebra-cas-derivasjon-oppg5.png](Assets/20241014T1102-geogebra-cas-derivasjon-oppg5.png)

La $k,n,a,b \in \mathbb{R}$

$$
f \left( x \right) = k \implies f' \left( x \right) = 0
$$

```functionplot
f(x)=5
```

$$
f \left( x \right) = ax + b \implies f' \left( x \right) = a
$$

```functionplot
f(x)=2x + 1
```

$$
f \left( x \right) = x^{n} \implies f' \left( x \right) = nx^{n-1}
$$

```functionplot
---
bounds: [-5,5,0,20]
---
f(x)=x^2
```
