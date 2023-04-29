#include <stdio.h>

int main() {
    char studentname = "Suriya.M";
    float studentmark = 98.96;
    int studentage = 19;
    printf("Name of the student: %s\nMark of the student: %f\nAge of the student: %i\n", studentname, studentmark, studentage);

    // Decimal precision
    printf("%.3f\n", studentmark);

    // decimal value
    double studentnumber = 12345678901234567890.12;
    printf("%lf\n", studentnumber);
}
