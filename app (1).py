import json
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Agency Agents Directory", page_icon="🤖", layout="wide")

GITHUB_BASE = "https://github.com/msitarzewski/agency-agents/blob/main/"
PAGE_SIZE = 25


@st.cache_data
def load_agents():
    p = Path(__file__).with_name("agents.json")
    return json.loads(p.read_text(encoding="utf-8"))


agents = load_agents()
divisions = sorted({a["division_label"] for a in agents})

st.title("🤖 Agency Agents Directory")
st.caption(
    f"{len(agents)} specialist AI agents from the open-source "
    "[agency-agents](https://github.com/msitarzewski/agency-agents) collection (MIT license). "
    "Search, filter by division, and open any agent to read its full instructions."
)

c1, c2 = st.columns([2, 1])
with c1:
    q = st.text_input("Search", placeholder="e.g. seo, python, bookkeeping…").strip().lower()
with c2:
    div = st.selectbox("Division", ["All"] + divisions)


def matches(a):
    if div != "All" and a["division_label"] != div:
        return False
    if not q:
        return True
    hay = " ".join(
        [a["name"], a["description"], a["vibe"], a["division_label"]] + a["sections"]
    ).lower()
    return all(w in hay for w in q.split())


results = [a for a in agents if matches(a)]
st.write(f"**{len(results)}** agents found")

pages = max(1, (len(results) + PAGE_SIZE - 1) // PAGE_SIZE)
page = st.number_input("Page", min_value=1, max_value=pages, value=1) if pages > 1 else 1
start = (page - 1) * PAGE_SIZE

for a in results[start : start + PAGE_SIZE]:
    with st.expander(f"{a['emoji']} {a['name']} · {a['division_label']}"):
        st.write(a["description"])
        if a["vibe"]:
            st.caption(f"*{a['vibe']}*")
        if a["sections"]:
            st.write("**Covers:** " + ", ".join(a["sections"]))
        with st.expander("View full agent instructions"):
            st.markdown(a["body"])
        st.link_button("Source file on GitHub", GITHUB_BASE + a["source_path"])

st.divider()
st.caption("Data: agency-agents by msitarzewski (MIT). Directory built with Streamlit.")
