//THIS CODE IS CREATED AS AN ALARM SYSTEM 
//FIRST OF ALL I REQUEST TO PRESS THE BUTTON WHILE 
//REGISTERING THE INPUT FOR 1-2 SECONDS IN ORDER TO 
//REGISTER THE INPUT ON LED
//IF SOMEONE COMES IN RANGE OF 3 METER TO THE GATE IT WILL TICK THE ALARM
//AFTER THAT USER NEEDS TO PROVIDE A BUTTON SEQUENCE TO GIVE A PASSWORD
//FOR THIS CASE THE PASSWORD IS 1010 I.E 10
//USER CAN RESET THE PASSWORD AND TRY AGAIN IF INPUT IS WRONG
//THANKYOU
//PASSWORD - 1010
int speaker = 12; 
int i ;
int alarm = 523;
int switchpin[] = {13,7,4,2,6};
int ledpin[] = {0,1,8,11};
int pin ;
int password[] = {0,0,0,0};
int pass = 0;
const int trigPin = 9;
const int echoPin = 10;
float duration, distance; 
/*	 THIS FUNCTION WILL CONTROL THE ULTRASONIC AND GIVE BACK THE DISTANCE*/
int ultradis(){
	digitalWrite(trigPin, LOW); 
	delayMicroseconds(2); 
	digitalWrite(trigPin, HIGH); 
	delayMicroseconds(10); 
	digitalWrite(trigPin, LOW);
  
	duration = pulseIn(echoPin, HIGH);
 
	distance = (duration*.0343)/2;

return distance;}
/*THIS FUNCTION IS FOR RESET BUTTON ON THE LEFT*/
void reset(){
	for(i = 0 ; i<4; i++){
    	digitalWrite(ledpin[i],LOW);}
	for(i = 0 ; i<4; i++){
    	password[i] = 0;}
  	pass = 0;

}
/* THIS FUNCTION WILL CHECK IF THE KEY PRESSED BY BUTTONS CHECKS OUT THE PASSWORD AND STOPS THE ALARM*/
int enterpassword(){
	if((digitalRead(switchpin[0])== HIGH ))
  		{ password[0] = 1;
   		digitalWrite(ledpin[0],HIGH);}
  	if((digitalRead(switchpin[2])== HIGH ))
  		{password[2] = 1;
  		digitalWrite(ledpin[2],HIGH);}
  	if((digitalRead(switchpin[1])== HIGH ))
  		{password[1] = 1;
   		digitalWrite(ledpin[1],HIGH);}
  	if((digitalRead(switchpin[3])== HIGH ))
  		{password[3] = 1;
   		digitalWrite(ledpin[3],HIGH);}
  	if(password[0] == 1 && password[1] == 0 && password[2] == 1 && password[3] == 0)
  		{pin = 1;}
  	else 
    {pin = 0 ;}
return pin;}

/*THIS IS SETUP FUNCTION*/
void setup()
	{for(i = 0 ; i<5; i++){
  		pinMode(switchpin[i],INPUT);}
 	for(i = 0 ; i<4; i++){
  		pinMode(ledpin[i],OUTPUT);
    	digitalWrite(ledpin[i],LOW);}
 	pinMode(trigPin, OUTPUT);
 	pinMode(echoPin, INPUT);
}
/* LOOP FIUCNTION*/
void loop()
{	if((digitalRead(switchpin[4])== HIGH ))//IF RESSETING BUTTON ID PRESSED THE  CODE RESETS
  		{ reset();}
  	distance= ultradis();//CALLING TO GET THE DISTANCE  
   	pass = enterpassword();//CHECKING IF USER ENTERED PASSWORD IS CORRECT OF WRONG
	if(distance < 300 && pass == 0){ 
    	tone(speaker, alarm,500);  
    	delay(1000);
      	}//USING SPEAKER TO GIVE ALARM
}
