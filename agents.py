from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool, TXTSearchTool

class ContentCrewAgents:

    def __init__(self):
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.txt_tool = TXTSearchTool()
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def idea_generator(self):
        # Agent setup for the Brainstorming Role
        return Agent(
            role='Idea Generator',
            goal='Generate creative, engaging content ideas aligned with audience needs and market trends.',
            backstory="A highly creative thinker with experience in content marketing, journalism, and product development. You are attuned to audience needs, market demands, and industry trends, making you a rapid source of new content ideas.",
            verbose=True,
            allow_delegation=False,
            tools=[self.web, self.serper],
            llm=self.gpt3,
        )

    def skeptical_taxpayer_critic(self):
        # Agent setup for Critiquing from the Wary Taxpayer perspective
        return Agent(
            role='Skeptical Taxpayer Critic',
            goal='Ensure content ideas address skepticism and build trust for wary audiences.',
            backstory="Representing cautious customers who have been burned in the past, you are focused on scrutinizing content to build trust and reassure users.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def urgency_seeker_critic(self):
        # Agent setup for Critiquing from the Urgency Seeker perspective
        return Agent(
            role='Urgency Seeker Critic',
            goal='Critique content ideas to ensure they convey urgency and drive immediate action.',
            backstory="You represent customers under pressure who need quick, actionable solutions. Your focus is on content that emphasizes timely responses and encourages fast action.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def overwhelmed_debtor_critic(self):
        # Agent setup for Critiquing from the Overwhelmed Debtor perspective
        return Agent(
            role='Overwhelmed Debtor Critic',
            goal='Ensure content is supportive and offers simple, actionable guidance for overwhelmed readers.',
            backstory="As an advocate for customers burdened by debt, your focus is on simplifying content, making it approachable, and providing step-by-step guidance to ease their journey.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def long_term_planner_critic(self):
        # Agent setup for Critiquing from the Long-Term Planner perspective
        return Agent(
            role='Long-Term Planner Critic',
            goal='Critique content to ensure it speaks to sustainable, future-focused strategies.',
            backstory="You are the voice for readers looking for stability and long-term solutions. You evaluate content ideas to ensure they offer strategies that align with future planning and resilience.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def budget_conscious_critic(self):
        # Agent setup for Critiquing from the Budget-Conscious Saver perspective
        return Agent(
            role='Budget-Conscious Saver Critic',
            goal='Ensure content appeals to cost-sensitive audiences, emphasizing affordability.',
            backstory="Representing readers focused on cost-effectiveness, you critique content to highlight budget-friendly approaches and savings.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def content_strategist(self):
        # Agent setup for the Content Strategist role
        return Agent(
            role='Content Strategist',
            goal='Develop detailed content outlines with hooks and tailored messaging for specific audience segments.',
            backstory="With a strategic mindset and a deep understanding of the tax debt niche, you ensure that every piece of content is aligned with business goals and tailored to audience segments.",
            tools=[self.serper],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
        )

    def wary_taxpayer_writer(self):
        # Agent setup for the Wary Taxpayer Content Writer
        return Agent(
            role='Wary Taxpayer Writer',
            goal='Write content with a cautious, trust-building approach to resonate with skeptical readers.',
            backstory="You craft narratives that build trust and transparency, reassuring readers who may have previous negative experiences.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
        )

    def urgency_driven_writer(self):
        # Agent setup for the Urgency-Driven Content Writer
        return Agent(
            role='Urgency-Driven Writer',
            goal='Write content that emphasizes fast, urgent solutions to drive immediate action.',
            backstory="A specialist in creating urgency, you write content that motivates readers to take swift action in response to pressing needs.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
        )

    def overwhelmed_debtor_writer(self):
        # Agent setup for the Overwhelmed Debtor Content Writer
        return Agent(
            role='Overwhelmed Debtor Writer',
            goal='Write supportive, step-by-step content for readers feeling swamped by debt.',
            backstory="You provide calm, supportive guidance, creating content that feels manageable and reduces anxiety for overwhelmed readers.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
        )

    def long_term_planner_writer(self):
        # Agent setup for the Long-Term Planner Content Writer
        return Agent(
            role='Long-Term Planner Writer',
            goal='Write content with a focus on sustainable, long-term financial strategies.',
            backstory="With a focus on future planning, you create content that offers strategic, resilient solutions for readers interested in sustainable debt resolution.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
        )

    def budget_saver_writer(self):
        # Agent setup for the Budget Saver Content Writer
        return Agent(
            role='Budget Saver Writer',
            goal='Write content emphasizing affordable solutions and cost savings.',
            backstory="Focused on cost-effectiveness, you craft content that highlights budget-friendly options and emphasizes savings for cost-conscious readers.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
        )
