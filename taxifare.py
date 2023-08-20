import streamlit as st

def calculate_taxi_fare(minutes, miles):
    minute_rate = 0.56
    mile_rate = 1.31
    fare = (minute_rate * minutes) + (mile_rate * miles)
    return fare

def main():
    st.title("Taxi Fare Calculator")

    # Input fields for ETA and distance
    eta_minutes = st.number_input("Enter ETA in minutes:", value=0, step=1)
    distance_miles = st.number_input("Enter distance in miles:", value=0.0, step=0.1)

    # Calculate fare
    fare = calculate_taxi_fare(eta_minutes, distance_miles)

    # Display fare and sum of ETA and distance
    st.subheader(f"Taxi Fare: ${fare:.2f}")  

if __name__ == "__main__":
    main()
