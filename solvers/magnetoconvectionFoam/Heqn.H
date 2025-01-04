{
scalar cond = 0.0;
scalar cond2 = 0.0;
scalar cond3 = 0.0;
//scalar cond4 = 0.0;

                forAll(H,i)
                {
                        const scalar x = mesh.C() [i][0];
		        const scalar y = mesh.C() [i][1];
            		const scalar z = mesh.C() [i][2];

				
	if((y<(0.15-(mag_height.value()/2))) || (y>(0.15+(mag_height.value()/2)))) 
	{cond = 0.0;}
	else
	{cond = 1.0;}
	
	if((z>0.125)) 
		{cond2 = 0.0;}
		else
		{cond2 = 1.0;}
		
	if((z<0.075)) 
	{cond3 = 0.0;}
	else
	{cond3 = 1.0;}		
	
	
		
/*	if((z<(0.1-(mag_height.value()/2))) || (z>mag_height.value())) 
	{cond2 = 0.0;}
	else
	{cond2 = 1.0;}	

	if(z> (0.2-mag_height.value())) 
		{cond2 = 1.0;}
		else
		{cond2 = 0.0;}	
	
	if((z> (0.1-(mag_height.value()/2))) || (z<(0.1+(mag_height.value()/2)))) 
		{cond3 = 1.0;}
		else
		{cond3 = 0.0;}								

	if(z<(mag_height.value())) 
		{cond4 = 1.0;}
		else
		{cond4 = 0.0;}		*/						


			// constant-gradient applied field
		 	H[i][0] = Hmax.value()*x*cond*cond2*cond3;
			H[i][1] = 0.0;
			H[i][2] = 0.0;			
// H[i] = vector(Hmax*x*Foam::mathematical::sin(10.0*runTime.value()) , 0., 0.);
                }
}


