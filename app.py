import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Spring Planner",
    page_icon="🌱",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("🌱 Spring Planner")
st.subheader(
    "Stop Managing Tasks. Start Prioritizing Impact."
)

# =====================================================
# SESSION STATE
# =====================================================

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "results" not in st.session_state:
    st.session_state.results = []

# =====================================================
# FUNCTIONS
# =====================================================

def calculate_score(impact, effort):

    impact_score = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    effort_score = {
        "Easy": 3,
        "Medium": 2,
        "Hard": 1
    }

    return impact_score[impact] * effort_score[effort]


def get_priority(impact, effort):

    if impact == "High" and effort == "Easy":
        return "🚀 Immediate"

    elif impact == "High" and effort == "Medium":
        return "🚀 Immediate"

    elif impact == "High" and effort == "Hard":
        return "📅 Plan"

    elif impact == "Medium" and effort == "Easy":
        return "📅 Plan"

    elif impact == "Medium":
        return "🤔 Consider"

    elif impact == "Low" and effort == "Easy":
        return "🤔 Consider"

    else:
        return "❌ Drop"


# =====================================================
# TASK ENTRY
# =====================================================

st.header("➕ Add Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task_name = st.text_input(
        "Task Name"
    )

with col2:
    impact = st.selectbox(
        "Impact",
        ["High", "Medium", "Low"]
    )

with col3:
    effort = st.selectbox(
        "Ease of Execution",
        ["Easy", "Medium", "Hard"]
    )

if st.button("➕ Add Task"):

    if task_name.strip() != "":

        st.session_state.tasks.append(
            {
                "Task": task_name,
                "Impact": impact,
                "Effort": effort
            }
        )

        st.success(f"✅ '{task_name}' added")

# =====================================================
# TASKS PENDING ANALYSIS
# =====================================================

if len(st.session_state.tasks) > 0:

    st.subheader("📋 Tasks Waiting For Analysis")

    st.dataframe(
        pd.DataFrame(st.session_state.tasks),
        use_container_width=True
    )

# =====================================================
# ANALYZE BUTTON
# =====================================================

if st.button("📊 Analyze My Day"):

    results = []

    for task in st.session_state.tasks:

        score = calculate_score(
            task["Impact"],
            task["Effort"]
        )

        priority = get_priority(
            task["Impact"],
      
