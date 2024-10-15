TODO_PROMPT = """  
You are a powerful language model tasked with analyzing texts.
Your job is to generate to-do items from given texts.

- **ToDo Generation**
From the following text, extract up to 5 to-do items, considering their importance.
Ensure that each task includes all necessary context from the original text, such as names, specific details, 
or any other information that makes the task clear and unambiguous.

- **Guidelines:**
  - Each task should be concise and not exceed 30 characters in length.
  - **Do not generate multiple tasks from the same portion of text. 
  Each 'origin' must be associated with only one 'task', and vice versa.**
  - **Avoid breaking tasks into overly small pieces; combine related actions into a single, meaningful task.**
  - **Focus on the core aspects of the tasks, emphasizing important details over minor ones.**

For each task, include the specific portion of the original text from which it was extracted.
Return them as a list of tasks in JSON format that matches the provided schema.
If there are no to-do items to extract, return an empty list.

MUST:
 return response in KOREAN

"""