import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Kitui County Healthcare Dashboard",
    layout="wide",
    page_icon="🏥"
)

sub_counties = [
    "Kitui Central",
    "Kitui West",
    "Kitui Rural",
    "Mwingi North",
    "Mwingi West",
    "Mwingi Central",
    "Kitui South",
    "Kitui East"
]

facilities = [35, 28, 31, 24, 22, 27, 19, 21]
patients = [120000, 95000, 101000, 76000, 71000, 83000, 64000, 69000]
staff = [420, 310, 355, 250, 230, 275, 190, 210]
budget = [450, 360, 390, 280, 250, 300, 220, 240]

health_df = pd.DataFrame({
    "Sub County": sub_counties,
    "Healthcare Facilities": facilities,
    "Annual Patients": patients,
    "Medical Staff": staff,
    "Healthcare Budget (Million KES)": budget
})

disease_df = pd.DataFrame({
    "Disease": [
        "Malaria",
        "Respiratory Infections",
        "Diarrheal Diseases",
        "HIV/AIDS",
        "Hypertension",
        "Diabetes"
    ],
    "Cases": [18500, 14200, 9800, 6200, 5300, 4100]
})

st.sidebar.title("Dashboard Filters")

selected_subcounty = st.sidebar.multiselect(
    "Select Sub Counties",
    options=health_df["Sub County"],
    default=health_df["Sub County"]
)

filtered_df = health_df[health_df["Sub County"].isin(selected_subcounty)]

st.title("🏥 Kitui County Healthcare Services Dashboard")
st.markdown("### Monitoring Healthcare Performance and Service Delivery")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Facilities", int(filtered_df["Healthcare Facilities"].sum()))

with col2:
    st.metric("Annual Patients", f"{filtered_df['Annual Patients'].sum():,}")

with col3:
    st.metric("Medical Staff", int(filtered_df["Medical Staff"].sum()))

with col4:
    st.metric(
        "Budget Allocation",
        f"KES {filtered_df['Healthcare Budget (Million KES)'].sum()}M"
    )

st.divider()

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        filtered_df,
        x="Sub County",
        y="Healthcare Facilities",
        title="Healthcare Facilities by Sub County",
        text_auto=True
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(
        filtered_df,
        names="Sub County",
        values="Annual Patients",
        title="Patient Distribution Across Sub Counties"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

fig3 = px.scatter(
    filtered_df,
    x="Medical Staff",
    y="Annual Patients",
    size="Healthcare Facilities",
    color="Sub County",
    title="Medical Staff vs Annual Patients"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

fig4 = px.bar(
    disease_df,
    x="Disease",
    y="Cases",
    color="Disease",
    title="Common Disease Burden in Kitui County",
    text_auto=True
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

fig5 = go.Figure()

fig5.add_trace(go.Scatter(
    x=filtered_df["Sub County"],
    y=filtered_df["Healthcare Budget (Million KES)"],
    mode='lines+markers',
    name='Budget'
))

fig5.update_layout(
    title="Healthcare Budget Allocation by Sub County",
    xaxis_title="Sub County",
    yaxis_title="Budget (Million KES)"
)

st.plotly_chart(fig5, use_container_width=True)

st.divider()

st.subheader("Healthcare Data Table")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown(
    "**Prepared for Academic Grading Purposes** | Kitui County Healthcare Services Analysis Dashboard"
)
