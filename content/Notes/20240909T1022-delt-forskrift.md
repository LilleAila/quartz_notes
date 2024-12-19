---
id: 20240909T1022-delt-forskrift
aliases:
  - delt forskrift
tags: []
---

#matte [[20240616T1007-matte|matte]] [[20240616T1007-funksjon|funksjon]]

# Funksjoner med delt forskrift

Eksempel: billetter koster

- 60 kr for barn
- 100 kr for voksne

$$
p(x) = \begin{cases}
60 & 0 \leq x < 18 \\
100 & 18 \leq x < 100
\end{cases}
$$

$f \left( x \right) = \begin{cases} x & , & x < 0 \\ x + 1 & , & x \geq 0 \end{cases}$

Man kan også skrive det som

$$
p(x) = \begin{cases}
60 & \text{for } x \in \left[ 0, 18 \right\rangle \\
100 & \text{for } x \in \left[ 18, 100 \right\rangle
\end{cases}
$$

$$
p(x) = \begin{cases}
60 & \text{, } 0 \leq x < 18 \\
100 & \text{, } 0 \leq x < 100
\end{cases}
$$

$$
p(x) = \begin{cases}
60 & \text{når } 0 \leq x < 18 \\
100 & \text{når } 18 \leq x < 100
\end{cases}
$$

etc.

## GeoGebra

```
p(x) = Dersom(Vilkår, Så)
p(x) = Dersom(Vilkår, Så, Ellers)

p(x) = Dersom(0 <= x < 18, 60, 100)
```

På engelsk GeoGebra vil dette bli

```
p(x) = If(0 <= x < 18, 60, 100)
```

![20240909T1024-geogebra-dersom.png](Assets/20240909T1024-geogebra-dersom.png)

## Annet eksempel

$$
f(x) = \begin{cases}
\frac{1}{4}x^{2}-4 & x < 4 \\
\frac{1}{2}x-2 & x \geq 4
\end{cases}
$$

GeoGebra bruker "ellers", i stedet for $x\geq4$

![20240909T1033-geogebra-delt-forskrift.png](Assets/20240909T1033-geogebra-delt-forskrift.png)
