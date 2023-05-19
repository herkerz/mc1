from neo4j import GraphDatabase
import csv

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "PASSWORD"

# CSV file path
csv_file = "links.csv"

# Cypher query to create relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source:Nodos), (target:Nodos)
WHERE source.id = row.source AND target.id = row.target AND row.type = 'ownership'
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
MATCH (source:Nodos), (target:Nodos)
WHERE source.id = row.source AND target.id = row.target AND row.type = 'membership'
CREATE (source)-[:membership]->(target)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))
    
# Cypher query to create relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source:Nodos), (target:Nodos)
WHERE source.id = row.source AND target.id = row.target AND row.type = 'family_relationship'
CREATE (source)-[:family_relationship]->(target)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))


# Cypher query to create relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
MATCH (source:Nodos), (target:Nodos)
WHERE source.id = row.source AND target.id = row.target AND row.type = 'partnership'
CREATE (source)-[:partnership]->(target)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create relationships
    session.run(create_query.format(csv_file=csv_file))
# Close the Neo4j driver
driver.close()
