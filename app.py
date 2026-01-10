import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Career AI Advisor",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM UI STYLING
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

.stApp {
    font-family: 'Poppins', sans-serif;
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: #e5e7eb;
}

h1 {
    background: linear-gradient(90deg, #38bdf8, #818cf8, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

input, textarea {
    color: #1e40af !important;
    font-weight: 500 !important;
}

div[data-baseweb="input"] > div {
    background: rgba(255,255,255,0.95) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
}

input::placeholder {
    color: #64748b !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #6366f1, #ec4899);
    color: white;
    border-radius: 16px;
    padding: 0.7rem 1.6rem;
    font-weight: 600;
    border: none;
}

.career-card {
    background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.03));
    backdrop-filter: blur(16px);
    border-radius: 22px;
    padding: 1.6rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255,255,255,0.15);
}

.score-bar {
    height: 10px;
    border-radius: 10px;
    background: linear-gradient(90deg, #22d3ee, #818cf8, #ec4899);
    margin-bottom: 1rem;
}

.label {
    color: #c7d2fe;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🎓 Career AI Advisor")
st.caption("AI-inspired career guidance • Edulnnovate hackathon")

# --------------------------------------------------
# CAREER DATA
# --------------------------------------------------
CAREER_DATA = {
    "Software Developer": {"python", "java", "c", "dsa", "problem solving","c++","cpp"},
    "Data Analyst": {"python", "sql", "excel", "statistics", "data analysis"},
    "Cybersecurity Analyst": {"networking", "linux", "security", "python", "cryptography"},
    "AI / ML Engineer": {"python", "machine learning", "math", "statistics", "data","ml",}
}

CAREER_INSIGHTS = {
    "Software Developer": {
        "present": "High demand across startups, product companies, and service-based firms.",
        "future": "Will remain evergreen with growth in AI-assisted development and cloud-native apps.",
        "companies": ["Google", "Microsoft", "Amazon", "Infosys", "TCS", "Zoho"],
        "hackathons": ["Smart India Hackathon", "Google Solution Challenge", "MLH Hackathons"],
        "competitions": ["CodeChef", "LeetCode", "HackerRank"]
    },
    "Data Analyst": {
        "present": "Strong demand in finance, healthcare, e-commerce, and analytics firms.",
        "future": "Demand will grow with data-driven decision making and AI integration.",
        "companies": ["Deloitte", "EY", "Accenture", "Amazon", "Flipkart"],
        "hackathons": ["Analytics Vidhya Hackathons", "Kaggle Days"],
        "competitions": ["Kaggle", "StrataScratch"]
    },
    "Cybersecurity Analyst": {
        "present": "Rising demand due to increasing cyber threats and data breaches.",
        "future": "Critical role as cloud, IoT, and digital payments expand.",
        "companies": ["Cisco", "Palo Alto Networks", "IBM", "Microsoft"],
        "hackathons": ["Cyber Apocalypse", "CTFtime Events"],
        "competitions": ["Hack The Box", "TryHackMe"]
    },
    "AI / ML Engineer": {
        "present": "High demand in AI startups, research labs, and big tech companies.",
        "future": "Explosive growth as AI adoption increases across industries.",
        "companies": ["OpenAI", "Google DeepMind", "Meta", "NVIDIA"],
        "hackathons": ["AI Hackathons", "Kaggle Competitions"],
        "competitions": ["Kaggle", "AIcrowd"]
    }
}

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
st.subheader("🔍 Enter your skills")
user_input = st.text_input(
    label="Your Skills",
    placeholder="Example: Python, SQL, problem solving"
)

# --------------------------------------------------
# PROCESSING CAREER MATCH
# --------------------------------------------------
if st.button("Analyze Career Options 🚀"):

    if user_input.strip() == "":
        st.warning("Please enter at least one skill.")
    else:
        user_skills = {s.strip().lower() for s in user_input.split(",")}
        results = []

        for career, skills in CAREER_DATA.items():
            required = {s.lower() for s in skills}
            matched = user_skills & required
            score = int((len(matched) / len(required)) * 100)
            results.append((career, score, matched, required - matched))

        results.sort(key=lambda x: x[1], reverse=True)

        # Save results to session_state
        st.session_state["career_results"] = results

        st.success("🚀 Top Career Matches")
        for career, score, matched, missing in results[:3]:
            st.markdown(
f"""
<div class="career-card">
  <h3>🎯 {career}</h3>
  <p class="label">Match Score: {score}%</p>
  <div class="score-bar" style="width:{score}%"></div>

  <p><strong>Matched Skills:</strong><br>
  {', '.join(sorted(matched)) if matched else 'None'}</p>

  <p><strong>Skills to Improve:</strong><br>
  {', '.join(sorted(missing)) if missing else 'None'}</p>
</div>
""",
                unsafe_allow_html=True
            )

# --------------------------------------------------
# DEEPER GUIDANCE WITH EXPANDERS
# --------------------------------------------------
if "career_results" in st.session_state:
    results = st.session_state["career_results"]
    st.subheader("🎯 Deeper Career Guidance")
    tabs = st.tabs([career for career, _, _, _ in results[:3]])

    # ---------------- Predefined Links & Details ----------------
    COMPANY_DETAILS = {
        "Google": {"url":"https://careers.google.com/", "desc":"Google Careers: Apply for tech roles and internships."},
        "Microsoft": {"url":"https://careers.microsoft.com/", "desc":"Microsoft Careers: Explore opportunities in cloud, AI, software."},
        "Amazon": {"url":"https://www.amazon.jobs/", "desc":"Amazon Careers: Apply for software, data, and business roles."},
        "Infosys": {"url":"https://www.infosys.com/careers/", "desc":"Infosys Careers: Opportunities in IT and consulting."},
        "TCS": {"url":"https://www.tcs.com/careers", "desc":"TCS Careers: Software, consulting, and tech internships."},
        "Zoho": {"url":"https://www.zoho.com/careers.html", "desc":"Zoho Careers: Join a product-based tech company."},
        "Deloitte": {"url":"https://www2.deloitte.com/global/en/careers.html", "desc":"Deloitte Careers: Analytics, consulting and finance roles."},
        "EY": {"url":"https://www.ey.com/en_gl/careers", "desc":"EY Careers: Audit, consulting, and tech roles."},
        "Accenture": {"url":"https://www.accenture.com/us-en/careers", "desc":"Accenture Careers: IT, consulting, AI and cloud roles."},
        "Flipkart": {"url":"https://www.flipkartcareers.com/", "desc":"Flipkart Careers: E-commerce software and analytics."},
        "Cisco": {"url":"https://jobs.cisco.com/", "desc":"Cisco Careers: Networking, security, and tech roles."},
        "Palo Alto Networks": {"url":"https://www.paloaltonetworks.com/careers", "desc":"Cybersecurity roles at Palo Alto Networks."},
        "IBM": {"url":"https://www.ibm.com/employment/", "desc":"IBM Careers: Software, AI, cloud, and research roles."},
        "OpenAI": {"url":"https://openai.com/careers", "desc":"OpenAI Careers: AI research and engineering."},
        "Google DeepMind": {"url":"https://www.deepmind.com/careers", "desc":"DeepMind Careers: AI and ML research positions."},
        "Meta": {"url":"https://www.metacareers.com/", "desc":"Meta Careers: Software, AI, and product roles."},
        "NVIDIA": {"url":"https://www.nvidia.com/en-us/about-nvidia/careers/", "desc":"NVIDIA Careers: AI, GPU, and software roles."}
    }

    HACKATHON_DETAILS = {
        "Smart India Hackathon": {"url":"https://www.sih.gov.in/", "desc":"India's largest government-led hackathon."},
        "Google Solution Challenge": {"url":"https://developers.google.com/community/dsc/challenges", "desc":"Google DSC challenge for building solutions using Google tech."},
        "MLH Hackathons": {"url":"https://mlh.io/", "desc":"Major League Hacking community hackathons."},
        "Analytics Vidhya Hackathons": {"url":"https://datahack.analyticsvidhya.com/", "desc":"Data science hackathons organized by Analytics Vidhya."},
        "Kaggle Days": {"url":"https://www.kaggle.com/competitions", "desc":"Kaggle competitions for real-world datasets."},
        "Cyber Apocalypse": {"url":"https://www.ctf365.com/", "desc":"Cybersecurity Capture The Flag challenges."},
        "CTFtime Events": {"url":"https://ctftime.org/", "desc":"Global CTF competitions in cybersecurity."},
        "AI Hackathons": {"url":"https://www.hackathon.com/", "desc":"AI-focused hackathons worldwide."},
        "Kaggle Competitions": {"url":"https://www.kaggle.com/competitions", "desc":"AI and ML competitions for all levels."}
    }

    COMPETITION_DETAILS = {
        "CodeChef": {"url":"https://www.codechef.com/contests", "desc":"Competitive programming contests on CodeChef."},
        "LeetCode": {"url":"https://leetcode.com/contest/", "desc":"Weekly coding contests on LeetCode."},
        "HackerRank": {"url":"https://www.hackerrank.com/contests", "desc":"Programming contests on HackerRank."},
        "Kaggle": {"url":"https://www.kaggle.com/competitions", "desc":"Data science competitions on Kaggle."},
        "StrataScratch": {"url":"https://www.stratascratch.com/solutions/", "desc":"Data science problem-solving challenges."},
        "Hack The Box": {"url":"https://www.hackthebox.eu/", "desc":"Cybersecurity challenges platform."},
        "TryHackMe": {"url":"https://tryhackme.com/", "desc":"Learn and compete in cybersecurity labs and challenges."}
    }

    # ---------------- Render tabs with expanders ----------------
    for i, (career, score, matched, missing) in enumerate(results[:3]):
        with tabs[i]:
            insight = CAREER_INSIGHTS[career]

            st.markdown(f"### 📌 Career Guidance: {career}")
            st.markdown(f"**📊 Present Demand:** {insight['present']}")
            st.markdown(f"**🚀 Future Scope:** {insight['future']}")
            st.markdown(f"**🤖 AI Advice:** Focus on real-world projects, internships, and consistent problem-solving.")

            # Function to create expandable details
            def render_modal(label, details):
                with st.expander(label):
                    st.markdown(f"**Description:** {details['desc']}")
                    st.markdown(f"[Go to Website]({details['url']})", unsafe_allow_html=True)

            st.markdown("### 🏢 Companies to Apply:")
            for c in insight['companies']:
                render_modal(c, COMPANY_DETAILS.get(c, {"url":"#","desc":"No details available."}))

            st.markdown("### 🏆 Hackathons to Participate:")
            for h in insight['hackathons']:
                render_modal(h, HACKATHON_DETAILS.get(h, {"url":"#","desc":"No details available."}))

            st.markdown("### 💻 Coding Competitions:")
            for comp in insight['competitions']:
                render_modal(comp, COMPETITION_DETAILS.get(comp, {"url":"#","desc":"No details available."}))

            st.markdown(f"**⚡ Missing Skills:** {', '.join(sorted(missing)) if missing else 'None'}")
            st.info("💡 Click any company, hackathon, or competition to see details without leaving the page.")


from fpdf import FPDF
import base64

if "career_results" in st.session_state:
    results = st.session_state["career_results"]

    if st.button("📄 Download My Career Report PDF"):
        
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Career AI Advisor Report", ln=True, align="C")
        pdf.ln(10)

        for career, score, matched, missing in results[:3]:
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, f"{career} - Match Score: {score}%", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 8, f"Matched Skills: {', '.join(sorted(matched)) if matched else 'None'}")
            pdf.multi_cell(0, 8, f"Skills to Improve: {', '.join(sorted(missing)) if missing else 'None'}")

            insight = CAREER_INSIGHTS[career]
            pdf.multi_cell(0, 8, f"Present Demand: {insight['present']}")
            pdf.multi_cell(0, 8, f"Future Scope: {insight['future']}")
            pdf.multi_cell(0, 8, f"AI Advice: Focus on real-world projects, internships, and consistent problem-solving.")

            pdf.multi_cell(0, 8, f"Companies to Apply: {', '.join(insight['companies'])}")
            pdf.multi_cell(0, 8, f"Hackathons to Participate: {', '.join(insight['hackathons'])}")
            pdf.multi_cell(0, 8, f"Coding Competitions: {', '.join(insight['competitions'])}")
            pdf.ln(5)

        # Save PDF to bytes
        pdf_output = pdf.output(dest='S').encode('latin-1')
        b64 = base64.b64encode(pdf_output).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="career_report.pdf">Click here to download your PDF report</a>'
        st.markdown(href, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption("Made by : Hetvi Siddhpura • email : siddhpurahetvi007@gmail.com • Aspiring AI Learner")
