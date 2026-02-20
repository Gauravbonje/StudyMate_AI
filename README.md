# StudyMate AI – Multi-Agent Learning Assistant

**Course:** CSET395 – Latest Advances in Engineering & Technology
**Author:** Gaurav Yadav

---

## 1. Project Overview

StudyMate AI is a **Multi-Agent Learning System** built using CrewAI and Streamlit.

It simulates how different AI agents collaborate to create a complete study pack.

Agents used:

1. Research Expert → Collects detailed information
2. Teacher → Explains topic in simple language
3. Quiz Maker → Creates MCQs
4. Summarizer → Creates revision notes

This project is designed to **study behaviour of multi-agent systems** and analyze their limitations.

---

## 2. Folder Structure

```
StudyMate_AI
├── agents.py
├── app.py
├── check_models.py
├── pdf_generator.py
└── requirements.txt
```

---

## 3. How to Run

```
pip install -r requirements.txt
streamlit run app.py
```

---

## 4. Research Goal

The main goal is to observe:

* How multiple AI agents collaborate
* Where errors happen
* How information quality changes
* How architecture affects results

This project is not just an app, it is a **research prototype**.

---

## 5. Observations Found Till Now

### 1. Echo Chamber Problem

Agents sometimes repeat same information instead of improving it.

Example:
Teacher repeats Researcher output without adding clarity.

Impact:
Accuracy doesn’t improve after multiple rounds.

---

### 2. Role Boundary Confusion

Sometimes Summarizer starts researching again.

Reason:
Agents don’t fully respect their role prompts.

This shows need for stronger role enforcement.

---

### 3. Communication Latency

Each agent call increases latency.

Example:
Sequential architecture → High response time.

Observation:
Parallel architecture may be faster.

---

### 4. API Rate Limit Problem

Gemini free tier allows limited requests per day.

Example error:
`429 quota exceeded`

Impact:
Research experiments stop suddenly.

This shows real-world limitation of AI systems.

---

### 5. Model Availability Issue

Older models like gemini-pro are removed or unsupported.

Observation:
Multi-agent systems depend heavily on model availability.

---

### 6. Hallucination Risk

Research agent sometimes gives outdated or incorrect facts.

This shows need for:

* Verification agent
* Source checking

---

## 6. Metrics Measured

* Communication Latency
* Task Completion Time
* Output Quality
* Role Confusion Rate
* API Failure Rate

These metrics help compare architectures like Sequential vs Parallel.

---

## 7. Limitations of Current System

* Depends on external API
* No fact-checking agent
* Sequential architecture is slow
* Agents may repeat information
* Free tier quota is limited

---

## 8. Future Improvements

Planned improvements:

1. Add Judge Agent to reduce echo chamber
2. Add Fact-Check Agent
3. Use Local LLM for unlimited testing
4. Add Parallel Architecture
5. Add Agent Audit Dashboard
6. Improve UI and visualization

---

## 9. Research Importance

Multi-agent AI is the future of complex automation.

But real systems face problems like:

* Infinite loops
* Role confusion
* Memory drift
* API failures
* Overconfidence

This project demonstrates these issues practically.

---

## 10. Conclusion

StudyMate AI shows that multi-agent systems are powerful but still imperfect.

Careful architecture design and monitoring is required to build reliable AI systems.

---

## 11. Author Notes

This project is built for learning and research purposes only.
API limits and model changes affected experiments, which itself became an important research observation.

---

⭐ Thank you
