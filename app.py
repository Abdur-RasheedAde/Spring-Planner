import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Spring Planner",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Spring Planner")
st.subheader(
    "Plan your day using the Lean Impact Matrix"
)

# Storage

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Functions

def calculate_score(impact, ease):

    impact_score = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    ease_score = {
        "Easy": 3,
        "Medium": 2,
        "Hard": 1
    }

    return impact_score[impact] * ease_score[ease]


def get_priority(impact, ease):

    if impact == "High" and ease in ["Easy", "Medium"]:
        return "🚀 Immediate"

    elif impact == "High" and ease == "Hard":
        return "📅 Plan"

    elif impact == "Medium":
        return "🤔 Consider"

    elif impact == "Low" and ease == "Easy":
        return "🤔 Consider"

    else:
        return "❌ Drop"


# Input Section

st.header("Add Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task = st.text_input("Task Name")

with col2:
    impact = st.selectbox(
        "Impact",
        ["High", "Medium", "Low"]
    )

with col3:
    ease = st.selectbox(
        "Ease",
        ["Easy", "Medium", "Hard"]
    )

if st.button("➕ Add Task"):

    if task.strip():

        st.session_state.tasks.append(
            {
                "Task": task,
                "Impact": impact,
                "Ease": ease
            }
        )

        st.success("Task Added")

# Show current queue

if len(st.session_state.tasks) > 0:

    st.subheader("Tasks Waiting For Analysis")

    st.dataframe(
        pd.DataFrame(st.session_state.tasks),
        use_container_width=True
    )

# Analyze

if st.button("📊 Analyze My Day"):

    results = []

    for row in st.session_state.tasks:

        score = calculate_score(
            row["Impact"],
            row["Ease"]
        )

        priority = get_priority(
            row["Impact"],
            row["Ease"]
        )

        results.append(
            {
                "Task": row["Task"],
                "Priority": priority,
                "Matrix Score": score
            }
        )

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="Matrix Score",
        ascending=False
    )

    st.header("🌱 Recommended Task Order")

    st.dataframe(
        df,
        use_container_width=True
    )
