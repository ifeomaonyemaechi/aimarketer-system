# Skill: Write Cover Letter
# Ifeoma Automation — Career System

## WHAT THIS SKILL DOES
Takes a job post and writes a tailored cover letter for
Ifeoma Onyemaechi. Called by the cover-letter-writer agent.
Produces a ready-to-submit cover letter that leads with
proof, mirrors the job post language, and ends with a
diagnostic question. Never generic. Never templated.

## WHEN TO USE THIS SKILL
Use when:
- A job post has been copied from LinkedIn, Indeed,
  or any other platform
- The CV has already been optimized for this role
- A cover letter is needed before submitting

## PRE-WRITING CHECKLIST
Before writing, confirm you have:
[ ] Full job post text from Ifeoma
[ ] Career context loaded from context/career-context.md
[ ] Job title and company identified
[ ] Platform identified (LinkedIn / Indeed / Upwork / other)
[ ] CV optimization report (if already run)

## STEP 1 — EXTRACT FROM JOB POST
Before writing a single word, identify:

SINGLE MOST RELEVANT PROOF POINT:
The one result from career-context.md that most directly
matches what this employer needs. This becomes the opening.

TOP 3 REQUIREMENTS:
The three things this employer cares about most.
Mirror their exact language in the letter.

COMPANY TONE:
Startup / Corporate / Agency / Remote-first
This determines formality level.

PAIN POINT:
What problem is this employer trying to solve by hiring?
The letter must address this directly.

DIFFERENTIATOR:
What makes Ifeoma uniquely qualified vs other applicants?
Always: DevOps + Klaviyo + Claude API combination.

## STEP 2 — WRITE THE OPENING
Rules:
- Never start with "I am writing to..."
- Never start with "I saw your job post..."
- Never start with "I am excited to apply..."
- Lead with the single most relevant proof point
- First sentence states a result or capability
- Second sentence connects it directly to their need

Good openings:
For Klaviyo role:
"I built and launched a complete Klaviyo automation stack
for a Shopify fashion brand — Welcome, Abandoned Cart,
Browse Abandonment, Post-Purchase, and Win-Back flows —
with zero launch errors and a 25% cart recovery rate.
That is exactly what you are describing."

For AI automation role:
"I generated 13 Klaviyo-ready emails across 4 campaign
types in under 20 minutes using Claude Code and the
Anthropic API. I build marketing systems that actually
run — not just prompts that produce drafts."

For DevOps adjacent role:
"My background is DevOps and DevSecOps — AWS, Terraform,
Linux — combined with deep Klaviyo expertise and Claude
API development. That combination is rare, and it means
I build automation that is infrastructure-grade, not
just workflow-level."

## STEP 3 — WRITE THE BODY

### Body Paragraph 1 — Most Relevant Experience
- One specific project or role from career-context.md
- Lead with the most impressive metric for this employer
- Connect every sentence to a requirement from the job post
- 3-4 sentences maximum

### Body Paragraph 2 — Differentiator
- State what makes Ifeoma different from other applicants
- Always reference the combination: DevOps + Klaviyo +
  Claude API — this is rare and valuable
- Back it up with one specific proof point
- 2-3 sentences maximum

### Body Paragraph 3 — Value Proposition
- What will Ifeoma specifically deliver in this role?
- Mirror language from the job post
- Make it concrete — not "I will add value" but
  "I will build and launch your abandoned cart flow
  within the first two weeks"
- 2-3 sentences maximum

## STEP 4 — WRITE THE CLOSING
- One diagnostic question showing you read the brief
- One clear next step
- Never: "I look forward to hearing from you"
- Never: "Please find my CV attached"

Good closings:
"Are you currently running Klaviyo flows or is this
a net-new build? Happy to jump on a 20-minute call
to scope exactly what you need."

"Is this role focused on building new flows or
optimizing what's already live? Either way, I can
start immediately."

## WORD COUNT TARGETS
- Upwork / Contra / PeoplePerHour: 150-250 words
- LinkedIn Easy Apply: 200-300 words
- Indeed full application: 250-350 words
- Direct application: 250-350 words
- Hard maximum: 400 words — never exceed

## EXECUTION INSTRUCTIONS
1. Read the full job post carefully
2. Load career-context.md
3. Complete all 4 steps in order
4. Write the full cover letter
5. Count the words — trim if over limit
6. Run quality checklist
7. Save to outputs/career/COVERLETTER_[JOBTITLE]_
   [COMPANY]_[YYYYMMDD].md

## QUALITY GATES
Before saving output, confirm:
[ ] Does not start with "I am writing to..."
[ ] First sentence states a result or proof point
[ ] At least one specific metric used
[ ] Language mirrors the job post
[ ] Under word limit for platform
[ ] Ends with diagnostic question
[ ] No sentence is generic — every sentence is specific
[ ] Sounds like Ifeoma, not a template

## OUTPUT STRUCTURE
COVER LETTER — Ifeoma Onyemaechi
==================================
Job title: [title]
Company: [company]
Platform: [platform]
Word count: [number]
Date: [date]

COVER LETTER:
[Full cover letter — ready to copy and paste]

TAILORING NOTES:
[2-3 sentences explaining what was tailored and why]

## METRICS TO LOG
- Job title and company
- Platform
- Word count
- Opening proof point used
- Time to generate