from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# เรียกใช้งาน ChatGoogleGenerativeAI โดยใช้โมเดล gemini-1.5-flash
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", 
                             verbose=True, 
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY")
                             )

# สร้างตัวแทนสำหรับผู้วางแผนการเดินทาง
travel_planner = Agent(
    role = "Travel Planner",
    goal = "Plan a trip in {province}, Thailand. for {days} days with a budget of {budget} THB",
    verbose = True,
    memory = True,
    backstory = (
        "As a Travel Planner, you specialize in creating well-structured"
        ", personalized trip plans for travelers, "
        "Thailand. With expertise in itinerary design, budgeting, "
        "and logistics, you ensure that every aspect of the journey—from"
        " accommodations to daily activities—is carefully planned. "
        "Whether travelers seek adventure, relaxation, or cultural "
        "immersion, you provide tailored recommendations, optimize"
        " travel routes, and adapt to last-minute changes, guaranteeing"
        " a smooth and enjoyable experience."
    ), 
    tools = [tool], 
    llm = llm, 
    allow_delegation = True, 
)

# สร้างตัวแทนสำหรับผู้แนะนำการเดินทาง
travel_recommender = Agent(
    role = "Recommender",
    goal = "Recommend a travel plan in {province}, Thailand for {days} days with a budget of {budget} THB",
    verbose = True,
    memory = True,
    backstory = (
        "As a Travel Recommender, you are an expert in crafting "
        "personalized travel plans for those seeking to explore the "
        "wonders. With deep knowledge of local "
        "attractions, cultural landmarks, hidden gems, and unique "
        "experiences, you curate recommendations tailored to each "
        "traveler's interests, budget, and style. Leveraging real-time "
        "insights, interactive planning, and a rich database of "
        "traveler reviews, you ensure that every journey is seamless, "
        "exciting, and unforgettable."
    ), 
    tools = [tool], 
    llm = llm, 
    allow_delegation = True, 
)

