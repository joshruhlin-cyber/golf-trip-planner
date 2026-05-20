import streamlit as st
import anthropic
import os
from tavily import TavilyClient
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.cell.cell import MergedCell
from dotenv import load_dotenv
import io

load_dotenv()

tavily = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

st.title("⛳ Golf Trip Planner")
st.write("Fill out the details below and we'll build your full trip estimate.")

# Input fields
city = st.text_input("Where are you planning to golf?")
dates = st.text_input("What dates? (e.g. Oct 11-13)")
nights = st.number_input("How many nights? (for hotel/accomodation estimates)", min_value=1, max_value=7, value=2)
golfers = st.text_input("How many golfers?")
transport = st.radio("Will you be driving or flying?", ["Drive", "Fly"])
departure = ""
if transport == "Fly":
    departure = st.text_input("What city are you flying from?")
hotel = st.radio("Include hotel pricing?", ["Yes", "No"])

if st.button("🔍 Plan My Trip"):
    if not city or not dates or not golfers:
        st.error("Please fill out all fields before searching.")
    else:
        with st.spinner("Building your trip..."):
            search1 = tavily.search(f"golf courses weekend green fees pricing {city} 2026")
            search2 = tavily.search(f"best public golf courses {city} tee times rates")
            search_text = "\n".join([r["content"] for r in search1["results"] + search2["results"]])

            prompt = f"""
            Based on the following real web search results, put together a golf trip plan for {city} from {dates} for {golfers} golfers.

            SEARCH RESULTS:
            {search_text}

            Please provide exactly 5 golf courses with the following info for each:
            - Course name
            - Weekend green fee per person (low estimate)
            - Weekend green fee per person (high estimate)
            - One sentence description

            Format your response exactly like this for each course:
            COURSE: [name]
            LOW: [number only]
            HIGH: [number only]
            DESC: [one sentence]
            """

            message = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}]
            )
            response_text = message.content[0].text

        # Parse courses
        lines = response_text.split("\n")
        courses = []
        current = {}
        for line in lines:
            if line.startswith("COURSE:"):
                if current:
                    courses.append(current)
                current = {"name": line.replace("COURSE:", "").strip()}
            elif line.startswith("LOW:"):
                try:
                    current["low"] = int(line.replace("LOW:", "").strip())
                except:
                    current["low"] = 0
            elif line.startswith("HIGH:"):
                try:
                    current["high"] = int(line.replace("HIGH:", "").strip())
                except:
                    current["high"] = 0
            elif line.startswith("DESC:"):
                current["desc"] = line.replace("DESC:", "").strip()
        if current:
            courses.append(current)

        # Display golf results
        st.subheader("⛳ Golf Courses")
        for course in courses:
            golfers_int = int(golfers)
            with st.expander(f"{course['name']}"):
                st.write(f"**💰 Green Fee:** \\${course['low']}–\\${course['high']} per person")
                st.write(f"**👥 Group total:** \\${course['low'] * golfers_int:,}–\\${course['high'] * golfers_int:,}")
                st.write(course['desc'])
                course_search = course['name'].replace(' ', '+')
                golfnow_url = f"https://www.golfnow.com/tee-times/search#search/facility-name={course_search}"
                st.markdown(f"[⛳ Check Tee Times on GolfNow]({golfnow_url})")

        flight_info = ""
        if transport == "Fly" and departure:
            with st.spinner("Searching for flights and rental cars..."):
                flight_search = tavily.search(f"flights from {departure} to {city} {dates} 2026 price")
                rental_search = tavily.search(f"rental car {city} airport {dates} 2026 average price")
                flight_text = "\n".join([r["content"] for r in flight_search["results"]])
                rental_text = "\n".join([r["content"] for r in rental_search["results"]])

                flight_prompt = f"""
                Based on these search results, provide estimates for:
                1. Round trip flight cost per person from {departure} to {city} for {dates}
                2. Rental car cost for the trip (total, not per person)

                FLIGHT SEARCH RESULTS:
                {flight_text}

                RENTAL CAR SEARCH RESULTS:
                {rental_text}

                Format exactly like this:
                FLIGHT_LOW: [number only]
                FLIGHT_HIGH: [number only]
                RENTAL_LOW: [number only]
                RENTAL_HIGH: [number only]
                FLIGHT_DESC: [one sentence summary]
                RENTAL_DESC: [one sentence summary]
                """

                flight_message = client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=1024,
                    messages=[{"role": "user", "content": flight_prompt}]
                )
                flight_info = flight_message.content[0].text

            flight_data = {}
            for line in flight_info.split("\n"):
                for key in ["FLIGHT_LOW", "FLIGHT_HIGH", "RENTAL_LOW", "RENTAL_HIGH", "FLIGHT_DESC", "RENTAL_DESC"]:
                    if line.startswith(f"{key}:"):
                        flight_data[key] = line.replace(f"{key}:", "").strip()

            st.subheader("✈️ Flights & Rental Car")

            st.write("**✈️ Flights**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Per person (low)", f"${flight_data.get('FLIGHT_LOW', 'N/A')}")
            with col2:
                st.metric("Per person (high)", f"${flight_data.get('FLIGHT_HIGH', 'N/A')}")
            st.write(flight_data.get('FLIGHT_DESC', '').replace('$', '\\$'))

            st.divider()
            
            st.write("**🚗 Rental Car**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total (low)", f"${flight_data.get('RENTAL_LOW', 'N/A')}")
            with col2:
                st.metric("Total (high)", f"${flight_data.get('RENTAL_HIGH', 'N/A')}")
            st.write(flight_data.get('RENTAL_DESC', '').replace('$', '\\$'))

        hotel_info = ""
        hotels = []
        if hotel == "Yes":
            with st.spinner("Searching for hotels..."):
                hotel_search = tavily.search(f"hotels near golf courses {city} {dates} price per night 2026")
                hotel_text = "\n".join([r["content"] for r in hotel_search["results"]])

                hotel_prompt = f"""
                Based on these search results, provide 3 hotel options near golf courses in {city} for {dates}.

                SEARCH RESULTS:
                {hotel_text}

                Format exactly like this for each:
                HOTEL: [name]
                HOTEL_LOW: [number only, per night]
                HOTEL_HIGH: [number only, per night]
                HOTEL_DESC: [one sentence]
                """

                hotel_message = client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=1024,
                    messages=[{"role": "user", "content": hotel_prompt}]
                )
                hotel_info = hotel_message.content[0].text

            current_hotel = {}
            for line in hotel_info.split("\n"):
                if line.startswith("HOTEL:"):
                    if current_hotel:
                        hotels.append(current_hotel)
                    current_hotel = {"name": line.replace("HOTEL:", "").strip()}
                elif line.startswith("HOTEL_LOW:"):
                    current_hotel["low"] = line.replace("HOTEL_LOW:", "").strip()
                elif line.startswith("HOTEL_HIGH:"):
                    current_hotel["high"] = line.replace("HOTEL_HIGH:", "").strip()
                elif line.startswith("HOTEL_DESC:"):
                    current_hotel["desc"] = line.replace("HOTEL_DESC:", "").strip()
            if current_hotel:
                hotels.append(current_hotel)

            st.subheader("🏨 Hotels")
            for h in hotels:
                with st.expander(f"{h['name']}"):
                    st.write(f"**💰 Room Rate:** \\${h.get('low', 'N/A')}–\\${h.get('high', 'N/A')} per night")
                    try:
                        nights = int(nights)
                        low_total = int(h.get('low', 0)) * nights
                        high_total = int(h.get('high', 0)) * nights
                        st.write(f"**👥 Group total ({nights} nights):** \\${low_total:,}–\\${high_total:,}")
                    except:
                        pass
                    st.write(h.get('desc', ''))

        # Build and offer Excel download
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Golf Trip"
        header_font = Font(bold=True, color="FFFFFF", size=12)
        header_fill = PatternFill(fill_type="solid", fgColor="2E7D32")

        ws["A1"] = f"Golf Trip to {city} | {dates} | {golfers} Golfers"
        ws["A1"].font = Font(bold=True, size=16)
        ws.merge_cells("A1:F1")

        headers = ["Course", "Low Fee/Person", "High Fee/Person", "Low Total (Group)", "High Total (Group)", "Description"]
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=3, column=col, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center")

        for row, course in enumerate(courses, 4):
            golfers_int = int(golfers)
            ws.cell(row=row, column=1, value=course.get("name", ""))
            ws.cell(row=row, column=2, value=f"${course.get('low', 0)}")
            ws.cell(row=row, column=3, value=f"${course.get('high', 0)}")
            ws.cell(row=row, column=4, value=f"${course.get('low', 0) * golfers_int}")
            ws.cell(row=row, column=5, value=f"${course.get('high', 0) * golfers_int}")
            ws.cell(row=row, column=6, value=course.get("desc", ""))

        current_row = len(courses) + 5

        if flight_info:
            ws.cell(row=current_row, column=1, value="FLIGHTS & RENTAL CAR").font = Font(bold=True, size=13)
            current_row += 1
            for col, header in enumerate(["", "Low Estimate", "High Estimate", "", "", "Notes"], 1):
                cell = ws.cell(row=current_row, column=col, value=header)
                cell.font = header_font
                cell.fill = header_fill
            current_row += 1
            ws.cell(row=current_row, column=1, value=f"Flights ({departure} to {city}) per person")
            ws.cell(row=current_row, column=2, value=f"${flight_data.get('FLIGHT_LOW', 'N/A')}")
            ws.cell(row=current_row, column=3, value=f"${flight_data.get('FLIGHT_HIGH', 'N/A')}")
            ws.cell(row=current_row, column=6, value=flight_data.get('FLIGHT_DESC', ''))
            current_row += 1
            ws.cell(row=current_row, column=1, value="Rental Car (total for group)")
            ws.cell(row=current_row, column=2, value=f"${flight_data.get('RENTAL_LOW', 'N/A')}")
            ws.cell(row=current_row, column=3, value=f"${flight_data.get('RENTAL_HIGH', 'N/A')}")
            ws.cell(row=current_row, column=6, value=flight_data.get('RENTAL_DESC', ''))
            current_row += 2

        if hotels:
            ws.cell(row=current_row, column=1, value="HOTELS").font = Font(bold=True, size=13)
            current_row += 1
            for col, header in enumerate(["Hotel", "Low/Night", "High/Night", "", "", "Description"], 1):
                cell = ws.cell(row=current_row, column=col, value=header)
                cell.font = header_font
                cell.fill = header_fill
            current_row += 1
            for h in hotels:
                ws.cell(row=current_row, column=1, value=h.get("name", ""))
                ws.cell(row=current_row, column=2, value=f"${h.get('low', 'N/A')}")
                ws.cell(row=current_row, column=3, value=f"${h.get('high', 'N/A')}")
                ws.cell(row=current_row, column=6, value=h.get("desc", ""))
                current_row += 1

        for col_idx in range(1, 7):
            col_letter = openpyxl.utils.get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = 60 if col_idx == 6 else (35 if col_idx == 1 else 20)

        # Save to memory for download
        buffer = io.BytesIO()
        wb.save(buffer)
        buffer.seek(0)

        st.success("✅ Trip plan complete!")
        st.download_button(
            label="📥 Download Excel",
            data=buffer,
            file_name=f"golf_trip_{city.replace(' ', '_')}_{dates.replace(' ', '_')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )