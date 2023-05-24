from neo4j import GraphDatabase
from pyvis.network import Network
import networkx as nx

# Connect to the Neo4j database
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "a"))

# Define the Cypher query
cypher_query = """
MATCH (node)-[rel1]-(lvl1)-[rel2]-(lvl2)
WHERE (node.id = "Mar de la Vida OJSC" OR
        node.id = "979893388" OR
        node.id = "Oceanfront Oasis Inc Carriers" OR
        node.id = "8327") AND
        (lvl2.id = "Mar de la Vida OJSC" OR
        lvl2.id = "979893388" OR
        lvl2.id = "Oceanfront Oasis Inc Carriers" OR
        lvl2.id = "8327" OR
        lvl1.id = "Mar de la Vida OJSC" OR
        lvl1.id = "979893388" OR
        lvl1.id = "Oceanfront Oasis Inc Carriers" OR
        lvl1.id = "8327")
        AND (node.id <> lvl1.id AND node.id <> lvl2.id AND lvl1.id <> lvl2.id)
RETURN node, rel1, lvl1, rel2, lvl2
"""

# Execute the query and retrieve the graph data
with driver.session() as session:
    result = session.run(cypher_query)
    graph_data = [(record["node"]["id"],record["node"]["type"],record["lvl1"]["id"], record["lvl1"]["type"],record["lvl2"]["id"], record["lvl2"]["type"], record["rel1"].type, record["rel2"].type) for record in result]

# Create a Pyvis Network object
network = Network(height="500px", width="100%", notebook=True, cdn_resources='remote')

# Add nodes and edges to the network
for source, sourcet, level1, level1t, target, targett, rela1, rela2, in graph_data:
    #if source != "979893388" and target != "979893388" and level1 != "979893388" and level2 != "979893388":
    #   if source in ["Mar de la Vida OJSC","979893388","Oceanfront Oasis Inc Carriers","8327"] or target in ["Mar de la Vida OJSC","979893388","Oceanfront Oasis Inc Carriers","8327"]:
        if source == "Mar de la Vida OJSC":
            network.add_node(source,title = sourcet, shape = "star" ,color = "navy")
        elif source == "979893388":
            network.add_node(source,title = sourcet, shape = "star" ,color = "green")
        elif source == "Oceanfront Oasis Inc Carriers":
            network.add_node(source,title = sourcet, shape = "star" ,color = "orange")
        elif source == "8327":
            network.add_node(source,title = sourcet, shape = "star" ,color = "purple")    
        else:
            network.add_node(source, title = sourcet)
        if level1 == "Mar de la Vida OJSC":
            network.add_node(level1,title = level1t, shape = "star" ,color = "navy")
        elif level1 == "979893388":
            network.add_node(level1,title = level1t, shape = "star" ,color = "green")
        elif level1 == "Oceanfront Oasis Inc Carriers":
            network.add_node(level1,title = level1t, shape = "star" ,color = "orange")
        elif level1 == "8327":
            network.add_node(level1,title = level1t, shape = "star" ,color = "purple")    
        else:
            network.add_node(level1,title = level1t)
        if target == "Mar de la Vida OJSC":
            network.add_node(target,title = targett, shape = "star" ,color = "navy")
            network.add_edge(level1, target, title=rela2)
        elif target == "979893388":
            network.add_node(target,title = targett, shape = "star" ,color = "green")
            network.add_edge(level1, target, title=rela2)
        elif target == "Oceanfront Oasis Inc Carriers":
            network.add_node(target,title = targett, shape = "star" ,color = "orange")
            network.add_edge(level1, target, title=rela2)
        elif target == "8327":
            network.add_node(target,title = targett, shape = "star" ,color = "purple")
            network.add_edge(level1, target, title=rela2)
        network.add_edge(source, level1, title=rela1)
        

# Visualize the network
network.show("3_Graph_lvl12.html")

# Close the Neo4j driver connection
driver.close()