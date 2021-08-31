real function bessel(n,m,x)
implicit none
real :: x
integer n,m,i,k
REAL(kind = 8), Allocatable :: J(:)
REAL(kind = 8) :: SUM
REAL(kind = 8) :: coff
Allocate(J(0:m-1))
i=m-3
J(m-1) = 0.0
J(m-2) = 1.0
do while(i>=0)
    J(i)=2*(i+1)*J(i+1)/x-J(i+2)
    i=i-1
end do
SUM=J(0)**2
k = M-1
DO while(k>=1)
SUM=SUM+2*J(k)**2
k =k-1
END DO
coff=(1.0/SUM)**0.5
bessel = coff*J(n)
end function