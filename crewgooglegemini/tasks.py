from crewai import Task
from tools import tool
from agents import travel_planner, travel_recommender

# สร้างงานสำหรับการวางแผนการเดินทาง
plan_task = Task(
    description=(
        "Develop a comprehensive and optimized travel itinerary "
        "that aligns with the traveler's preferences, budget, and schedule. "
        "The plan should include accommodations, transportation, key attractions, "
        "daily activities, meal recommendations, and contingency options to ensure "
        "a smooth and enjoyable trip in {province}, Thailand. for {days} days with a budget of {budget} THB"
    ), 
    expected_output=(
        "A detailed, well-structured travel itinerary that includes daily schedules, "
        "accommodation details, transport options, activity recommendations, estimated costs, "
        "and alternative plans for unforeseen circumstances."
    ), 
    tools=[tool],
    agent=travel_planner,
)


# สร้างงานสำหรับการแนะนำการเดินทาง
recommend_task = Task(
    description=(
        "Curate a well-researched and personalized list of recommended "
        "destinations, accommodations, activities, and dining options "
        "that align with the traveler's interests, budget, and travel style. "
        "Each recommendation should include key details, highlights, and reasons "
        "why it suits the traveler, ensuring a unique and memorable experience in {province}, Thailand. for {days} days with a budget of {budget} THB"
    ), 
    expected_output=(
        "A structured list of travel recommendations, categorized by destinations, accommodations, "
        "activities, and dining options, each with descriptions, key highlights, estimated costs, and alternative choices."
    ), 
    tools=[tool],
    agent=travel_recommender,
    async_execution=False, 
    output_file="travel_recommendations.md",
)

