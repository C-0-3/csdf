#include <stdio.h>

#include <string.h>

void unsafe_string_copy(char *source) {
char buffer[50]; // Buffer with fixed size
strcpy(buffer, source); // Unsafe function: no bounds checking
printf("Copied string: %s\n", buffer);

}

int main() {
char user_input[100];
printf ("Enter a string: ");
fgets (user_input, sizeof(user_input), stdin);
// Remove the newline character if present
user_input[strespn(user_input, "\n")] = \0';
unsafe_string_copy(user_input);
return 8;

}
