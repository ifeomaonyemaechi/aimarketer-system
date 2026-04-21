# Skill: Write Follow-Up Sequence
# Ifeoma Automation Operations System

## WHAT THIS SKILL DOES
Generates a 3-touch follow-up sequence for a single lead
who has not responded to initial outreach. Called by the
outreach-writer agent. Each touch uses a different angle —
value, relevance, and clean close.

## WHEN TO USE THIS SKILL
Use when:
- Initial outreach has been sent with no response after 3 days
- A warm lead has gone quiet
- A job post applicant needs follow-up

## THE 3-TOUCH RULE
Maximum 3 follow-up touches per lead. No exceptions.
After touch 3, mark the lead as closed and move on.

## TOUCH STRUCTURE

### Touch 1 — VALUE ADD (Day 3 after initial outreach)
PURPOSE: Give something useful before asking for anything.
ANGLE: Share an insight, data point, or observation
specific to their industry or situation.
TONE: Helpful, peer-to-peer, no pitch.
LENGTH: Under 100 words.
MUST NOT: Mention the previous email or ask if they saw it.
MUST: Reference something current or specific to their brand.

### Touch 2 — TIMELY RELEVANCE (Day 7 after initial outreach)
PURPOSE: Create genuine urgency using a real opportunity.
ANGLE: Seasonal moment, algorithm change, competitor move,
or market timing that is relevant to them right now.
TONE: Informative, direct, slightly urgent but not pushy.
LENGTH: Under 120 words.
MUST NOT: Use manufactured urgency or fake deadlines.
MUST: Reference a specific window of opportunity with
a real reason why it closes.

### Touch 3 — CLEAN CLOSE (Day 14 after initial outreach)
PURPOSE: Give them an easy yes or no. Leave with dignity.
ANGLE: Honest final message. No guilt. No countdown.
Acknowledge it may not be the right time.
TONE: Calm, direct, respectful.
LENGTH: Under 80 words.
MUST NOT: Guilt trip, use "just checking in", or beg.
MUST: Leave the door open for future contact.
MUST: Include one final low-friction offer or insight.

## EXECUTION INSTRUCTIONS
1. Confirm lead name, brand, and initial outreach date
2. Confirm what was sent in the initial outreach
3. Write all 3 touches in sequence
4. Each touch must have a different angle
5. Check word counts for each touch
6. Run quality checklist
7. Save to outputs/AIMARKETER_FOLLOWUP_[BRAND]_[YYYYMMDD].md

## QUALITY GATES
Before saving output, confirm:
[ ] Touch 1 gives value without asking for anything
[ ] Touch 2 uses real urgency — not manufactured
[ ] Touch 3 is clean and leaves door open
[ ] No touch says "just checking in" or "following up"
[ ] Each touch is a different angle
[ ] Word counts respected for each touch
[ ] No banned agency words used

## OUTPUT STRUCTURE
FOLLOW-UP SEQUENCE — AIMarketer.co
====================================
Lead: [name]
Brand: [brand name]
Initial outreach date: [date]
Platform: [platform]

TOUCH 1 — VALUE ADD (Send: Day 3)
Subject (if email): [subject line]
Message: [full message]
Word count: [number]

TOUCH 2 — TIMELY RELEVANCE (Send: Day 7)
Subject (if email): [subject line]
Message: [full message]
Word count: [number]

TOUCH 3 — CLEAN CLOSE (Send: Day 14)
Subject (if email): [subject line]
Message: [full message]
Word count: [number]

SEQUENCE SUMMARY:
Total touches: 3
Total word count: [number]
Recommended send dates: [date 1], [date 2], [date 3]

## METRICS TO LOG
- Lead name and brand
- Platform
- Time to generate all 3 touches
- Total word count
- Angles used per touch