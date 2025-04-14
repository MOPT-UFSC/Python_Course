#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int* random_matrix(int n) {
    int* matrix = malloc(n * n * sizeof(int));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i * n + j] = rand() % 100;
        }
    }

    return matrix;
}


int* matmul(int* m1, int* m2, int n) {
    int* result = malloc(n * n * sizeof(int));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                result[i * n + j] += m1[i * n + k] * m2[k * n + j];
            }
        }
    }

    return result;
}


int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    int* m1 = random_matrix(n);
    int* m2 = random_matrix(n);
    int* result = matmul(m1, m2, n);
    return 0;
}