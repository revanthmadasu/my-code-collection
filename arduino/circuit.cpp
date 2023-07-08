byte pin[] = {2, 3, 4, 5, 6, 7, 8, 9};//arduino pin array
 
int number[9][8] = {//number array
  {1, 1, 0, 0, 0, 1, 1, 1},//1
  {0, 0, 1, 0, 0, 0, 1, 0},//2
  {1, 0, 0, 0, 0, 0, 1, 0},//3
  {1, 1, 0, 0, 0, 1, 0, 0},//4
  {1, 0, 0, 0, 1, 0, 0, 0},//5
  {0, 0, 0, 0, 1, 0, 0, 0},//6
  {1, 1, 0, 0, 0, 0, 0, 1},//7
  {0, 0, 0, 0, 0, 0, 0, 0},//8
  {1, 1, 0, 0, 0, 0, 0, 0},//9
};
 
void setup() {
  for (byte a = 0; a < 8; a++) {
    pinMode(pin[a], OUTPUT);//define output pins
  }
}
 
void loop() {
  for (int a = 0; a < 9; a++) {
    for (int b = 0; b < 8; b++) {
      digitalWrite(pin[b], number[a][b]);//display numbers
    }
    delay(500);//delay
  }
}