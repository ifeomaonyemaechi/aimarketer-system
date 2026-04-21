# Skill: qualify-lead
# Ifeoma Automation Operations System

## PURPOSE
Score and qualify an inbound lead or job post against the AIMarketer.co
ideal client profile. Produce a structured qualification report with a
numeric score, tier, recommendation, and ready-to-use outreach opener.

## INPUTS REQUIRED
- Brand name and contact (if known)
- Platform (Upwork, Contra, PeoplePerHour, LinkedIn, email/DM)
- Lead brief or job post text

## STEPS

1. Answer all 7 qualification questions:
   1. What is their core problem? (one sentence)
   2. What platform are they on?
   3. What industry are they in?
   4. Do they use Klaviyo or Shopify?
   5. What is their budget (if stated)?
   6. What service does this map to?
   7. What is the closest portfolio proof point?

2. Apply the scoring rubric:

   GREEN FLAGS (add points):
   - Shopify or eCommerce brand: +20
   - Uses or mentions Klaviyo: +20
   - Mentions email marketing problem: +15
   - Mentions content volume or consistency problem: +15
   - Founder-led, 1-5 person team: +10
   - Fitness, wellness, beauty, sustainable fashion, home/lifestyle: +10
   - Budget mentioned and above R5,000 / $300: +10
   - Mentions AI or automation interest: +10
   - Active on Instagram or TikTok: +5
   - Has existing email list: +5

   RED FLAGS (subtract points):
   - No budget mentioned and timeline is urgent: -15
   - B2B or SaaS product (not eCommerce): -20
   - Wants one-off task with no system thinking: -10
   - Mentions 10+ other applicants already hired: -10
   - Asks for spec work or free samples: -20
   - Brief is vague with no specific problem stated: -15
   - Requires tools Ifeoma doesn't use (HubSpot, Mailchimp as primary): -10

3. Assign a tier:
   - 90–100: Priority — write outreach immediately
   - 70–89: Strong — write outreach within 24 hours
   - 50–69: Moderate — pursue if pipeline is quiet
   - 30–49: Weak — deprioritise, template outreach only
   - 0–29: Skip — not a fit, do not pursue

4. Write a 2–3 sentence recommendation: whether to pursue, which service
   to lead with, and which proof point to reference.

5. Write 3 outreach opener options (A/B/C) customised to this specific lead.

## OUTPUT FORMAT

LEAD QUALIFICATION — AIMarketer.co
====================================
Lead name: [name]
Platform: [platform]
Date qualified: [date]

QUALIFICATION ANSWERS:
1. Core problem: [answer]
2. Platform: [answer]
3. Industry: [answer]
4. Klaviyo/Shopify: [yes / no / unknown]
5. Budget: [amount or "not stated"]
6. Service match: [service name]
7. Closest proof point: [metric or result]

SCORING:
Green flags triggered: [list each with points]
Red flags triggered: [list each with points]
Total score: [X]/100

TIER: [Priority / Strong / Moderate / Weak / Skip]

RECOMMENDATION:
[2–3 sentences — specific, not generic]

SUGGESTED FIRST LINE FOR OUTREACH:
Option A (problem-led): [line]
Option B (result-led): [line]
Option C (specific-to-brief): [line]

QUALITY CHECKLIST:
[x] All 7 questions answered
[x] Score calculated from green and red flags only
[x] Tier assigned correctly
[x] Recommendation is specific, not generic
[x] Suggested first line is customised to this lead

METRICS LOG:
- Lead: [name] | [platform]
- Final score: [X]/100
- Tier: [tier]
- Time to qualify: [time]
- Service recommended: [service]

## SAVE RULE
Save output to: outputs/AIMARKETER_QUALIFY_[CLIENTNAME]_[YYYYMMDD].md
