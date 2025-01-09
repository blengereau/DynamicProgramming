# WIP: Dynamic Programming Applied to a Neo-Classical Growth Model

This project involves solving an optimal growth model using recursive methods, with an exploration of the case of a greedy policy. Additionally, it includes a resolution of the optimal policy using a neural network approach.

Model:

An agent allocates his time between producing the consumption good C and accumulating human capital H.
He seeks to maximize his discounted utility:

\[
\begin{aligned}
&\max_{\{C_t\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t U(C_t) \\[6pt]
\text{subject to:} \quad
& (i)\; C_t = H_t^\alpha \, L_t, \\[3pt]
& (ii)\; H_t = (1-\delta)\,H_{t+1} + \bigl(1 - L_{t-1}\bigr), \\[3pt]
& (iii)\; L_t \in [0,1].
\end{aligned}
\]
