
const int  analog_pin = A1;
const int  no_led = 5;
int led[] = {2,3,4,5,6};

//-----------SETUP-----------//
void setup()
{int i = 0;
 while(i< no_led){
   pinMode(led[i],OUTPUT);//SETTING PINMODE
   i++;
 }pinMode(analog_pin,INPUT);
}
//-------------LOOP----------//
void loop()
{int pot_read = analogRead(analog_pin);//READING ANALOG VALUE OF POTENTIOMETER
 int ledlvl = map(pot_read,0,1023,0,no_led);//MAPPING 0-1023 to 0-5 
 int i = 0;//SETTING UP LED  STATE BY LOOP HIGH OR LOW
 while(i<no_led){
   if(i<ledlvl){
     digitalWrite(led[i],HIGH);}
   else digitalWrite(led[i],LOW);
   i++;
 }
} 