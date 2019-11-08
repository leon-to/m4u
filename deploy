docker container rm -f m4u
docker rmi -f m4u
docker image build -t m4u .
docker container run --publish 8000:8000 --detach --name m4u m4u