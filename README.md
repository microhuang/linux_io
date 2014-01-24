linux_io
========


//涉及i/o操作
connect()
send()
recv()
sendto()
recvfrom()

//监视I/O的状态，其目的是在I/O可用时，通知用户进行I/O操作，不涉及io操作
select()/poll()/epoll()

//不涉及io操作
socket();  
bind();  
listen();  
accept();  
close();  
shutdown();  
gethostbyname();  
gethostbyaddr();  
htons()、htonl()、ntohs()、ntohl();  
getsockopt()/setsockopt();  
inet_addr()/inet_ntoa();  
