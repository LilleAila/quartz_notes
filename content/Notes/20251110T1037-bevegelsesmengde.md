---
id: 20251110T1037-bevegelsesmengde
aliases:
  - bevegelsesmengde
tags: []
date: "2025-11-10"
title: bevegelsesmengde
---

#fysikk [[20250820T0820-fysikk-1|fysikk 1]] [[20250827T0824-bevegelse|bevegelse]] [[20250910T0834-krefter|krefter]]

# bevegelsesmengde

Bevegelsesmengden er en størrelse definert som

$$
\vec{p} = m \vec{v} \,\left[ \mathrm{kg \frac{m}{s}} \right]
$$

Bevegelsesmengde er alltid bevart, uavhengig av alle eksterne faktorer som blant annet friksjon, i motsetning til for eksempel mekanisk energi.

Newtons andre lov var opprinnelig formulert ved hjelp av bevegelsesmengde:

$$
\sum F = \frac{\Delta p}{\Delta t} = \frac{mv - mv_{0}}{t} = m \cdot \frac{v - v_{0}}{t} = m \cdot a
$$

Man kan også bruke dette som følger. Det kalles også "impuls" ($I$):

$$
\sum F \cdot \Delta t = \Delta p = I
$$

Man kan også si at

$$
\sum F = p' \left( t \right)
$$

## Støt

Et støt er elastisk hvis den totale kinetiske energien til systemet er bevart. Om den kinetiske energien bilr omgjort til andre energiformer i støtet, er det uelastisk.

# Oppgaver

## 5.05 (s. 151)

Kristoffer kaster en basketball fra høyden $1.8 \,\mathrm{m}$j over gulvet slik at den får farten $9.8 \,\mathrm{\frac{m}{s}}$ rett oppover. Ballen har massen $0.63 \,\mathrm{kg}$.

**a**

> Hva er bevegelsesmengden til balen idet den kastes?

$$
\begin{align}
  p &= m v & \\
  &= 0.63 \cdot 9.8 & \\
  &= 6.173 = 6.2 &
\end{align}
$$

**b**

> Hvor lang tid tar det før bevegelsesmengden til ballen er halvert?

$$
\begin{align}
  v &= a \cdot t + v_{0} & \\
  4.9 &= -9.81 t + 9.8 & \\
  t &= 0.49 &
\end{align}
$$

**c**

> Hva er bevegelsesmengden til ballen rett før den treffer bakken?

$$
\begin{align}
  2 \cdot -9.81 \cdot -1.8 &= v^{2} - 9.8^{2} & \\
  v &= \pm 11.461 & \\
  p &= m \cdot v = -7.2 &
\end{align}
$$

Setter negativ da jeg vet at den går nedover og satte positiv retning opp.

**d**

> Hvor stor er den totale endringen i bevegelsesmengden til ballen?

$$
\Delta p = 6.2 - \left( -7.2 \right) = 13.4 \,\mathrm{kg \frac{m}{s}}
$$

## 5.06

**a**

> Hvor stor er bevegelsesmengden før og etter kollisjonen?

$$
\begin{align}
  p_{0} &= 0.8 \cdot 0.35 = 0.28 & \\
  p_{1} &= -0.4 \cdot 0.35 = -0.14 &
\end{align}
$$

**b**

> Hvor stor var endringen i bevegelsesmengde i kollisjonen?

$$
\Delta p = -0.14 - 0.28 = -0.42
$$

## 5.07

**a**

> Utled Newtons 2. lov uttrykt ved bevegelsesmengde.

$$
\begin{align}
  \sum F &= \lim_{\Delta t \to 0} \frac{\Delta p}{\Delta t} & \\
  &= p' \left( t \right) & \\
  &= \left( m \left( t \right) \cdot v \left( t \right) \right) & \\
  &= m' \left( t \right) \cdot v \left( t \right) + m \left( t \right) \cdot v' \left( t \right) & \\
  & \text{Antar konstant masse:} & \\
  \sum F &= m \cdot a \left( t \right) &
\end{align}
$$

**b**

$$
\begin{align}
  \left[ \mathrm{N} \right] &= \left[ \mathrm{\frac{kg \frac{m}{s}}{s}} \right] & \\
  \left[ \mathrm{Ns} \right] &= \left[ \mathrm{kg \frac{m}{s}} \right] &
\end{align}
$$

**c**

> Uttrykk Newtons 1. lov med bevegelsesmengde

$$
\begin{align}
  v' \left( t \right) &= 0 & \\
  \sum F &= p' \left( t \right) & \\
  &= m \cdot 0 & \\
  &= 0 & \\
  v' \left( t \right) = 0 &\implies \sum F = 0 &
\end{align}
$$

## 5.08

Et legeme har massen $0.75 \,\mathrm{kg}$ og beveger seg med bevegelsesmengden $10 \,\mathrm{kg \frac{m}{s}}$ når det blir påvirket av kraftsummen $\sum F = 5.0 \,\mathrm{N}$ i bevegelsesretningen. Kraftsummen opphører etter $4.0 \,\mathrm{s}$.

**a**

> Hvor mye endres bevegelsesmengden totalt?

$$
\begin{align}
  \sum F &= \frac{\Delta p}{\Delta t} & \\
  5 \,\mathrm{N} &= \frac{\Delta p}{4 \,\mathrm{s}} & \\
  \Delta p &= 20 \,\mathrm{kg \frac{m}{s}} &
\end{align}
$$

**b**

> Hvor stor ble farten?

$$
\begin{align}
  p &= p_{0} + \Delta p & \\
  p &= 10 + 20 = 30 \,\mathrm{kg \frac{m}{s}} & \\
  p &= m v & \\
  v &= \frac{p}{m} & \\
  v &= \frac{30}{0.75} = 40 \,\mathrm{\frac{m}{s}} &
\end{align}
$$

**c**

> Hvor langt forflyttet legemet seg på de fire sekundene?

$$
\begin{align}
  s &= \frac{1}{2} \left( v + v_{0} \right)t & \\
  s &= \frac{1}{2} \left( 40 + \frac{10}{0.75} \right) \cdot 4 & \\
  s &= 106.6667 & \\
  &\approx 0.11 \cdot 10^{3} \,\mathrm{m} = 0.11 \,\mathrm{km} &
\end{align}
$$

## 5.10

En bil med massen $m$ beveger seg rettiljet med farten $v_{0}$. I løpet av tiden $t$ blir bilden påvirket av en kraftsum $\sum F$ i fartsretningen, og farten øker.

**a**

> Sett opp et uttrykk for farten etter kraft-påvirkningen.

$$
\begin{align}
  \sum F &= \frac{\Delta p}{\Delta t} & \\
  \sum F &= \frac{m v - m v_{0}}{\Delta t} & \\
  \sum F \Delta t &= mv - mv_{0} & \\
  v &= \frac{\sum F}{m} \Delta t + v_{0} & \\
  v &= at+v_{0} &
\end{align}
$$

**b**

> Bilen har massen $2750 \,\mathrm{kg}$ og kjører med farten $60 \,\mathrm{\frac{km}{h}}$. I $3.2\,\mathrm{s}$ virker en gjennomsnittlig kraft på $4.77 \,\mathrm{kN}$ i fartsretningen på bilen.
>
> Hvor stor er farten etter $3.2 \,\mathrm{s}$

$$
\begin{align}
  v &= \frac{4770}{2750} \cdot 3.2 + \frac{60}{3.6} & \\
  &\approx 22.22 \,\mathrm{\frac{m}{s}} &
\end{align}
$$

**c**

> Hvor stor måtte kraften ha vært dersom den samme fartsendringen skulle skje på halvparten av tiden?

$$
\begin{align}
  22.2 &= \frac{F}{2750} \cdot 1.6 + \frac{60}{3.6} & \\
  F &\approx 9.51\,\mathrm{kN} &
\end{align}
$$

**d**

> Bilen kjører med farten $80 \,\mathrm{\frac{km}{h}}$. Hvor stor må bremsekraften på bilen være for at bilen skal klare å bremse helt ned på $4.0\,\mathrm{s}$?

$$
\begin{align}
  0 &= \frac{R}{2750} \cdot 4 + \frac{80}{3.6} & \\
  R &= -15277.8 \,\mathrm{N} = -15.3 \,\mathrm{kN} &
\end{align}
$$

**e**

> Hvor stor ville bremsekraften i oppgave d være hvis massen til bilen var $3000 \,\mathrm{kg}$?

$$
\begin{align}
  0 &= \frac{R}{3000} \cdot 4 + \frac{80}{3.6} & \\
  R &= -16666.7 \,\mathrm{N} = -16.7 \,\mathrm{kN} &
\end{align}
$$

## 5.11

En tennissball med massen $58\,\mathrm{g}$ har farten $20 \,\mathrm{\frac{m}{s}}$ idet den blir truffet av en rekkert. Kontakten mellom ballen og rekkerten varer i $0.020 \,\mathrm{s}$. Idet ballen mister kontakten med rekkerten, har den $30\,\mathrm{\frac{m}{s}}$ i motsatt retning.

**a**

> Hvor stor er den gjennomsnittlige kraften fra rekkerten på ballen?

$$
\begin{align}
  \bar{F} &= \frac{\Delta p}{\Delta t} & \\
  \bar{F} &= \frac{0.058 \cdot 30 + 0.058 \cdot 20}{0.02} & \\
  \bar{F} &= 145 \,\mathrm{N} & \\
  \bar{F} &\approx 0.15 \,\mathrm{kN} &
\end{align}
$$

**b**

> Regn ut forholdet mellom den gjennomsnittlige kraften fra rekkerten og gravitasjonskraften på ballen. Kommenter svaret.

$$
\begin{align}
  G &= 9.81 \cdot 0.058 = 0.56898 \,\mathrm{N} & \\
  \frac{F}{G} &= \frac{145}{0.56898} = 255 &
\end{align}
$$

Ser at kraftsummen fra rekkerten er $255$ ganger større enn gravitasjonskreften. Dermed kan vi se bort fra gravitasjonskraften, da den er negligerbar.

## 5.13

En bil med massen $1.5$ tonn kjører med konstnat fart på $40 \,\mathrm{\frac{km}{h}}$

**a**

> Hvor stor er bevegelsesmengden til bilen?

$$
p = m v = 1500 \cdot \frac{40}{3.6} = 16666 = 1.7 \cdot 10^{4} \,\mathrm{kg \frac{m}{s}}
$$

**b**

> Etter $1.0 \,\mathrm{s}$ tråkker sjåføren på fgassen slik at bilen akselererer. Motoren yter da en gjennomsnittlig framdriftskraft på $45 \,\mathrm{kN}$ i $3.0 \,\mathrm{s}$ før sjåføren slipper opp gassen. Bilen kjører så videre med konstant fart. Vi ser bort fra andre horisontale krefter på bilen.
>
> Hvor stor bilr bevegelsesmengden til bilen?

$$
\begin{align}
  F &= \frac{\Delta p}{\Delta t} & \\
  45000 &= \frac{1500 v - 1500 \cdot 11.11}{3} & \\
  v &= 101.11 \,\mathrm{\frac{m}{s}} & \\
  p &= 101.11 \cdot 1500 = 151665 = 15 \cdot 10^{4} \,\mathrm{kg \frac{m}{s}} &
\end{align}
$$

**c**

Hvor stort arbeid utførte frandriftskraften?

$$
\begin{align}
  W &= F \cdot s & \\
  s &= \frac{1}{2} \left( v + v_{0} \right)t & \\
  s &= \frac{1}{2} \left( 101.11 + 40 \right) \cdot 1 = 70.555\,\mathrm{m} & \\
  W &= 45000 \cdot 70.555 = 3174975 = 3.2 \cdot 10^{6} \,\mathrm{J} &
\end{align}
$$
