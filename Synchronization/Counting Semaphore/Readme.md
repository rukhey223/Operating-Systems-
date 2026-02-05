 Counting Semaphore

Implementation of a Counting semaphore to control access to a shared resource among multiple threads. In this counter variable is set to specific or unrestricted value, that value 
decides how many processes can execute critical section, but remember that these processes will 
be independent of each other. When each process enters critical section, it will decrease the 
counter value until it reaches 0 and beyond that process will go to waiting list.  
