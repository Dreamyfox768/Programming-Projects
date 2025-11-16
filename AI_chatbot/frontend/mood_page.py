# pages/mood_page.py
import streamlit as st
from datetime import datetime
from database import Database
from chart_builder import ChartBuilder

db = Database()

class MoodPage:
    @staticmethod
    def render():
        st.title("Mood Tracker")

        moods = st.multiselect(
            "How are you feeling today?",
            options=["Great", "Ok", "Meh", "Not Well", "Awful"]
        )

        if st.button("Save Mood"):
            db.add_mood(
                date=datetime.now().date(),
                moods=moods
            )
            st.success("Mood saved to database!")

        st.subheader("Mood Trend (last 10 days)")

        raw_data = db.get_moods_last_10_days()
        processed = ChartBuilder.preprocess_multiselect(raw_data)
        chart_data = ChartBuilder.build_chart_data(processed)

        ChartBuilder.render_mood_chart(chart_data)
