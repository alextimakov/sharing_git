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

# grant privileges

# dump on selected collection
mongodump --authenticationDatabase admin -u user -p password -d db -c collection --archive=/data/storage/tmp/mongodump/db-collection.tgz -v

# restore (Mongo < 4.X.X)
sudo mongorestore --host 0.0.0.0 --authenticationDatabase admin -u username -p password --nsFrom="db.*" --nsTo="new_db.*" --dryRun

# check all open tcp connection to Mongo
sudo lsof | grep mongod | grep TCP

# check all open client connections
db.currentOp(true).inprog.reduce((accumulator, connection) => { ipaddress = connection.client ? connection.client.split(":")[0] : "unknown"; accumulator[ipaddress] = (accumulator[ipaddress] || 0) + 1; accumulator["TOTAL_CONNECTION_COUNT"]++; return accumulator; }, { TOTAL_CONNECTION_COUNT: 0 })

# 
```

```shell script
# useful Mongo requests

``` 