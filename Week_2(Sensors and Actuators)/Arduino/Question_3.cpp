//SEE THE EFFECT OF BRIGHTNESS ON SERVO MOTOR
#include<Servo.h>//USING SERVO LIBRARY
Servo servo;
int ldr = A0;
/*--------------------------------------*/
void setup()
	{servo.attach(3);//SETTING THE MOTOR ANF LDR TO THE PINS
     pinMode(ldr, INPUT);
	 }
/*---------------------------------------*/
void loop()
	{int ldrval = analogRead(ldr);//READING LDR
     int ldrmap = map(ldrval,6,679,0,180);//MAPPING THE VALUES W.R.T ANGLE
     servo.write(ldrmap);//WRITING THE VALUES TO SERVO
     delay(20);//GIVING A DELAY FOR MOTOR TO TAKE POSITION
	}
/*----------------------------------------*/