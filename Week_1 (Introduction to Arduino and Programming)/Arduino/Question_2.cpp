
int a[] = {0,0,0,0,0}; // THIS ARRAY STORES THE ON-OFF OF THE RESPECTIVE LEDS
int ledpin[5] = {3,5,6,9,10};//TO OPTIMISE THE INITILIZATION OF THE LEDS
int potread =0;//READING OF POTENTIOMETER
int input = 0;//INPUT PROVIDED BY DEFAULT IS 0

//-------------SETUP-----------//
void setup()
{
  Serial.begin(9600);//SERIAL BEGIN
  int i = 0;//SETTING THE PINMODES OF THE DEVELOPMENT BOARD
  while(i<=4){
    pinMode(ledpin[i],OUTPUT);
   i++;}
  pinMode(A1, INPUT);// ANALOG INPUT BY THE POTENTIOMETER
}
//------------LOOP------------//
void loop()
{
 while(Serial.available()>0)//GETTING THE INPUT FROM SERIAL MONITOR
 {
 	input = Serial.parseInt();//PSRDEINT WONT REQUIRE ASCII CORRECTION
 	Serial.println(input);
   if(input>31 || input <0)//PROVIDING ERROR MESSAGE FOR THE WRONG INPUT
     Serial.println("Invalid input");
   else Serial.println("Birnary Representation will be displayed");
 }
 while(Serial.available()==0)
 {	
   	int pot_read = analogRead(A1);
   	int ledlvl = map(pot_read, 0, 1023, 0, 255);//MAPPING OF THE ANALOG INPUT
  	int dummy = input;
	int i = 0;
 	while(i<=4)//STORING THE VALUES OF THE ON OF IN ARRAY
    {
    	a[i] = dummy&1;
      	dummy = dummy >> 1;  
      	i++;
    }
  	i=0;//LIGHITING UP THE RESPECTIVE LEDS
   while(i<=4){
    if(a[i]==1)
      analogWrite(ledpin[i],ledlvl);
    else 
      digitalWrite(ledpin[i],LOW);
     i++;
   }         
 }
}
//-----------------END--------------//