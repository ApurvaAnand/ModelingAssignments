function [] = MAPK()


% m=4;
kRAS=0.5;
GDPRAS=4;
a1=2;
RAS=5;
a2=3;
b1=nchoosek(GDPRAS,a1);
b2=nchoosek(RAS,a2);

%EGF=0
%EGFR=1
%GRB2=2
%SOS=3
%RAS=4
%GDP-RAS
%RAS_GTP=5
%RAF=6
%MEK=7
%MAPK=8
%CREB=9
%S6=10
%MYC=11

N=16
N_states=[];

for i=1:N
    N_states(i)=0;
end

time=0;
next=0;

for i=1:50
    t_min=10000;
    
    for j=1:N
        if (N_states(j)==0)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
                
            end 
        end
        if  (N_states(j)==1)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            if tij<t_min
                t_min=tij;
                next=j;
                
            end
        end
        
        if (N_states(j)==2)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
            end
        end
         if (N_states(j)==3)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
            end
         end
        if (N_states(j)==4)
            lambda_ij=kRAS*b1*b2;
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
            end
        end
        
        if (N_states(j)==5)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
            end
        end
        
        if (N_states(j)==6)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
            end
        end
        
        if (N_states(j)==7)
            lambda_ij=rand(1);
            tij=exprnd(1/lambda_ij);
            
            if tij<t_min
                t_min=tij;
                next=j;
            end
        end
        
       
        if (N_states(j)==8)
            lambda_ij_1=rand(1);
            lambda_ij_2=rand(1);
            lambda_ij_3=rand(1);
            tij_1=exprnd(1/lambda_ij_1);
            tij_2=exprnd(1/lambda_ij_2);
            tij_3=exprnd(1/lambda_ij_3);
            
            if tij_1<t_min
                t_min=tij_1;
                next=j;
                future_state=9;
                
            end
            if tij_2<t_min
                t_min=tij_2;
                next=j;
                future_state=10;
                
            end
            if tij_3<t_min
                t_min=tij_3;
                next=j;
                future_state=11;
            end
            
        end
        
    end
    if N_states(next)==0
        N_states(next)=1;
    elseif N_states(next)==1
        N_states(next)=2;
    elseif N_states(next)==2
        N_states(next)=3;
    elseif N_states(next)==3
        N_states(next)=4;
    elseif N_states(next)==4
        N_states(next)=5;
    elseif N_states(next)==5
        N_states(next)=6;
    elseif N_states(next)==6
        N_states(next)=7;
    elseif N_states(next)==7
        N_states(next)=8;
    elseif N_states(next)==8
        N_states(next)=future_state;
        
    end
    time=time+t_min;
    check=sum(N_states==0);
    
    
end
time
N_states
end
