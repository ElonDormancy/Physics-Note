real(kind = 8) function mont(n,m)
IMPLICIT NONE
real(kind = 8):: x,y,i
integer j,k,n,m
call RANDOM_SEED ()
i = 0
DO j =1,n
DO k =1,m
call RANDOM_NUMBER(x)
call RANDOM_NUMBER(y)
if (x**2 + y**2 <=1) THEN
i = i+1
endif
END DO
END DO
mont = i/(n*m)
end

