#include <Servo.h>

Servo servothumb;          
Servo servoindex;          
Servo servomiddle;
Servo servoring;
Servo servopinky;


char number[50];
char c;
int state = 0;
String myStringRec;
int stringCounter = 0;
bool stringCounterStart = false;
String myRevivedString;
int stringLength = 6;

int servoPinky,servoMiddle,servoIndex,servoThumb,servoRing;
int myVals[] ={0,0,0,0,0} ;


void setup() {
  Serial.begin(9600);
  servothumb.attach(9); 
  servoindex.attach(10);  


  delay(500); 
}

void loop() {

receiveData();


if (servoIndex == 2){
  servoindex.write(180);
}
else if (servoIndex == 1){
  servoindex.write(30);
}
else{
  servoindex.write(0);
}

if (servoThumb == 2){
  servothumb.write(180);
}
else if (servoThumb == 1){
  servothumb.write(30);
}
else{
  servothumb.write(0);
}


}

void receiveData() {
  int i = 0;
  while (Serial.available()) {
   char c = Serial.read();
  
    if (c == '$') {
      stringCounterStart = true;
    }
    if (stringCounterStart == true )
    {
      if (stringCounter < stringLength)
      {
        myRevivedString = String(myRevivedString + c);
        stringCounter++;
      }
      if (stringCounter >= stringLength) {
        stringCounter = 0; stringCounterStart = false;
        servoPinky = myRevivedString.substring(5, 6).toInt();
        servoRing = myRevivedString.substring(4, 5).toInt();
        servoMiddle = myRevivedString.substring(3, 4).toInt();
        servoIndex = myRevivedString.substring(2, 3).toInt();
        servoThumb = myRevivedString.substring(1, 2).toInt();   
        Serial.print(servoIndex); 
        myRevivedString = "";
        
      }
    }
  }
}