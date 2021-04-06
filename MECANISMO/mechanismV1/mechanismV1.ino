#define STEP_MT1 4      // pin STEP de A4988 a pin 4
#define DIR_MT1 5     // pin DIR de A4988 a pin 5

int entryByte;

void setup() 
{
  // initialize serial communication:
  Serial.begin(9600);

  
  pinMode(STEP_MT1, OUTPUT);  // pin 4 como salida
  pinMode(DIR_MT1, OUTPUT);   // pin 5 como salida
}

void loop() {
  if(Serial.available() >0){
    entryByte = Serial.read();

    //MOVER ALA DERECHA 1 PASO
    if(entryByte == 'D'){
      digitalWrite(DIR_MT1, HIGH);    // giro en un sentido
      digitalWrite(STEP_MT1, HIGH);       // nivel alto
      delay(10);  
      digitalWrite(STEP_MT1, LOW);       // nivel alto
      delay(10);        
    }
    //MOVER ALA IZQUIERDA UN PASO
    if(entryByte == 'I'){
      digitalWrite(DIR_MT1, LOW);    // giro en SENTIDO OPUESTO
      digitalWrite(STEP_MT1, HIGH);       // nivel alto
      delay(10);  
      digitalWrite(STEP_MT1, LOW);       // nivel alto
      delay(10); 
     
    }
    
  }

}
