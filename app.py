import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Spring Planner",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Spring Planner")
st.subheader(
    "Where Growth Begins"
)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.sidebar.header("Add Task")

task = st.sidebar.text_input("Task Name")

category = st.sidebar.selectbox(
    "Category",
    [
        "Career",
        "Research",
        "Faith",
        "Health",
        "Finance",
        "Family",
        "Learning"
    ]
)

impact = st.sidebar.slider("Impact",1,5,3)
effort = st.sidebar.slider("Effort",1,5,3)
urgency = st.sidebar.slider("Urgency",1,5,3)
goal = st.sidebar.slider("Goal Alignment",1,5,3)

if st.sidebar.button("Add Task"):

    if task != "":

        score = (
            impact * 0.4
            +
            urgency * 0.3
            +
            goal * 0.2
            -
            effort * 0.1
        )

        st.session_state.tasks.append(
            {
                "Task":task,
                "Category":category,
                "Impact":impact,
                "Effort":effort,
                "Urgency":urgency,
                "Goal":goal,
                "Priority Score":round(score,2)
            }
        )

if st.session_state.tasks:

    df = pd.DataFrame(
        st.session_state.tasks
    )

    df = df.sort_values(
        "Priority Score",
        ascending=False
    )

    st.subheader("Today's Priorities")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success(
        f"🌱 Focus First On: {df.iloc[0]['Task']}"
    )

    fig = px.scatter(
        df,
        x="Effort",
        y="Impact",
        text="Task",
        size="Priority Score",
        color="Category",
        hover_name="Task"
    )

    fig.add_vline(
        x=3,
        line_dash="dash"
    )

    fig.add_hline(
        y=3,
        line_dash="dash"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "Add your first task."
    )
