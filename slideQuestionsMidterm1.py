 


 1 - a. Local beam search with k = 1

	//Hill climbing search


2 - b. Local beam search with one initial state and no limit on the number of states retained

	// Local beam search with k = ∞: strictly speaking, this doesn’t make sense. The idea is that if
	// every successor is retained (because k is unbounded), then the search resembles breadth-first
    // search in that it adds one complete layer of nodes before adding the next layer. Starting from one
    // state, the algorithm would be essentially identical to breadth-first search except that each layer is
    // generated all at once.


3 - c. Simulated annealing with T = 0 at all times (and omitting the termination test)
	
	c. Simulated annealing with T = 0 at all times: ignoring the fact that the termination step
	   would be triggered immediately, the search would be identical to first-choice hill climbing
       because every downward successor would be rejected with probability 1.



4 - d. Genetic algorithm with population size N = 1
	e. Genetic algorithm with population size N = 1: if the population size is 1, then the two selected
parents will be the same individual; crossover yields an exact copy of the individual; then there is
a small chance of mutation. Thus, the algorithm executes a random walk in the space of
individuals.




Question 1
■ Define the following items:
■ State, state space, search tree

1. State - #Representation of an agent where the agent is part of a particular instance. It explains what to 
#do in a particular situation.

2. State space -  #A working environment of an agent. Contains all necessary information of all possible states 
#that can be reached from inital state.

3. Search Tree -  #A tree in which the children are originated from the initial state. A tree which contains a 
#root node (initial state) and each child node is the states reachable by taking the actions.

■ Does a finite state space always lead to a
finite search tree?
#A finite state space does not always lead to a finite search tree because we can go through any circular path infinitely

■ How about a finite state space that is a tree
or a finite directed acyclic graph? 
# There are no cycles in a tree so there will be a finite search tree.
#  Finite direct acylic graph also has no loops. (and directed simply means the actions that map from
#one state to another are not symmetric, so you cannot jump between two adjacent states
#infinitely).

Question 2
■ Give a complete problem formulation for
each of the following.
■ You have to color a planar map using only four
colors, in such a way that no two adjacent
regions have the same color.

1. Initial State - no regions colored
2. Transition Model - The previously uncolored region has the assigned color. 
3. Goal tests - All regions colored, and no two adjacent regions have the same color.  
4. actions - Assign a color to an uncolored region.
5. Path Cost - Number of assignments. 


■ A 3-foot-tall monkey is in a room where some
bananas are suspended from the 8-foot ceiling.
He would like to get the bananas. The room
contains two stackable, movable, climbable
3-foot-high crates. CS 42

1. Initial State  - The room is the way it is (described in text)
2. Transition Model - The monkey 
3. Goal tests - The monkey gets the bananas
4. actions - Move crates, hop on crates, stack crates, walk, grab bananas 
5. Path Cost - Number of actions 


Consider a state space where the start state
is number 1 and the successor function for
state n returns two states, numbers 2n and
2n+1 

Draw the portion of the state space from 1 to 15
■ Suppose the goal state is 11. List the order in
which nodes will be visited for BFS, DLS with limit
3, and IDS.
(b) BFS: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11.
DFS: 1 → 2 → 4 → 8 → 9 → 5 → 10 → 11.
IDS: 1; 1 → 2 → 3; 1 → 2 → 4 → 5 → 3 → 6 → 7; 1 → 2 → 4 → 8 →
9 → 5 → 10 → 11.

■ How well would bidirectional search work on this
problem?

#Yes. In this problem, the predecessor of each state x is x/2 
#which is easily computable. Assume that we use breadth-first search in both
#forward and backward direction, the search steps may be as Table 1.
visited node fringe
forward 1 ForwardFringe={2,3}
backward 11 BackwardFringe={5}
forward 2 ForwardFringe={3,4,5}
backward 5 BackwardFringe={2}
Table 1: The search steps
#Note that the algorithm stops when the search in backward direction
#visited node 5, because node 5 is in the fringe of forward direction.


def Show that uniform-cost search and BFS with
constant step costs are optimal when used
with the Graph-Search algorithm.

#Its identical if step costs are equal. 
#Since the costs of each step are constant, when an unvisited node is visited
#by breadth-first search (uniform-cost search), the cost will be the lowest
#one. Moreover, since we use GRAPH-SEARCH algorithm, no node will
#be visited more than once. Thus if the goal node is visited, we will get
#the optimal solution

def Show a state space with varying step costs
in which Graph-Search using iterative
deepening finds a suboptimal solution.

#
#
#


def Describe a state space in which iterative
deepening search performs much worse than
depth-first search (for example, O(n2
) vs. O(n)).
#Consider a domain in which every state has a single successor, and there is a single goal at depth n. Then
#depth-first search will find the goal in n steps, whereas iterative deepening search will take 1 + 2 + 3 + … + n =
#O(n2) steps.


def Can there be more than one agent program that implements a given agent function?
#Yes. Assume we are given an agent function whose actions only depend on the previous p percepts.
#One program can remember the previous p percepts to implement the agent function, 
#while another could remember greater than p percepts and still implement
#the same agent function.


def Given a fixed machine architecture, does each agent program implement exactly one agent function?
#Yes. Given a percept sequence, an agent program will select an action. To implement multiple agent 
#functions this would require the agent program to select different actions 
#(or different distributions of actions) given the
#same percept sequence

def A simple agent that cleans a square if it is dirty and moves to the other square if not Is it rational?
#Assumption:
#performance measure: 1 point for each clean square at each time step
#environment is known a priori
#actions = {left, right, suck, no-op}
#agent is able to perceive the location and dirt in that location
#Given different assumption, it might not be rational anymore

def Given the assumption on slide 2. Describe a rational agent function for the modified performance measure 
def that deducts one point for each movement. Does the agent program require internal state?
#It is better to do NoOp once the world is clean.  it would seem that the agent must have some memory to say whether the other
#square has already been cleaned. 
#As a general strategy, an agent can use the environment itself as a form of external memory – a common
#technique for humans who use things like appointment calendars. 


def Discuss possible agent designs for the cases in which clean squares can become dirty and
def the geography of the environment is unknown.
#If we consider asymptotically long lifetimes, then it is clear that learning a map (in some form) provides an
#advantage because it means that the agent can avoid bumping into walls. It can also learn where dirt is
#most likely to accumulate and can devise an optimal inspection strategy. 


Task environment	Observable 		Deterministic 		Episodic		Static 		Discrete 		Agents 
-----------------------------------------------------------------------------------------------------------

Crossword Puzzle	fully   		deterministic 		sequential 		static 		discrete 		singles
Chess with a clock	fully 			strategic 			sequential 		semi 		discrete 		multi
Taxi Driver			partially 		stochastic 			sequential      dynamic 	conti. 			multi
Mushroom Picking	partially 		stochastic 			episodic 		dynamic 	conti. 			single


The environment type largely determines the agent design
■ The real world is (of course) partially observable, stochastic,
sequential, dynamic, continuous, multi-agent


Develop PEAS description for the following
task environment:
■ Robot soccer player

1. Performance Measure - goals scored. +1 for each goal
2. Environment - soccer field, other players, terrain, ball
3. Actuators - Moving, stopping, kicking, running
4. Sensors - Camera, engine, accelerator, communication, touch sensors  


■ Shopping for used AI books on the Internet
1. Performance Measure - Book bought. Minimizing cost 
2. Environment - Internet, browsers 
3. Actuators - Creditcard (currency), add new order, retrieve existing order information 
4. Sensors - User interface, web pages 

///////////////////////

T/F 

def An agent that senses only partial information about the state cannot be perfectly rational.

False. The vacuum-cleaning agent from Section 2.2.1 is 
rational but doesn’t observe the state of the square that is adjacent to it

def Suppose an agent selects its action uniformly at  random from the set of possible actions. 
def There exists a deterministic task environment in which this agentis rational.

True. Again consider the ”all actions always give equal reward” case

def It is possible for a given agent to be perfectly rational in two distinct task environments.
True. Consider two environments based on betting on the outcomes of
a roll of two dice. In one environment, the dice are fair, in the other, the dice are
biased to always give 3 and 4. The agent can bet on what the sum of the dice will
be, with equal reward on all possible outcomes for guessing correctly. The agent
that always bets on 7 will be rational in both cases.


def A perfectly rational poker-playing agent never loses.

False. Put two perfectly playing agents against each other. 
Someone (the one with poorer luck) must lose.








