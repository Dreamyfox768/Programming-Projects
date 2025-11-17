from datetime import datetime, timedelta
from streamlit_lightweight_charts import renderLightweightCharts


class ChartBuilder:
    """
    A utility class that transforms mood entries into chart-ready data and renders a mood trend chart.
    """

    mood_map = {
        "Great": 5,
        "Ok": 4,
        "Meh": 3,
        "Not Well": 2,
        "Awful": 1
    }

    @staticmethod
    def preprocess_multiselect(mood_data):
        """
        Converts raw mood entries into numerical values.
        Each entry contains a date and a list of mood labels.
        Mood labels are converted to numbers using mood_map.
        If multiple moods are selected for a day, the function computes the average value.
        Returns a processed list containing:
            { "date": date_object, "mood_value": number or None }
        """
        processed = []

        for entry in mood_data:
            moods = entry["moods"]

            if not moods:
                avg_value = None
            else:
                numeric_values = [
                    ChartBuilder.mood_map[m]
                    for m in moods if m in ChartBuilder.mood_map
                ]
                avg_value = sum(numeric_values) / len(numeric_values)

            processed.append({
                "date": datetime.strptime(entry["date"], "%Y-%m-%d").date(),
                "mood_value": avg_value
            })

        return processed

    @staticmethod
    def build_chart_data(mood_data):
        """
        Builds chart-friendly data for the past 10 days.
        For each day:
            - Finds the most recent mood entry for that day (if any)
            - Uses None if no mood was recorded
        Returns a list of:
            { "time": "YYYY-MM-DD", "value": number or None }
        """
        chart_data = []
        last_10_days = [datetime.now().date() - timedelta(days=i) for i in range(10)][::-1]

        for day in last_10_days:
            day_data = [m for m in mood_data if m["date"] == day]
            value = day_data[-1]["mood_value"] if day_data else None

            chart_data.append({
                "time": str(day),
                "value": value
            })

        return chart_data

    @staticmethod
    def render_mood_chart(chart_data):
        """
        Renders a line chart using lightweight-charts.
        Uses a dark theme with a teal line.
        Expects 'chart_data' produced by build_chart_data().
        """
        chart_options = {
            "height": 300,
            "layout": {
                "background": {"type": "solid", "color": "#131722"},
                "textColor": "#d1d4dc"
            },
            "grid": {
                "vertLines": {"color": "rgba(42, 46, 57, 0)"},
                "horzLines": {"color": "rgba(42, 46, 57, 0.6)"}
            }
        }

        series = [
            {
                "type": "Line",
                "data": chart_data,
                "options": {"lineColor": "#26a69a", "lineWidth": 3}
            }
        ]

        renderLightweightCharts(
            [{"chart": chart_options, "series": series}],
            "moodChart"
        )
