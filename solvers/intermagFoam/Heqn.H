{
                forAll(H,i)
                {
                        const scalar x = mesh.C() [i][0];
//		        const scalar y = mesh.C() [i][1];
//	       		const scalar z = mesh.C() [i][2];


			// linear-gradient applied field no the x direction
		 	H[i][0] = Hmax.value()*x;
			H[i][1] = 0.0;
			H[i][2] = 0.0;			
                }
}


