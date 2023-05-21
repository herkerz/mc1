from neo4j import GraphDatabase
from pyvis.network import Network

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a"))

# Define the Cypher query
cypher_query = """
MATCH (node)-[r:ownership|membership|partnership|family_relationship]-(n)
WHERE (node:organization OR node:company OR node:person OR node:political_organization OR node:vessel OR node:location OR node:notype)
  AND (n:organization OR n:company OR n:person OR n:political_organization OR n:vessel OR n:location OR n:notype)
  AND node.id IN ["Mar de la Vida OJSC", "979893388", "Oceanfront Oasis Inc Carriers", "8327"]
RETURN node, r, n
"""

# Execute the query and retrieve the graph data
with driver.session() as session:
    result = session.run(cypher_query)
    graph_data = [(record["node"]["id"], record["n"]["id"], record["r"].type) for record in result]

# Create a Pyvis Network object
network = Network(height="500px", width="100%", notebook=True)

# Add nodes and edges to the network
for source, target, relation_type in graph_data:
    network.add_node(source)
    network.add_node(target)
    network.add_edge(source, target, title=relation_type)

# Visualize the network
network.show("graph.html")

# Close the Neo4j driver connection
driver.close()
