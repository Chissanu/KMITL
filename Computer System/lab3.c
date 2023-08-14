#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>

int count;
int sum;
int amount,n_threads;
float m;
int n;
int totalNum;

void *runner(void *arg) {
    int count;

    count = ceil(m/n);
    for (int i = 1; i <= count ; i++) {
        sum += totalNum;
        totalNum -= 1;
    }
    m -= count;
    n -= 1;
    printf("Threads: %d\n" ,n);
    printf("Current sum is %d\n",sum);
}

int main(int argc, char *argv[]) {
    n_threads = atoi(argv[1]);
    amount = atoi(argv[2]);

    if (n_threads > amount) {
        n_threads = amount;
    }
    if (n_threads < 1|| amount < 1) {
        printf("N and M must be at least 1!\n");
        return -1;
    }
    totalNum = amount;
    n = n_threads;
    m = amount;


    pthread_t threads[n_threads];
    int threads_limits[n_threads];

    for (int i = 0; i < n_threads; i++) {
        threads_limits[i] = i;
        pthread_create(&threads[i], NULL, runner, &threads_limits[i]);
        pthread_join(threads[i], NULL);
    }

    printf("The total sum is %d\n", sum);
    return 0;
}