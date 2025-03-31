import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load trained models
arctic_model = joblib.load("arctic_model.pkl")
sea_level_model = joblib.load("sea_level_model.pkl")
temperature_model = joblib.load("temperature_model.pkl")

# Load dataset
df = pd.read_csv("climate_data.csv")

# Streamlit App Layout
st.title("🌎 Climate Change Dashboard")

# Filters for Year Range
st.sidebar.header("🔎 Filters")
start_year, end_year = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2000, 2023)
)

# Filtered Data
filtered_df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]

# Climate Trends Section
st.header("📊 Climate Trends Over the Years")
st.write(f"Showing data from **{start_year} to {end_year}**")

# Arctic Ice Chart
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df["Year"], y=filtered_df["Arctic Ice (Million sq km)"], marker="o", color="blue")
ax.set_title("Arctic Ice Over Time")
ax.set_ylabel("Million sq km")
st.pyplot(fig)

st.markdown("---")  # Adds space between charts

# Sea Level Rise Chart
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df["Year"], y=filtered_df["Sea Level Rise (mm)"], marker="o", color="green")
ax.set_title("Sea Level Rise Over Time")
ax.set_ylabel("Sea Level Rise (mm)")
st.pyplot(fig)

st.markdown("---")

# Temperature Anomaly Chart
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df["Year"], y=filtered_df["Temperature Anomaly (°C)"], marker="o", color="red")
ax.set_title("Temperature Anomaly Over Time")
ax.set_ylabel("Temperature Anomaly (°C)")
st.pyplot(fig)

# Predict Future Climate Data
st.header("🔮 Climate Predictions (2025-2050)")
future_years = np.arange(2025, 2051)
future_years_df = pd.DataFrame({"Year": future_years})

# Ensure only expected features are used
features = ["Year"]

# Make Predictions
future_years_df["Arctic Ice (Million sq km)"] = arctic_model.predict(future_years_df[features])
future_years_df["Sea Level Rise (mm)"] = sea_level_model.predict(future_years_df[features])
future_years_df["Temperature Anomaly (°C)"] = temperature_model.predict(future_years_df[features])

# Toggle to Show Predictions Table
if st.checkbox("Show Predictions Table"):
    st.write("### 📅 Predicted Climate Data (2025-2050)")
    st.dataframe(future_years_df)

st.markdown("---")

# Predicted Trends
st.subheader("📈 Future Trends")

# Arctic Ice Predictions
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=future_years_df["Year"], y=future_years_df["Arctic Ice (Million sq km)"], marker="o", color="blue")
ax.set_title("Predicted Arctic Ice")
st.pyplot(fig)

st.markdown("---")

# Sea Level Rise Predictions
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=future_years_df["Year"], y=future_years_df["Sea Level Rise (mm)"], marker="o", color="green")
ax.set_title("Predicted Sea Level Rise")
st.pyplot(fig)

st.markdown("---")

# Temperature Predictions
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=future_years_df["Year"], y=future_years_df["Temperature Anomaly (°C)"], marker="o", color="red")
ax.set_title("Predicted Temperature Anomaly")
st.pyplot(fig)

# Download Predictions
st.download_button(
    label="📥 Download Predictions",
    data=future_years_df.to_csv(index=False),
    file_name="climate_predictions.csv",
    mime="text/csv",
)


