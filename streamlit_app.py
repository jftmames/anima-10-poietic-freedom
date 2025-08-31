import glob
import io
import csv
import networkx as nx
import streamlit as st
from src.pipeline import eval_case
from src.mdl_delta import mdl_delta
from src.network_rupture import rupture_score
from src.lstar import l_star, DEFAULT_WEIGHTS

st.title("ANIMa-10 Poietic Freedom Demo")

case_files = ["" ] + sorted(glob.glob("data/case_files/**/**/*.json", recursive=True))
case_path = st.selectbox("Choose a case file", case_files)

if case_path:
    result = eval_case(case_path)
    st.subheader("Case results")
    st.json(result)

st.header("Manual Example")
pre_text = st.text_area("Pre text", height=150)
post_text = st.text_area("Post text", height=150)
if pre_text and post_text:
    st.write("MDL Δ:", mdl_delta(pre_text, post_text))

pre_edges = st.file_uploader("Pre graph (CSV edge list)", type="csv", key="pre")
post_edges = st.file_uploader("Post graph (CSV edge list)", type="csv", key="post")
if pre_edges and post_edges:
    def load_graph(upload):
        upload.seek(0)
        G = nx.Graph()
        for row in csv.reader(io.StringIO(upload.getvalue().decode("utf-8"))):
            if row and not row[0].startswith('#'):
                G.add_edge(row[0], row[1])
        return G
    G0 = load_graph(pre_edges)
    G1 = load_graph(post_edges)
    st.write("Network rupture:", rupture_score(G0, G1))

st.subheader("L* score")
scores = {k: st.selectbox(k, [0, 1], format_func=lambda x: "Yes" if x else "No") for k in DEFAULT_WEIGHTS}
st.write("L* =", l_star(scores))
