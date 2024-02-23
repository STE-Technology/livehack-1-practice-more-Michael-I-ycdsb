# ICS3U LiveHack 1 - Practice More

## Problem 1: Boiling Water

At sea level, atmospheric pressure is 100 kPa and water begins to boil at 100°C. As you go above sea level, atmospheric pressure decreases, and water boils at lower temperatures. As you go below sea level, atmospheric pressure increases, and water boils at higher temperatures. 

A formula relating atmospheric pressure to the temperature at which water begins to
boil is:

$P = 5 \times B - 400$

where $P$ is atmospheric pressure measured in kPa, and $B$ is the temperature at which water
begins to boil measured in °C.

Given the temperature at which water begins to boil, determine atmospheric pressure. 

Write your program in the file `problem1.py`.

*Note that the science of this problem is generally correct but the values of 100°C and 100 kPa are approximate and the formula is a simplification of the exact relationship between water’s boiling point and atmospheric pressure.*

### Input Specification
The input is one line containing an integer $B$ where $B ≥ 80$ and $B ≤ 200$. This represents the temperature in °C at which water begins to boil.

### Output Specification
The output is one line containing an integer which is atmospheric pressure measured in kPa. 

#### Sample Input 1
```
99
```

#### Output for Sample Input 1
```
95
```

#### Explanation of Output for Sample Input 1
When $B = 99$, we can substitute into the formula and get $P = 5 \times 99 − 400$ which equals $95$.

#### Sample Input 2
```
102
```

#### Output for Sample Input 2
```
110
```

#### Explanation of Output for Sample Input 2
When $B = 102$, we can substitute into the formula and get $P = 5 \times 102 − 400$ which equals $110$.

<br><br>

## Problem 2: Next in Line
You know a family with three children. Their ages form an arithmetic sequence: the difference in ages between the middle child and youngest child is the same as the difference in ages between the oldest child and the middle child. For example, their ages could be 5, 10 and 15, since both adjacent pairs have a difference of 5 years.

Given the ages of the youngest and middle children, what is the age of the oldest child?

Write your solution in the file `problem2.py`.

### Input Specification
The input consists of two integers, each on a separate line. The first line is the age $Y$ of the youngest child ($0 ≤ Y ≤ 50$). The second line is the age $M$ of the middle child ($Y ≤ M ≤ 50$).

### Output Specification
The output will be the age of the oldest child.

#### Sample Input 1
```
12
15
```

#### Output for Sample Input 1
```
18
```

#### Sample Input 2
```
10
10
```

#### Output for Sample Input 2
```
10
```