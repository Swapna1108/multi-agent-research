import streamlit as st
import requests
from bs4 import BeautifulSoup
from groq import Groq
import os
from dotenv import load_dotenv

import os; 
groq_key = os.getenv('GROQ_API_KEY')

st.set_page_config(
    page_title="ResearchAI",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Inter:wght@300;400;500;600&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background: #0a0a0f !important;
}

.stApp {
    background: #0a0a0f !important;
}

/* Remove white cards */
[data-testid="stVerticalBlock"] > div {
    background: transparent !important;
    padding: 0 !important;
    border-radius: 0 !important;
    backdrop-filter: none !important;
}

/* All text */
p, div, span, label, li {
    color: #e2e8f0 !important;
}

/* Input */
input[type="text"], textarea {
    background: #13131a !important;
    border: 1.5px solid #2d2d3d !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    padding: 14px 18px !important;
    font-size: 0.95rem !important;
    font-family: 'Inter', sans-serif !important;
    width: 100% !important;
}

input[type="text"]:focus {
    border-color: #6d28d9 !important;
    box-shadow: 0 0 0 3px rgba(109,40,217,0.15) !important;
}

/* Select box */
.stSelectbox > div > div {
    background: #13131a !important;
    border: 1.5px solid #2d2d3d !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}

/* Button */
.stButton button {
    background: linear-gradient(135deg, #6d28d9, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    font-family: 'Inter', sans-serif !important;
    width: 100% !important;
    transition: 0.2s !important;
    letter-spacing: 0.02em !important;
}

.stButton button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(109,40,217,0.35) !important;
}

/* Download button */
.stDownloadButton button {
    background: transparent !important;
    border: 1.5px solid #6d28d9 !important;
    color: #a78bfa !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 500 !important;
    width: auto !important;
}

/* Warning */
.stWarning {
    background: rgba(234,179,8,0.1) !important;
    border-left: 3px solid #eab308 !important;
    border-radius: 8px !important;
    color: #fef08a !important;
}

/* Spinner */
.stSpinner > div { border-top-color: #6d28d9 !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #2d2d3d; border-radius: 10px; }

#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── TOP NAVBAR ──
st.markdown("""
<div style='
    background: #0d0d14;
    border-bottom: 1px solid #1e1e2e;
    padding: 1rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2rem;
'>
    <div style='display:flex; align-items:center; gap:0.8rem;'>
        <span style='font-size:1.4rem;'>🔬</span>
        <span style='
            font-family: Cormorant Garamond, serif;
            font-size: 1.6rem;
            font-weight: 600;
            font-style: italic;
            color: #a78bfa;
            letter-spacing: 0.04em;
        '>ResearchAI</span>
    </div>
    <div style='
        font-size: 0.8rem;
        color: #4b5563;
        font-family: Inter, sans-serif;
        letter-spacing: 0.05em;
    '>
        AUTONOMOUS MULTI-AGENT RESEARCH
    </div>
</div>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div style='text-align:center; padding: 3rem 1rem 2.5rem;'>
    <div style='
        display: inline-block;
        background: rgba(109,40,217,0.12);
        border: 1px solid rgba(109,40,217,0.3);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.75rem;
        color: #a78bfa;
        letter-spacing: 0.1em;
        margin-bottom: 1.2rem;
        font-family: Inter, sans-serif;
        font-weight: 500;
    '>
        POWERED BY LLAMA 3.1 · 4 AI AGENTS
    </div>
    <div style='
        font-family: Cormorant Garamond, serif;
        font-size: 4rem;
        font-weight: 600;
        font-style: italic;
        color: #f1f5f9;
        line-height: 1.1;
        margin-bottom: 1rem;
        letter-spacing: 0.02em;
    '>
        Research anything.<br/>
        <span style='color: #a78bfa;'>Instantly.</span>
    </div>
    <div style='
        font-size: 1.05rem;
        color: #64748b;
        font-family: Inter, sans-serif;
        font-weight: 300;
        letter-spacing: 0.02em;
    '>
        Four specialized AI agents collaborate to search, read, analyse,<br/>
        and write comprehensive research reports — automatically.
    </div>
</div>
""", unsafe_allow_html=True)

# ── HOW IT WORKS ──
st.markdown("""
<div style='
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 0 0 3rem;
'>
    <div style='background:#13131a; border:1px solid #1e1e2e; border-radius:16px; padding:1.2rem;'>
        <div style='font-size:1.5rem; margin-bottom:0.5rem;'>🔍</div>
        <div style='font-size:0.75rem; color:#6d28d9; font-weight:600; letter-spacing:0.08em; margin-bottom:0.3rem;'>AGENT 1</div>
        <div style='font-size:0.95rem; color:#e2e8f0; font-weight:500; margin-bottom:0.3rem;'>Search</div>
        <div style='font-size:0.8rem; color:#4b5563; line-height:1.5;'>Finds the most relevant sources across the web</div>
    </div>
    <div style='background:#13131a; border:1px solid #1e1e2e; border-radius:16px; padding:1.2rem;'>
        <div style='font-size:1.5rem; margin-bottom:0.5rem;'>📖</div>
        <div style='font-size:0.75rem; color:#6d28d9; font-weight:600; letter-spacing:0.08em; margin-bottom:0.3rem;'>AGENT 2</div>
        <div style='font-size:0.95rem; color:#e2e8f0; font-weight:500; margin-bottom:0.3rem;'>Reader</div>
        <div style='font-size:0.8rem; color:#4b5563; line-height:1.5;'>Extracts and processes content from each source</div>
    </div>
    <div style='background:#13131a; border:1px solid #1e1e2e; border-radius:16px; padding:1.2rem;'>
        <div style='font-size:1.5rem; margin-bottom:0.5rem;'>🧠</div>
        <div style='font-size:0.75rem; color:#6d28d9; font-weight:600; letter-spacing:0.08em; margin-bottom:0.3rem;'>AGENT 3</div>
        <div style='font-size:0.95rem; color:#e2e8f0; font-weight:500; margin-bottom:0.3rem;'>Analyst</div>
        <div style='font-size:0.8rem; color:#4b5563; line-height:1.5;'>Identifies patterns, themes and key insights</div>
    </div>
    <div style='background:#13131a; border:1px solid #1e1e2e; border-radius:16px; padding:1.2rem;'>
        <div style='font-size:1.5rem; margin-bottom:0.5rem;'>✍️</div>
        <div style='font-size:0.75rem; color:#6d28d9; font-weight:600; letter-spacing:0.08em; margin-bottom:0.3rem;'>AGENT 4</div>
        <div style='font-size:0.95rem; color:#e2e8f0; font-weight:500; margin-bottom:0.3rem;'>Writer</div>
        <div style='font-size:0.8rem; color:#4b5563; line-height:1.5;'>Produces a structured, professional report</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='border-top:1px solid #1e1e2e; margin-bottom:2rem;'></div>", unsafe_allow_html=True)

# ── Session state ──
if "research_done" not in st.session_state:
    st.session_state.research_done = False
if "report" not in st.session_state:
    st.session_state.report = ""
if "sources" not in st.session_state:
    st.session_state.sources = []
if "agent_logs" not in st.session_state:
    st.session_state.agent_logs = []
if "topic_used" not in st.session_state:
    st.session_state.topic_used = ""

# ── Agent Functions ──
def log(msg):
    st.session_state.agent_logs.append(msg)

def search_agent(topic):
    log(f"🔍 Search Agent: Searching for '{topic}'...")
    headers = {"User-Agent": "Mozilla/5.0"}
    query = topic.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}&num=5"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "/url?q=" in href:
                clean = href.split("/url?q=")[1].split("&")[0]
                if clean.startswith("http") and "google" not in clean:
                    links.append(clean)
            if len(links) >= 5:
                break
        log(f"✅ Search Agent: Found {len(links)} sources")
        return links
    except:
        log("⚠️ Search Agent: Using fallback")
        return []

def reader_agent(url):
    log(f"📖 Reader Agent: Reading {url[:50]}...")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        text = " ".join(text.split())[:3000]
        log(f"✅ Reader Agent: Extracted {len(text)} characters")
        return text
    except:
        log(f"⚠️ Reader Agent: Could not read source")
        return ""

def analyst_agent(topic, contents):
    log("🧠 Analyst Agent: Analysing all sources...")
    combined = "\n\n".join([f"Source {i+1}:\n{c}" for i, c in enumerate(contents) if c])
    prompt = f"""You are a research analyst. Based on the following content, extract and organize key information about: {topic}

Content:
{combined[:6000]}

Provide:
1. Key findings (5-7 bullet points)
2. Main themes
3. Important facts and statistics
4. Current trends

Be specific and factual."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    log("✅ Analyst Agent: Analysis complete")
    return response.choices[0].message.content

def writer_agent(topic, analysis):
    log("✍️ Writer Agent: Writing research report...")
    prompt = f"""You are an expert research writer. Write a comprehensive research report about: {topic}

Based on this analysis:
{analysis}

Write a professional report with these exact sections:
# Executive Summary
# Introduction  
# Key Findings
# Detailed Analysis
# Current Trends
# Conclusion

Use clear headings, be detailed and informative. Write at least 500 words."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    log("✅ Writer Agent: Report complete!")
    return response.choices[0].message.content

# ── MAIN INPUT SECTION ──
st.markdown("""
<div style='
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
'>
    <div style='
        font-family: Cormorant Garamond, serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 1.5rem;
    '>
        Start your research
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    topic = st.text_input(
        "topic",
        placeholder="e.g. Latest breakthroughs in quantum computing...",
        label_visibility="collapsed"
    )

with col2:
    depth = st.selectbox(
        "depth",
        ["Quick · 2 sources", "Standard · 3 sources", "Deep · 5 sources"],
        label_visibility="collapsed"
    )

with col3:
    start = st.button("🚀 Start Research")

st.markdown("</div>", unsafe_allow_html=True)

if start:
    if topic.strip():
        st.session_state.research_done = False
        st.session_state.report = ""
        st.session_state.sources = []
        st.session_state.agent_logs = []
        st.session_state.topic_used = topic

        num_sources = 2 if "Quick" in depth else 3 if "Standard" in depth else 5

        with st.spinner("🤖 Agents working on your research..."):
            urls = search_agent(topic)
            urls = urls[:num_sources]
            st.session_state.sources = urls

            contents = []
            for url in urls:
                content = reader_agent(url)
                contents.append(content)

            if contents:
                analysis = analyst_agent(topic, contents)
            else:
                analysis = f"Research on {topic} based on general knowledge."

            report = writer_agent(topic, analysis)
            st.session_state.report = report
            st.session_state.research_done = True
            st.rerun()
    else:
        st.warning("Please enter a research topic first.")

# ── RESULTS ──
if st.session_state.research_done and st.session_state.report:

    # Agent activity + sources row
    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        # Agent logs
        st.markdown("""
        <div style='
            background: #13131a;
            border: 1px solid #1e1e2e;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        '>
            <div style='
                font-size: 0.75rem;
                color: #6d28d9;
                font-weight: 600;
                letter-spacing: 0.08em;
                margin-bottom: 1rem;
            '>AGENT ACTIVITY</div>
        """, unsafe_allow_html=True)

        for log_msg in st.session_state.agent_logs:
            icon_color = "#22c55e" if "✅" in log_msg else "#eab308" if "⚠️" in log_msg else "#a78bfa"
            st.markdown(f"""
            <div style='
                padding: 8px 0;
                border-bottom: 1px solid #1e1e2e;
                font-size: 0.82rem;
                color: {icon_color} !important;
                font-family: Inter, sans-serif;
            '>{log_msg}</div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Sources
        if st.session_state.sources:
            st.markdown("""
            <div style='
                background: #13131a;
                border: 1px solid #1e1e2e;
                border-radius: 16px;
                padding: 1.5rem;
            '>
                <div style='
                    font-size: 0.75rem;
                    color: #6d28d9;
                    font-weight: 600;
                    letter-spacing: 0.08em;
                    margin-bottom: 1rem;
                '>SOURCES</div>
            """, unsafe_allow_html=True)

            for i, url in enumerate(st.session_state.sources):
                domain = url.split("/")[2] if len(url.split("/")) > 2 else url
                st.markdown(f"""
                <div style='
                    padding: 10px 0;
                    border-bottom: 1px solid #1e1e2e;
                '>
                    <div style='font-size:0.75rem; color:#6d28d9 !important; margin-bottom:2px;'>
                        Source {i+1}
                    </div>
                    <div style='font-size:0.82rem; color:#94a3b8 !important; 
                                word-break:break-all; line-height:1.4;'>
                        {domain}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

    with right_col:
        # Report
        st.markdown(f"""
        <div style='
            background: #13131a;
            border: 1px solid #1e1e2e;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1rem;
        '>
            <div style='
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 1.5rem;
                padding-bottom: 1rem;
                border-bottom: 1px solid #1e1e2e;
            '>
                <div style='
                    font-family: Cormorant Garamond, serif;
                    font-size: 1.3rem;
                    font-weight: 600;
                    font-style: italic;
                    color: #e2e8f0;
                '>
                    {st.session_state.topic_used}
                </div>
                <div style='
                    background: rgba(109,40,217,0.15);
                    border: 1px solid rgba(109,40,217,0.3);
                    border-radius: 8px;
                    padding: 4px 12px;
                    font-size: 0.75rem;
                    color: #a78bfa;
                    font-weight: 500;
                '>
                    COMPLETE
                </div>
            </div>
            <div style='
                color: #cbd5e1 !important;
                font-size: 0.92rem;
                line-height: 1.9;
                white-space: pre-wrap;
                font-family: Inter, sans-serif;
            '>
                {st.session_state.report}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Report as .txt",
            data=st.session_state.report,
            file_name=f"research_{st.session_state.topic_used.replace(' ','_')}.txt",
            mime="text/plain"
        )