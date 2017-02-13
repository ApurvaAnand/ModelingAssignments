%ode

n = 3;
k = 1;
delta_t = 0.001;

A_ode=[];
B_ode=[];

time=1/delta_t;

for m=1:time
    if m==1
        A_ode(m)=1;
        B_ode(m)=0;
    end
    
    A_ode(m+1)=A_ode(m)+delta_t*((-(n*k)*(A_ode(m))^n)+(n*k*B_ode(m)));
    B_ode(m+1)=B_ode(m)+delta_t*((k*(A_ode(m))^n)-(k*B_ode(m)));
    
    
end
B_ode


%pde

delta_x=0.1;
space=1/delta_x;
d=1;


A_pde=zeros(time,space);
B_pde=zeros(time,space);
average_B=[];

A_initial=rand(space,1);

B_pde(1,:)=0;
A_pde(1,:)=A_initial/sum(A_initial);
xmax=space;

for x=1:space
    
    for m=1:time
        
        if x==1
            second_term=A_pde(m,xmax);
            A_pde(m+1,x)=A_pde(m,x)+delta_t*((d*((A_pde(m,x+1))+second_term-2*(A_pde(m,x)))/((delta_x)^2))+(-(n*k)*(A_pde(m,x))^n)+(n*k*B_pde(m,x)));
            B_pde(m+1,x)=B_pde(m,x)+delta_t*((d*((B_pde(m,x+1))+second_term-2*(B_pde(m,x)))/((delta_x)^2))+(k*(A_ode(m))^n)-(k*B_ode(m)));
        end
        
        if x==space
            A_pde(m,x+1)=A_pde(m,1);
            B_pde(m,x+1)=B_pde(m,1);
            
        end
        
        if x>1 
            A_pde(m+1,x)=A_pde(m,x)+delta_t*((d*((A_pde(m,x+1))+(A_pde(m,x-1))-2*(A_pde(m,x)))/((delta_x)^2))+(-(n*k)*(A_pde(m,x))^n)+(n*k*B_pde(m,x)));
            B_pde(m+1,x)=B_pde(m,x)+delta_t*((d*((B_pde(m,x+1))+(B_pde(m,x-1))-2*(B_pde(m,x)))/((delta_x)^2))+(k*(A_ode(m))^n)-(k*B_ode(m)));
        end
          
    end  
    
end
    
 B_over_time=transpose(mean(B_pde,2))   
 plot(B_over_time)




