{
	forAll(alpha,i)
	{	       
	    alpha[i] = mu0.value()*m.value()* modH[i]/(kb.value()* T[i]);	    
	}    
}
