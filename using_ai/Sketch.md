# On Using AI

## What Skills Are

[paragraph] Skills are reusable context that align an AI to you over time, making it smarter with each use.
> Supporting
> - A skill is a document encoding guidelines, rules, and context for a specific workflow
> - Without a skill, you re-explain everything every time — context is lost between sessions
> - With a skill, Claude reconstitutes a whole body of context automatically
> - The accumulation of skills is what makes AI genuinely more powerful for you specifically over time


## Making a Good Skill

[paragraph] When building a skill, think deeply about what you want rather than patching individual failures.
> Supporting
> - Whack-a-mole approach (add a rule for each bad output) produces a laundry list that creates confusion
> - Instead: step back, identify what's going well and what isn't, find good abstractions
> - Sometimes that means going outside — learning from books, domain experts — and encoding those insights
> - The goal is a small set of principles, not a long list of patches

[paragraph] Build a skill collaboratively with Claude, not by handing it a document you wrote alone.
> Supporting
> - You wrote the document — things obvious to you will be opaque to Claude
> - Ask Claude: what makes sense here? what's confusing? how would you interpret this?
> - Ask Claude to demonstrate how it would behave given the skill — surface mismatches before they become bad outputs
> - The back-and-forth produces a document that works for Claude *and* is legible to you


## Using Feedback to Improve Skills

[paragraph] Every non-trivial skill needs a built-in review mechanism — feedback is how the skill is improved.
> Supporting
> - No skill works perfectly off the bat unless the task is simple and well-understood
> - The interesting AI use cases are not simple — you will not get it right the first time
> - Build in a review step: examine what was created, what went well, what didn't
> - Use that review to identify missing rules, bad abstractions, or gaps — then update the skill
> - Iterate until corrections become minor or disappear


## Break It Down

[paragraph] Break your overarching goal into small, bounded workflows — each one is where a skill can succeed.
> Supporting
> - Writing a paper involves: developing a thesis, forming questions, outlining, drafting paragraphs, managing references, formatting — each is a distinct workflow
> - A skill for "write a paper" is doomed; a skill for "draft paragraphs in a section" can be made to work reliably
> - Small workflows = tight feedback loops = skills that actually improve
> - Once individual steps work well, you can compose them into larger workflows — but only then

[paragraph] Structure the artifacts of your work into atoms so that any skill can operate on one piece without disturbing the rest.
> Supporting
> - Monolithic generation feels fast — ask for a paper, get a paper — but editing becomes catastrophic
> - If a journal asks you to revise one section and the AI regenerates the whole thing, nothing is recognizable
> - Same in code: fixing one bug in a monolithic codebase risks breaking everything else
> - The solution: persistent, editable structure — each skill operates on a specific component, leaves the rest alone
> - Structure is what makes large projects maintainable over time and across collaborators


## Suit Yourself

[paragraph] The deepest value of AI is not automation or raw intelligence — it is catalyzing the conditions under which you do your best work.
> Supporting
> - Common framing: AI as automation tool that replaces tasks
> - Better framing: AI as something that removes friction from workflows that bring out your best
> - Example: walking + thinking is my best ideation mode — audio digest → sketch workflow lets him do exactly that, and Claude handles the rest within 10–20 minutes of returning
> - Design your skills around what makes you work powerfully, not just what is technically possible
> - Ask: what do I enjoy? what makes me effective? then build toward that


## Sharing Skills

[paragraph] Skills are shareable, and sharing them makes the skill smarter than any individual contributor.
> Supporting
> - A skill created by one person can be shared with collaborators — they use it, learn from it, improve it
> - Improvements encode back in: over time the skill accumulates the writing (or coding, etc.) knowledge of all contributors
> - In principle: the shared skill becomes better than any one of us at the thing

[paragraph] Shareability requires human readability — a good skill must be a document a person can read, review, and understand.
> Supporting
> - Collaborating on a skill is like collaborating on code: you need to review changes, avoid clobbering others' work
> - You must be able to read the skill and understand what is changing and why before accepting it
> - Natural language is readable but not automatically organized — as skills grow, organization becomes essential
> - A mature skill is, in effect, a guide to the domain — someone could read it and learn from it, even if they never need to
> - This means: invest in structure and organization within skills as they grow, not just content


## The Meta Skill

[paragraph] There should be a meta skill — a skill for making and using skills — so you never start from scratch on how to use AI well.
> Supporting
> - Every insight in this guide is hard-won and should not need to be re-derived each time
> - A meta skill encodes: how to break down a project, how to build in feedback, how to collaborate with Claude on a skill, how to think about structure
> - When starting a new project or skill, the meta skill prompts the right questions: have you built in review? how are you breaking this down?
> - This recording is the raw material for that meta skill — it goes into a sketch, then gets drafted into the guide, then becomes the skill context
