# AIMarketer.co — Agency Operations System
# Powered by Claude Code | Built by Ifeoma Onyemaechi

## SYSTEM OVERVIEW
This is the agency operations system for AIMarketer.co, an
AI-powered marketing automation agency. This system handles
all client-facing work: lead generation, outreach, proposal
writing, audit delivery, and campaign management for clients.

## ABOUT AIMARKETER.CO
Agency: Ifeoma Automation — AI-powered marketing automation agency
Website: ifeomaautomation.com
Founder: Ifeoma Onyemaechi
Specialty: AI-powered marketing automation for eCommerce and
Shopify brands
Background: DevOps/DevSecOps + Klaviyo email marketing
Differentiator: Technical infrastructure thinking applied to
marketing automation — rare combination
Contact: ifeomaonyemaechi1@gmail.com
Platforms: Contra, Upwork, PeoplePerHour, Linkedin

## IDEAL CLIENT PROFILE
- Shopify or eCommerce brands doing R50,000-R500,000/month
- Using Klaviyo or considering it
- 1-5 person team, founder-led
- Posting on Instagram and/or TikTok
- Has email list but not maximising it
- Frustrated with content volume and consistency
- Industries: fitness, wellness, beauty, sustainable fashion,
  home and lifestyle

## AGENCY VOICE
Direct. Specific. Builder energy. No buzzwords.
We don't "leverage synergies" or "unlock potential."
We build systems, fix flows, and show the revenue impact.

Never use: leverage, synergy, unlock potential, cutting-edge,
revolutionary, game-changing, world-class, holistic approach,
best-in-class, innovative solutions

Always use: specific metrics, time saved, revenue recovered,
flows built, emails generated, seconds to completion

## AGENTS
All subagents live in .claude/agents/. Each handles one
agency function.

- lead-qualifier — scores and qualifies inbound leads
- outreach-writer — writes cold email, LinkedIn, and DM copy
- proposal-writer — generates client proposals from briefs
- campaign-manager — manages client campaign execution

## SKILLS
Reusable task templates live in .claude/skills/.

- qualify-lead.md
- write-cold-outreach.md
- write-follow-up-sequence.md
- generate-proposal.md
- write-audit-summary.md

## SLASH COMMANDS
/qualify [lead brief] — score and qualify a lead
/outreach [brand name] [platform] — generate outreach message
/proposal [client brief] — generate full proposal
/followup [lead name] [touch number] — generate follow-up
/audit-summary [channel data] — generate audit summary

## FOLDER STRUCTURE
.claude/agents/ — subagent definition files
.claude/skills/ — reusable skill markdown files
.claude/hooks/ — pre and post hooks for quality control
context/ — agency context, client profiles, templates
scripts/ — Python scripts using the Anthropic API
outputs/ — all generated content saved here

## OUTPUT RULES
- All generated content saved to outputs/ with timestamp
- Format: AIMARKETER_[TYPE]_[CLIENTNAME]_[YYYYMMDD].md
- Every proposal must include metrics from portfolio
- Every outreach message must reference something specific
  about the prospect's brand — no generic templates

## METRICS TO TRACK
Log these for every generation run:
- Task type
- Client or lead name
- Number of pieces generated
- Time to completion
- Touchpoints created