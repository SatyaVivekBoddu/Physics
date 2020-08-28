# Physics
Python implementations of various numerical methods used in physics.

Many of these methods were discussed and a result of the problem-sheets of my Numerical Analysis II class at ETH Zürich.

### Euler and RK4
Running compare.py gives us two graphs in phase space and two graphs plotting position over time. The first two graphs show the Explicit Euler method in blue, the Implicit Euler method in red, the Implicit Midpoint
method in purple and finally the RK4 scheme in grey. The last two graphs show the Implicit Midpoint Method in purple and the classical 4-order Runge-Kutta method in grey for longer times.

![Figure 1](https://github.com/SatyaVivekBoddu/Physics/blob/master/Euler%20and%20RK4/Figure_1.png)
![Figure 2](https://github.com/SatyaVivekBoddu/Physics/blob/master/Euler%20and%20RK4/Figure_2.png)

As seen in Figure 1, the Implicit Euler solution tends quickly towards zero as the steps increase. A longer time interval is necessary to observe the behavior for RungeKutta 4 (cf. Figure 3).

![Figure 4](https://github.com/SatyaVivekBoddu/Physics/blob/master/Euler%20and%20RK4/Figure_4.png)
![Figure 3](https://github.com/SatyaVivekBoddu/Physics/blob/master/Euler%20and%20RK4/Figure_3.png)

The implicit Euler and RK4 solutions have a so-called ”numerical friction”, although there is no friction in the model and the total energy is (supposed to be) conserved. The solution of the explicit Euler method blows-up in Figure 1 and 2. Only the solution of the implicit mid-point rule inherits the stability of the exact
solution (cf. Figure 3 and Figure 4).

Explanation adapted from solutions provided by the class.
