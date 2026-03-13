---
name: search-strategy
description: Builds a search strategy for a question or topic — decomposing it into searchable threads, translating concepts into field vocabulary, drafting targeted queries, and iterating based on results. Works for academic literature (Google Scholar, Scholar Lab) and general research. Activate when the user wants to search for sources, build search queries, find literature, or develop a research strategy for a question.
metadata:
  author: marcelgietzmann-sanders
  version: "1.0"
allowed-tools: Read Write
---

# Search Strategy

## When to activate

Activate when the user wants to find sources or literature for a question — whether academic, grey literature, or general research.

## Setup

Understand the question being researched. Read any relevant context (`Sketch.md`, `Questions.md`, or whatever the user provides). If the question isn't clear, ask the user to state it before proceeding.

Ask whether the user has existing sources on hand (from a library, notebook, or previous searches) that might already be relevant — before building new queries.

---

## The Process

### Step 1: Think before searching

Pause and think with the user about the landscape before generating queries:
- What kind of sources are likely to hold the answer? (empirical studies, reviews, grey literature, reports, specific authors or institutions?)
- Is this question likely to have a well-established literature, or is it more niche?
- What databases or search tools make sense for this question?

### Step 2: Decompose

Pull the question apart into its constituent concepts. Most questions contain 2–5 distinct phenomena, mechanisms, or claims — each of which likely has its own literature.

Ask:
- What are the moving parts of this question?
- If you had to answer it from scratch, what sub-questions would you need to answer first?
- Are there implied geographic, temporal, taxonomic, or domain scopes that narrow the search?

Name each thread plainly — don't use the question's exact phrasing, which is often too abstract. Aim for noun phrases: "bloom patchiness at mesoscale," "peak bloom duration in high-latitude systems."

### Step 3: Translate

For each thread, identify how the relevant field or literature actually refers to these concepts. The right term unlocks a literature that the intuitive term misses entirely.

Ask:
- What are the technical terms of art for this concept?
- Are there common abbreviations or named phenomena?
- Are there named geographic regions, systems, or frameworks that literature clusters around?
- What are common proxies or indices used to measure what you care about?

Surface 2–3 vocabulary variants per thread.

### Step 4: Decide on source type

For each thread, decide what kind of source would best serve the question:

- **Empirical** — specific measurements, observations, or experiments. Queries should anchor to phenomena, regions, or methods.
- **Review / synthesis** — existing knowledge summarised. Add terms like "review," "synthesis," "meta-analysis," or "global."
- **Theoretical / conceptual** — foundational ideas or frameworks. Search for author names, classic texts, or "theoretical basis."

Most threads benefit from at least one empirical and one review query.

### Step 5: Draft queries

Write concrete queries as **full natural language questions** for semantic search tools (e.g. Google Scholar Lab):
- Phrase as a complete question: "How do mesoscale eddies influence phytoplankton bloom duration?" not "mesoscale eddy bloom duration."
- Be specific enough that the question has a clear answer type.
- For reviews: "What do we know about X?" or "How well understood is X?"
- Use field-specific vocabulary within the question.

For **keyword-based search** (e.g. standard Google Scholar), also provide stripped-down keyword strings with Boolean operators (AND, OR, NOT) where useful.

Produce 2–3 queries per thread. Provide them in a form the user can copy and paste directly.

### Step 6: Iterate

After the user tests queries, return here to refine:
- Which queries returned useful results? Which came up empty or off-target?
- Did any results surface new vocabulary worth folding into other queries?
- Are there threads not being served — too broad, too narrow, or poorly anchored?
- Did results reveal that a thread needs to be split or merged?

Repeat until the user has a solid, focused set of sources.

---

## Guidance

- Don't over-gather. A focused set of high-quality sources is better than a sprawling pile.
- The user knows their field better than you do. Offer queries as drafts, not prescriptions — they may know immediately that certain terminology is off.
- If searches consistently turn up nothing, reconsider whether the question is well-formed or whether it exists in the literature under a different framing.
- The goal is a resource list ready to work with — not an exhaustive bibliography.
