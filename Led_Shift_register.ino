int DS1_pin = 14; // data pin  A0
int STCP1_pin = 15; // Latch   A1
int SHCP1_pin = 16 ; // Clock  A2
String command;
int digits [30][29] {
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //0
  {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //1
  {0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //2
  {0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //3
  {0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //4
  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //5
  {0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  //6
  {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//7
  {0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//8
  {0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//9
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//10
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//11
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//12
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//13
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//14
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//15
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//16
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//17
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//18
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},//19
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},//20
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},//21
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0},//22
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0},//23
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},//24
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0},//25
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},//26
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},//27
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0},//28
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},//29
  /*  {0,1,1,1,1,1,1,0}, // digit
    {0,0,1,1,0,0,0,0}, // digit 1
    {0,1,1,0,1,1,0,1}, // digit 2
    {0,1,1,1,1,0,0,1}, // digit 3
    {0,0,1,1,0,0,1,1}, // digit 4
    {0,1,0,1,1,0,1,1}, // digit 5
    {0,1,0,1,1,1,1,1}, // digit 6
    {0,1,1,1,0,0,0,0}, // digit 7
    {0,1,1,1,1,1,1,1}, // digit 8
    {0,1,1,1,1,0,1,1}  // digit 9*/
};


void display_digit(int d) {
  if (digits[d][0] == 1) {} //A
  if (digits[d][1] == 1) {} //B
  if (digits[d][2] == 1) {} //C
  if (digits[d][3] == 1) {} //D
  if (digits[d][4] == 1) {} //E
  if (digits[d][5] == 1) {} //F
  if (digits[d][6] == 1) {} //G
}

void DisplayDigit(int Digit)
{
  digitalWrite(STCP1_pin, LOW);
  for (int i = 29; i >= 0; i--)
  {
    digitalWrite(SHCP1_pin, LOW);
    if (digits[Digit][i] == 1) digitalWrite(DS1_pin, HIGH);
    if (digits[Digit][i] == 0) digitalWrite(DS1_pin, LOW);
    digitalWrite(SHCP1_pin, HIGH);
  }
  digitalWrite(STCP1_pin, HIGH);
}


void setup() {
  pinMode(DS1_pin, OUTPUT);
  pinMode(STCP1_pin, OUTPUT);
  pinMode(SHCP1_pin, OUTPUT);
}

void loop() {

  delay(500);
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
    command.trim();
    if (command.equals("Amravati")) {
      DisplayDigit (0);
      DisplayDigit (1);
    }
    if (command.equals("Itanagr")) {
      DisplayDigit (0);
      DisplayDigit (2);
    }
    if (command.equals("Dispur")) {
      DisplayDigit (0);
      DisplayDigit (3);
    }
    if (command.equals("Patna")) {
      DisplayDigit (0);
      DisplayDigit (4);
    }
    if (command.equals("Raipur")) {
      DisplayDigit (0);
      DisplayDigit (5);
    }
    if (command.equals("Panaji")) {
      DisplayDigit (0);
      DisplayDigit (6);
    }
    if (command.equals("Gandhinagar")) {
      DisplayDigit (0);
      DisplayDigit (7);
    }
    if (command.equals("Chandigarh")) {
      DisplayDigit (0);
      DisplayDigit (8);
    }
    if (command.equals("Shimla")) {
      DisplayDigit (0);
      DisplayDigit (9);
    }
    if (command.equals("Srinagar")) {
      DisplayDigit (0);
      DisplayDigit (10);
    }
    if (command.equals("Ranchi")) {
      DisplayDigit (0);
      DisplayDigit (11);
    }
    if (command.equals("Bengaluru")) {
      DisplayDigit (0);
      DisplayDigit (12);
    }
    if (command.equals("Trivandrum")) {
      DisplayDigit (0);
      DisplayDigit (13);
    }
    if (command.equals("Bhopal")) {
      DisplayDigit (0);
      DisplayDigit (14);
    }
    if (command.equals("Mumbai")) {
      DisplayDigit (0);
      DisplayDigit (15);
    }
    if (command.equals("Imphal")) {
      DisplayDigit (0);
      DisplayDigit (16);
    }
    if (command.equals("Shillong")) {
      DisplayDigit (0);
      DisplayDigit (17);
    }
    if (command.equals("Aizawl")) {
      DisplayDigit (0);
      DisplayDigit (18);    ///////
    }
    if (command.equals("Jaipur")) {
      DisplayDigit (0);
      DisplayDigit (19);
    }
    if (command.equals("Gangtok")) {
      DisplayDigit (0);
      DisplayDigit (20);
    }
    if (command.equals("Hyderabad")) {
      DisplayDigit (0);
      DisplayDigit (21);
    }
    if (command.equals("Lucknow")) {
      DisplayDigit (0);
      DisplayDigit (22);
    }
    if (command.equals("Dehradun")) {
      DisplayDigit (0);
      DisplayDigit (23);
    }
    if (command.equals("Kolkata")) {
      DisplayDigit (0);
      DisplayDigit (24);
    }
    if (command.equals("Kolkata")) {
      DisplayDigit (0);
      DisplayDigit (25);
    }
    if (command.equals("Kohima")) {
      DisplayDigit (0);
      DisplayDigit (26);
    }
    if (command.equals("Bhubaneswar")) {
      DisplayDigit (0);
      DisplayDigit (27);
    }
    if (command.equals("Jammu")) {
      DisplayDigit (0);
      DisplayDigit (28);
    }
    if (command.equals("Clear")) {
      DisplayDigit (0);
    }
  }
}
