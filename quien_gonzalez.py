from neo4j import GraphDatabase
from pyvis.network import Network

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a"))

# Define the Cypher query
cypher_query = """
MATCH (node)-[r]-(n)
WHERE node.id =~ 'John Gonzalez'
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
    "organization": "#1f78b4",
    "company": "#b15928",
    "person": "#fb9a99",
    "political_organization": "#a6cee3",
    "vessel": "#b2df8a",
    "location": "#6a3d9a",
    "notype": "#fdbf6f",
    "event": "#ff7f00",
    "movement": "#cab2d6"
}


leads_color = {
    "Mar de la Vida OJSC": "navy",
    "979893388": "navy",
    "Oceanfront Oasis Inc Carriers": "navy",
    "8327": "navy"
}


# Add nodes and edges to the network
for source, source_type, target, target_type, relation_type in graph_data:
    if source in leads_color:
        network.add_node(source, title=source_type, color=leads_color[source], shape="star")
    else:
        if "illegal" in source.lower():
            network.add_node(source, title=source_type, shape="image",image="https://purepng.com/public/uploads/large/purepng.com-pirate-flagpirateact-of-robberycriminalviolenceshipboatattackerspirates-1421526962232bovj5.png ")
        if "john gonzalez" in source.lower():
            network.add_node(source, title=source_type, shape="image",image="https://www.pngall.com/wp-content/uploads/13/Futurama-PNG-File.png")
        else:
            network.add_node(source, title=source_type, color=node_colors.get(source_type, "gray"))
    
    if target in leads_color:
        network.add_node(target, title=target_type, color=leads_color[target], shape="star")
    else:
        if "illegal" in target.lower():
            network.add_node(target, title=target_type, shape="image",image="https://purepng.com/public/uploads/large/purepng.com-pirate-flagpirateact-of-robberycriminalviolenceshipboatattackerspirates-1421526962232bovj5.png ")
        if "john gonzalez" in target.lower():
            network.add_node(target, title=target_type, shape="image",image="https://www.pngall.com/wp-content/uploads/13/Futurama-PNG-File.png")

        else:
            network.add_node(target, title=target_type, color=node_colors.get(target_type, "gray"))
    
    network.add_edge(source, target, title=relation_type)

# Visualize the network
network.show("8_quien_gonzalez.html")

# Close the Neo4j driver connection
driver.close()




