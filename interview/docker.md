

#### Dockerfile组成

```dockerfile
FROM 
WORKDIR
COPY
RUN
EXPOSE
CMD
```

- **FROM**: Start from a base image. This could be an os like Alpine or Ubuntu, or a known image that contains dependencies for us like databases, or language tools.
- **WORKDIR**: set a working directory inside the container.
- **COPY**: copy the files you need. For simplicity, I copy it all and build inside the container.
- **RUN**: you can add multiple RUN commands, each of them is a simple command to be executed in the terminal, those will run when building the image.
- **EXPOSE**: you can set ports to expose. I chose 8000 since I also use that port in the servers.
- **CMD**: a command to run when starting the container. Sometimes you would see it as an array `CMD ['npm', 'start']`, and sometimes as a command `CMD npm start` - both are accepted.

```dockerfile
# inherit from the Go official Image
FROM golang:1.8

# set a workdir inside docker
WORKDIR /go/src/server

# copy . (all in the current directory) to . (WORKDIR)
COPY . .

# run a command - this will run when building the image
RUN go build -o server

# the port we wish to expose
EXPOSE 8000

# run a command when running the container
CMD ./server
```



#### RUN container

`docker run it -p 8000:8000 containerId`

#### Push to Docker Hub

```shell
# with tag latest
docker tag 294ebde018fe lironavon/my-server

# or with a custom tag
docker tag 8675fc90ccdd lironavon/my-server:v0.1

# with tag latest
docker push lironavon/my-server

# or with a custom tag
docker push lironavon/my-server:v0.1

```



#### Docker Command

```shell
# show a table of all the running containers
docker ps

# show a table of all the local images
docker images

# see more information about a container, you can use its ID or its name.
docker inspect 8675fc90ccdd

# similar to git pull, it pulls image updates
docker pull 8675fc90ccdd

# see logs from a container, useful for debugging
docker logs 8675fc90ccdd

# removes a running container
docker rm 8675fc90ccdd

# removes an image
docker rmi 8675fc90ccdd

# stop a running container
docker stop 8675fc90ccdd
Docker 'ps' command is very strong, it has two nice flags that allows it to mix with other commands easily:

docker ps -q : lists the running containers
docker ps -a -q : lists all the containers
Here are some common use cases for them:

# kill all running containers
docker kill $(docker ps -q)

# remove all running containers
docker rm $(docker ps -a -q)

# remove all images
docker rmi $(docker images -q)
```

