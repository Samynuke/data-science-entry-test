prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""
prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""

Task 1
Read both prompts above carefully, then answer the questions below as comments.

Q8a: Which prompt do you think will get a better response from an AI?
Prompt B

Q8b: Give TWO reasons to support your choice.
(Reason 1): Prompt B breaks the task into clear, numbered steps
(identify low scores -> extract themes -> summarise), which guides the AI
through a logical process instead of leaving it to figure out the order
and structure on its own.

(Reason 2): Prompt B explicitly assigns a role ("You are a
data analyst") and states the audience and constraints ("CEO presentation",
"concise and free of technical jargon") as separate, scannable fields.
This reduces ambiguity and makes it easier for the AI to match tone and
depth to what's actually needed.

Q8c: What is ONE strength of the prompt you did NOT choose?
Your answer: Prompt A reads more naturally and includes real-world context
(who the person is, why the task matters, what happened before it) which
can help the AI infer nuance -- e.g. that this is a first-time report to
a CEO, so tone should be a bit more careful/polished than a routine update.
That kind of narrative context is sometimes lost in a bullet-point format.

Task 2
Rewrite either prompt by borrowing ONE element from the other 
to make it stronger. Explain what you borrowed and why.
answer:
prompt_a_improved = """
I am a marketing manager at a retail company and we have just finished
a three-month campaign. My team has collected customer feedback through
an online survey and we now have about 500 responses stored in a
spreadsheet. Each response includes the customer's age group, the
product they purchased, their satisfaction rating from 1 to 5, and a
short written comment. I need to present the findings to our CEO next
Friday in a way that is easy to understand.

Please follow these steps:
1. Identify which age groups and products have the lowest satisfaction scores.
2. Identify the most common complaints from the written comments.
3. Summarise everything in a short, jargon-free paragraph I can use as an
   executive summary.

I borrowed the numbered step-by-step structure from Prompt B and added it
to Prompt A. Prompt A already had strong context and a clear goal, but it
asked for four things in one run-on sentence, which risks the AI blending
steps together or skipping one. Breaking it into explicit steps (like
Prompt B) keeps Prompt A's natural, human context while making the
expected output structure just as clear as Prompt B's.
