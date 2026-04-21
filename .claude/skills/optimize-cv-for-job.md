# Skill: Optimize CV for Job
# Ifeoma Automation — Career System

## WHAT THIS SKILL DOES
Takes a job post pasted by Ifeoma and optimizes her CV
to match that specific role. Called by the cv-optimizer
agent. Produces a rewritten CV tailored for ATS screening
and human review, plus a fit score and gaps report.

## WHEN TO USE THIS SKILL
Use when:
- Ifeoma wants to apply for a specific job
- A job post has been copied from LinkedIn, Indeed,
  or any other platform
- The CV needs to be tailored before submitting

## PRE-OPTIMIZATION CHECKLIST
Before rewriting, confirm you have:
[ ] Full job post text from Ifeoma
[ ] Career context loaded from context/career-context.md
[ ] Job title and company identified
[ ] Platform identified (LinkedIn / Indeed / other)

## STEP 1 — ANALYZE THE JOB POST
Extract these from the job post:

REQUIRED SKILLS:
List every technical skill, tool, and platform mentioned
as required. Use exact words from the post.

PREFERRED SKILLS:
List everything marked as nice-to-have or preferred.

KEY RESPONSIBILITIES:
List the 5 most important things this role needs done.

ATS KEYWORDS:
Every tool, platform, certification, and technical term
mentioned. These are what the ATS will scan for.

COMPANY TONE:
Startup / Corporate / Agency / Remote-first / Other
This affects how formal the cover letter should be.

SENIORITY LEVEL:
Entry / Mid / Senior / Lead / Manager
This affects how achievements are framed.

## STEP 2 — SCORE THE FIT
Compare job requirements against career-context.md.

For each required skill:
- Found in Ifeoma's background: +10 points
- Partially matches: +5 points
- Not found: 0 points

Calculate: (total points earned / total points possible) x 10

FIT SCORE TIERS:
9-10: Excellent fit — apply immediately
7-8: Strong fit — apply with confidence
5-6: Moderate fit — apply, address gaps in cover letter
3-4: Weak fit — only apply if pipeline is empty
1-2: Poor fit — skip, not worth the effort

## STEP 3 — REWRITE THE CV

### Professional Summary
- Change job title in summary to match the job post title
- Include top 3 ATS keywords naturally
- Reference the most relevant proof metric for this role
- Keep under 80 words

### Core Skills Section
- Move skills that match the job post to the top
- Add exact tool names from job post if Ifeoma has them
- Remove skills completely irrelevant to this role
- Maximum 6 categories, most relevant first

### Work Experience
For each role, reorder and rewrite bullets:
- Put bullets most relevant to this job first
- Add ATS keywords naturally into existing bullet text
- Use STAR format: Action verb + Task + Result
- Every bullet must have a measurable outcome where possible

### Portfolio Projects
- Reorder projects — most relevant to this job first
- Add ATS keywords from job post into descriptions
- Emphasize metrics that match what employer values
- For AI roles: lead with Claude Code and API projects
- For Klaviyo roles: lead with email automation projects

### Certifications
- Reorder — most relevant certifications first
- For AI roles: list all 8 Anthropic Academy courses
- For email roles: list all Klaviyo certifications first

## STEP 4 — IDENTIFY GAPS
For every required skill not in Ifeoma's background:
- State the gap clearly
- Suggest how to address it:
  Option A: Portfolio project that demonstrates the skill
  Option B: Certification or course to take
  Option C: Frame existing experience as adjacent

## EXECUTION INSTRUCTIONS
1. Read the full job post carefully
2. Load career-context.md for Ifeoma's full background
3. Complete all 4 steps in order
4. Write the full optimized CV
5. Flag all gaps honestly
6. Save to outputs/career/CV_[JOBTITLE]_[COMPANY]_
   [YYYYMMDD].md

## QUALITY GATES
Before saving output, confirm:
[ ] Every ATS keyword from job post added naturally
[ ] Summary rewritten to match job title
[ ] Most relevant experience appears first
[ ] No fabricated experience or inflated metrics
[ ] Gaps identified and addressed honestly
[ ] Fit score calculated correctly
[ ] Output is a complete CV — not just the changes

## OUTPUT STRUCTURE
CV OPTIMIZATION — Ifeoma Onyemaechi
=====================================
Job title: [title]
Company: [company]
Platform: [platform]
Date: [date]

JOB ANALYSIS:
Required skills in CV: [list]
Required skills NOT in CV: [list]
ATS keywords added: [list]
Fit score: [X/10]
Recommendation: [Apply now / Apply with note / Skip]

OPTIMIZED CV:
[Complete rewritten CV — ready to copy and submit]

GAPS REPORT:
[Honest gaps with specific suggestions to address each]

## METRICS TO LOG
- Job title and company
- Fit score
- ATS keywords added
- Time to complete
- Recommendation