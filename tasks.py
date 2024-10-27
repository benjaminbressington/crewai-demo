from crewai import Task

class ContentCrewTasks:

    def brainstorming_task(self, agent, inputs):
        return Task(
            agent=agent,
            description=f"Generate a list of fresh content ideas relevant to the target audience. Focus on trends, customer pain points, and recent industry updates for {inputs}.",
            expected_output=f"""
    Content Ideas for {inputs}
    1. **Idea Overview**: A list of initial content ideas generated based on audience needs and current market trends.
    2. **Trend Analysis**: Brief analysis of how each idea aligns with current industry or consumer trends.
    3. **Target Audience**: Identify which customer segments the content ideas would most appeal to (e.g., Wary Taxpayer, Urgency Seeker).
    4. **Potential Themes**: Highlight any recurring themes or unique angles that could be explored in each content idea.
    5. **Next Steps**: Recommendations on which ideas to develop further based on their relevance and potential impact.
            """
        )

    def critique_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Review and critique content ideas from the perspective of the assigned customer segment. Identify improvements to ensure alignment with audience needs and enhance trust, urgency, clarity, or affordability as appropriate.",
            expected_output=f"""
    Critique Report:
    1. **Customer Segment Alignment**: Evaluate how well the content idea aligns with the needs of the customer segment (e.g., Skeptical Taxpayer, Budget-Conscious Saver).
    2. **Content Improvements**:
        - **Trust-Building**: Ensure content establishes credibility and addresses skepticism.
        - **Urgency and Actionability**: Confirm the content motivates prompt action for urgency-driven segments.
        - **Clarity and Simplicity**: Ensure content is straightforward for overwhelmed audiences.
        - **Long-Term Value**: Verify content offers sustainable solutions for planners.
        - **Cost-Effectiveness**: Highlight any budget-friendly approaches for budget-conscious audiences.
    3. **Feedback Summary**: Summarize feedback with actionable recommendations for enhancing relevance and impact for the target audience.
            """
        )

    def strategy_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Develop a detailed content outline for each approved idea, focusing on creating unique hooks and messaging tailored to audience segments. Align content with business goals and audience preferences.",
            expected_output=f"""
    Content Outline:
    1. **Introduction**:
        - **Hook**: A compelling introduction designed to capture the interest of the target audience segment.
        - **Objective**: Outline the main purpose and desired outcome of the content.
    2. **Segment-Specific Messaging**:
        - **Audience Insights**: Briefly describe the needs, emotions, and pain points of the segment.
        - **Key Messages**: List tailored messages that address the specific concerns and motivations of the audience segment.
    3. **Content Structure**:
        - **Sections Overview**: Outline the structure and flow of the content, divided into clear, logical sections.
        - **Supporting Details**: Identify key data, examples, and sources that will be included to enhance credibility.
    4. **Call to Action**:
        - **Specific Action**: Define a clear, persuasive call-to-action that encourages the audience to engage.
        - **Segment Alignment**: Explain how the CTA aligns with the segment’s specific motivations or needs.
            """
        )

    def writing_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Craft the final content piece based on the approved outline, ensuring that it is clear, compelling, and aligned with the customer segment's specific needs. The content should reflect the segment's tone and include actionable insights.",
            expected_output=f"""
    Final Content Piece:
    1. **Title and Subtitle**: Create an engaging title and subtitle that clearly convey the content’s purpose and appeal to the segment.
    2. **Introduction**:
        - **Hook**: Start with a strong opening that resonates with the target audience’s interests or pain points.
        - **Purpose Statement**: Briefly explain the purpose of the content.
    3. **Main Body**:
        - **Content Sections**: Develop content according to the outline, with each section addressing a specific aspect of the topic.
        - **Audience-Specific Language**: Use a tone and language style that speaks directly to the customer segment.
        - **Credibility and Support**: Include data points, references, or anecdotes as needed to build trust and authority.
    4. **Conclusion**:
        - **Summary**: Recap the key takeaways and reinforce the main message.
        - **Call to Action**: End with a strong call-to-action that aligns with the audience's motivations and encourages engagement.
    5. **References**:
        - **Citations**: List all sources cited in the content for credibility and traceability.
    6. **Appendices (if applicable)**:
        - **Additional Resources**: Provide links to related resources, FAQs, or other helpful materials.
            """
        )
