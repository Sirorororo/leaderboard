import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load leaderboard data from JSON file
def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Display title and QR code
st.title("🏆 Contribution Leaderboard")

max_amount = 140000

# Load and display leaderboard
leaderboard = load_leaderboard()
if leaderboard:

    total_amount = sum(entry["Amount"] for entry in leaderboard)
    # Sort by amount in descending order
    leaderboard.sort(key=lambda x: x["Amount"], reverse=True)

    # Format amounts with commas
    for entry in leaderboard:
        entry["Amount"] = f"{entry['Amount']:,}"

    # Convert to DataFrame and display as a table without index
    df = pd.DataFrame(leaderboard)
    # Display without index
    st.dataframe(df, use_container_width=True,hide_index=True)

else:
    st.warning("Leaderboard is empty. Add data to 'leaderboard.json'.")

col1, col2 = st.columns([5,1])

with col1:
# Data

    remaining_amount = max_amount - total_amount

    # Total collected progress
    st.progress(total_amount / max_amount)

    # Optional: Display the values as text as well
    st.write(f"Total Collected: Rs. {'{:,}'.format(total_amount)}")
    st.write(f"Remaining Amount: Rs. {'{:,}'.format(remaining_amount)}")
with col2:
    st.image("images/esewa_anup.jpg", caption="Scan to Contribute", width=100)
    

