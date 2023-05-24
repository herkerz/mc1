from neo4j import GraphDatabase
import csv

# Neo4j connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "a"

# CSV file path
csv_file = "nodes.csv"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'person' THEN [1] ELSE [] END |
    CREATE (n:person)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)

"""

# Connect to Neo4j


# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))


# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'organization' THEN [1] ELSE [] END |
    CREATE (n:organization)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""


# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))
    
    
# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'company' THEN [1] ELSE [] END |
    CREATE (n:company)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))
    

# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'political_organization' THEN [1] ELSE [] END |
    CREATE (n:political_organization)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))
    

# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'vessel' THEN [1] ELSE [] END |
    CREATE (n:vessel)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))


# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'location' THEN [1] ELSE [] END |
    CREATE (n:location)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))
    

# Cypher query to create nodes and relationships
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'notype' THEN [1] ELSE [] END |
    CREATE (n:notype)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))
    
create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'event' THEN [1] ELSE [] END |
    CREATE (n:event)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))

create_query = """
LOAD CSV WITH HEADERS FROM 'file:///{csv_file}' AS row
FOREACH (_ IN CASE WHEN row.type = 'movement' THEN [1] ELSE [] END |
    CREATE (n:movement)
    SET n.type = row.type,
        n.country = row.country,
        n.id = row.id
)
"""

# Open a Neo4j session
with driver.session() as session:
    # Execute the Cypher query to create nodes and relationships
    session.run(create_query.format(csv_file=csv_file))


# Close the Neo4j driver
driver.close()
