# 🧠 Prompt Engineering with LangChain

Prompts are the backbone of any interaction with a language model. In LangChain, the `Prompt` component plays a crucial role in shaping how we communicate with LLMs.

---

## ❓ What is a Prompt?

A **prompt** is the text you send to a language model to get a meaningful response. It can be a question, a command, or a structured template that guides the model's behavior.

LangChain enhances this by letting you build **prompt templates** with variables, input placeholders, and dynamic content—making your prompts scalable, modular, and reusable.

---

## 💡 Why Use Prompt Templates?

Using prompts directly is fine for simple tasks. But when you're building real-world applications, **reusability** and **modularity** become key.

Here's what LangChain prompt templates help you achieve:

- 🔁 **Reusable prompts** across multiple tasks
- 📦 **Modular design** for chaining
- ⚙️ **Dynamic input injection** at runtime
- 🧪 **Easier prompt experimentation**

---

## 🛠️ Basics of Prompt in LangChain

LangChain provides the `PromptTemplate` class to create and manage prompt templates.

### 🔤 Example: Basic Prompt Template

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What are the benefits of using {product}?"
)

formatted_prompt = prompt.format(product="LangChain")
print(formatted_prompt)

🧩 Where Prompts Fit in LangChain
In the LangChain stack, prompts are often the first step in a chain. They take structured input and craft the full text that gets passed to an LLM like GPT-4.

User Input → PromptTemplate → LLM → Response
