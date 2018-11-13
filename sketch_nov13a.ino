void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  for(int i = 0; i < 1000000; i++)
  {
    digitalWrite(4, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1);                       // wait for a millisecond
    digitalWrite(4, LOW);    // turn the LED off by making the voltage LOW
  //delay(1);  
  }
}
