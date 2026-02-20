import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# -------- Gemini LLM --------
llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    temperature=0.3
)

def create_study_crew(topic):

    # -------- Agents --------

    researcher = Agent(
        role="Research Expert",
        goal=f"Find accurate information about {topic}",
        backstory="Expert academic researcher.",
        llm=llm,
        verbose=True
    )

    teacher = Agent(
        role="Teacher",
        goal=f"Explain {topic} in simple language",
        backstory="Friendly professor.",
        llm=llm,
        verbose=True
    )

    quiz_maker = Agent(
        role="Quiz Maker",
        goal=f"Create MCQ quiz about {topic}",
        backstory="Exam preparation expert.",
        llm=llm,
        verbose=True
    )

    summarizer = Agent(
        role="Summarizer",
        goal=f"Create short revision notes for {topic}",
        backstory="Revision notes expert.",
        llm=llm,
        verbose=True
    )

    judge = Agent(
        role="Judge",
        goal=f"Check study pack accuracy about {topic}",
        backstory="Strict professor checking mistakes.",
        llm=llm,
        verbose=True
    )

    # -------- Tasks --------

    t1 = Task(
        description=f"Research detailed information about {topic}",
        agent=researcher
    )

    t2 = Task(
        description=f"Explain {topic} simply for beginners",
        agent=teacher
    )

    t3 = Task(
        description=f"Create 5 MCQs about {topic} with answers",
        agent=quiz_maker
    )

    t4 = Task(
        description=f"Write short revision notes about {topic}",
        agent=summarizer
    )

    t5 = Task(
        description="Check entire study pack for mistakes and improve it",
        agent=judge
    )

    # -------- Crew --------

    crew = Crew(
        agents=[researcher, teacher, quiz_maker, summarizer, judge],
        tasks=[t1, t2, t3, t4, t5],
        verbose=True
    )

    return crew
