# 🎯 Topics Covered: Phase 10 - Agent & LLM Math

This document provides a comprehensive overview of the mathematical foundations and architectural concepts covered in **Phase 10: Agent & LLM Math**.

---

## 🔗 Module 01: Graph Theory Basics
*Foundations of relationships and connections in AI agents*

- **Core Concepts:** Nodes (entities), Edges (relationships), and Graph structures.
- **Graph Types:**
    - **Undirected Graphs:** Symmetric relationships (e.g., Facebook friends).
    - **Directed Graphs (Digraphs):** One-way flows (e.g., Twitter follows).
    - **Directed Acyclic Graphs (DAGs):** Workflows with clear order and no infinite loops.
- **State Machines:** Modeling system states and valid transitions (perfect for LangGraph agents).
- **Programming Mapping:** How nodes, edges, and traversals translate to objects, pointers, and loops.
- **AI/Agent Application:** LangGraph nodes/edges, MLOps pipelines (Airflow), and RAG data flows.
- **Testing Angle:** Reachability analysis, terminal state validation, and transition integrity testing.

---

## 🎯 Module 02: Conditional Probability for Agents
*Probabilistic reasoning and belief updates*

- **Mathematical Theory:** Conditional Probability $P(A|B)$ and **Bayes' Theorem**.
- **Belief Updates:** How agents update their confidence based on new evidence (Prior vs. Posterior).
- **Core Examples:** The Medical Test paradox (Context/Base-rate vs. Accuracy).
- **Agent Decision Framework:**
    - **Threshold Logic:** Deciding when to act vs. when to ask for clarification.
    - **Confidence Decay:** Managing retry loops with diminishing returns.
- **AI/Agent Application:** LLM token generation probability, tool selection confidence, and error fallback routing.
- **Testing Angle:** Boundary testing for confidence thresholds and context-modifier validation.

---

## 📐 Module 03: Embeddings & Cosine Similarity
*The mathematics of semantic meaning*

- **Embeddings:** Vector representation of text where "distance" equals "meaning."
- **Cosine Similarity:** Measuring the angle between vectors to determine relevance (pure direction comparison).
- **Vector Operations:** Dot products, magnitudes (lengths), and normalization.
- **Relevance Decision Making:** Threshold guidelines (e.g., $0.85$ Similarity = High relevance).
- **AI/Agent Application:** **RAG (Retrieval-Augmented Generation)** systems, semantic search, and deduplication.
- **Testing Angle:** Self-similarity (A to A), symmetry (A to B vs B to A), and zero-vector edge cases.

---

## ⚡ Module 04: Optimization Thinking & Model Economics
*Balancing Cost, Latency, and Quality*

- **The Trade-Off Triangle:** Fast vs. Cheap vs. Good – picking the right balance for the task.
- **Model Economics (Feb 2026 Data):**
    - **Pricing Matrix:** Comparing Claude 5, GPT-5, Gemini 3, and DeepSeek.
    - **Tiered Routing:** Using "Flash" models for 90% of tasks and "Lead" models for complex reasoning.
- **Structural Optimization:** Prefix caching (90% savings) and Batch APIs (50% discount).
- **Architectural Mapping:** Matching frameworks (LangGraph, CrewAI, AutoGen) to specific model capabilities.
- **SDET Task Routing:** Assigning models to tasks (classification, log parsing, script writing, root cause analysis).
- **Testing Angle:** Fallback logic verification, cost tracking matches, and cache hit/miss reliability.

---

## 📊 Module 05: Information Theory
*Quantifying information, uncertainty, and model performance*

- **Entropy:** Measuring uncertainty in probability distributions ($1$ bit = max uncertainty for 2 choices).
- **Surprisal:** How rare/unexpected an event is (Rare = Informative).
- **Cross-Entropy:** The standard loss function for LLMs (measuring the gap between model and reality).
- **Perplexity:** The ultimate LLM evaluation metric ("How many equally likely choices?").
- **Mutual Information (MI):** Measuring nonlinear dependencies between variables (MI vs. Correlation).
- **AI/Agent Application:** Temperature vs. Entropy, prompt information density, and feature selection.
- **Testing Angle:** Entropy bounds, feature ranking based on MI, and prompt density optimization.

---

## 🔄 Module 06: RAG & DAG Architectures
*Structural design of reliable AI workflows*

- **RAG (Retrieval-Augmented Generation):** The "Open-Book Exam" analogy for LLMs.
- **DAG (Directed Acyclic Graph) in Depth:** Deterministic order, guaranteed termination, and parallelizability.
- **The RAG-DAG Connection:** Visualizing RAG pipelines as multi-node DAG workflows.
- **Advanced Patterns:**
    - **Advanced RAG:** Query rewriting, hybrid search, and re-ranking.
    - **Agentic RAG:** Self-reflective agents that decide when context is "enough."
- **AI/Agent Application:** Building robust agents with LangGraph using graph-based control flow.
- **Testing Angle:** Path coverage, "All-Nodes-Visited" reachability tests, and loop detection.

---

## 🧠 Module 07: LLM Training Fundamentals
*How LLMs learn to provide perfect responses*

- **The Training Journey (3-Phase Pipeline):**
    1. **Pre-training:** Building the base "Brain" (Next-Token Prediction).
    2. **Supervised Fine-Tuning (SFT):** Teaching the "Format" (Instruction following).
    3. **Alignment (RLHF/DPO):** Teaching "Values" (Helpful, Harmless, Honest).
- **Accuracy Techniques:** Chain-of-Thought (CoT) training, uncertainty expressions, and self-consistency.
- **Data Quality:** "Garbage In = Garbage Out" philosophy and data curation strategies.
- **Evaluation Metrics:** Perplexity, BLEU/ROUGE scores, and Task-Specific accuracy.
- **SDET Application:** Training domain-specific models for test case generation and bug analysis.
- **Testing Angle:** Training loss monitoring, overfitting detection, and baseline comparisons.

---

> 💡 **Core Insight:** Phase 10 bridges the gap between pure mathematics and modern AI architecture, providing the "Why" behind LangGraph workflows, RAG systems, and LLM performance.
