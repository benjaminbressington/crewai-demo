import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ContentCrewAgents
from tasks import ContentCrewTasks

class ContentStrategyCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = ContentCrewAgents()
        self.tasks = ContentCrewTasks()

    def run(self):
        # Initialize agents for content strategy and critique roles
        idea_generator = self.agents.idea_generator()
        skeptical_critic = self.agents.skeptical_taxpayer_critic()
        urgency_critic = self.agents.urgency_seeker_critic()
        overwhelmed_critic = self.agents.overwhelmed_debtor_critic()
        planner_critic = self.agents.long_term_planner_critic()
        budget_critic = self.agents.budget_conscious_critic()
        strategist = self.agents.content_strategist()

        # Initialize agents for content writing roles
        wary_writer = self.agents.wary_taxpayer_writer()
        urgency_writer = self.agents.urgency_driven_writer()
        overwhelmed_writer = self.agents.overwhelmed_debtor_writer()
        planner_writer = self.agents.long_term_planner_writer()
        budget_writer = self.agents.budget_saver_writer()

        # Initialize tasks with respective agents
        brainstorming_task = self.tasks.brainstorming_task(idea_generator, self.inputs)
        critique_tasks = [
            self.tasks.critique_task(skeptical_critic, [brainstorming_task]),
            self.tasks.critique_task(urgency_critic, [brainstorming_task]),
            self.tasks.critique_task(overwhelmed_critic, [brainstorming_task]),
            self.tasks.critique_task(planner_critic, [brainstorming_task]),
            self.tasks.critique_task(budget_critic, [brainstorming_task]),
        ]
        strategy_task = self.tasks.strategy_task(strategist, critique_tasks)
        writing_tasks = [
            self.tasks.writing_task(wary_writer, [strategy_task]),
            self.tasks.writing_task(urgency_writer, [strategy_task]),
            self.tasks.writing_task(overwhelmed_writer, [strategy_task]),
            self.tasks.writing_task(planner_writer, [strategy_task]),
            self.tasks.writing_task(budget_writer, [strategy_task]),
        ]

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[
                idea_generator, skeptical_critic, urgency_critic, overwhelmed_critic,
                planner_critic, budget_critic, strategist,
                wary_writer, urgency_writer, overwhelmed_writer, planner_writer, budget_writer
            ],
            tasks=[brainstorming_task] + critique_tasks + [strategy_task] + writing_tasks,
            process=Process.sequential
        )

        # Execute the crew to carry out the content strategy project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Content Strategy Crew Setup")
    print("------------------------------------------")
    topic = input("Please enter the main topic or theme for the content strategy: ")
    target_segments = input("What specific audience segments are you targeting? ")
    content_focus = input("Any particular themes or messages to emphasize? ")

    inputs = f"Content Topic: {topic}\nTarget Segments: {target_segments}\nContent Focus: {content_focus}"
    content_strategy_crew = ContentStrategyCrew(inputs)
    result = content_strategy_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your content strategy project:")
    print("##############################\n")
    print(result)
