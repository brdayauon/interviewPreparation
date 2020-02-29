2. (20 points total, 5 pts off for each wrong answer, but not negative) Label the following as T (=
True) or F (= False). Unless stated otherwise, assume a finite branching factor, step costs ≥ ε >
0, and at least one goal at a finite depth. You may be in either a tree or a graph.



a. (5 pts) An admissible heuristic NEVER OVER-ESTIMATES the remaining cost (or distance) to
the goal.
TRUE, by definition of admissible


b. (5 pts) Best-first search when the queue is sorted by f(n) = g(n) + h (n) is both complete and
optimal when the heuristic is admissible and the total cost estimate f(n) is monotonic increasing
on any path to a goal node.
TRUE, because the search described is A* and the heuristic described is both admissible and
consistent.


c. (5 pts) Most search effort is expended while examining the interior branch nodes of a search
tree.

FALSE. Most search effort is expended while examining leaf node of the tree.


d. (5 pts) Uniform-cost search (sort queue by g(n)) is both complete and optimal when the path
cost never decreases.

TRUE, because uniform-cost search is A* search with h(n) = 0, which is admissible.


e. (5 pts) Greedy best-first search (sort queue by h(n)) is both complete and optimal when the
heuristic is admissible and the path cost never decreases.

FALSE. Your book gives a counter-example (Fig. 3.23, 3rd ed.; Fig. 4.2, 2nd ed.)


f. (5 pts) Beam search uses O(bd) space and O(bd) time.

FALSE. For a beam search in a tree using k nodes total, the space used is O(bk) and the time is
O(bmk). For a beam search in a graph, the space is again O(bk) but it can waste time in loops.


g. (5 pts) Simulated annealing uses O(constant) space and can escape from local optima.

TRUE. The space is constant and it accepts bad moves with probability exp(-delta(Value)).


h. (5 pts) Genetic algorithms use O(constant) space and can escape from local optima.

TRUE. The space is constant and it can accept bad moves by creating bad offspring.


i. (5 pts) Gradient descent uses O(constant) space and can escape from local optima.

FALSE. The space is constant, but it generally moves toward, and gets stuck on, a local optima.















