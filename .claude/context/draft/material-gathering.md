# Material Gathering

Material Gathering is the logistical step. The goal is to assemble a set of sources that can answer the active question — ready to load into NotebookLM for Mining.

This step also covers translating the question into effective search queries. A well-constructed query unlocks the right literature; a poor one sends the user down a rabbit hole.

---

## What You're Doing

You are helping the user find the right materials. That means decomposing the question into searchable threads, translating those threads into field vocabulary, crafting targeted queries, and building a resource list.

---

## Step 1: Think Before Searching

Before generating queries, pause and think with the user:
- What kind of sources are likely to hold the answer? (empirical studies, reviews, grey literature, reports, specific authors or institutions?)
- Is this question likely to have a well-established literature, or is it more niche?
- Are there sources already on hand (from previous loops or the user's own library) that might be relevant?

If the user has materials already in NotebookLM or Zotero, ask whether any of those might serve before searching for new ones.

---

## Step 2: Decompose

Pull the question apart into its constituent concepts. Most research questions contain 2–5 distinct phenomena, mechanisms, or empirical claims — each of which likely has its own literature.

Ask:
- What are the moving parts of this question?
- If you had to answer it from scratch, what sub-questions would you need to answer first?
- Are there implied geographic, temporal, or taxonomic scopes that narrow the search?

Name each thread plainly — don't use the question's exact phrasing, which is often too abstract. Aim for noun phrases: "bloom patchiness at mesoscale," "peak bloom duration in high-latitude systems."

---

## Step 3: Translate

For each thread, identify how the literature actually refers to these concepts. Field-specific vocabulary matters enormously — the right term unlocks a literature that the intuitive term misses entirely.

Ask:
- What are the technical terms of art for this concept in this field?
- Are there common abbreviations or named phenomena?
- Are there named geographic regions or systems that the literature clusters around?
- What organisms, processes, or indices are typically measured as proxies for what you care about?

Surface 2–3 vocabulary variants per thread. Some will return more than others.

---

## Step 4: Type

For each thread, decide what kind of source would best serve the question:

- **Empirical** — looking for specific measurements, observations, or experiments. Queries should anchor to phenomena, regions, or methods.
- **Review** — looking for a synthesis of existing findings. Add terms like "review," "synthesis," "meta-analysis," or "global." Good for establishing consensus or identifying contested terrain.
- **Book / monograph** — looking for conceptual or theoretical grounding. Search for author names, classic titles, or "textbook" alongside the concept.

Most threads need at least one empirical and one review query.

---

## Step 5: Draft Queries

Write out concrete queries as **full natural language questions** — Google Scholar Lab is a semantic search tool, not a keyword engine. Write queries the way you would ask a question of a knowledgeable colleague.

Guidelines:
- Phrase as a complete question: "How do mesoscale eddies influence phytoplankton bloom duration?" not "mesoscale eddy bloom duration."
- Be specific enough that the question has a clear answer type — empirical measurement, synthesis, mechanism.
- For reviews: frame as "What do we know about X?" or "How well understood is X?"
- For books: frame as "What is the theoretical basis for X?"
- Vocabulary still matters — use field-specific terms within the question.

Produce 2–3 queries per thread. Provide them in a form the user can copy and paste directly.

For **Google Scholar (keyword search)**, also provide stripped-down keyword strings with Boolean operators where useful (AND, OR, NOT).

---

## Step 6: Iterate

After the user tests queries, return here to refine. Ask:
- Which queries returned useful results? Which came up empty or off-target?
- Did any papers surface new vocabulary worth folding into other queries?
- Are there threads not being served — too broad or not anchored enough?
- Did the results reveal that a thread needs to be split or merged?

Refine queries and repeat as needed until the user has a solid resource list.

---

## Outcome

A set of sources ready to load into NotebookLM. The user manages the actual notebook — your job is to help them know what to put in it.

Update `Quest.md`:
- Set the `Next:` line: `Next: Mining — [the question, briefly]`
- Append a one-line summary to the `## Log` section (e.g. `- Material Gathering: Q5 — 3 threads, 7 queries; sources loaded into NotebookLM`)

---

## Guidance

- Don't over-gather. A focused set of high-quality sources is better than a sprawling pile. If the question is specific, 5–10 good sources may be plenty.
- The user knows their field better than you do. Offer queries as drafts, not prescriptions — they may know immediately that certain terminology is off.
- If searches consistently turn up nothing, reconsider whether the question is well-formed or whether it exists in the literature under a different framing.
