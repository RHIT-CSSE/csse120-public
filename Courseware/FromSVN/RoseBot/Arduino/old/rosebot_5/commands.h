#define MAX_COMMAND_DATA_BYTES 4
#define MAX_NUMBER_OF_COMMANDS 8

#define ANALOG_READ 0
#define ANALOG_WRITE 1
#define DIGITAL_READ 2
#define DIGITAL_WRITE 3
#define PIN_MODE 4
#define TONE 5
#define NO_TONE 6
 
typedef struct {
  byte opcode;
  byte number_of_data_bytes;
  byte pin;
  byte value;
  byte opcode_byte;
  byte data_bytes[MAX_COMMAND_DATA_BYTES];
} Command;



