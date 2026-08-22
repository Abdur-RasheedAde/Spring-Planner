import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Spring Planner",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Spring Planner")
st.subheader("Prioritize your day using the Lean Impact Matrix")

# Store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Function to classify tasks
def classify_task(impact, effort):

    if impact == "High" and effort == "Easy":
        return "🚀 Immediate"

    elif impact == "High" and effort in ["Medium", "Hard"]:
        return "📅 Plan"

    elif impact in ["Medium", "Low"] and effort == "Easy":
        return "🤔 Consider"

    else:
        return "❌ Drop"

# Sidebar
st.sidebar.header("Add Task")

task = st.sidebar.text_input("Task Name")

impact = st.sidebar.selectbox(
    "Impact",
    ["High", "Medium", "Low"]
)

effort = st.sidebar.selectbox(
    "Ease of Execution",
    ["Easy", "Medium", "Hard"]
)

if st.sidebar.button("Add Task"):

    if task.strip():

        category = classify_task(
            impact,
            effort
        )

        st.session_state.tasks.append(
            {
                "Task": task,
                "Impact": impact,
                "Effort": effort,
                "Category": category
            }
        )

# Display Results
if st.session_state.tasks:

    df = pd.DataFrame(
        st.session_state.tasks
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    immediate = df[df["Category"]=="🚀 Immediate"]
    plan = df[df["Category"]=="📅 Plan"]
    consider = df[df["Category"]=="🤔 Consider"]
    drop = df[df["Category"]=="❌ Drop"]

    col1.metric("🚀 Immediate", len(immediate))
    col2.metric("📅 Plan", len(plan))
    col3.metric("🤔 Consider", len(consider))
    col4.metric("❌ Drop", len(drop))

    st.divider()

    st.header("🚀 Immediate")

    if len(immediate) > 0:
        st.dataframe(
            immediate,
            use_container_width=True
        )
    else:
        st.info("No Immediate tasks")

    st.header("📅 Plan")

    if len(plan) > 0:
        st.dataframe(
            plan,
            use_container_width=True
        )
    else:
        st.info("No Plan tasks")

    st.header("🤔 Consider")

    if len(consider) > 0:
        st.dataframe(
            consider,
            use_container_width=True
        )
    else:
        st.info("No Consider tasks")

    st.header("❌ Drop")

    if len(drop) > 0:
        st.dataframe(
            drop,
            use_container_width=True
        )
    else:
        st.info("No Drop tasks")

else:

    st.info(
        "Add your tasks from the sidebar to begin planning your day."
    )
