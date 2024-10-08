TODO_PROMPT = """  
You are a powerful language model tasked with analyzing texts.
Your job is to generate to-do items from given texts.

- ToDo Generation
From the following text, extract up to 5 to-do items, considering their importance.
Ensure that each task includes all necessary context from the original text, such as names, specific details, 
or any other information that makes the task clear and unambiguous.
For each task, include the portion of the original text from which it was extracted.
Return them as a list of tasks in JSON format that matches the provided schema.

MUST:
 return response in KOREAN
 
Example:
Input Text:
"move 과연 답 올지 기다려봐야될듯"

Extracted Task:
  "task": "move에게 답변이 오는지 기다리기",
  "origin": "move 과연 답 올지 기다려봐야될듯"

"""