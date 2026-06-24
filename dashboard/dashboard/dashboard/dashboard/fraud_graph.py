import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Fraud Network Graph Intelligence")

G = nx.Graph()

G.add_edges_from([
    ("Victim A", "Mule Account 1"),
    ("Victim B", "Mule Account 1"),
    ("Victim C", "Mule Account 2"),
    ("Mule Account 1", "Scammer Hub"),
    ("Mule Account 2", "Scammer Hub")
])

fig, ax = plt.subplots(figsize=(8, 6))

nx.draw(
    G,
    with_labels=True,
    node_size=3000,
    font_size=8,
    ax=ax
)

st.pyplot(fig)