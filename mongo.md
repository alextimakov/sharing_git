# Работа с MongoDB

```shell script
# connect to instance
mongo  # if default host:port

# create new user
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: passwordPrompt(), // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

# grant priviliges

# dump on selected collection
mongodump --authenticationDatabase admin -u user -p password -d db -c collection --archive=/data/storage/tmp/mongodump/db-collection.tgz -v

# restore (Mongo < 4.X.X)
sudo mongorestore --host 0.0.0.0 --authenticationDatabase admin -u username -p password --nsFrom="db.*" --nsTo="new_db.*" --dryRun


``` 