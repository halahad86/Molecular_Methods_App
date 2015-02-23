function calculateForm1(){
	var op1=document.getElementById('vol');
	var op2=document.getElementById('M');
	var op3=document.getElementById('MW');
	var result=document.getElementById('res1');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	if(op3.value=="" || op3.value != parseFloat(op3.value)) op3.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=parseFloat(op1.value)*parseFloat(op2.value)*parseFloat(op3.value);
}

function calculateForm2(){
	var op1=document.getElementById('op1');
	var op2=document.getElementById('op2');
	var op3=document.getElementById('op3');
	var result=document.getElementById('res2');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	if(op3.value=="" || op3.value != parseFloat(op3.value)) op3.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=parseFloat(op1.value)/(parseFloat(op2.value)*parseFloat(op3.value));
}

function calculateForm3(){
	var op1=document.getElementById('op4');
	var op2=document.getElementById('op5');
	var op3=document.getElementById('op6');
	var result=document.getElementById('res3');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	if(op3.value=="" || op3.value != parseFloat(op3.value)) op3.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=parseFloat(op1.value)/(parseFloat(op2.value)*parseFloat(op3.value));
}

function calculateForm4(){
	var op1=document.getElementById('op7');
	var op2=document.getElementById('op8');
	var op3=document.getElementById('op9');
	var result=document.getElementById('res4');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	if(op3.value=="" || op3.value != parseFloat(op3.value)) op3.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=parseFloat(op1.value)/(parseFloat(op2.value)*parseFloat(op3.value));
}

function calculateForm5(){
	var op1=document.getElementById('op1');
	var op2=document.getElementById('op2');
	var result=document.getElementById('res');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=parseFloat(op1.value)/parseFloat(op2.value)*100;
}

function calculateForm6(){
	var op1=document.getElementById('op3');
	var op2=document.getElementById('op4');
	var result=document.getElementById('res2');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=parseFloat(op1.value)/parseFloat(op2.value)*100;
}

function calculateForm7(){
	var op1=document.getElementById('op1');
	var op2=document.getElementById('op2');
	var op3=document.getElementById('op3');
	var result=document.getElementById('res');
	
	if(op1.value=="" || op1.value != parseFloat(op1.value)) op1.value=0;
	if(op2.value=="" || op2.value != parseFloat(op2.value)) op2.value=0;
	if(op3.value=="" || op3.value != parseFloat(op3.value)) op3.value=0;
	
	result.value=0;
	result.value=parseFloat(result.value);

	result.value=(parseFloat(op1.value)/parseFloat(op2.value))*parseFloat(op3.value);
}
