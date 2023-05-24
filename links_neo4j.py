from neo4j import GraphDatabase
import csv

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "a"

# CSV file path
csv_file = "links.csv"

# Cypher query to create relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source)
WHERE source.id = row.source AND row.type = 'ownership' AND (source:organization OR source:company OR source:person OR source:political_organization OR source:vessel OR source:location OR source:notype OR source:event OR source:movement)
MATCH (target)
WHERE target.id = row.target AND (target:organization OR target:company OR target:person OR target:political_organization OR target:vessel OR target:location OR target:notype OR target:event OR target:movement)
CREATE (source)-[:ownership]->(target)
"""

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))

# Cypher query to create relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source)
WHERE source.id = row.source AND row.type = 'membership' AND (source:organization OR source:company OR source:person OR source:political_organization OR source:vessel OR source:location OR source:notype OR source:event OR source:movement)
MATCH (target)
WHERE target.id = row.target AND (target:organization OR target:company OR target:person OR target:political_organization OR target:vessel OR target:location OR target:notype OR target:event OR target:movement)
CREATE (source)-[:membership]->(target)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))
    
# Cypher query to create relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source)
WHERE source.id = row.source AND row.type = 'family_relationship' AND (source:organization OR source:company OR source:person OR source:political_organization OR source:vessel OR source:location OR source:notype OR source:event OR source:movement)
MATCH (target)
WHERE target.id = row.target AND (target:organization OR target:company OR target:person OR target:political_organization OR target:vessel OR target:location OR target:notype OR target:event OR target:movement)
CREATE (source)-[:family_relationship]->(target)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))


# Cypher query to create relationships
create_query = """

LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source)
WHERE source.id = row.source AND row.type = 'partnership' AND (source:organization OR source:company OR source:person OR source:political_organization OR source:vessel OR source:location OR source:notype OR source:event OR source:movement)
MATCH (target)
WHERE target.id = row.target AND (target:organization OR target:company OR target:person OR target:political_organization OR target:vessel OR target:location OR target:notype OR target:event OR target:movement)
CREATE (source)-[:partnership]->(target)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))
# Close the Neo4j driver
driver.close()
