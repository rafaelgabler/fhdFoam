{
     // Defining mathematical functions used in the expressions bellow
       volScalarField    MATH1 = exp(-pow(T/T1-363,2)/12); 
       volScalarField    MATH2 = 1.83e-7*pow(T/T1-310,4.8);  

     forAll(T,i)
     {
     forAll(ID,i)
     {        
     if(ID[i]==0)
     // Expression for the blood perfusion on the healthy region			
     {     
     if(T[i]<=318) // condition for T <= 45°C (Healthy region)
     {        
     W[i]=4.5e-4 + (3.55e-3)*MATH1[i];
     }
     else // condition for T > 45°C (Healthy region)
     {
     W[i] = 4.0e-3;
     }     
     }          
     else
     // Expression for the blood perfusion inside the tumour
     {
     if(T[i]<310) // condition for T < 37°C (Tumour region)
     {
     W[i] = 8.33e-4;
     }
     else
     {
     if(T[i]<=315) // condition for 37°C <= T <= 42°C (Tumour region)
     {
     W[i]= 8.33e-4- MATH2[i];
     }
     else // condition for T > 42°C (Tumour region)
     {
     W[i]=4.16e-4;
     }
     }     
     }      
     }
     }
}
