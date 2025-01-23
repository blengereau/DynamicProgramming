# Dynamic Programming & Reinforcement Learning applied to a Neo-Classical Growth Model

This project solves an optimal growth model using Dynamic Programming techniques by approximating iteratively the value function. It also involves <b>evaluating arbitrary policies</b> on the agent control variable, and produce a Reinforcement Learning algorithm of <b>greedy procedure to update the policy function</b> of the agent.

Additionally, this project <b>calibrates a Neural Network that approximates the optimal path </b> of capital accumulation from an arbitrary amount of capital.

## 1. Model

Consider an agent who allocates her time between producing the consumption good C, and accumulating human capital H. The agent seeks to maximize her discounted utility, as captured by the following objective:

![Model](images/problem.png)

The production function reads in (i).
Normalizing the labor supply of the agent to one, the accumulation law for human capital is given by (ii), where 𝛿 is the depreciation rate of human capital, while 𝐿t is the share of the labor supply dedicated to the production of the consumption good.

We assume a CRRA Utility function: U(C) = C^(1-𝜎)/(1-𝜎).

## 2. Value function and optimal policy
The Bellman Equation of the agent is:

![Bellman Equation and Feasability set](images/bellman_equation.png)

We iteratively approximate the value function, reached by the following optimal policy function:

![Value Function](images/value_function.png)

![Policy function](images/policy_function.png)

## 3. Evaluation of arbitrary policies


## 4. calibration of a Neural Network to estimate the optimal path
We aim to calibrate a neural network that approximates the path starting from an arbitrary initial stock of human capital and converging toward the steady state.
To calibrate the neural network, we minimize the distance between the simulated and theoretical values of the:
- Euler equation

![Euler Equation](images/euler_equation.png)

- Accumulation law of human capital

![Accumulation law](images/accumulation_law.png)

- Initial stock of human capital

![Initial condition](images/initial_condition.png)

We estimate the optimal path using a deep neural network calibration with back propagation of the loss of the residuals associated with the three equations. We observe a convergence to the steady state of the model.

![Optimal path](images/optimal_path.png)
