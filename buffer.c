/* Here's a file with no contents to try */
#include <stdio.h>
#include <string.h>
void vulnerable _function(char *input) {
char buffer[10]; // Small buffer size
strcpy (buffer, input); // Unsafe function: no bounds checking
printf("Buffer content: %s\n", buffer);
}
int main() {
char user_input[100];
printf("Enter some text: *);
fgets(user_input, sizeof(user_input), stdin);
// Remove the newline character from the end of the input
user_input[strcspn(user_input, "\n")] = "\@';
vulnerable_function(user_input);
return 0;
}
