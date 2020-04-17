# Data manipulation in Cypher

```shell script
# find nodes without label
match (n)
where size(labels(n)) = 0
return n

# create node with defined label
create (n:Label{name: 'Non-existing label'})
return n

# create relationship between 2 nodes
match (n1:Label), (n2:Label)
where n1.name = "Non-existing" and n2.name = "Non-existing Part 2"
create (n1)-[:REL_TYPE]->(n2)

# create relationship in one-liner
create p = ((n1:Label{name: "n1"})<-[:REL_TYPE]-(n2:Label{name: "n2"}))
return p

# delete single node
match (n)
where size(labels(n)) = 0 
delete n

# set needed properties
match (n1:Label)
where n1.name = "Non-existing"
set n1.is_true = true, n1.to_delete = false

# delete a property via assigning to null
match (n1:Label)
where n1.name = "Non-existing"
set n1.is_true = NULL, n1.to_delete = NULL

# set properties similar to other node's properties
match (n1:Label), (real_ent:Label)
where n1.name = "Non-existing" and real_ent.id = '1'
set n1 = real_ent

# set label to node
match (n1:Label)
set n1:OtherLabel

# remove label from node
match (n1:Label)
remove n1:OtherLabel

# remove property from node
match (n1:Label)
remove n1.is_true

# merge - returns if exists otherwise creates
merge (n1:Label{name: 'Non-existing', other_prop: 'X'})
return n1

# merge relationships
match (n1:Entity{name: 'Non-existing'})--(n2:Entity)
merge (n1)-[r:SAME_NAME_AS]-(n2)
return r

# foreach - iterator to set properties \ labels
match p=((n1:Label)-[]-(n2:Label))
where n2.name = "Non-existing"
foreach (n in nodes(p)| set n.is_true = false)

# detach and delete relationships
match p=((n1:Label)-[r]-(n2:Label))
where n2.name = "Non-existing"
detach delete r

# find by internal id and delete
match (n1:Label)
where ID(n1) > number
delete n1

# indexes to speed up reads
create index on :Label(property)
drop index on :Label(property)

# add constraints - checks for uniqueness
create constraint on (n:Label)
assert n.property is unique

drop constraint on (n:Label)
assert n.property is unique

# apoc commands
apoc.import.graph('file_path', )

# import csv
load csv with headers from 'file_path.csv | http://file.csv'
as csvLine
match()
merge()
create (n:Node{property: toInt(csvLine.property)})
```
