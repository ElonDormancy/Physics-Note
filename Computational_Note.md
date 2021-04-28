# Numerical Recipes in Physics and Astronomy

## Lecture 1[Introduction]

### Intro

#### Subjects To Learn

+ Program organization, accuracy and stability {准确性和稳定性}
+ Solutions of equations in one variable {单变量方程的解}
+  Interpolation and polynomial approximation {插值和多项式拟合}
+  Numerical differentiation and integration {数值的积分和微分}
+  Fourier analysis {傅里叶变换}
+  Time-dependent partially differential equation{含时的偏微分方程} 
+  Introduction to parallel programming {并行编程介绍}

#### Literature[参考文献]

+ J.D. Faires and R.L. Burden, Numerical Analysis (available in the library)
+ W.H. Press, S.A. Teukolsky, W.T. Vetterling and B.P . Flannery,    
  Numerical Recipes (electronic version http://numerical.recipes )

#### Programming style[编程风格]:

1. Keep it simple, stupid (KISS principle). [简单易懂原则]
2. Make the code structured. Use modules, subroutines and functions. [模块化]
3. Add comments extensively. The comments help for : [必要的注释]
  + Reading the program for others and also for yourself in future (you may reuse 
    the code many years later after writing it). 
  + Debugging the codes 
4. Name the variables appropriately and uniformly, which are easier to be 
    recognized, helpful for using and reading. [命名变量尽量用原意]
5. Try to avoid explicit branches, such as “if…..goto”, which make the reading of the 
    codes more difficult. Use if…then, do while…, etc. 
6. Make the code in parallel for numerically intensive calculations (OpenMP , MPI) [并行编写代码]

### Accuracy and Stability

#### Error and accuracy[错误和精度]

计算机中数字的存储包括两种基本类型:定点和浮点。45和45.0不一样。

不动点指的是精确的、离散的整数。用于循环下标，数组下标。

浮点指的是有小数点的数字。

#### Roundoff error[舍入误差]

It is most problematic when numbers of very different size are added or subtracted: 
For example: in single-precision[当 + 或 - 非常不同大小的数字时]

1.0 + 0.001   = 1.0010000 

1.0 + 0.000000001  = 1.0000000

Solutions to underflow and overflow errors: [下溢，溢出]
1. Use double precision  [使用双精度]

2. Rescale or use a logarithmic scale [重标或使用对数标度]

3. Choose proper order of operations[选择正确的操作顺序] 
     For example:

      $10^{-30} \times 10^{-30}/ 10^{-30} =0,\\ 10^{-30} /10^{-30} \times 10^{-30} = 10^{-30} $

Numerical differentiation: [数值微分]

For a function$ f(x) $and at a point $x=x_0$, the first derivative can be estimated by 
$f′(x0)≈[f(x_0+h)−f(x_0−h)]/2h $
where h is a step-size. 

### Homework 1

~~~Python
import matplotlib.pyplot as plt
import numpy as np
#Recurrence Relation
def Bessel(x,n,m):
    if n>= m:
        return 0
    elif n == m-1:
        return 1
    else :
        return -Bessel(x,n+2,m) + 2*(n+1)*Bessel(x,n+1,m)/x
coefficient = 0
#Sum to normalized
def normailzed(x,m):
    sum = Bessel(x,0,m)**2
    for i in range(1,m+1):
        sum += 2*Bessel(x,i,m)**2
    
    coefficient = (1/sum)**0.5
    
    return coefficient

#Plot BesselFunction
x = np.linspace(1e-15, 30, 500)
for v in range(0,11):
    plt.plot(x, normailzed(x,10)*Bessel(x,v,10))
plt.xlim((0, 30))
plt.ylim((-0.5, 1.1))
plt.legend(('${J}_0(x)$', '${J}_1(x)$', '${J}_2(x)$',
            '${J}_3(x)$', '${J}_4(x)$', '${J}_5(x)$',
            '${J}_6(x)$', '${J}_7(x)$', '${J}_8(x)$',
            '${J}_9(x)$', '${J}_{10}(x)$'),loc = 0)
plt.xlabel('$x$',fontsize = "12")
plt.ylabel('${J}_n(x)$',fontsize = "12")
plt.grid(True)
plt.tight_layout(0.5)
plt.show()

~~~

**m= 10**和 **m=20**的图像有显著差别由于精度的关系

详细见Homework 1.py

## Lecture 2[Root Finding]

##### Approach 1：Bisection Method[二分法]

~~~
#伪代码
calculate[a_1,b_1]
set a_1 = a,b_1 = b
let p_1 = (a_1+b_1)/2
if f(p_1) = 0:
	p = p_1
else:
	if f(p_1)/f(a_1) >0:
		set a_2 = p_1
		set b_2 = b_1
	else:
		set a_2 = a_1
		set b_2 = p_1
calculate[a_2,b_2]
~~~

**INPUT :** [a,b]

**OUTPUT :** approximate root : p

#### Example:

 Show that $f(x) = x^3+4x^2 -10 =0$has a root in [1, 2], and use the Bisection 
method to determine an approximation to the root that is accurate to at least within 
$10^{−4}$.

Code:

~~~python
def f(x):
    f = x**3+4*x**2-10
    return f

def Bisection(a, b):
    p = a+(b-a)/2
    if -1e-8 < f(p) < 1e-8:
        print(p)
    else:
        if f(a)*f(p) > 0:
            a = p
            return Bisection(a, b)
        else:
            b = p
            return Bisection(a, b)

Bisection(1,2)
~~~

OUTPUT : p = 1.365230013616383



##### Approach 2：Fixed-point Iteration Method[不动点方法]

+ A fixed point for a function is a number at which the value of the function does not 
  change: 
+ The number p is a fixed point for a given function g if g( p) = p.

Fixed-point Iteration Method{定点迭代法}

Given a root-finding problem$ f (p)$ = 0, we can define functions $g(x)$ with a fixed point 
at p in a number of ways, for example, as:$g(x) = x-f(x)$ 

+ (i) if $g \in C[a,b]$ and $g(x)\in [a,b]$ for all x in $[a,b]$,then **$g$ has at least one fixed point at $[a,b]$**
+ (ii) if if in addition $g'(x)$ exists on $(a,b)$ and a positive constant $k<1$ exists with: $|g'(x)|\le k$ for all $x \in (a,b)$ 

> Step : Choose a initial approximation p_0 and generate the list {$p_n$}
> and the Recurrence relationship is $p_n =g(p_{n-1})$[function iteration]

Example :

Find the solution of $f(x)=x^3+4x^2−10=0$ in [1, 2] by using the fixed-point iteration method.

Support : $g(x) = x-x^3-4x^2+10$

Code:

~~~Python
def a(x):
    v1= x - x**3 -4*x**2 +10
    return v1
def b(x):
    v2= 0.5*(10-x**3)**0.5
    return v2

def iteration(x):
    for i in range(100):
        x = b(x)
    print(x)

iteration(1.5)
~~~

OUTPUT  = 1.3652300134140969

##### Approach 3: Newton's Method

assuming that since $|p-p_0|$ is small and the term invoving $(p-p_0)^2$ is much smaller

so $$0 \approx f(p_0) +(p-p_0)f'(p_0)$$

we can solving for $p$ gives:

$$p\approx p_0-\frac{f(p_0)}{f'(p_0)} \equiv p_1$$

we get the iterative relationship

$$p_n = p_{n-1}-\frac{f(p_{n-1})}{f'(p_{n-1})}$$

Example:Consider the function $f (x) = cos x−x = 0$. Approximate a root of $f$ using

 (a) Fixed-point method

 (b) Newton’s Method.

Code:

~~~Python
import math as mt
pi = 3.1415926535


def f(x):
    g = mt.cos(x) - x
    return g


def fix_point(x):
    for i in range(50):
        x = f(x) + x
    print(x)


def Newton(x):

    for i in range(50):
        x = x - f(x)/(-mt.sin(x)-1)
    print(x)


fix_point(0.74)
Newton(pi/4)

~~~

OUTPUT :(a)0.7390851332175704
						 (b)0.7390851332151607



The Taylor series derivation of Newton’s method at the beginning of the section points out the importance of an accurate initial approximation.[$(p-p_0)^2$尽可能的小]



##### Approach 4: Secant Method

$f'(p_{n-1}) = \lim_{x \to p_{n-1}}\frac{f(x)-f(p_{n-1})}{x-p_{n-1}} $

If $P_{n-2}$ is close to $p_{n-1}$,then

$f'(p_{n-1})\approx \frac{f(p_{n-2})-f(p_{n-1})}{p_{n-2}-p_{n-1}}=\frac{f(p_{n-1})-f(p_{n-2})}{p_{n-1}-p_{n-2}}$

带入第一个式子得到

$p_n = p_{n-1}-\frac{f(p_{n-1})(p_{n-1}-p_{n-2})}{f(p_{n-1})-f(p_{n-2})}$

We can also compare with four approch:

~~~Python
from sympy import *
pi = 3.1415926535


def f(x):
    g = cos(x) - x
    return g


def f_1(x):
    t = symbols('t')
    expr = diff(cos(t) - t, t)
    return expr.subs(t, x)


def Bisection(a, b):
    p = a+(b-a)/2
    if -1e-8 < f(p) < 1e-8:
        print(p)
    else:
        if f(a)*f(p) > 0:
            a = p
            return Bisection(a, b)
        else:
            b = p
            return Bisection(a, b)


def fix_point(x):
    for i in range(50):
        x = f(x) + x
    print(x)


def Newton(x):

    for i in range(50):
        x = x - f(x)/(f_1(x))
    print(x)


def Secant(x0, x1):
    for i in range(50):
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        if abs(x2-x0) < 0.00000001:
            break
    print(x2)


Bisection(0.5, 0.8)
fix_point(0.74)
Newton(pi/4)
Secant(0.5, 0.8)

~~~

OUTPUT：

> Bisection :0.7390851378440858
> 		Fix_point :0.739085133217570
> 		Newton: 0.739085133215161
> 		Secant: 0.739085133215161

#### [RootFind] Summary:

+ Bisection Method
+ Fixed-point Iteration Method
+ Newton’s Method
+ Secant Method

## Lecture 3[Numerical Integration ]

### Polynomial interpolation

Weierstrass Approximation Theorem 

Suppose  that $f$ is defined and continuous on$[a,b]$so For each $\varepsilon >0$,there always exist a polynomial $P(x)$ with $|f(x)-P(x)|<\varepsilon $ for all $x$ in$[a,b]$

$P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots a_1x+a_0$

$Taylor$  $series$精度集中在某点附近，整个区间内泰勒多项式做不

#### Lagrange Interpolating Polynomials

simple example: Two Points

Define the functions:

$L_0(x)=\frac{x-x_1}{x_0-x_1}$ and $L_1(x)=\frac{x-x_0}{x_1-x_0}$

so $P(x)=L_0(x)f(x_0)+L_1(x)f(x_1)$

so **How to generate the interpolation to n+1 points?**

构造一个最高次方为$n$次方的多项式来通过$n+1$个点

consider:

$L_{n,k}(x)=\frac{(x-x_0)(x-x_1)\cdots(x-x_{k-1})(x-x_{k+1})\cdots(x-x_n)}{(x_k-x_0)(x_k-x_1)\cdots(x_k-x_{k-1})(x_k-x_{k+1})\cdots(x_k-x_n)}=\prod_{i=0 (i\not=k)}^{n} \frac{x-x_i}{x_k-x_i}\tag{3.1}$

so $P(x)=L_{n,0}f(x_0)+L_{n,1}f(x_1)+\cdots L_{n,n}f(x_n)$

### Numerical Integration

#### Approch 1:Rectangular approximation

$\int_a^bf(x)dx=\lim_{max\Delta x_i \to 0}\sum_{i=1}^nf(z_i)x_i=\lim_{n \to \infty}\frac{b-a}{n}\sum_{i=0}^nf(x_i)\tag{3.2}$

##### Trapezoidal rule

$\int_a^bf(x)dx \approx (b-a)\frac{f(a)+f(b)}{2}$

and 

$\int_a^bf(x)dx\approx\frac{h}{2}\sum_{k=1}^n(f(x_{k+1})+f(x_{k}))=\frac{b-a}{2N}(f(x_1)+2f(x_2)+2f(x_3)\cdots2f(x_{N-1})+f(x_N))\tag{3.3}$



#### Approch 2: Simpson’s rule

$\int_a^b f(x)dx\approx\frac{b-a}{6}[f(a)+4f(\frac{a+b}{2})+f(b)]$

$\int_a^bf(x)dx\approx\frac{h}{3}[f(x_0)+4f(x_1)+2f(x_2)+4f(x_3)+2f(x_4)+\cdots4f(x_{n-1})+f(x_n)]$



**How to derive them?** 

通过对拉格朗日插值的多项式积分得到：[舍去高阶项]

$P_n(x)=\sum_{i=0}^nf(x_i)L_i(x)$

$\int_a^bf(x)dx=\sum_{i=0}^n\int_a^bf(x_i)L_i(x)dx=\sum_{i=0}^na_if(x_i)$

其中$a_i=\int_a^bL_i(x)dx$



so Trapezoidal rule : n=1

$P_1(x)=\frac{x-x_1}{x_0-x_1}f(x_0)+\frac{x-x_0}{x_1-x_0}f(x_1)$

so:

$\int_a^bP_1(x)dx=\int_{x_0}^{x_1}P_1(x)dx=\frac{x_1-x_0}{2}[f(x_0)+f(x_1)]$

so Simpson’s rule : n=2

$P_2(x) = \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}f(x_0)+\frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)}f(x_1)+\frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}f(x_2)$

so:

$\int_a^bP_2(x)dx=\int_{x_0}^{x_2}P_2(x)dx=\frac{h}{3}[f(x_0)+4f(x_1)+f(x_2)]$

​	

##### Newton-Cotes formula

###### Example1：Calculate $\int_0^{\frac{\pi}{4}}sinx dx$

Solution :

~~~Python
from sympy import *

Pi = 3.1415926


def L(n, k, a, b):
    x = symbols('x')
    h = (b-a)/n
    prob = 1
    for i in range(n+1):
        if i == k:
            pass
        else:
            prob = prob*(x - (a+i*h))/(k*h-i*h)
    return integrate(prob, (x, a, b))


def f(x):
    g = sin(x)
    return g


def P(n, a, b):
    h = (b-a)/n
    p = 0
    for i in range(n+1):
        p = p + f(a+i*h)*L(n, i, a, b)
    return p


print(P(1, 0, Pi/4))
print(P(2, 0, Pi/4))
print(P(3, 0, Pi/4))
~~~

OUTPUT:

> n= 1：0.277680175177979
>
> n=  2：0.292932628362332
>
> n = 3：0.292910693073977

###### Example 2 Determine the value of $h$ that will ensure an approximation error of less than 0.00002 when approxmating $\int_0^{\pi}sinxdx$ and employing

(a)Composite Trapezodial  rule and (b) Composite Simpon's rule

此处需要考虑误差项：

$f(x)=P(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)(x-x_1)\cdots (x-x_n)$

(a)$n=1$时 

误差项为$|\frac{\pi h^2}{12}f''(\xi)|<0.00002$

$h=\frac{\pi}{n}$则得到$n\ge360$

(b)$n=2$时

误差项为$|\frac{\pi h^4}{180}f^{(4)}(\xi)|<0.00002$

$h=\frac{\pi}{n}$则得到$n\ge18$

Code:

~~~Python
from sympy import *

Pi = 3.1415926535898


def L(n, k, a, b):
    x = symbols('x')
    h = (b-a)/n
    prob = 1
    for i in range(n+1):
        if i == k:
            pass
        else:
            prob = prob*(x - (a+i*h))/(k*h-i*h)
    return integrate(prob, (x, a, b))


def f(x):
    g = sin(x)
    return g


def P(n, a, b):
    h = (b-a)/n
    p = 0
    for i in range(n+1):
        p = p + f(a+i*h)*L(n, i, a, b)
    return p


def Composite(n, m, a, b):
    s = (b-a)/m
    r = 0
    for i in range(m):
        r = r + P(n, a+i*s, a+(i+1)*s)
    return r

print(Composite(1, 360, 0, Pi))
print(Composite(2, 18, 0, Pi))
~~~

OUTPUT:

> 1.99998730759189
>         2.00000064497207

#### Monte Carlo Integration

This method is particularly useful for higher-dimensional integrals. 

such as 2-dim

$\iint_Rf(x,y)dA = \int_a^b(\int_c^df(x,y)dy)dx$

Apply Trapezoidal rule

$\int_c^df(x,y)dy \approx\frac{k}{2}[f(x,c)+f(x,d)+2f(x,\frac{c+d}{2})] $

Also apply Trapezoidal rule

we can get:

$\iint_Rf(x,y)dA\approx$

$\frac{(b-a)(d-c)}{16}[f(a,c)+f(a,d)+f(b,c)+f(b,d)+2[f(\frac{a+b}{2},c)+f(\frac{a+b}{2},d)+f(a,\frac{c+d}{2})+f(b,\frac{c+d}{2})]+4f(\frac{a+b}{2},\frac{c+d}{2})]$

Apply Simpson’s rule we can also get the almost same result

#### Numerical Differentiation

$f'(x)=\lim_{h \to 0}\frac{f(x+h)-f(x)}{h}$

$f'(x)=\lim_{h \to 0}\frac{f(x+h)-f(x-h)}{2h}$

$f'(x)=\lim_{h \to 0}\frac{-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h)}{12h}+\frac{h^4}{30}f^{(5)}(c)$

from the above discusstion we can get:

$f(x)=\sum_{k=0}^nf(x_k)L_k(x)+\frac{(x-x_0)\cdots(x-x_n)}{(n+1)!}f^{(n+1)}(\xi(x))$

so

$f'(x)=\sum_{k=0}^nf(x_k)L_k'(x)+(\frac{(x-x_0)\cdots(x-x_n)}{(n+1)!}f^{(n+1)}(\xi(x)))'$问题？

and we can get the approxmate (n+1)-point formula

$f'(x_j)=\sum_{k=0}^nf(x_k)L'_k(x_j)+\frac{f^{(n+1)(\xi(x_j))}}{(n+1)!}\prod_{k=0 (k\not=j)}^{n} (x_j-x_k)$

first we use three-point formulas and consider their errors

$L_0(x)=\frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}$

so we get

$L'_0(x)=\frac{2x-x_1-x_2}{(x_0-x_1)(x_0-x_1)}$

so 

$f'(x_j)=f(x_0)[\frac{2x_j-x_1-x_2}{(x_0-x_1)(x_0-x_2)}]+f(x_1)[\frac{2x_j-x_0-x_2}{(x_1-x_0)(x_1-x_2)}]+f(x_2)[\frac{2x_j-x_0-x_1}{(x_2-x_0)(x_2-x_1)}]+\frac{1}{6}f^{(3)}(\xi_j) \prod_{k=0,k\not=j}^2(x_j-x_k)$

则

$f'(x_0)=\frac{1}{2h}[-3f(x_0)+4f(x_0+h)-f(x_0+2h)]+\frac{h^2}{3}f^{(3)}(\xi_0)$

### Monte Carlo Intergration

$F=\int_a^bf(x)dx$

sample mean method

$F_n=(b-a)<f>=(b-a)\frac{1}{n}\sum f(x_i)$

#### Error Analysis

run another n trial and get the the average of error

define $\sigma^2_m=<M^2>-<M>^2$

and $<M>=\frac{1}{m}\sum_{\alpha=1}^mM_\alpha$

$<M^2>=\frac{1}{m}\sum_{\alpha=1}^mM_\alpha^2$

consider m set of measurement and n trial

and index $\alpha$ to denote a particular value of measurement and i is the ith trial 

so we get $M_\alpha=\frac{1}{n}\sum_{i=1}^nx_{\alpha,i}$

and $\bar{M}=\frac{1}{m}\sum_{\alpha=1}^mM_\alpha=\frac{1}{mn}\sum_{\alpha=1}^m\sum_{i=1}^nx_{\alpha,i}$

the difference between $M_\alpha$  and $\bar{M}$ define $e_\alpha=M_\alpha-\bar{M}$

so $\sigma_m^2=<M^2>-<M>^2$

and $\frac{1}{m}\sum_{\alpha=1}^me_\alpha^2=\frac{1}{m}\sum(M_\alpha-\bar{M})^2=\frac{1}{m}\sum(M_\alpha^2-2M_\alpha\bar{M}+\bar{M}^2)$

and $\sum \bar{M}=\sum M_\alpha$

so $\sigma_m^2=<M^2>-\frac{1}{m}\bar{M}(\sum 2M_\alpha-\sum\bar{M})=<M^2>-<M>^2=\frac{1}{m}\sum_{\alpha=1}^me_\alpha^2$

The discrepancy of  $d_{\alpha,i}=x_{\alpha,i}-\bar{M}$

$\sigma^2=\frac{1}{mn}\sum_{\alpha=1}^m\sum_{i=1}^nd_{\alpha,i}^2$

from the calculation

we can get $\sigma_m^2=\frac{\sigma^2}{n}$

### Monte Carlo Integration: Metropolis Algorithm

define $<f>=\frac{\int p(x)f(x)dx}{\int p(x)dx}$

For example:

模拟一个由N个粒子组成的系统，体积V，温度T固定的系统并展示他的运动

+ 假设我们希望使用重要抽样来根据任意概率密度$$p(x)$$生成随机变量。Metropolis算法产生点${xi}$的随机游走，这些点的渐近概率分布接近$$p(x)$$
+ 随机漫步定义为从一个值$x_i$到另一个值$x_j$的转移概率$T(x_i→x_j)$，使点$$x_0,x_1,x_2，\cdots$$收敛于$$p (x)$$。
+ $p(x_i)T(x_i\to x_j)=p(x_j)T(x_j\to x_i)$

$T(x_i\to x_j)=min[1,\frac{p(x_i)}{p(x_j)}]$

如何生成$x_{j+1}$

+ 选择其中任何一个位置$x_{tri}=x_i+\delta_i[\delta_i\in[-\delta,+\delta]]$
+ 计算$w=\frac{p(x_{tri})}{p(x_i)}$
  + if$w>1$则$x_{tri}=x_{i+1}$
  + else$w<1$:generate a random number $r$
    + if r<w: accept the change and let $x_{i+1}=x_{tri}$
    + else : $x_{i+1}=x_i$

A rough criterion: one third to one half of the trial steps should be accepted. 

calculate to attain the asymptotic probability $p(x)$

### Homework 2

#### 1.Calculate numerically the value of $\pi$ by using the integral

$I=\int_0^1\frac{4}{1+x^2}=\pi$

(a) Trapezoidal rule and (b) Simpson's rule.

~~~Python
from sympy import *
Pi = 3.1415926535

def L(n, k, a, b):
    x = symbols('x')
    h = (b-a)/n
    prob = 1
    for i in range(n+1):
        if i == k:
            pass
        else:
            prob = prob*(x - (a+i*h))/(k*h-i*h)
    return integrate(prob, (x, a, b))


def f(x):
    g = 4/(1+x**2)
    return g


def P(n, a, b):
    h = (b-a)/n
    p = 0
    for i in range(n+1):
        p = p + f(a+i*h)*L(n, i, a, b)
    return p


print(f"Trapezoidal rule method result{P(1, 0, 1)}")  # Trapezoidal rule
print(f"Simpson's rule method result {P(2, 0, 1)}")  # Simpson's rule.
print(abs(P(1, 0, 1)-Pi)/Pi)
print(abs(P(2, 0, 1)-Pi)/Pi)
~~~

OUTPUT:

Trapezoidal rule method result3.00000000000000
		Simpson's rule method result 3.13333333333333
		0.0450703414213341
		0.00262902326228246

#### 2.Consider the function

$H(x,y)=\begin{cases}
 1 & \text{ if } x^2+y^2<1 \\
 0 & else
\end{cases}$

use the Monte Carlo method to calculate $\pi$:

Find the relation between the relative error ($|I_N-\pi|/\pi$) and the Monte Carlo samples N.

~~~Python
import random
Pi = 3.14159265358979
m = 10
N = 1000000
a = 0
b = 0
for j in range(m):
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            a = a + 1
        else:
            a = a
    b = a+b
print(f"Result = {4*a/(m*N)}")
print(f"{abs(4*a/(m*N)-Pi)/Pi}")
~~~

OUTPUT：Result = 3.1409924
						   0.00019106665184746358

More details in Python Code

## Lecture 5[Fourier Transform]

frequency to time and time to frequency 

Consider

$H(f)=\int_{-\infty}^{\infty}h(t)e^{iwt}dt$

and $h(t) = \int_{-\infty}^{\infty}H(f)e^{-iwt}dw$

$w=2\pi f$

Convolution

$g*h=\int_{-\infty}^{\infty}g(\tau)f(t-\tau)d\tau $

$g*h = G(f)H(f)$

### Discrete Fourier Transform

$h(t)$ is recorded spaced intervals in time

$h_n = h(n\Delta)$[$n = \cdots -3,-2,-1,0,1,2,3\cdots$]

and $h_k \equiv h(t_k)[t_k \equiv k\Delta]$

so $H(f_n) = \int_{-\infty}^{\infty}h(t)e^{2\pi i f_nt}dt\approx\sum_{k=0}^{N-1}h_ke^{2\pi i f_nt_k}\Delta$

per cycle has two sampled value

$f_c \equiv\frac{1}{2\Delta}$

**Sampling theorem**

+ $h(t)$ is continuous
+ sampled limited to frequencies smaller in magnitude than $f_c$

采样定理：采样定理指出，如果信号是带限的，并且采样频率高于信号带宽的两倍，那么，原来的连续信号可以从采样样本中完全重建出来。

$f_S >2f_{MAX}$

Discrete Fourier Transform Example:

$x(t) = sin{2\pi x}$ 

~~~Python
from sympy import *
import matplotlib.pyplot as plt
import numpy as np


def GET(fs, N):
    # define sampled frequency:
    T = N/fs
    h = T/N
    x = []
    for l in range(N):
        x.append(f(l*h).evalf(3))
    return x


def f(x):
    g = sin(2*pi*x)
    return g

# Method 1


def DFT1(x, fs):
    w = 0
    y = []
    p = []
    # DFT:
    for j in range(fs):
        for i in range(fs):
            w = w + x[i]*(cos(2*pi*(j)*i/fs) - I*sin(2*pi*(j)*i/fs)).evalf()
        y.append(w)
        w = 0
    for o in y:
        p.append(abs(o**2))
    return p
# Method 2


def DFT2(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    p = []
    for o in np.dot(M, x).reshape(N, 1):
        p.append(abs(o**2))
    return p


x = []
for i in range(8):
    x.append(i)
plt.scatter(x, DFT1(GET(8, 8), 8), c="red")
plt.scatter(x, DFT2(GET(8, 8)), c="blue")
plt.show()
~~~

OUTPUT:

More detail in Python code

得到$f= 1 $则$w = 2\pi f=2\pi$

$FFT$快速傅里叶变换

$DFT$

$X(k) = \sum_{n=0}^{N-1}x(n)e^{-j\frac{2\pi}{N}nk}$

研究一下$e^{-j\frac{2\pi}{N}nk}=W_N^{nk}$

如我们现在有个$N=4$的信号$x(n)$

$X(k)=\sum_{n=0}^3x(n)\cdot W_4^{nk}$

下面我们来研究一下$W_N^{nk}$的性质

+ 周期性

  $$W^{n(N-k)}_N=W_N^{-nk},W_N^{k(N-n)}=W_N^{-nk}$$

  $W_N^{nk}=W_N^{r}[r =(nk)modN]$

+ 对称性

  $W_N^{nk+\frac{N}{2}}= -W_N^{nk}$

则我们可以设$N=2^m(m\in N^+)$ 

则$X(k) = \sum_{r = 0}^{\frac{N}{2}-1}x(2r)W_N^{2rk}+\sum_{r = 0}^{\frac{N}{2}-1}x(2r+1)W_N^{(2r+1)k}$

由于$r = (mN)modN =0$

则$W^{mN}_N=W_N^0 =1$

同样的利用对称性得到

$W_N^{nk+\frac{N}{2}}=W_N^{mN+\frac{N}{2}}=-W_N^{mN}=-1$

$W_N^{2rk}=W_{\frac{N}{2}}^{rk}$

则$X(k)=\sum_{r = 0}^{\frac{N}{2}-1}x(2r)W_N^{2rk}+\sum_{r = 0}^{\frac{N}{2}-1}x(2r+1)W_N^{(2r+1)k}=\sum_{r = 0}^{\frac{N}{2}-1}x(2r)W_{\frac{N}{2}}^{rk}+W_N^k\cdot\sum_{r = 0}^{\frac{N}{2}-1}x(2r+1)W_{\frac{N}{2}}^{rk}$

令$G(k)=\sum_{r = 0}^{\frac{N}{2}-1}x(2r)W_{\frac{N}{2}}^{rk},H(k)=\sum_{r = 0}^{\frac{N}{2}-1}x(2r+1)W_{\frac{N}{2}}^{rk}$

$G(k)$性质：$G(k+\frac{N}{2})=G(k)$

$H(k)$性质：$W_N^{k+\frac{N}{2}}H(k+\frac{N}{2})=-W_N^{k}H(k)$

## Homework 3

~~~Python
import numpy as np


def DFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized set 32
        return DFT(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N) / N)
        X = np.concatenate(
            [X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])
    return X


def iDFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(np.linalg.inv(M), x).reshape(N, 1)


def iFFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized set 32
        return iDFT(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N) / N)
        X = np.concatenate(
            [X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])
    return X


def CFFT(x, ISIGN):
    if ISIGN == 1:
        a = FFT(x)
    elif ISIGN == -1:
        a = iFFT(x)
    else:
        print("Please input the correct parameter")
    return a
~~~

## Homework 3-2

最终我们得到贝塞尔函数的图像

~~~Python
#标准贝塞尔函数
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spl
x = np.linspace(0, 30, 500)
for i in range(11):
    y = spl.jv(i, x)
    plt.plot(x, y)
plt.xlim((0, 30))
plt.ylim((-0.5, 1.1))
plt.legend(('${J}_0(x)$', '${J}_1(x)$', '${J}_2(x)$',
            '${J}_3(x)$', '${J}_4(x)$', '${J}_5(x)$',
            '${J}_6(x)$', '${J}_7(x)$', '${J}_8(x)$',
            '${J}_9(x)$', '${J}_{10}(x)$'), loc=0)
plt.xlabel('$x$', fontsize="12")
plt.ylabel('${J}_n(x)$', fontsize="12")
plt.grid(True)
plt.tight_layout(0.5)
plt.show()
~~~



~~~python
#FFT
import numpy as np
import matplotlib.pyplot as plt


def f(z, i, N):
    g = np.exp(1j*z*np.cos(2*np.pi*i/N))
    return g


def generatesq(z, N):
    s = []
    for m in range(N):
        s.append(f(z, m, N))
    return s


def DFT(x, n):
    w = 0
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    y = []
    # DFT:
    for k in range(N):
        w = w + x[k]*(1j**(-n)/N)*np.exp(2*np.pi*1j*n*k/N)
    y.append(w)
    return y


x = np.linspace(0, 30, 500)

for i in range(11):
    y = DFT(generatesq(x, 2**12), i)[0]
    plt.plot(x, y)

plt.xlim((0, 30))
plt.ylim((-0.5, 1.1))
plt.legend(('${J}_0(x)$', '${J}_1(x)$', '${J}_2(x)$',
            '${J}_3(x)$', '${J}_4(x)$', '${J}_5(x)$',
            '${J}_6(x)$', '${J}_7(x)$', '${J}_8(x)$',
            '${J}_9(x)$', '${J}_{10}(x)$'), loc=0)
plt.xlabel('$x$', fontsize="12")
plt.ylabel('${J}_n(x)$', fontsize="12")
plt.grid(True)
plt.tight_layout(0.5)
plt.show()
~~~



Homework 1 中图像之所以与此两个图像不相同是因为$M$取值较小，取值为$10$此处我们将Homework 1 中的10改为100即可得到较好的效果[运行速度较慢]



## Lecture 6[Partial Differential Equation]

### Partial Differential Equation

for example the wave equation

is a second-order linear partial differential equation for the description

It typically concerns a time variable t,one or more spatial

use a scalar function $u=u(x_1,x_2,\cdots ,t)$

$\frac{\partial ^2u}{\partial^2t}=c^2 \bigtriangledown ^2u$

Example 1:A pulse traveling through a string with fixed endpoints as modeled by the wave equation

### 数值解微分方程

#### 1 一阶常微分方程差分求解

$\begin{cases}
 y'=f(y,t) \\
  y(t_0)=y_0
\end{cases}$

若离散化$y_n$与$f(y_n,t_n)$

则上述方程为$\frac{y_{n+1}-y_n}{\Delta t}=\frac{f(y_n,t_n)+f(y_{n+1},t_{n+1})}{2},y(0)=y_0$

#### 偏微分方程差分求解

$\frac{\partial u(x,t)}{\partial t}=\lambda\frac{\partial^2u(x,t)}{\partial x^2}$

$u(x,0)=f(x)$

$u(0,t)=g_1(t)$

$u(l,t)=g_2(t)$

时间空间离散化

$\frac{\partial^2u(x,t)}{\partial x^2}_{|i,k}=\frac{u_{i-1,k}-2u_{i,k}+u_{i,k+1}}{h^2}$

$\frac{\partial u(x,t)}{\partial t}_{|i,k}=\frac{u_{i,k+1}-u_{i,k}}{\tau}$

则我们得到差分方程

$\frac{u_{i,k+1}-u_{i,k}}{\tau}=\lambda\frac{u_{i-1,k}-2u_{i,k}+u_{i,k+1}}{h^2}$

$u_{i,0}=f(ih)$

$u_{0,k}=g_1(k\tau)$

$u_{N,k}=g_2(k\tau)$

由此得到递推关系$u_{i,k+1}=\frac{\lambda\tau}{h^2}u_{i+1,k}+(1-2\frac{\lambda\tau}{h^2})u_{i,k}+\frac{\lambda\tau}{h^2}u_{i-1,k}$

$u_{i,0}=f(ih) i=1,2,3\cdots N-1,N=\frac{l}{h}]$

$u_{0,k}=g_1(k\tau)$

$u_{N,k}=g_2(k\tau) k =0,1,3\cdots M,M=\frac{T}{\tau}$

Example:一维热传导方程：

$\frac{\partial u(x,t)}{\partial t}=\lambda\frac{\partial^2u(x,t)}{\partial x^2}$

其中 $\lambda\equiv\frac{\kappa}{c\rho}$

设$\lambda =1 ,l=3,T=1$

设边界条件为：

$u(x,0)=4x(3-x)$

$u(0,t)=0$

$u(3,t)=0$

设步长$h = 0.1,\tau = 0.0001$则$\frac{\tau \lambda}{h^2}=\frac{1}{100},N=\frac{l}{h}=30,M=\frac{T}{\tau}=10000$

从而我们得到递推关系为：

$u_{i,k+1}=\frac{1}{100}u_{i+1,k}+\frac{49}{50}u_{i,k}+\frac{1}{100}u_{i-1,k}$

$u_{i,0}=4ih(3-ih) i =0,1,2,\cdots29$

$u_{0,k}=0,u_{l,k}=0$

Code:

~~~Python
import numpy as np
import matplotlib.pyplot as plt

h = 0.1
N = 30
dt = 0.0001
M = 10000
A = dt/h**2
U = np.zeros([N+1, M+1])

space = np.arange(0, (N+1)*h, h)


for k in np.arange(0, M+1):
    U[0, k] = 0
    U[N, k] = 0

for i in np.arange(0, N):
    U[i, 0] = 4*h*i*(3-i*h)

for k in np.arange(0, M):
    for i in np.arange(0, N):
        U[i, k+1] = A*U[i+1, k]+(1-2*A)*U[i, k]+A*U[i-1, k]
extent = [0, 1, 0, 3]  # 时间和空间的取值范围
levels = np.arange(0, 10, 0.1)
plt.contourf(U, levels, origin='lower', extent=extent, cmap=plt.cm.jet)
plt.ylabel('x', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.show()
~~~

#### Wave function

$\frac{\partial^2 u }{\partial t^2} = c^2\bigtriangledown^2u $

It's solution has superposition

Given boundary condition

#### Maxwell's Equation

$\frac{\partial}{\partial t}H(t) =\frac{1}{-\mu}\bigtriangledown \times E(t)$

$\frac{\partial}{\partial t}E(t) =\frac{1}{\varepsilon }\bigtriangledown \times E(t)$

$\bigtriangledown\cdot\varepsilon E(t) = \rho(t)$

$\bigtriangledown\cdot\mu_0H(t) = 0$

$\frac{\partial^2}{\partial t^2}H(t) = -\frac{1}{\mu}\bigtriangledown\times\frac{1}{\varepsilon}\bigtriangledown\times E(t)$

if $\mu = \mu_0,\varepsilon = \varepsilon_0$

so $\frac{1}{\mu_0 \varepsilon_0}=c^2$

so 

$\frac{1}{c^2}\frac{\partial^2}{\partial t^2}H(t)=\bigtriangledown^2H(t) $

and $\bigtriangledown\times(\bigtriangledown\times X)=\bigtriangledown(\bigtriangledown\cdot X)-\bigtriangledown^2X$

$X(t)=\sqrt{\mu}H(t),Y(t) = \sqrt{\varepsilon}E(t)$

So the equation becomes 

$\frac{\partial }{\partial t}\begin{pmatrix}X(t) \\ Y(t)\end{pmatrix}=\begin{pmatrix}
  0& -\frac{1}{\sqrt{\mu}}\bigtriangledown \times\frac{1}{\sqrt\varepsilon} \\
 \frac{1}{\sqrt{\varepsilon}}\bigtriangledown \times\frac{1}{\sqrt\mu} & 0
\end{pmatrix}\begin{pmatrix}X(t) \\ Y(t)\end{pmatrix} \equiv H\begin{pmatrix}X(t) \\ Y(t)\end{pmatrix} $

$H$ is skew-symmetric i.e. $H^T = -H$

simplify the equation $\frac{\partial }{\partial t}\varphi (t)=H\varphi (t))$

consider $\varphi(t) = e^{tH}\varphi(0)\equiv U(t)\varphi(0)$

and $U(t)^T = U(-t)=e^{-tH}$

Wave function 

$\left \langle U(t)\varphi(0)  | U(0)\varphi(t) \right \rangle =\left \langle \varphi(t)  | \varphi(t)  \right \rangle =\left \langle \varphi(0)  | \varphi(0)  \right \rangle$

we can calculate the energy density of the electromagnetic

$||\varphi(t)||^2=\left \langle \varphi(t)  | \varphi(t)  \right \rangle = \int_V[\varepsilon E^2(r,t)+\mu H^2(r,t)]dr$

and energy density is $w(t) = \varepsilon E^2(r,t)+\mu H^2(r,t)$

and the time integration

$\varphi(t+\tau) = e^{\tau H}\varphi(t) = U(\tau)\varphi(t)$

and for $U(\tau)$ we can use Taylor expansion

$U(\tau) = e^{\tau H}=\sum_{0}^\infty\frac{(\tau H)^n}{n!}$

$\tilde{U(\tau)}  = I+\tau H$

But it is not orthogonal

Lie-Trotter-Suzuki time integration

$e^{t(H_1+H_2\cdots+H_p)}=\lim_{m\to \infty}(\prod_{i=1}^pe^{tH_i/m})^m$

![wiki-LiProduct](D:\桌面\Computational_Physics_Note\wiki-LiProduct.svg)

​		$H = \sum_{i=1}^pH_i$

and $U_1(\tau) = e^{\tau H_1}\cdots e^{\tau H_P}$

if $\tau$ is sufficiently small we can use $U_1(\tau)$ replace the $U(\tau)$

It show  that $||U(\tau)-U_1(\tau)||\le\frac{\tau^2}{2}\sum_{i<j}||[H_i,H_j]||$

$[H_i,H_j] = H_iH_j - H_jH_i$

Define $U_2(\tau) = U_1(-\frac{\tau}{2})^TU_1(\frac{\tau}{2}) = e^{\tau H_p/2}\cdots e^{\tau H_1/2}e^{\tau H_1/2}\cdots e^{\tau H_p/2}$

A particularly useful fourth-order approximation is given by:

$U_4(\tau) = U_2(a\tau)U_2(a\tau)U_2((1-4a)\tau)U_2(a\tau)U_2(a\tau)U_2$

$a \equiv 1/(4-4^{\frac{1}{3}})$

matrix H representing the  TDME must be real, skew-symmetric and be decomposable into a sum of p real, skew-symmetric matrices Hi.

#### Yee time integration

 The Cranck-Nicholson method:

$\tilde{U(\tau)}  = (I+\frac{\tau H}{2})(I - \frac{\tau H}{2})^{-1}$

坐标离散化

$$\frac{\partial }{\partial t}f^{n}(i,j,k)=\frac{f^{\frac{n+1}{2}}(i,j,k)-f^{\frac{n-1}{2}}(i,j,k)}{\Delta t}+O((\Delta t)^2)$$

For example：

$E^{n+1}_x(i,j,k)=E_x^n(i,j,k)+\frac{\Delta t }{\varepsilon(i,j,k)}[\frac{H_z^{\frac{n+1}{2}}(i,j+1,k)-H_z^{\frac{n-1}{2}}(i,j-1,k)}{\Delta y} - \frac{H_y^{\frac{n+1}{2}}(i,j,k+1)-H_y^{\frac{n-1}{2}}(i,j,k-1)}{\Delta z}]  $



#### Finite-difference time-domain (FDTD)

$\begin{pmatrix} H(t+\tau) \\ E(t+\frac{\tau}{2})\end{pmatrix} = (I+\tau A)(I+\tau B)\begin{pmatrix}H(t) \\ E(t-\frac{\tau}{2})\end{pmatrix}$

$\frac{\partial}{\partial t}H_y(t) = \frac{1}{\mu}\frac{\partial }{\partial x}E_z(t)$

and 

$\frac{\partial}{\partial t}E_z(t) = \frac{1}{\varepsilon}\frac{\partial }{\partial x}H_y(t)$

define $H_y(x,t) = \frac{X_y(x,t)}{\sqrt{\mu(x)}}$

$E_z(x,t) = \frac{Y_z(x,t)}{\sqrt{\varepsilon(x)}}$

from above we can get:

$\frac{\partial }{\partial t}X_y(x,t) = \frac{1}{\sqrt{\mu(x)}}\frac{\partial}{\partial x}(\frac{Y_z(x,t)}{\sqrt{\varepsilon(x)}})$

$\frac{\partial }{\partial t}Y_z(x,t) = \frac{1}{\sqrt{\mu(x)}}\frac{\partial}{\partial x}(\frac{X_y(x,t)}{\sqrt{\varepsilon(x)}})$

discrete it 

we get :

$\frac{\partial }{\partial t}X_y(i,t) = \frac{1}{\delta\sqrt{\mu_i}}(\frac{Y_z(i+1,t)}{\sqrt{\varepsilon_{i+1}}}-\frac{Y_z(i-1,t)}{\sqrt{\varepsilon_{i-1}}})$

$\frac{\partial }{\partial t}Y_z(j,t) = \frac{1}{\delta\sqrt{\varepsilon_j}}(\frac{X_y(j+1,t)}{\sqrt{\mu_{i+1}}}-\frac{X_y(j-1,t)}{\sqrt{\mu_{i-1}}})$

 





#### Chebyshev time integration

the expansion of  a scalar function in Chebyshev polynomials :

$f(x)= \frac{1}{2}a_0T_0(x)+\sum_{n=1}^\infty a_n T_n(x)$

where $a_n = \frac{2}{\pi} \int_0^\pi cos(n\theta)f(cos\theta)d\theta$

and chebyshev polynomials $T_n$ are given by $T_n(x) = cos(ncos^{-1}(x))$

and the recursion relation these function is 

$T_{n+1}(x) = 2xT_n(x)-T_{n-1}(x)$

with $T_0(x) = 1,T_1(x) =x$

$U(t) = exp(tH)$

$H$ is a real anti-symmetric matrix

the eigenvalues of skew-symmetric matrix H are purely imaginary so matrix$A = -iH$ is Heritian and all its eignvalues are real and lie in the range$[-\rho(A),\rho(A)]$

where $\rho(A)$ is the spectral radius of A

$\rho(A) = max_{1\le i\le n }|\lambda_i|$

 $\psi(t)=exp(tH)\psi(0) = exp(izB)\psi(0)=[\frac{1}{2}a_0(z)I+\sum_{n=1}^\infty a_n(z)T_n(B)]\psi(0)$ 

$a_n(z) = \frac{2}{\pi}\int_0^\pi cos(n\theta)exp(izcos\theta)d\theta=2J_n(z)i^n$

### Partial differential equations

$\frac{\partial^2 u(x,t)}{\partial x^2} \approx \frac{u(x_{i+1},t)-2u(x_i,t)+u(x_{i-1},t)}{\Delta x^2}$



### Maxwell Equation

$\begin{align}  \nabla\cdot  D &= \rho\\   \nabla\cdot  B &= 0\\   \nabla\times E &= -\frac{\partial B}{\partial t}  \\   \nabla\times H &= \frac{\partial D}{\partial t} + J\end{align}$

So the equation becomes 

$\frac{\partial }{\partial t}\begin{pmatrix}X(t) \\ Y(t)\end{pmatrix}=\begin{pmatrix}
  0& -\frac{1}{\sqrt{\mu}}\bigtriangledown \times\frac{1}{\sqrt\varepsilon} \\
 \frac{1}{\sqrt{\varepsilon}}\bigtriangledown \times\frac{1}{\sqrt\mu} & 0
\end{pmatrix}\begin{pmatrix}X(t) \\ Y(t)\end{pmatrix} \equiv H\begin{pmatrix}X(t) \\ Y(t)\end{pmatrix} $

and 

$X(t)=\sqrt{\mu}H(t),Y(t) = \sqrt{\varepsilon}E(t)$

### Schrödinger equation

one-dimensional time-dependent Schr¨odinger equation is given as

$i\hbar\frac{\partial \psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi(x,t)}{\partial x^2}+V(x)\psi(x,t)$

and we define $\psi(x,t)= \psi_{R}(x,t)+i\psi_I(x,t)$

and the equation can produce thus two coupled partial differential equation

$\hbar\frac{\psi_{R}(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi_I(x,t)}{\partial x^2}+V(x)\psi_I(x,t)$

$\hbar\frac{\psi_{I}(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi_R(x,t)}{\partial x^2}+V(x)\psi_R(x,t)$

mesh it

$x_l = l\Delta x,t_n = n\Delta t[0\le n\le N,0\le l \le L ]$

we can define $\psi(x_l,t_n) = \psi^n(l)$

so 

$\frac{\partial \psi_R(x_l,t_{\frac{n+1}{2}})}{\partial t} \approx \frac{\psi_R^{n+1}(l)-\psi_R^{n}(l)}{\Delta t}$

$\frac{\partial \psi_I(x_l,t_n)}{\partial t} \approx \frac{\psi_I^{\frac{n+1}{2}}(l)-\psi_I^{\frac{n-1}{2}}(l)}{\Delta t}$

$\frac{\partial^2 \psi_R(x_l,t_n)}{\partial x^2} \approx \frac{\psi_R^n(l+1)-2\psi^n_R(l)+\psi^n_R(l-1)}{\Delta x^2}$

so :

$\frac{\hbar}{\Delta t}[\psi_R^{n+1}(l)-\psi_R^{n}(l)] = -\frac{\hbar^2}{2m\Delta x^2}[\psi_I^\frac{n+1}{2}(l+1)-2\psi_I^\frac{n+1}{2}(l)+\psi_I^\frac{n+1}{2}(l-1)]+V(l)\psi_I^\frac{n+1}{2}(l)$

$\frac{\hbar}{\Delta t}[\psi_I^{\frac{n+1}{2}}(l)-\psi_I^{\frac{n-1}{2}}(l)] = \frac{\hbar^2}{2m\Delta x^2}[\psi_R^n(l+1)-2\psi^n_R(l)+\psi^n_R(l-1)]-V(l)\psi_R^n(l)$

for real-valued derivative

$t = (n+\frac{1}{2})\Delta t$

and imaginary-valued drivative is $t = n\Delta t$

$\psi^{n+1}_R(l) $is often called $future$ $state$  

and $\psi^{n}_R(l) $and $\psi_I^{\frac{n-1}{2}}$is often called $preseation$ $state$  

If we directly use the Schrödinger equation

we can get 

$\frac{i\hbar}{\Delta t}[\psi^{n+1}(l)-\psi^{n-1}(l)] = -\frac{\hbar^2}{2m\Delta x^2}[\psi^n(l+1)-2\psi^n(l)+\psi^n(l-1)]+V(l)\psi^n(l)$

运用差分方程的方法即可数值解该方程

