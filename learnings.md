<!-- docker db commands -->
to create container:
docker run --name xyz-db -e POSTGRES_USER=xyz -e POSTGRES_PASSWORD=xyz -p 5432:5432 -d postgres:16

to check if it was a success: docker ps (and see if status is UP)