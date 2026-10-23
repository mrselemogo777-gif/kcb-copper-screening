import streamlit as st
from datetime import datetime
from pathlib import Path
from ui.components import inject_css, hero, section, footer

st.set_page_config(page_title="Contact — KCB", page_icon="📬", layout="wide")
inject_css()
hero()

section("📬 Contact")
st.markdown(
    "Questions, feedback, or collaboration on **KCB Copper Target Screening**."
)

# Author block 
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("### 👤 Author")
    st.markdown(
        "**Legakwa Selemogo**\n\n"
        "Independent ML researcher · Botswana\n\n"
        "_Building decision-support tools for health, climate, and minerals in Africa._"
    )
    st.markdown(
        "[GitHub](https://github.com/mrselemogo777-gif) · "
        "[Email](mailto:Mrselemogo777@gmail.com)"
    )
with col2:
    st.markdown("### ✉️ Send a message")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name", placeholder="Jane Doe")
        email = st.text_input("Your email", placeholder="jane@example.org")
        org = st.text_input(
            "Organisation (optional)",
            placeholder="University / NGO / Mining company / Government",
        )
        topic = st.selectbox(
            "Topic",
            [
                "General question",
                "Data partnership",
                "Methodology feedback",
                "Deployment support",
                "Collaboration proposal",
            ],
        )
        message = st.text_area(
            "Message",
            placeholder="Briefly describe your question or proposal...",
            height=140,
        )
        submitted = st.form_submit_button("Send message ➤", use_container_width=True)

    if submitted:
        if not name or not email or not message:
            st.warning("Please fill in name, email, and message.")
        else:
            # Local log one row per submission
            log = Path("data") / "contact_log.csv"
            log.parent.mkdir(exist_ok=True)
            new = not log.exists()
            import csv
            with open(log, "a", newline="") as f:
                w = csv.writer(f)
                if new:
                    w.writerow(["timestamp", "name", "email", "org", "topic", "message"])
                w.writerow([
                    datetime.utcnow().isoformat(timespec="seconds"),
                    name, email, org, topic, message,
                ])
            st.success("Thank you — your message has been logged.")
            mailto = (
                f"mailto:Mrselemogo777@gmail.com"
                f"?subject=KCB%20Contact%20—%20{topic.replace(' ', '%20')}"
                f"&body=From%3A%20{name}%20({email})%0AOrg%3A%20{org}%0A%0A{message.replace(chr(10), '%0A')}"
            )
            st.link_button("Or open in your mail client", mailto)

# Collaboration list 
section("🤝 Collaboration")
st.markdown(
    """
I am open to:

- **Field validation** of this tool with geological teams in Botswana
- **Data partnerships** with mining companies, exploration groups, or government surveys
- **Methodology feedback** from economic geologists and sediment-hosted Cu specialists
- **Deployment support** for EICB and partner organisations
"""
)

footer()