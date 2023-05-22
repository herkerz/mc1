from neo4j import GraphDatabase
from pyvis.network import Network

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a"))

# Define the Cypher query
cypher_query = """
MATCH (node)-[r]-(n)
WHERE node.id =~ '(?i).*illegal.*'
RETURN node,r ,n
"""

# Execute the query and retrieve the graph data
with driver.session() as session:
    result = session.run(cypher_query)
    graph_data = [(record["node"]["id"], record["node"]["type"], record["n"]["id"], record["n"]["type"], record["r"].type) for record in result]

# Create a Pyvis Network object
network = Network(height="500px", width="100%", notebook=True)

# Define node colors based on source type
node_colors = {
    "organization": "navy",
    "company": "darkgreen",
    "person": "darkorange",
    "political_organization": "red",
    "vessel": "magenta",
    "location": "purple",
    "notype": "darkgrey",
    "event": "cyan",
    "movement": "black"
}

# Add nodes and edges to the network
for source, source_type, target, target_type, relation_type in graph_data:
    network.add_node(source, title=source_type, color=node_colors.get(source_type, "gray"))
    network.add_node(target, title=target_type, color=node_colors.get(target_type, "gray"))
    network.add_edge(source, target, title=relation_type)

# Visualize the network
network.show("illegal.html")

# Close the Neo4j driver connection
driver.close()