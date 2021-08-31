module DFT
    contains  
function DFT_fourier(x) result(w)
implicit none
integer n,i,j
complex :: x(:)
real :: pi
integer, dimension(size(x),1) :: k
complex :: Comp
complex, Allocatable :: result(:,:),x1(:,:)
complex, dimension(size(x)) :: w
pi = 3.1415926
Comp = (0,2)
n = size(x)
Allocate(x1(n,1))
Allocate(result(n,1))
x1 = reshape(x,(/n,1/))
DO j=0,n-1
k(j+1,1) = j
END DO
result = MATMUL(k,TRANSPOSE(k))
do i = 1,n
do j = 1,n
result(i,j) = exp(-Comp*pi*result(i,j)/n)
end do
end do
w = reshape(MATMUL(result,x1),(/n/))
end function
end module

function DFT_fourier(x) result(w)
implicit none
integer n,i,j
complex :: x(:)
real :: pi
integer, dimension(size(x),1) :: k
complex :: Comp
complex, Allocatable :: result(:,:),x1(:,:)
complex, dimension(size(x)) :: w
pi = 3.1415926
Comp = (0,2)
n = size(x)
Allocate(x1(n,1))
Allocate(result(n,1))
x1 = reshape(x,(/n,1/))
DO j=0,n-1
k(j+1,1) = j
END DO
result = MATMUL(k,TRANSPOSE(k))
do i = 1,n
do j = 1,n
result(i,j) = exp(-Comp*pi*result(i,j)/n)
end do
end do
w = reshape(MATMUL(result,x1),(/n/))
end function

recursive function FFT_fourier(x) result(w)
use DFT
implicit none
integer n,k
real :: pi
complex :: x(0:)
complex :: CompN,i,l
complex, Allocatable :: x_odd(:),x_even(:),w(:)
n = size(x)
Allocate(x_odd(0:n/2-1))
Allocate(x_even(0:n/2-1))
Allocate(w(0:n-1))
pi = 3.1415926535
i = (0,1)
CompN = exp(-2*i*pi/n)
DO k=0,(n/2)-1
    x_odd(k)=x(2*k+1)
    x_even(k)=x(2*k)
END DO
l = (1,0)
if (n<=4) then
w = DFT_fourier(x)
else
x_even = FFT_fourier(x_even)
x_odd = FFT_fourier(x_odd)
DO k=0,(n/2)-1
w(k)=x_even(k)+l*x_odd(k)
w(k+n/2)=x_even(k)-l*x_odd(k)
l = l*CompN
END DO
end if
end function

