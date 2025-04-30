import feedparser
import streamlit as st

my_clients = ["TalkTalk", "Octopus Energy"]
telecom_keywords = ["telecom", "5G", "fiber", "broadband", "AI in telecom", "Ofcom", "BT", "Vodafone"]
regulation_keywords = ["regulation", "policy", "fine", "Ofcom", "EU telecom law"]
investment_keywords = ["funding", "investment", "merger", "startup", "acquisition"]

rss_feeds = [
    "https://www.telecomtv.com/rss/news/",
    "https://www.totaltele.com/rss/news",
    "https://www.lightreading.com/rss",
    "https://www.reuters.com/technology/rss",
    "https://www.ft.com/technology?format=rss"
]

def categorize_article(title, summary):
    content = (title + " " + summary).lower()
    if any(kw.lower() in content for kw in my_clients):
        return "My Clients"
    elif any(kw.lower() in content for kw in regulation_keywords):
        return "Regulations & Policies"
    elif any(kw.lower() in content for kw in investment_keywords):
        return "Tech & AI Investments in Telecom"
    elif any(kw.lower() in content for kw in telecom_keywords):
        return "Industry Cases"
    else:
        return "Other"

st.title("📡 Telecom Intel Tracker")
st.markdown("Filtered news on telecom, regulations, AI investments, and clients.")

category_filter = st.multiselect("Select categories",
                                 ["My Clients", "Regulations & Policies", "Tech & AI Investments in Telecom", "Industry Cases", "Other"],
                                 default=["My Clients", "Regulations & Policies", "Tech & AI Investments in Telecom", "Industry Cases"])

st.write("---")
st.subheader("🗞️ News Feed")

for feed in rss_feeds:
    d = feedparser.parse(feed)
    for entry in d.entries[:10]:
        category = categorize_article(entry.title, entry.summary)
        if category in category_filter:
            st.markdown(f"**[{entry.title}]({entry.link})**  
*{category}*  
{entry.published}")
            st.write(entry.summary[:200] + "...")