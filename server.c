/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <errno.h>

#define MAX_EVENTS 64
void error(char *msg)
{
    perror(msg);
    exit(1);
}
int make_socket_non_blocking (int sfd)
{
  int flags, s;

  flags = fcntl (sfd, F_GETFL, 0);
  if (flags == -1)
    {
      perror ("fcntl");
      return -1;
    }

  flags |= O_NONBLOCK;
  s = fcntl (sfd, F_SETFL, flags);
  if (s == -1)
    {
      perror ("fcntl");
      return -1;
    }

  return 0;
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno, clilen;
     char buffer[256];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_STREAM, 0);
     if (sockfd < 0)
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
       make_socket_non_blocking(sockfd);
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
            sizeof(serv_addr)) < 0)
              error("ERROR on binding");

     listen(sockfd,5);
     /*clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
     if (newsockfd < 0)
          error("ERROR on accept");
     bzero(buffer,256);
     n = read(newsockfd,buffer,255);
     if (n < 0) error("ERROR reading from socket");
     printf("Here is the message: %s\n",buffer);
     n = write(newsockfd,"I got your message",18);
     if (n < 0) error("ERROR writing to socket");*/



     struct epoll_event event, events[MAX_EVENTS];;
     int epoll_fd=epoll_create1(0);

     if(epoll_fd == -1)
     {
        perror("Failed to create epoll file descriptor\n");
        return 1;
     }

    event.events = EPOLLIN;
    event.data.fd = sockfd;

    if(epoll_ctl(epoll_fd, EPOLL_CTL_ADD, sockfd, &event))
    {
        perror("Failed to add file descriptor to epoll\n");
        close(epoll_fd);
        return 1;
    }



     for (;;)
     {
        int nfds = epoll_wait(epoll_fd, events, MAX_EVENTS, -1);
        if (nfds == -1)
        {
            perror("epoll_wait");
            exit(EXIT_FAILURE);
        }

        for (int i = 0; i < nfds; i++)
	    {
            if (sockfd == events[i].data.fd)
            {
               newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
                if(newsockfd < 0)
                {
                    perror("accept");
                    continue;
                }
                make_socket_non_blocking(newsockfd);
                event.events = EPOLLIN | EPOLLET;
                event.data.fd = newsockfd;
                if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, newsockfd, &event) < 0)
                {
                    fprintf(stderr, "epoll set insertion error: fd=%d0", newsockfd);
                    return -1;
                }

                printf("New connection\n");
            }
            else
            {
                 bzero(buffer,256);
                 n = read(events[i].data.fd,buffer,255);
                 if (n < 0) error("ERROR reading from socket");

                 if(n>0)
                 {
                    printf("Here is the message: %s\n",buffer);
                    n = write(events[i].data.fd,"I got your message",18);
                 }
                 else
                 {
                    printf("Client closed connection");
                 }
                 if (n < 0) error("ERROR writing to socket");
            }
        }
    }
    if(close(epoll_fd))
    {
        perror("Failed to close epoll file descriptor\n");
        return 1;
    }

    return 0;
}
