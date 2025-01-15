import streamlit as st

# Use custom styling with Google Fonts (Roboto or Lato)
st.markdown("""
    <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
        
        
        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: "Lucida Console", "Courier New", monospace;
            margin-top: 150px; /* Add some margin-top for vertical space */
        }

        h1 {
            font-size: 7em;
            font-weight: 500;
            margin: 0;
        }

        h2 {
            font-size: 2em;
            font-weight: 500;
            margin: 0;
        }

        h3 {
            font-size: 1.5em;
            font-weight: 400;
            margin: 0;
        }
    </style>
    
    <div class="centered">
        <h1>Welcome</h1>
        <h3>to the</h3>
        <h3>Zomato Data Insights !!</h3>
    </div>
""", unsafe_allow_html=True)
