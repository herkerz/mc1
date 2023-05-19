from neo4j import GraphDatabase
import csv

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "PASSWORD"

# CSV file path
csv_file = "nodes.csv"

# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
CREATE (n:Nodos)
SET n.type = row.type,
    n.country = row.country,
    n.id = row.id
"""

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))

# Close the Neo4j driver
driver.close()
