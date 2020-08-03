int inputint = 3; 
int a;
int motorpin[] = {9,3};
int inputpin[] = {8,7,4,2};
int i;
/*----------------------------------*/
void setup() {
	for(i= 0;i<2;i++){
  		pinMode(motorpin[i],OUTPUT);
  	}
  	for( i = 0;i<4;i++){
    	pinMode(inputpin[i], OUTPUT);
  	}
  	for(i = 0;i<4;i++){
    	digitalWrite(inputpin[i], LOW);
  	}
  	Serial.begin(9600);
  	Serial.println("Press\n 1 for open\n 2 for close\n 3 for stop.");
}
/*-------------------------------------*/
void loop() {
	while(Serial.available()>0)
 	{	a = Serial.parseInt();//WRONG INPUT DETECTION
   		if(a>3 || a <1)
     		Serial.println("Invalid input");
      	else{
       		Serial.println("Valid input");
       		inputint = a;
     			}
    	}
    while(Serial.available()==0)
 	{//CALLING THE FUNCTION FOR CLAW
     claw();
      delay(1000);

    }
 
}
/*------------------------------------------------*/
//THIS FUNCTION WILL TAKE CARE OF THE OPENING AND CLOSEING OF CLAW 
void claw(){
  //PROVIDING SPEED INPUT TO THE MOTORS
	if(inputint == 1 | inputint == 2){
  		analogWrite(motorpin[0], 255);
		analogWrite(motorpin[1], 255);
  	}
  	else{
  		analogWrite(motorpin[0], 0);
		analogWrite(motorpin[1], 0);
    }
  //PROVIDING DIRECTION BASED ON THE INPUT 
	if(inputint == 1){
    	digitalWrite(inputpin[0], HIGH);
		digitalWrite(inputpin[1], LOW);
		digitalWrite(inputpin[2], LOW);
		digitalWrite(inputpin[3], HIGH);
  	}
  	else if(inputint == 2){
  		digitalWrite(inputpin[0], HIGH);
		digitalWrite(inputpin[1], LOW);
		digitalWrite(inputpin[2], HIGH);
		digitalWrite(inputpin[3], LOW);
    }
  	else {
  		digitalWrite(inputpin[0],LOW);
		digitalWrite(inputpin[1], LOW);
		digitalWrite(inputpin[2], LOW);
		digitalWrite(inputpin[3], LOW);
  	}
return ; 
}
/*---------------------------------------------------*/
