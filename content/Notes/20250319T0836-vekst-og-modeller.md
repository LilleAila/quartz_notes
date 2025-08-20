---
id: 20250319T0836-vekst-og-modeller
aliases:
  - Vekst og modeller
tags: []
date: "2025-03-19"
title: Vekst og modeller
---

#matte [[20240616T1007-matte-r1|Matte]]

# Vekst og modeller

Målet med å lage en matematisk modell er ofte å finne en funksjon som beskrive hvordan noe utvikler seg over tid. Man bruker ofte variabelen $t$.

Ved regresjon er $R$ et mål på hvor godt modellen passer til dataen.

## Jevn vekst

Beskrevet med en lineær funksjon $f \left( t \right) = at + b$.

## Eksponentiell vekst

Beskrevet med en eksponentialfunksjon gitt ved $f \left( t \right) = a \cdot b ^{t}$, der $a$ og $b$ er positive tall.
Parameteren $a$ er startverdien, det vil si verdien når $t=0$.
Parameteren $b$ er vekstfaktoren.

Vekstfarten er

$$
\begin{align}
  f' \left( t \right) &= a \cdot \left( b^{t} \right)' & \\
  &= a \cdot b^{t} \cdot \ln{b} & \\
  &= f \left( t \right) \cdot \ln{b} &
\end{align}
$$

Vekstfarten er til enhver tid proporsjonal med funksjonsverdien. Fortegnet til vekstfarten er bestemt av faktoren $\ln{b}$.

Hvis $b>1$ er $\ln{b} > 0$. $f' \left( t \right)$ er positiv for alle verdier av $t$. $f \left( t \right)$ vil øke ettersom $t$ øker, raskere og raskere med tiden.
Hvis $0<b<1$, er $\ln{b}<0$. Da er $f' \left( t \right)$ negativ for alle verdier av t, altså vil $f \left( t \right)$ minke over tid, saktere og saktere.

Ofte vanlig i naturvitenskap å bruke eulertallet ($e=2.71828182845904536028474$) som grunntall:

$$
f \left( t \right) = a \cdot e^{kt}
$$

Vekst uten ressursbegrensninger vil ofte gi eksponentiell vekst. Dyrker bakteriekultur, introduserer dyreart i område uten naturlige fiender, etc.

## Logistisk vekst

Vokser fortere til vendepunkt, vokser saktere.

![20250319T0943-logistisk-vekst-eksempel.png](Assets/20250319T0943-logistisk-vekst-eksempel.png)

Beskrevet med en funksjon gitt ved

$$
f \left( t \right) = \frac{C}{1 + a \cdot e^{-bt}}
$$

Veksten er tilnærmet eksponentiell i starten, konstant rundt vendepunktet og nærmer seg en konstant verdi (asymptote).

## Oppgaver

### 7.26

I et forsøk måler Eivind radioaktiviteten fra en bariumisotop hvert minutt. Han fører resultatene inn i en tabell og føyer til en rad i tabellen for forholdstallet mellom to påfølgende målinger.

#### a

Skriv av og fyll ut resten av tabellen. Begrunn at aktiviteten følger en eksponentiell modell.

| t (min)      | 0   | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| ------------ | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A (Bq)       | 200 | 147  | 112  | 80   | 55   | 42   | 32   | 25   |
| Forholdstall | -   | 0.74 | 0.76 | 0.71 | 0.69 | 0.76 | 0.76 | 0.78 |

Forholdstallet mellom de ulike verdiene er omtrent det samme. Dette betyr at for hver $t$ synker verdien med en konstant faktor, altså synker den mer for høyere verdier og mindre for lavere verdier. Derfor følger denne aktiviteten en eksponentiell modell.

#### b

Finn ved regresjon en modell for utviklingen i aktiviteten på formen

1. $A \left( t \right) = A_{0} \cdot b^{t}$
2. $A \left( t \right) = A_{0} \cdot e^{kt}$

![20250319T0959-modell 1.png](Assets/20250319T0959-modell-1.png)

![20250319T0959-modell 2.png](Assets/20250319T0959-modell-2.png)

Begge gir tilnærmet den samme funksjonen. Kunne sikkert regnet ut og bevist at det er _nøyaktig_ den samme funksjonen.

1. $a \approx 200.59945655 \land b \approx 0.7352796$
1. $a \approx 200.59945655 \land k \approx -0.30750443$

### Eksempel 12 s. 322

Tabellen viser samlet antall som var smittet av koronavirus i Norge for utvalgte datoer våren 2020.

| Dato   | 21.02 | 29.02 | 12.03 | 20.03 | 31.03 | 15.04 | 30.04 | 15.05 | 31.05 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Antall | 1     | 21    | 1118  | 2580  | 5107  | 6890  | 7787  | 8823  | 8433  |
| t      | 0     | 8     | 20    | 28    | 39    | 54    | 69    | 84    | 100   |

Lag en logistisk modell som beskriver utviklingen i antall meldte tilfeller $t$ dager etter at det første tilfellet ble registrert 21.02.

Brukte python, se ipynb-fil.

$$
a \approx 4.61564119e+01 \land b \approx 1.05781899e-01 \land C \approx 8.39383985e+03
$$

Måtte sette startverdi for $C$, ellers klarer den ikke å regne ut:

```py
coeffs, _ = curve_fit(model, x, y, p0=[0, 0, 8433])
```

![20250319T1021-logistisk-modell-matplotlib.png](Assets/20250319T1021-logistisk-modell-matplotlib.png)

#### Finne startverdier til `curve_fit`

Verdien til $c$ skal være lik den høyeste av $y$-verdiene

$$
C_{\text{start}} = \text{max} \left\{ y_1, y_2, \dots, y_N \right\}
$$

I dette tilfellet blir startverdien for $C$ lik $8433$.
