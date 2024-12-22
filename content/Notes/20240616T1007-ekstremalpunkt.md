---
id: 20240616T1007-ekstremalpunkt
aliases:
  - ekstremalpunkt
tags: []
date: "2024-06-16"
title: Ekstremalpunkt
---

#matte [[20240616T1007-matte|matte]] [[20240616T1007-funksjon|funksjoner]]

# Ekstremalpunkt

Topp -eller bunnpunktet til en funksjon. [[20241121T1132-monotoniegenskaper|monotoniegenskaper]]

Ekstremalpunkter og [[20240616T1007-terrassepunkt|terrassepunkter]] er stasjonære punkter.

$A$ -> bunnpunkt
$a$ -> minimalpunkt (x-verdien)
$f \left( a \right)$ -> minimalverdi (y-verdien)

$B$ -> toppunkt
$b$ -> maksimalpunkt (x-verdien)
$f \left( b \right)$ -> maksimalverdi (y-verdien)

Både minimalpunkt og maksimalpunkt -> ekstremalpunkt (ifølge boken)
Både bunnpunkt og toppunkt -> også ekstremalpunkt. (dette er det vi bruker til vanlig)
Både minimalverdi og maksimalverdi -> ekstremalverdier

## Eksempel

I denne funksjonen, kan jeg se at den har et bunnpunkt, og dette punktet er på $x=0$.

```functionplot
---
title: f(x)=x^2
xLabel: x
yLabel: y
bounds: [-4,4,-1,10]
disableZoom: false
grid: true
---
f(x)=x^2
```

For [[20240616T1007-funksjon|funksjoner]] som "peker oppover", vil det være et bunnpunkt, og funksjoner som "peker nedover", vil ha et toppunkt, for eksempel denne:

```functionplot
---
title: f(x)=-x^2
xLabel: x
yLabel: y
bounds: [-4,4,-10,1]
disableZoom: false
grid: true
---
f(x)=-x^2
```

Denne funksjonen har topppunktet $x=0$.

## Finne ekstremalpunkt

Ekstremalpunkt kan finnes ved hjelp av [[20240616T1007-derivasjon|derivasjon]]. Man løser likningen

$$
f'(x)=0
$$

Dette gir deg alle $x$-verdiene hvor funksjonsverdien ikke øker eller synker på akkurat dette punktet, altså ==stasjonære punkter==. Dette inkluderer både ekstremalpunkter, og [[20240616T1007-terrassepunkt|terrassepunkt]].
