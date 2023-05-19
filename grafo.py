from neo4j import GraphDatabase
from pyvis.network import Network

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a"))

# Define the Cypher query
cypher_query = """
MATCH (node:Nodos)-[r:ownership|membership|partnership|family_relationship]-(n:Nodos)
WHERE node.id = "Mar de la Vida OJSC" OR
	    node.id = "979893388" OR
        node.id = "Oceanfront Oasis Inc Carriers" OR
        node.id = "8327"
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
