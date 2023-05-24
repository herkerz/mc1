from neo4j import GraphDatabase
from pyvis.network import Network
import networkx as nx

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a"))

# Define the Cypher query
cypher_query = """
MATCH (node)-[r:ownership|membership|partnership|family_relationship]-(n)
WHERE node.id = "Mar de la Vida OJSC" OR
	    node.id = "979893388" OR
        node.id = "Oceanfront Oasis Inc Carriers" OR
        node.id = "8327"
RETURN node, r, n
"""

source_color = {
    "Mar de la Vida OJSC":"navy",
    "979893388" : "green",
    "Oceanfront Oasis Inc Carriers":"orange",
    "8327":"purple"
}

# Execute the query and retrieve the graph data
with driver.session() as session:
    result = session.run(cypher_query)
    graph_data = [(record["node"]["id"], record["n"]["id"], record["r"].type) for record in result]

# Create a Pyvis Network object
network = Network(height="500px", width="100%", notebook=True, cdn_resources='remote')

# Add nodes and edges to the network
for source, target, relation_type in graph_data:
    if source == "Mar de la Vida OJSC":
        network.add_node(source,title = source, shape = "star" ,color = source_color.get(source,"gray"))
    elif source == "979893388":
        network.add_node(source,title = source, shape = "star" ,color = source_color.get(source,"gray"))
    elif source == "Oceanfront Oasis Inc Carriers":
        network.add_node(source,title = source, shape = "star" ,color = source_color.get(source,"gray"))
    elif source == "8327":
        network.add_node(source,title = source, shape = "star" ,color = source_color.get(source,"gray"))    
    else:
        network.add_node(source, title = source)
    if target == "Mar de la Vida OJSC":
        network.add_node(target,title = target, shape = "star" ,color = source_color.get(target,"gray"))
    elif target == "979893388":
        network.add_node(target,title = target, shape = "star" ,color = source_color.get(target,"gray"))
    elif target == "Oceanfront Oasis Inc Carriers":
        network.add_node(target,title = target, shape = "star" ,color = source_color.get(target,"gray"))
    elif target == "8327":
        network.add_node(target,title = target, shape = "star" ,color = source_color.get(target,"gray"))    
    else:
        network.add_node(target,title = target)
    network.add_edge(source, target, title=relation_type)

# Visualize the network
network.show("2_Graph_Entities_Ilegal.html")

# Close the Neo4j driver connection
driver.close()