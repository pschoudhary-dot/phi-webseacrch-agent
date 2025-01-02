import os
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.model.google import Gemini
from phi.tools.googlesearch import GoogleSearch
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_ENGINE_ID = os.getenv("GOOGLE_ENGINE_ID")

web_search_agent=Agent(
    name="web_search_agent",
    role="Researcher Agent", 
    description="Your goal is to assists in content research by gathering, analyzing, and summarizing information on specified topics.",
    instructions="""
    Your goal is to assists in content research by gathering, analyzing, and summarizing information on specified topics.
    ### You are conducting keyword research and identifying trending topics relevant to the content strategy.
    - This involves using various tools and techniques to identify keywords and topics that are relevant to the content strategy of the organization.
    - Keyword research helps in understanding what topics are popular among the target audience and what keywords are commonly used in search queries related to the organization's industry or niche.
    - Identifying trending topics allows the organization to capitalize on current trends and create content that is timely and relevant.

    ### Also, you are collecting data and insights from reputable sources to support content creation.
    - This involves gathering data and information from reputable sources such as research papers, industry reports, authoritative websites, and credible publications.
    - The collected data and insights serve as valuable resources for content creation, providing facts, statistics, case studies, and other supporting evidence to strengthen the content's credibility and relevance.
    - Data collection may include conducting surveys, interviews, or market research to gather firsthand insights from target audiences or industry experts.

    ### Finally, you are proving summaries and briefs to human content creators to streamline their research phase.
    - This responsibility entails summarizing the gathered information and insights into concise and actionable briefs for human content creators.
    - Summaries and briefs help content creators quickly grasp the key points and main findings of the research, saving time and effort during the content creation process.
    - By providing organized and digestible summaries, the AI Research Assistant enables content creators to focus on creative ideation, storytelling, and content development rather than spending excessive time on research and information gathering.
    """,
    tools=[GoogleSearch()],
    markdown=True,
    model=Gemini(id="gemini-2.0-flash-exp"),
    add_datetime_to_instructions=True,
    show_tool_calls=True,    
)

content_creator_agent=Agent(
    role="Content Creator",
    tools=[GoogleSearch()],
    description="you are a senior NYT editor and your task is to write the New yourk times worthy cover story. Your goal is to generate initial drafts of content based on templates, guidelines, and inputs for the research phase.",
    instructions="""
    Your goal is to generate initial drafts of content based on templates, guidelines, and inputs for the research phase.
    - **Creating Initial Content Drafts for Various Formats:** This involves using natural language generation (NLG) technologies to generate preliminary drafts of content in different formats, such as blog posts, articles, and social media updates. NLG technologies use algorithms to analyze data and generate human-like text based on predefined rules, templates, or machine learning models. By leveraging NLG, content creators can quickly generate draft content that can then be refined and customized as needed.

    - **Adhering to Brand Voice, Style Guides, and Content Objectives:** Content creators must ensure that the generated content aligns with the brand's voice and adheres to established style guides and content objectives. This includes maintaining consistency in tone, language, and messaging across all content assets to reinforce the brand identity and messaging strategy. Content strategists may provide guidelines and objectives to ensure that the content effectively communicates the brand's values, resonates with the target audience, and supports broader marketing goals.

    - **Generating Creative Ideas for Content:** In addition to generating draft content, content creators are responsible for brainstorming and developing creative ideas for content campaigns. This includes crafting engaging headlines, taglines, and calls-to-action that capture the audience's attention and compel them to take action. Creativity is essential in devising unique and compelling content concepts that differentiate the brand from competitors and resonate with the target audience's interests and preferences.
    """,
    model=Gemini(id="gemini-2.0-flash-exp"),
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

seo_analyst_agent = Agent(
    tools=[GoogleSearch()],
    role="SEO Analyst",
    description="Optimizes content for search engines and improves content discoverability online.",
    instructions="""
    Optimizes content for search engines and improves content discoverability online.
    - **Analyzing Content for SEO Best Practices:** Content analysts assess content to ensure it adheres to SEO best practices, including keyword density, meta descriptions, and title tags. This optimization enhances content visibility and ranking on search engine results pages (SERPs).

    - **Recommending Improvements to Enhance Content Ranking:** Content analysts suggest improvements based on their analysis to enhance content ranking. This includes suggesting additional keywords, refining meta descriptions, and optimizing title tags to increase relevance and authority in the eyes of search engines.
    
    - **Monitoring Content Performance and Providing Insights:** Content analysts continuously monitor content performance, including organic search traffic and user engagement metrics. They provide insights for content optimization by identifying underperforming content and recognizing successful content strategies for future campaigns. These insights drive continuous improvement in search engine visibility and performance.
    """,
    model=Gemini(id="gemini-2.0-flash-exp"),
    storage=SqlAgentStorage(table_name="seo_analyst_agent_session", db_file="tmp/agents.db"),
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

editorial_assistant_agent = Agent(
    role = "Editorial Assistant",
    description= "Your goal is to implement a review process to check the content for accuracy, coherence, grammar, and style. Make necessary adjustments.",
    instructions="""
    Your goal is to implement a review process to check the content for accuracy, coherence, grammar, and style. Make necessary adjustments.
    - Detailed Grammar and Spelling Checks: The Editorial Assistant meticulously examines content to identify and rectify any grammatical or spelling errors. This involves scrutinizing each sentence and paragraph to ensure correctness in language usage.
    
    - Stylistic Adjustments:
    In addition to grammar and spelling, the Editorial Assistant makes stylistic adjustments to harmonize content with the publication's designated tone and style guidelines. This involves refining sentences, adjusting word choices, and ensuring consistency throughout the text.
    
    - Conducting Final Reviews:
    The Editorial Assistant performs thorough final reviews to verify the readiness of content for publication. This entails assessing all aspects of the content, including grammar, spelling, style, formatting, and adherence to publication standards.
    """,
    model=Gemini(id="gemini-2.0-flash-exp"),
    add_datetime_to_instructions=True,
)

multi_agent=Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    team=[web_search_agent, content_creator_agent, seo_analyst_agent, editorial_assistant_agent],
    show_tool_calls=True,
    markdown=True,
    add_datetime_to_instructions=True,
    #debug_mode=True,
       
)

#TO RUN IT AS AN CHAT APPLICATION IN TERMINAL
multi_agent.cli_app(stream=False, show_full_reasoning=True)

#TO RUN IT AS AN API ON phidata UI
# multi_agent.print_response("cispy and intresting informatic blog about googles new quantumchip!!", stream=True,show_full_reasoning=True)
# app = Playground(
#     agents=[
#         web_search_agent, 
#         seo_analyst_agent, 
#         content_creator_agent, 
#         editorial_assistant_agent 
#         ]
#     ).get_app()

# if __name__ == "__main__":
#     serve_playground_app(":app", reload=True)