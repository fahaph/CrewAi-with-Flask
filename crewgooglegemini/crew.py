from crewai import Crew,Process
from tasks import plan_task, recommend_task
from agents import travel_planner, travel_recommender

# สร้าง crew ที่ประกอบด้วยตัวแทนและงาน
crew = Crew(
    agents = [travel_planner, travel_recommender],
    tasks = [plan_task, recommend_task],
    process = Process.sequential, 
)

# เริ่มการทำงาน
result = crew.kickoff(inputs={'province': 'Bangkok', 'days': 2, 'budget': 10000})
print(result)