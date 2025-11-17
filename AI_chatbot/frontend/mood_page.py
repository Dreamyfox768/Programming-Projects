import streamlit as st
from datetime import datetime
from database import Database
from chart_builder import ChartBuilder

db = Database()


class MoodPage:
    """
    Renders the mood tracking page.
    Allows the user to select their mood, saves it to the database,
    and displays a 10-day mood trend chart.
    """

    @staticmethod
    def render():
        """
        Builds and displays the full mood tracking interface.
        Handles saving mood entries and generating the chart.
        """

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
