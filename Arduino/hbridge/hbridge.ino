
#define in1 2
#define in2 4
#define enA 9
void setup() {
  // put your setup code here, to run once:

pinMode(in1, OUTPUT);
pinMode(in2, OUTPUT);
pinMode(enA, OUTPUT);
digitalWrite(in1, LOW);
digitalWrite(in2, HIGH );
analogWrite(enA, 255);
}

void loop() {
  // put your main code here, to run repeatedly:


}
