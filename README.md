docker-compose up -d
docker exec -it ${container_id} bash

psql -U postgres < /var/lib/postgresql/dump/restore.sql

psql -U postgres -d dvdrental
CREATE USER test WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE dvdrental TO test;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO test;
