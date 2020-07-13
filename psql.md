### psql shell
- exit shell: `\q`
- show users: `\du`
- drop user: `DROP OWNED BY <username>; DROP ROLE <username>;`
- create user: `createuser <username>;`
- show dbs: `\l`
- drop database: `DROP DATABASE <database>;`
- choose database: `\c <database>`
- show tables: `\dt`
```shell script
sudo mkdir /home/shared_folder/postgres_tablespace
sudo chown postgres postgres_tablespace
su - postgres psql
# https://stackoverflow.com/questions/29806332/how-to-get-the-current-free-disk-space-in-postgres
# https://severalnines.com/database-blog/my-postgresql-database-out-disk-space
CREATE TABLESPACE mytspace OWNER postgres LOCATION '/home/shared_folder/postgres_tablespace';
CREATE DATABASE pbi_test WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = mytspace;
CREATE TABLE foo(i int) TABLESPACE mytspace; # optional 
GRANT CONNECT ON DATABASE pbi_test TO selected_user;
GRANT USAGE ON SCHEMA public TO selected_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO selected_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO selected_user;
```