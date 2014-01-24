//(同步)阻塞模型
//请求/响应模式，阻塞式套接字如果需要实现全双工通迅，意味着程序为每个连接必须存在两个线程。

//server
'''
socket
  |
bind
  |
listen
  |
accept
  |
read/write
  |
close
'''

//client
'''
socket
  |
connect                  
  |
write/read
  |
close
'''


//（同步）非阻塞模型
//通过轮询，如果没有可读取数据内核直接返回未准备就绪的信号，等待用户程序的下一次轮询。

//server
'''
socket
  |
bind
  |
listen
  |
accept
  |
read(null) -> read(null) -> read(null) -> ... read(data)
  |
write(null) -> write(null) -> write(null) -> ... write(data)
  |
close
'''

//client
'''
socket
  |
[设置为非阻塞模式NONBLOCK)]
  |
connect//-1&&EINPROGRESS,0成功
  |
[设置为非阻塞模式NONBLOCK)]
  |
read(null) -> read(null) -> read(null) -> ... read(data)//-1&&EWOULDBLOCK,0成功
  |
write(null) -> write(null) -> write(null) -> ... write(data)//-1&&EWOULDBLOCK,0成功
  |
close
'''


//I/O复用模型
//select、poll、epoll

//server
'''
socket
  |
bind
  |
listen
  |
select  <=============
  |                  |
accept/read/write ====
  |
close
'''

//client
'''
socket
  |
connect
  |
select  <=============
  |                  |
read/write ===========
  |
close
'''


//信号驱动I/O模型



//异步I/O模型
