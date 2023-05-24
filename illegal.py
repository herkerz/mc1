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
    "organization": "#a6cee3",
    "company": "#a6cee3",
    "person": "#a6cee3",
    "political_organization": "#a6cee3",
    "vessel": "#a6cee3",
    "location": "#a6cee3",
    "notype": "#a6cee3",
    "event": "#a6cee3",
    "movement": "#a6cee3"
}


leads_color = {
    "Mar de la Vida OJSC": "navy",
    "979893388": "green",
    "Oceanfront Oasis Inc Carriers": "orange",
    "8327": "purple"
}


# Add nodes and edges to the network
for source, source_type, target, target_type, relation_type in graph_data:
    if source in leads_color:
        network.add_node(source, title=source_type, color=leads_color[source], shape="star")
    else:
        if "illegal" in source.lower():
            network.add_node(source, title=source_type, shape="image",image="https://purepng.com/public/uploads/large/purepng.com-pirate-flagpirateact-of-robberycriminalviolenceshipboatattackerspirates-1421526962232bovj5.png ")
        else:
            network.add_node(source, title=source_type, color=node_colors.get(source_type, "gray"))
    
    if target in leads_color:
        network.add_node(target, title=target_type, color=leads_color[target], shape="star")
    else:
        if "illegal" in target.lower():
            network.add_node(target, title=target_type, shape="image",image="https://purepng.com/public/uploads/large/purepng.com-pirate-flagpirateact-of-robberycriminalviolenceshipboatattackerspirates-1421526962232bovj5.png ")
        else:
            network.add_node(target, title=target_type, color=node_colors.get(target_type, "gray"))
    
    network.add_edge(source, target, title=relation_type)

# Visualize the network
network.show("5_illegal.html")

# Close the Neo4j driver connection
driver.close()
