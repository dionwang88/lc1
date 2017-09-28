/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
*/


The distribution of the elements is period.

P   A   H   N
A P L S I I G
Y   I   R
For example, the following has 4 periods(cycles):

P   | A   | H   | N
A P | L S | I I | G
Y   | I   | R   |
The size of every period is defined as "cycle"

cycle = (2*nRows - 2), except nRows == 1.
In this example, (2*nRows - 2) = 4.

In every period, every row has 2 elements, except the first row and the last row.

Suppose the current row is i, the index of the first element is j:

j = i + cycle*k, k = 0, 1, 2, ...
The index of the second element is secondJ:

secondJ = (j - i) + cycle - i
(j-i) is the start of current period, (j-i) + cycle is the start of next period.
