# Lecture 1:INTRODUCE
##1.1 About the Course
### (a)Class:
Web. Class Ｉ－４－201
### (b)Email:
Email : Yong-Zhang@whu.edu.cn
### (c)References:
(1)YongZhang Online lecture notes on QIC Version 4
(2)Nielsen and Chuang : QC and QI

## 1.2 Information and Computation
### 1.2(a)
David Deutsch,1985
What computers can or cannot compute is determined by the law of physics and not mathematics 


|  Computer  |  Physical System  |
| --- | --- |
|  Computation  |  Motion  |
|  Input  | Initial state   |
|  Rules  |  Law of motion  |
|  Output  | Final state   |

Information is physical (Rolf Landauer 1961)
and is encoded in the state of a physical system

Classical Information ->{encoded} Classical System

Quanta information ->{encoded} Quanta System

Computation is a physical process (David 1985) and is performed is an physical realizable process 

Universe is Quanta Information

###1.2(b)Definition of Quanta Information and Quanta Computation

#### Def1:
QIC is the study of *using fundamental principles of quanta mechanics to perform information processing and computational tasks

#### Def2(Experiment Physics):
QIC is the study of performing information processing and computation tasks in quanta mechanical system

#### Def3(Classical System):
QIC is the study of combing quanta systems and classical systems to perform information process and computational tasks 

#### Def4(Fundamental Principles)

QIC represents a further development of quanta mechanics and understands fundamental principles of quanta mechanics from the point of information and computation

### Think style of QI and QC
a)think about information and computation physically namely detise physical system to represent and process information
b)think about physics computationally and informationally namely describe physics in terms of information and computation

# Lecture 2: QUBITS
## 2.1 Basic concepts of qubit
Qubit: Quantum Binary Digit

Unit: Smallest unit of quantum information

Range set : two dimensional Hilbert space(linear space)

State:

$\left | \psi \right \rangle = \alpha \left | 0 \right \rangle + \beta \left | 1 \right \rangle$

Vectors as an element of linear space[$\left | 0 \right \rangle, \left | 1 \right \rangle$]

[$\left | 0 \right \rangle, \left | 1 \right \rangle$] are orthogonal basis of $H_2 = space{[\left | 0 \right \rangle, \left | 1 \right \rangle]}$

$|\alpha|^2+|\beta|^2=1$

Hidden information is infinity

COPY:No-cloning theorem(No perfect quanta copy)

Measurement:

|Classical  | Quanta   |
| --- | --- |
|  0->0,1->1{Deterministic}  |Random|

Observed Information:2 state

QIC is a kind of ART

$\infty \to 2$


|    |  Bit  | Qubit   |
| --- | --- | --- |
|  Object  |  Mathematical  |  Mathematical  |
|  Hidden information  | 2   | infity   |
|  Measurement outcome |  deterministic  |   probabilistic |
|Observed information | 2| 2|

$\left | \psi \right \rangle = \alpha \left | 0 \right \rangle + \beta \left | 1 \right \rangle$ Quantum measurements
(Wave function collerse)
NOT unitary evolution 
NOT Schrodinger equation

Probability $|\alpha|^2$[After measurement]

$\left | \psi \right \rangle ->{|\alpha|^2}\left | 0 \right \rangle$

Information loss

Irreversible process 

Un-unitary process

QIC is powerful because its hidden information is infinitely large due to linear superposition principle

But it is difficult to manipulate such hidden information

Because of quantum measurement the weirdness

Classical bits : 0 or 1[2 Choice]
Quantum bits : $\left | \psi \right \rangle = \alpha \left | 0 \right \rangle + \beta \left | 1 \right \rangle$ has [$\infty$ choice]

Qubit

### 2.1(a)The state of vector formalism of a qubit

$H_2 = span\{\left | 0 \right \rangle ,\left | 1 \right \rangle\}$

Computation basis

$\left | 0 \right \rangle = (1,0)$ And $\left | 1 \right \rangle$

A normalized state vector modules global(phase factor)


$\left | \psi \right \rangle = \alpha \left | 0 \right \rangle + \beta \left | 1 \right \rangle$ 

$|\alpha|^2+ |\beta|^2 =1$

$ \alpha $ and $ \beta \notin$ Complex Numbers​

$\alpha,\beta$ -> 4 real numbers

$|\alpha|^2+|\beta|^2 =1 $ -> one real constraints

Irrelevant global phase -> one real constrains

Two indepent real parameters to characterize a qubit

$\left | \psi_+ \right \rangle = cos\frac{\theta}{2}\left | 0 \right \rangle
+e^{i\varphi}sin\frac{\theta}{2}\left | 1 \right \rangle$

Bloch vector $\vec{n} = (sin\theta cos\varphi,sin\theta sin\theta sin\varphi cos\theta)$

When $\vec{n} = (1,0,0) = \vec{e_x}|_{\theta = \frac{\pi}{2},\varphi = \pi}$

So we can get:

$\left | \psi_+(\vec{e_y}) \right \rangle
=\frac{1}{\sqrt{2}}(\left | 0 \right \rangle + i\left | 1 \right \rangle)$=$\left |+ \right \rangle ^{'} $

$\left | \psi_+\vec(n) \right \rangle$depends on the value of $\theta  $ and $ \varphi$

Quanta mechanics:
+ Schrodinger Equation
+ Heisenbeo QM

### 2.2 The Stabilzer formalism of a qubit

Group Theory(concepts such as Pauli Group)

$\left | \psi_+(\theta,\varphi) \right \rangle$ is completely fixed as the eigenstate of $\sigma_n = \vec{\sigma_n}\cdot\vec{n}$ with eigenvalue

And $\left | \psi_+(\theta, \varphi) \right \rangle |  0\le \theta \le \pi,0 \le \varphi \le 2\pi$ in the bolch sphere

And $\{\left | \psi\right \rangle\ | \sigma_n | \psi \rangle=\left | \psi\right \rangle\}$

$\vec{\sigma} = (\sigma_x,\sigma_y,\sigma_z)$[Pauli matrix]

$\sigma_x = \begin{pmatrix}
 0 &1 \\
  1&0
\end{pmatrix}$ ; $\sigma_y = \begin{pmatrix}
 0 &-i \\
  i&0
\end{pmatrix}$ ; $\sigma_z = \begin{pmatrix}
 1&0 \\
 0&1
\end{pmatrix}$

spin

$\vec{n} = (n_x,n_y,n_z)$ is the Bloch Vector

and $\vec{\sigma_n}=\vec{\sigma}\cdot\vec{n} = \sigma_xn_x+\sigma_yn_y+\sigma_zn_z$

$\left | \psi_+(\theta, \varphi) \right \rangle = \begin{pmatrix}
  cos\frac{\theta}{2}\\e^{i\varphi}sin\frac{\theta}{2}
\end{pmatrix}$



Stabilizer formalism of qubit

expectation value

$\left \langle \psi_+(\theta,\varphi)  |\vec{\sigma}\cdot\vec{m}| \psi_+(\theta,\varphi)  \right \rangle =\vec{m}\cdot\vec{n}$

NOTE:$(\vec{\sigma}\cdot\vec{n})(\vec{\sigma}\cdot\vec{n})=(\sigma_in_i)(\sigma_jn_j)=(\sigma_i\sigma_j)(n_in_j)=\delta_{ij}+i\varepsilon _{ijk}\sigma_k$

Quanta System Open System

Schrodinger eq. - > Closed System

(State Vector)

We consider the density matrix of a qubit

$\rho$:density matrix

and $\rho$ has some property

+ $\rho \ge 0$
+ $tr(\rho) = 1$
+ $\rho^{+}=\rho$

quantum statistic mechanics

and consider$\vec{P}$ = polarzation vector[$\rho(\vec{P}) = \frac{1}{2}(I_2+\vec{P}\cdot\vec{\sigma})$]

| Classical    | {0,1}        |
| ------------ | ------------ |
| Corpotation  | Bloch sphere |
| State Vector | Bloch ball   |
| Density      |              |



### 2.3 Two bit system

The corpotational basis of orthonormal

=span{$\left | x_1x_2 \right \rangle,x_1,x_2 = 0,1$} = span{$\left | 00 \right \rangle,\left | 01 \right \rangle,\left | 10 \right \rangle,\left | 11 \right \rangle$}

$\left | \psi \right \rangle = \sum_{x_1,x_2} \alpha_{x_1,x_2}| x_1x_2 \rangle$

Genetri picture of 2-qubit-system

and we define: $| x_1x_2 \rangle = | x_1\rangle\otimes | x_2 \rangle$[Tensor Product]

Maximalled entanglend state{For examples : Bell States}

$| \beta_{x,y}\rangle$

for example:

$\beta_{x_1,x_2} = \frac{1}{\sqrt{2}}(| 0x_2\rangle+ (-1)^{x_1}|0\bar{x_2}\rangle)$[$\bar{x_2} = 1\otimes x_2$]

