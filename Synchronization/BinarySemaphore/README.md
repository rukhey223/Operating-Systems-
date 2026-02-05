# Binary Semaphore

This folder contains a Python program demonstrating a binary semaphore 
for controlling access to a shared resource between multiple threads. In binary semaphores counter variable ranges from 0 to 1, means only 1 
process can go to critical section and when it is released then the waiting process will enter the 
critical section. That process will again increase the semaphore value. We set this global 
counter to 0 because in binary semaphore it cannot be negative and will be incremented to 1 
when a process enters the critical section. We have thread lock which is the semaphore and only 
one thread can acquire it at a time, which ensures mutual exclusion in the critical section. Also, 
we suppose there are 5 threads
