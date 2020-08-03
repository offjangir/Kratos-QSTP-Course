// CHANGING THE BRIGHTNESS ON LDR WILL CHANGE THE SPEED OF MOTOR
int ldr = A0; //TAKING ANALOG INPUT USING PIN A0
int dcmotor = 3;//USING PIN 3 TO CONTROL SPEED OF MOTOR
/*------------------------------------------------*/
void setup()
{ //SERRING PINMODE
    pinMode(ldr,INPUT);
    pinMode(dcmotor,OUTPUT);
  
}
/*-------------------------------------------------*/
void loop()
{   int ldrval = analogRead(ldr);//READING VALUE FROM PIN
    ldrval = constrain(ldrval,10,670);// CONSTRAINING THE VALUE IN NEARBY RANGE
    int ldrmap = map(ldrval,10,670,0,255);//MAPPING THE VALUE FOR MOTOR
    analogWrite(dcmotor,ldrmap);//GIVING OUTPUT ON MOTOR
}
/*-------------------------------------------------*/