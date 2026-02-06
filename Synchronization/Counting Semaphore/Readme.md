 Counting Semaphore

Implementation of a Counting semaphore to control access to a shared resource among multiple threads. In this counter variable is set to specific or unrestricted value, that value 
decides how many processes can execute critical section, but remember that these processes will 
be independent of each other. When each process enters critical section, it will decrease the 
counter value until it reaches 0 and beyond that process/thread will go to waiting list. In my code i used the counting semaphore limit upto 3, and there are total of 6 threads including short and long tasks, when any 3 of the total threads acquire the lock they decrement the value of semaphore to 0  then the other remaining threads will not be able to acquire it and will be automatically blocked but when 1 thread exits the crtical section it will update the semaphore value to 1 allowing the other waiting/blocked  thread to acquire lock. So OS uses FIFO agoritham that which one thread should be the next to enter critical section. When all 6 threads exit there critical section then the semaphore value be incremented again upto 3 
