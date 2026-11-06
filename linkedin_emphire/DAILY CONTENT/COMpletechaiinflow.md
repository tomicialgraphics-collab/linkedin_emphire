═══════════════════════════════════════
🔗 CHAIN: DAILY POST CREATION
═══════════════════════════════════════

PURPOSE: Create a complete LinkedIn post from 
scratch, ready to publish
TIME: 15-20 minutes manually
AUTOMATED TIME: 3-5 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: TOPIC IDEATION
Agent: Strategist
Input: Today's date, day of week, pillar rotation, 
       recent post performance

Prompt:
"Based on my content pillar rotation and last week's 
performance, suggest today's post topic. Consider:
- Which pillar am I due to post from?
- What's my audience most engaged with lately?
- What's timely or trending in my space?
- What haven't I covered recently?

Return:
1. Recommended topic (specific)
2. Content pillar it serves
3. Suggested content style
4. Why this topic today
5. Angle recommendation"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: HOOK GENERATION
Agent: Content Creator
Input: Topic + angle from Step 1

Prompt:
"Using this topic and angle: [PASTE STEP 1 OUTPUT]

Generate 5 hook options using different styles:
1. Story-based hook
2. Question hook
3. Bold statement hook
4. Statistic/data hook
5. Contrarian opinion hook

For each hook:
- Full text
- Style used
- Predicted engagement type
- Emotion it triggers

Then recommend the strongest hook with reasoning."

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: FULL POST WRITING
Agent: Content Creator
Input: Selected hook from Step 2

Prompt:
"Using this hook: [PASTE SELECTED HOOK]

Write the complete LinkedIn post:

Requirements:
- 800-1500 characters
- Line breaks between paragraphs (max 2 lines each)
- Bold key phrases with asterisks
- Uses '→' for lists
- Natural CTA at end
- My authentic voice (reference voice_dna.txt)
- Zero banned words
- Include personal experience/perspective

Structure:
- Hook (2-3 lines)
- Context/problem
- Insight/story/framework
- Practical takeaway
- Natural CTA
- Optional: 3 relevant hashtags

Return the complete post ready to publish."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: VOICE VERIFICATION
Agent: Content Creator (or dedicated voice checker)
Input: Complete post from Step 3

Prompt:
"Review this post: [PASTE POST]

Voice check:
□ Does it sound like Timothy?
□ Are contractions used naturally?
□ Includes personal perspective?
□ Zero banned words used?
□ Has em dashes, fragments, or rhetorical questions?
□ Nigerian/African context if relevant?
□ Ends with natural CTA?

If any check fails, rewrite that section.
Return either:
- APPROVED: [post as-is]
- REVISED: [improved version]

Explain any changes made."

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: VISUAL BRIEF (Optional)
Agent: Visual Designer
Input: Approved post from Step 4

Prompt:
"For this post: [PASTE APPROVED POST]

Determine if it needs a visual:
- Text-only post (no visual): Justify why
- Simple graphic: Provide design brief
- Carousel: Provide multi-slide outline

If visual recommended, provide:
1. Type (poster/carousel/quote card)
2. Layout recommendation (A-F from templates)
3. Photo pose suggestion
4. Text overlay (max 6 words)
5. Color scheme
6. Canva execution steps"

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: METADATA & PUBLISHING PREP
Agent: Strategist
Input: Post + visual from Steps 4-5

Prompt:
"Prepare publishing metadata:

1. Best posting time (based on my audience)
2. Three relevant hashtags
3. Suggested tags (people to tag if relevant)
4. Predicted performance (LOW/MED/HIGH)
5. Follow-up plan (comments to engage with)
6. Cross-platform adaptation notes

Also provide:
- 2 alternative CTAs to test
- Reply templates for likely comments
- Follow-up post ideas from this post"

Output → FINAL: Complete content package

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Approved post ready to publish
✓ Visual design brief (if needed)
✓ Hashtags and metadata
✓ Best posting time
✓ Predicted performance
✓ Alternative CTAs
✓ Reply templates
✓ Follow-up content ideas

═══════════════════════════════════════
HOW TO RUN THIS CHAIN:
═══════════════════════════════════════

MANUAL METHOD (Using ChatGPT Projects):

1. Open Strategist project → Run Step 1
2. Copy output
3. Open Content Creator project → Paste output → Run Step 2
4. Copy output
5. Same project → Paste output → Run Step 3
6. Continue through all steps

Time: 15-20 minutes total

AUTOMATED METHOD (Using CrewAI or similar):

Build workflow that:
- Calls each agent sequentially
- Passes outputs automatically
- Returns final package

Time: 3-5 minutes total (mostly waiting for API)



═══════════════════════════════════════
🔗 CHAIN: WEEKLY 5-POST BATCH
═══════════════════════════════════════

PURPOSE: Create all 5 posts for the week in one 
session (Sunday batching)
TIME: 90 minutes manually
AUTOMATED: 15-20 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: WEEKLY REVIEW
Agent: Strategist
Input: Last week's performance data

Prompt:
"Analyze last week's LinkedIn performance:

[PASTE YOUR METRICS - impressions, engagement, 
best/worst posts, follower growth]

Provide:
1. Performance summary (3 sentences)
2. What worked (with why)
3. What didn't work (with why)
4. Pillar balance analysis
5. Emerging patterns
6. Recommendations for next week"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: WEEKLY THEME & CALENDAR
Agent: Strategist
Input: Review from Step 1

Prompt:
"Based on last week's analysis and my pillar rotation, 
plan next week's 5 posts (Monday-Friday):

For each day, provide:
- Day and best posting time
- Content pillar (across the week: balance!)
- Content style (variety across the week)
- Specific topic
- Hook angle
- Predicted performance

Rules:
- No same pillar two days in row
- Mix of technical + leadership + personal
- Include at least 1 story post
- Include at least 1 opinion/hot take
- Include at least 1 educational/framework

Return as calendar table with all 5 posts outlined."

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: BATCH POST WRITING
Agent: Content Creator
Input: Calendar from Step 2

Prompt:
"Write complete LinkedIn posts for all 5 days.

Here's the week plan: [PASTE CALENDAR]

For each post:
1. Generate 3 hook options
2. Select strongest
3. Write full 800-1500 char post
4. Format with proper line breaks
5. Include natural CTA
6. Suggest 3 hashtags

Ensure:
- Voice consistency across all 5
- Zero banned words in any post
- Variety in structure/style
- Each stands alone and provides value

Return all 5 complete posts, clearly separated 
by day."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: VOICE & QUALITY REVIEW
Agent: Content Creator
Input: All 5 posts from Step 3

Prompt:
"Review all 5 posts:

[PASTE ALL 5 POSTS]

Quality check for each:
- Voice matches Timothy
- No banned words
- Has hook that stops scrolling
- Contains real insight/value
- Ends with natural CTA
- Mobile-friendly formatting

Flag any that need revision.
Provide improved versions where needed.

Return:
- Approved posts (as-is)
- Revised posts (with changes explained)"

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: VISUAL BRIEFS FOR CAROUSEL DAYS
Agent: Visual Designer
Input: Approved posts

Prompt:
"Review these 5 posts: [PASTE APPROVED POSTS]

Identify 2-3 posts that would benefit from carousels 
or posters.

For each visual-worthy post:
1. Determine visual type (poster/carousel/quote)
2. Provide complete design brief
3. Slide-by-slide script if carousel
4. Photo pose recommendation
5. Canva execution steps

Return visual briefs for chosen posts."

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: SCHEDULING & PUBLICATION PACKAGE
Agent: Strategist
Input: All posts and visuals

Prompt:
"Create the complete publication package for this week:

For each of the 5 posts:
- Day and time to publish
- Hashtag recommendations
- Predicted performance
- Optional engagement strategy
- Follow-up post ideas from each

Also provide:
- Weekly engagement targets (comments, DMs, etc.)
- Creators to prioritize engaging with this week
- Any collaboration opportunities to pursue
- One optional Friday/Saturday casual post idea

Format as a week-at-a-glance publishing plan."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ 5 complete posts (Mon-Fri) ready to schedule
✓ 2-3 visual design briefs
✓ Publishing calendar with times
✓ Hashtags for each post
✓ Engagement strategy for the week
✓ Performance predictions
✓ Bonus content ideas for weekend







═══════════════════════════════════════
🔗 CHAIN: DAILY ENGAGEMENT ROUTINE
═══════════════════════════════════════

PURPOSE: Prepare all daily comments and engagement
TIME: 15 minutes manually
AUTOMATED: 3-5 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: TARGET IDENTIFICATION
Agent: Strategist
Input: List of target creators + today's date

Prompt:
"For today's engagement session, identify which 
creators to prioritize.

From my target creator list: [PASTE OR REFERENCE]

Consider:
- Who posts frequently and I haven't engaged with recently?
- Who has posted in last 24 hours (high visibility)?
- Who aligns with today's content focus?
- Who's in my target industries (AI, engineering, career)?

Return:
- Top 10 creators to engage with today
- 1-line reason for each
- Suggested comment type (agreement/challenge/story/question)"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: COMMENT GENERATION (Batch)
Agent: Engagement Specialist
Input: Target list + their recent posts

Prompt:
"For each of these 10 creator posts, generate a 
substantive comment:

[PASTE 10 POSTS OR SUMMARIES]

For each post, provide:
1. Brief post summary (so I remember what it's about)
2. THREE comment options:
   A) Add expertise angle
   B) Personal story angle  
   C) Respectful challenge angle
3. Recommended option with reasoning
4. Tone notes

Requirements:
- Never generic ('great post!')
- Reference specific point from their post
- Add value or perspective
- Include personal experience where relevant
- 3-5 sentences ideal
- Natural voice (contractions, phrases)
- Zero banned words

Return all 10 comment sets."

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: DM DRAFTING (If any warm leads)
Agent: Engagement Specialist
Input: Warm connection list

Prompt:
"Draft DMs for these warm connections today:

[LIST OF PEOPLE TO DM]

For each person, provide:
1. Context reminder (why we're connecting/who they are)
2. Initial DM (if new connection)
3. Follow-up DM (if continuing conversation)
4. Value-add message (if warming a relationship)

Rules:
- Under 100 words each
- Personalized to them specifically
- Value-first, no pitching
- Ends with easy-to-answer question
- Warm but professional"

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: COMMENT REPLIES (On my posts)
Agent: Engagement Specialist
Input: Comments received on my recent posts

Prompt:
"Draft replies to these comments on my posts:

[PASTE COMMENTS]

For each comment:
1. Reply draft (2-3 sentences)
2. Alternative version if they were:
   - Disagreeing
   - Asking a question
   - Just being nice
3. Whether to continue conversation further

Requirements:
- Acknowledge their specific point
- Add value or continue conversation
- Include question when appropriate
- Warm but not overly formal
- Reference their comment specifically"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ 10 comments ready to post on target creators' posts
✓ 3-5 DMs ready to send
✓ Replies to comments on my posts
✓ Estimated 15 minutes to execute all










═══════════════════════════════════════
🔗 CHAIN: JOB APPLICATION PACKAGE
═══════════════════════════════════════

PURPOSE: Complete application package for a single 
job opportunity
TIME: 45-60 minutes manually
AUTOMATED: 15-20 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPPORTUNITY ANALYSIS
Agent: Opportunities Manager
Input: Job description

Prompt:
"Analyze this job opportunity:

[PASTE FULL JOB DESCRIPTION]

Also provide:
- Company name and industry
- Any info about hiring manager if available

Provide:
1. Role summary
2. Required vs. nice-to-have skills breakdown
3. My match analysis:
   - Skills I have (with evidence from my background)
   - Skills I'm missing (with mitigation ideas)
4. Overall fit score (1-10)
5. Should I apply? (honest recommendation)
6. Key differentiators I bring
7. Potential concerns to address in application
8. Salary range research direction"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: RESEARCH & PREPARATION
Agent: Strategist + Opportunities Manager
Input: Analysis from Step 1

Prompt:
"Based on the analysis, prepare:

1. Company research to do:
   - Recent news to check
   - Products/services to understand
   - Company culture indicators to research
   - Team members to look up on LinkedIn

2. Hiring manager research (if identifiable):
   - Their background patterns
   - Their recent posts/interests
   - Common connections
   - Best angle for outreach

3. Application strategy:
   - Priority skills to emphasize
   - Stories to include
   - Multi-domain background angle
   - Nigerian/African perspective angle

4. Materials to prepare:
   - Portfolio pieces relevant to role
   - Case studies from my work
   - Certifications to highlight"

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: LINKEDIN CONNECTION REQUEST
Agent: Opportunities Manager
Input: Hiring manager info + strategy

Prompt:
"Craft a LinkedIn connection request for the 
hiring manager:

Requirements:
- Under 300 characters
- References something specific about them or company
- Does NOT mention the job initially
- Professional but warm
- Sounds like Timothy wrote it
- Culturally appropriate

Provide 3 versions:
A) Based on their recent post/activity
B) Based on company news/product
C) Based on shared interest/connection

Recommend the strongest."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: FOLLOW-UP DM AFTER CONNECTION
Agent: Opportunities Manager
Input: Connection accepted context

Prompt:
"Draft the follow-up DM to send after they accept 
the connection request:

Requirements:
- Under 150 words
- Acknowledges the connection
- Provides some value
- Naturally mentions your interest
- Asks intelligent question about team/role
- Doesn't seem transactional

Provide 2 versions:
A) Value-first approach (share something useful)
B) Question-first approach (ask about their work)

Recommend based on context."

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: APPLICATION COVER MESSAGE
Agent: Opportunities Manager
Input: All previous outputs

Prompt:
"Write the cover message/letter for the application:

Requirements:
- 150-200 words
- Leads with strongest relevant achievement
- Connects multi-domain background to role
- Specific to their company/needs
- Ends with clear next step
- Sounds like Timothy wrote it
- Not generic

Include:
- Opening hook (why I'm reaching out)
- 2-3 key relevant achievements with numbers
- Why I'm interested in THIS company
- What I can bring specifically
- Clear CTA (interview/call request)"

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: PROFILE OPTIMIZATION SUGGESTIONS
Agent: Strategist + Opportunities Manager
Input: Job requirements + current profile

Prompt:
"Based on this specific role, suggest LinkedIn 
profile optimizations:

1. Headline tweaks (if any)
2. About section adjustments (paragraphs to emphasize)
3. Featured section priorities
4. Skills to add or reorder
5. Experience descriptions to strengthen
6. Any new content to post before applying (to be 
   visible when they check my profile)

Note: Only recommend changes that align with my 
overall brand strategy, not just this one role."

Output → Feed to Step 7

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 7: INTERVIEW PREPARATION
Agent: Opportunities Manager
Input: Full role and application context

Prompt:
"Prepare initial interview materials:

1. Likely interview questions (10-15) based on JD

2. Answer frameworks for each (not scripts):
   - STAR method for behavioral
   - Technical answer structures
   - Company-specific angles

3. Smart questions to ask them (5-7):
   - About the team
   - About the role
   - About the technology
   - About growth/learning
   - About company culture

4. Salary negotiation preparation:
   - Market research direction
   - My value proposition
   - Response templates for common tactics
   - Walk-away number thinking

5. Follow-up sequence:
   - Thank you email template
   - Follow-up after 1 week if no response
   - Second follow-up after 2 weeks"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Complete opportunity analysis with recommendation
✓ Research checklist for company/hiring manager
✓ LinkedIn connection request (3 options + rec)
✓ Follow-up DM (2 options + rec)
✓ Application cover message
✓ Profile optimization checklist
✓ Interview prep materials
✓ Follow-up sequence templates









═══════════════════════════════════════
🔗 CHAIN: WEEKLY NEWSLETTER CREATION
═══════════════════════════════════════

PURPOSE: Complete Substack newsletter issue
TIME: 3-4 hours manually
AUTOMATED: 45-60 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: TOPIC SELECTION
Agent: Empire Builder + Strategist
Input: Recent LinkedIn posts, current events, 
       content bank

Prompt:
"Choose this week's Substack newsletter topic.

Consider:
- What was my best-performing LinkedIn post recently?
- What deserves longer exploration (2000+ words)?
- What questions have people been asking me?
- What's trending in AI/tech that I have a take on?
- What personal experience is worth expanding?

Return:
1. Recommended topic
2. Why this topic now (timeliness)
3. Angle/perspective to take
4. Predicted resonance with audience
5. Alternative topic if you'd choose differently"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: OUTLINE CREATION
Agent: Empire Builder
Input: Selected topic from Step 1

Prompt:
"Create detailed outline for Substack newsletter:

Topic: [PASTE FROM STEP 1]

Provide:
1. Working title (specific, intriguing)
2. Subtitle (what they'll learn)
3. Full outline:
   - Personal opener hook (100-150 words topic)
   - Main insight structure (7-10 sections)
   - Supporting examples/stories to include
   - Any frameworks or lists
   - Practical applications
4. Approximate word count per section
5. Total estimated length (aim for 1500-2500 words)"

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: DRAFT WRITING (Section by Section)
Agent: Empire Builder (Content Creator)
Input: Outline from Step 2

Prompt:
"Write the full newsletter draft using this outline: 
[PASTE OUTLINE]

Requirements:
- Match my authentic voice (reference voice_dna.txt)
- Personal opener with specific moment/story
- Deep exploration of main topic
- Include specific examples from my experience
- Add relevant code snippets if technical
- Include 1-2 rhetorical questions
- Include em dashes for emphasis
- Use short paragraphs (1-3 sentences typically)
- Zero banned words
- 1500-2500 words total

Structure sections clearly with subheadings.
End with question for readers to reply to."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: SUPPLEMENTARY SECTIONS
Agent: Empire Builder
Input: Main draft from Step 3

Prompt:
"Now add the supplementary sections to complete 
the newsletter:

For the newsletter draft: [REFERENCE DRAFT]

Create:

1. WHAT I'M READING (100 words)
   - 2-3 articles/posts/books I've engaged with
   - Brief description of each
   - Why worth reading

2. COMMUNITY HIGHLIGHT (50 words)
   - Spotlight on someone in my network
   - Their recent work worth sharing
   - Genuine appreciation

3. QUESTION FOR REPLIES (1 sentence)
   - Related to main topic
   - Easy to answer
   - Sparks conversation

4. SIGN-OFF
   - Personal note
   - Reminder about following on LinkedIn
   - Warm closing"

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: EDITING & POLISHING
Agent: Empire Builder
Input: Complete draft with all sections

Prompt:
"Edit and polish the complete newsletter:

[PASTE FULL DRAFT]

Check for:
1. Voice consistency throughout
2. Zero banned words
3. Sentence variety (mix short/long)
4. Strong opening (hook that pulls in)
5. Smooth transitions between sections
6. Compelling ending that invites replies
7. Any redundancies to cut
8. Any unclear points to clarify
9. Grammar and flow
10. Overall readability

Provide:
- Final polished version
- List of major changes made
- Any sections that could still improve"

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: PROMOTIONAL CONTENT
Agent: Content Creator + Empire Builder
Input: Final newsletter

Prompt:
"Create promotional content for the newsletter:

Newsletter title: [PASTE]
Main insight: [BRIEF SUMMARY]

Create:

1. LINKEDIN POST (Friday morning)
   - Announces the newsletter is out
   - Hook that makes people want to read
   - 800-1200 characters
   - Link at end

2. X (TWITTER) THREAD (Friday morning)
   - 5-8 tweets
   - Key insights from newsletter
   - Ends with link and CTA

3. EMAIL SUBJECT LINE (2-3 options)
   - For the newsletter itself
   - Under 60 characters
   - Compelling and specific

4. SHORT SOCIAL BLURB
   - For LinkedIn Notes or Stories
   - 1-2 sentences with hook

5. FOLLOW-UP LINKEDIN POST (Monday)
   - References newsletter
   - Different angle on same topic
   - Continues the conversation"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Complete polished Substack newsletter (1500-2500 words)
✓ All supplementary sections
✓ LinkedIn promotional post
✓ Twitter thread version
✓ Email subject lines to test
✓ Social media blurbs
✓ Follow-up content ideas
✓ Estimated total: 3-4 hours saved compared to manual











═══════════════════════════════════════
🔗 CHAIN: ONE POST → MULTI-PLATFORM
═══════════════════════════════════════

PURPOSE: Turn one great LinkedIn post into 
multiple platform-specific pieces
TIME: 45 minutes manually
AUTOMATED: 10 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: SOURCE POST ANALYSIS
Agent: Empire Builder
Input: High-performing LinkedIn post

Prompt:
"Analyze this LinkedIn post for cross-platform 
amplification:

[PASTE HIGH-PERFORMING POST]

Analysis:
1. Core insight/message (in one sentence)
2. Key supporting points
3. Personal story elements
4. Data/examples used
5. What made it work (why it performed well)
6. Multi-platform potential rating (1-10)

Then identify:
- Which platforms would benefit from this content
- What angle works best on each platform
- What length is appropriate for each"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: X (TWITTER) THREAD VERSION
Agent: Empire Builder
Input: Analysis from Step 1

Prompt:
"Convert the LinkedIn post into an X thread:

Original: [REFERENCE ORIGINAL POST]

Create a Twitter thread:
- 8-15 tweets total
- Each tweet under 280 characters
- Tweet 1: Hook that stops scroll
- Middle tweets: Build value progressively
- Last tweet: CTA (follow/RT/subscribe)

Requirements:
- Adapt to X culture (more casual, punchy)
- Each tweet can stand alone
- Numbered thread (2/x, 3/x format)
- Use line breaks within tweets for readability
- Emojis okay but sparingly (1-2 per tweet)

Also provide:
- Best time to post on X
- Suggested hashtags (max 2)"

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: STANDALONE X TWEETS
Agent: Empire Builder
Input: Original post + thread from Step 2

Prompt:
"Create 5 standalone X tweets from the same source:

Each tweet should:
- Extract ONE insight from the original post
- Work completely standalone
- Be under 280 characters
- Have its own hook
- Not require the original post for context

Vary the styles:
1. Observation tweet
2. Contrarian tweet  
3. Framework/list tweet
4. Question tweet
5. Personal insight tweet

These will be posted throughout the week to keep 
the topic alive on X."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: SUBSTACK EXPANSION
Agent: Empire Builder
Input: Original post + thread + tweets

Prompt:
"Create Substack expansion of this content:

Take the core insight from the LinkedIn post and 
expand it into a full Substack section (800-1500 
words).

Add:
- More personal story details
- Additional examples
- Deeper analysis
- Frameworks or step-by-step guidance
- Nuance not possible in LinkedIn's character limit
- Personal reflection at the end

Format:
- Compelling subheading
- Multiple sections with subheadings
- Rich detail
- Substack voice (more personal, longer)

This could be:
- Full newsletter issue
- Section within a larger newsletter
- Guest post pitch to other newsletters"

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: BLOG POST VERSION (Optional)
Agent: Empire Builder + Content Creator
Input: All previous versions

Prompt:
"Create a blog post version for personal website:

Requirements:
- 2000-3500 words (SEO-friendly length)
- H1, H2, H3 headings for structure
- Include images/diagrams recommendations
- Add code snippets if technical
- SEO-optimized title
- Meta description (150-160 chars)
- Suggested featured image
- Internal linking opportunities
- Call-to-action at end

Format:
- Introduction (hook + what they'll learn)
- Body (structured with subheadings)
- Conclusion (summary + CTA)
- Author bio (short version)

This blog post can:
- Live on your website
- Be pitched as guest post
- Be turned into a video script"

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: PROMOTION SCHEDULE
Agent: Strategist
Input: All content pieces created

Prompt:
"Create a 2-week promotion schedule for all this 
content:

WEEK 1:
Monday: Original LinkedIn post (already published)
Tuesday: [Recommend which piece]
Wednesday: [Recommend which piece]
Thursday: [Recommend which piece]
Friday: [Recommend which piece]

WEEK 2:
[Continue schedule with different platforms]

For each publication, specify:
- Platform
- Content piece to use
- Best time to post
- Specific promotional angle
- Which pieces should reference other pieces
- How to build compounding audience effect

Also include:
- Engagement strategy for each platform
- Cross-linking recommendations
- Metrics to track"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Original LinkedIn post (source)
✓ Complete X thread (8-15 tweets)
✓ 5 standalone tweets to spread out
✓ Substack expansion/section
✓ Full blog post version
✓ 2-week promotion schedule
✓ Cross-platform strategy

From ONE post → 20+ pieces of content













═══════════════════════════════════════
🔗 CHAIN: DEEP MONTHLY REVIEW
═══════════════════════════════════════

PURPOSE: Comprehensive month review with strategic 
adjustments
TIME: 90 minutes manually
AUTOMATED: 20-30 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: DATA COLLECTION
Agent: Strategist
Input: Monthly metrics from all platforms

Prompt:
"Analyze this month's complete performance data:

LINKEDIN METRICS:
[Paste: total impressions, engagement rate, top posts, 
worst posts, follower growth, profile views, etc.]

SUBSTACK METRICS (if applicable):
[Paste: subscribers, open rate, click rate, best 
performing issues, etc.]

X (TWITTER) METRICS (if applicable):
[Paste: followers, impressions, top tweets, etc.]

OTHER METRICS:
[Any client work, opportunities, income, etc.]

Provide comprehensive summary:
1. Overall growth (all platforms)
2. Engagement quality (not just quantity)
3. Best performing content types
4. Worst performing content types
5. Emerging patterns
6. Audience shifts
7. Opportunity indicators"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: PATTERN ANALYSIS
Agent: Strategist
Input: Data summary from Step 1

Prompt:
"Deep pattern analysis:

Based on this month's data:

1. WHAT'S WORKING:
   - Specific content that resonates
   - Times/days that perform best
   - Topics with highest engagement
   - Formats that drive followers

2. WHAT'S NOT WORKING:
   - Content types that flop
   - Times that underperform
   - Topics losing interest
   - Formats to abandon

3. PILLAR BALANCE ANALYSIS:
   - Which pillars got most attention?
   - Which pillars are underrepresented?
   - Which pillars drive best engagement?
   - Recommendations for balance shift

4. AUDIENCE INSIGHTS:
   - Who's engaging most?
   - What kind of people are following?
   - Are these my target audience?
   - Any audience shift concerns?

5. VOICE & POSITIONING CHECK:
   - Is my positioning coming through?
   - Am I attracting the right people?
   - Are my differentiators clear?
   - Any drift from strategy?"

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: STRATEGIC ADJUSTMENTS
Agent: Strategist
Input: Pattern analysis

Prompt:
"Based on this analysis, recommend strategic 
adjustments for next month:

1. CONTENT ADJUSTMENTS:
   - Content pillars to prioritize
   - Content styles to try more of
   - Content styles to abandon
   - Topics to explore
   - Topics to avoid

2. POSTING STRATEGY:
   - Optimal posting times based on data
   - Optimal posting frequency
   - Best days of week
   - Any format experiments to try

3. ENGAGEMENT STRATEGY:
   - Creators to prioritize engaging with
   - Community strategies to try
   - DM outreach opportunities
   - Collaboration possibilities

4. AUDIENCE BUILDING:
   - How to attract better audience match
   - What content will do this
   - How to filter for right people
   - Personal brand adjustments

5. PLATFORM PRIORITIES:
   - Where to double down
   - Where to reduce effort
   - Where to experiment
   - New platforms to consider

Format as actionable next-month plan."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: CONTENT PLAN FOR NEXT MONTH
Agent: Strategist + Content Creator
Input: Adjustments from Step 3

Prompt:
"Create high-level content plan for next month:

Based on the adjustments needed, plan:

WEEK 1 (Focus theme): [determined by data]
- Content pillar emphasis
- 5 post topic ideas
- Any special content (carousel, series, etc.)

WEEK 2 (Focus theme):
[Same structure]

WEEK 3 (Focus theme):
[Same structure]

WEEK 4 (Focus theme):
[Same structure]

Also plan:
- 4 Substack topics (one per week)
- Any special content initiatives
- Collaboration opportunities
- Speaking/podcast pitches
- Product/course promotion if applicable

Include metrics targets:
- Follower growth target
- Engagement rate target
- Newsletter subscriber target
- Any income targets"

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: GOAL PROGRESSION REVIEW
Agent: Strategist
Input: Original 90-day and 900-day goals

Prompt:
"Assess progress toward long-term goals:

MY GOALS:
- 90-day: [Reference original goals]
- 900-day: [Reference original goals]

Compare current position to targets:

1. ON TRACK METRICS:
   - Which goals are we on pace to hit?
   - Which are we exceeding?

2. BEHIND METRICS:
   - Which goals are falling behind?
   - What's the gap size?
   - What actions could close the gap?

3. RECALIBRATION NEEDED:
   - Any goals that need adjustment?
   - Any goals that should be more ambitious?
   - Any goals no longer serving me?

4. MOMENTUM CHECK:
   - Am I building compound momentum?
   - Are the right things compounding?
   - What might derail future compounding?

5. MOTIVATION CHECK:
   - Am I still excited about these goals?
   - Have my priorities shifted?
   - Any new goals emerging?

Provide honest assessment and any recommendations 
for goal adjustment."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Complete monthly analytics summary
✓ Pattern analysis with insights
✓ Strategic adjustments for next month
✓ 4-week content plan for next month
✓ Goal progression assessment
✓ Motivation and momentum check
✓ Clear priorities for the coming month











═══════════════════════════════════════
🔗 CHAIN: HANDLE INCOMING OPPORTUNITY
═══════════════════════════════════════

PURPOSE: Process any incoming opportunity 
professionally
TIME: 30 minutes manually
AUTOMATED: 10 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: OPPORTUNITY CATEGORIZATION
Agent: Opportunities Manager
Input: The message received

Prompt:
"Categorize this incoming opportunity:

[PASTE THE MESSAGE OR DM]

Also provide:
- Sender's info if known
- How we're connected (mutual, cold, previous work)

Categorize as:
□ Recruiter (job opportunity)
□ Consulting inquiry
□ Speaking invitation
□ Podcast/media invitation
□ Collaboration proposal
□ Partnership opportunity
□ Sales pitch (spam)
□ Mentorship request
□ Investment opportunity
□ Community/event invitation
□ Other: [specify]

Rate legitimacy (1-10):
- Is this genuinely worth pursuing?
- Any red flags?
- Any excellent signals?

Recommend response urgency:
□ Respond within 24 hours (high value)
□ Respond within 3 days (moderate value)
□ Respond when convenient (low priority)
□ No response needed (spam)"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: RESEARCH & CONTEXT GATHERING
Agent: Strategist + Opportunities Manager
Input: Categorization from Step 1

Prompt:
"For this opportunity, prepare research:

1. About the sender:
   - What to look up on LinkedIn
   - Their background/credibility
   - Their company/organization
   - Mutual connections

2. About the opportunity:
   - Market value if applicable
   - Similar opportunities I could compare to
   - Standard rates/terms if consulting
   - Typical process/timeline

3. Strategic fit:
   - How does this align with my 90-day goals?
   - How does this align with my 900-day vision?
   - Does this build my brand or dilute it?
   - What's the opportunity cost?

4. Questions to ask them:
   - What information do I need before deciding?
   - What would make this a clear yes?
   - What would make this a clear no?

5. Preparation needed:
   - Materials to have ready
   - Research to do
   - People to consult"

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: DECISION FRAMEWORK
Agent: Opportunities Manager
Input: Category + research

Prompt:
"Apply decision framework to this opportunity:

Score each dimension (1-10):

STRATEGIC ALIGNMENT:
- Aligns with career goals?
- Builds authority in my space?
- Serves my ideal audience?
- Uses my strengths?

FINANCIAL VALUE:
- Above/at/below market rate?
- Payment terms reasonable?
- Time-to-money ratio good?
- Opportunity cost acceptable?

LEARNING VALUE:
- Would I learn something significant?
- Would I meet valuable people?
- Would it open new doors?

RISK ASSESSMENT:
- Any red flags?
- Time commitment realistic?
- Reputational risk?
- Financial risk?

ENERGY MATCH:
- Am I genuinely excited about this?
- Does this energize or drain me?
- Does it fit my current capacity?

TOTAL SCORE (out of 50):
- 40+: Strong pursue
- 30-39: Pursue with caution
- 20-29: Consider carefully
- Below 20: Likely pass

RECOMMENDATION: [pursue/negotiate/decline]"

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: RESPONSE DRAFTING
Agent: Opportunities Manager
Input: Decision from Step 3

Prompt:
"Draft the response based on the decision:

DECISION: [pursue/negotiate/decline]

Provide THREE response options based on the decision:

IF PURSUING:
Option A: Enthusiastic acceptance with next steps
Option B: Interested but need more info (with questions)
Option C: Interested but with clear conditions/negotiation

IF DECLINING:
Option A: Warm decline with door left open
Option B: Decline with alternative suggestion
Option C: Decline with referral to someone else

IF NEGOTIATING:
Option A: Counter-offer with terms
Option B: Explore before committing
Option C: Test their flexibility

For each option:
- Complete message text
- Tone appropriate for the situation
- Length matched to opportunity type
- Voice authentic to Timothy
- Zero banned words
- Professional but warm

Recommend which option to use with reasoning."

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: FOLLOW-UP PLAN
Agent: Opportunities Manager
Input: Chosen response

Prompt:
"Create the follow-up plan:

Assuming the response goes out today, plan:

IF THEY RESPOND POSITIVELY:
- Next 24 hours: [specific actions]
- Next week: [specific actions]
- Any preparation needed

IF THEY DON'T RESPOND:
- Follow-up timing: [when]
- Follow-up message: [draft]
- Second follow-up if needed

IF THEY NEGOTIATE/PUSH BACK:
- Common objections to prepare for
- Response scripts for each
- Walk-away conditions

TRACKING:
- What to note about this conversation
- When to check back in your CRM/tracker
- Metrics to watch (do they view profile? engage?)

CONTINGENCY:
- If they say yes, but terms are wrong
- If they say no, but you want to stay connected
- If they ghost after initial interest"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Opportunity categorization and rating
✓ Complete research checklist
✓ Decision framework score
✓ Recommended response (3 options)
✓ Complete follow-up plan
✓ Contingency responses ready












═══════════════════════════════════════
🔗 CHAIN: QUARTERLY PROFILE REFRESH
═══════════════════════════════════════

PURPOSE: Complete LinkedIn profile audit and 
optimization
TIME: 2 hours manually
AUTOMATED: 45 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CURRENT STATE AUDIT
Agent: Strategist
Input: Current profile screenshots or descriptions

Prompt:
"Audit my current LinkedIn profile:

[PROVIDE CURRENT PROFILE STATE]:
- Current headline
- Current about section
- Current banner text
- Current featured section
- Current experience descriptions
- Current skills (top pinned)
- Current recommendations
- Current post activity

Score each element (1-10):
1. Headline effectiveness
2. About section persuasiveness
3. Banner design and messaging
4. Featured section strategy
5. Experience section storytelling
6. Skills relevance and ordering
7. Recommendations strength
8. Recent activity quality

Identify:
- Strongest elements (keep)
- Weakest elements (fix priority)
- Missing elements to add
- Elements that could be stronger"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: GOAL ALIGNMENT CHECK
Agent: Strategist
Input: Current state + goals

Prompt:
"Check profile alignment with current goals:

MY CURRENT GOALS:
- 90-day: [reference]
- 900-day: [reference]
- Career target: [Senior/Staff Software Engineer]
- Positioning: [Software Engineer with AI 
  specialization, from Nigeria]

For each profile element, evaluate:
1. Does it support these goals?
2. Does it position me correctly?
3. Does it attract right audience?
4. Does it filter out wrong audience?
5. Would target opportunities be attracted?

Identify misalignments:
- Elements working against goals
- Elements missing that would support goals
- Positioning drift that needs correction"

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: HEADLINE OPTIMIZATION
Agent: Strategist + Content Creator
Input: Current headline + alignment analysis

Prompt:
"Optimize my LinkedIn headline:

CURRENT HEADLINE: [PASTE]

Create 5 improved options that:
- Position as Software Engineer first
- Show multi-domain expertise
- Include specific specializations
- Match my authentic voice
- Fit within 220 characters
- Optimize for LinkedIn search
- Attract right opportunities

For each option:
- Full headline text
- Character count
- Why this works
- What it attracts
- What it filters out

Recommend the strongest with reasoning."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: ABOUT SECTION REWRITE
Agent: Content Creator
Input: Current about section + new headline

Prompt:
"Rewrite the About section:

CURRENT: [PASTE CURRENT]
NEW HEADLINE: [FROM STEP 3]

Create optimized About section:
- 1500-2000 characters
- Opens with compelling hook (2-3 sentences)
- Shows my origin story (Med Lab → Software)
- Establishes primary identity (Software Engineer)
- Lists specializations (AI Integration, CV, Multi-domain)
- Includes multi-dimensional experience
- Shows Nigerian/African identity as strength
- Includes 'What you'll find here' section
- Ends with clear CTA
- Uses my authentic voice
- Zero banned words

Provide:
- Complete rewritten About section
- Explanation of changes
- Alternative shorter version (1000 chars)"

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: EXPERIENCE SECTION OPTIMIZATION
Agent: Content Creator
Input: Current experience + new positioning

Prompt:
"Optimize experience section entries:

CURRENT EXPERIENCE ENTRIES:
[PASTE EACH ROLE]

For each experience, rewrite to:
- Lead with 'Software Engineer' title
- Show impact with specific numbers
- Include multi-domain work
- Highlight relevant achievements
- Use STAR format (Situation, Task, Action, Result)
- Include tools/technologies used
- Show progression/growth

For each role provide:
- Optimized title
- Rewritten description
- Key achievements to highlight (with metrics)
- Skills to emphasize

Ensure all entries support current positioning."

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: FEATURED SECTION STRATEGY
Agent: Strategist
Input: All above + current featured

Prompt:
"Optimize Featured section:

Currently featured: [LIST WHAT'S THERE]

Recommend Featured section strategy:

PRIORITY 1 (Must include):
- Best performing recent post
- Signature framework or content
- Multi-domain showcase

PRIORITY 2 (Should include):
- Client work examples
- Testimonials/recommendations
- Speaking engagements or podcasts

PRIORITY 3 (Nice to include):
- Media features
- Course/product links
- Newsletter signup

For each recommendation:
- Type (post, link, media, article)
- Purpose (what it demonstrates)
- Suggested text/description
- Best position in featured order

Total: 4-6 featured items maximum"

Output → Feed to Step 7

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 7: SKILLS OPTIMIZATION
Agent: Strategist
Input: All above + current skills

Prompt:
"Optimize skills section:

CURRENT SKILLS: [LIST TOP 20-30]

Recommend:

TOP 3 PINNED SKILLS (Most important - shown first):
1. [Recommendation with reasoning]
2. [Recommendation with reasoning]
3. [Recommendation with reasoning]

FULL SKILLS LIST (Ranked by relevance):
- Rearrange for optimal display
- Add missing skills for current positioning
- Remove outdated or irrelevant skills
- Prioritize skills matching target roles

Categorize skills:
- Core Software Engineering (must-haves)
- Specializations (AI, CV, etc.)
- Multi-domain (Web, DeFi, E-commerce)
- Soft skills (relevant ones only)

Also recommend:
- Skills to actively get endorsed for (top 5)
- Skills that could be certifications to pursue
- Any skills to remove that don't serve positioning"

Output → Feed to Step 8

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 8: BANNER REDESIGN BRIEF
Agent: Visual Designer
Input: All above + current banner

Prompt:
"Create banner redesign brief:

Based on updated positioning, provide:

TEXT CONTENT:
- Main headline (1 line)
- Sub-tagline (1 line)  
- Bottom line
- Any CTA text

DESIGN SPECIFICATIONS:
- Color palette (matching brand)
- Typography recommendations
- Photo placement
- Visual elements

CANVA EXECUTION STEPS:
- Complete redesign instructions
- Element positioning
- Colors and fonts to use
- Photos to include

Keep the design style similar to current 
but update text and refine visuals to match 
new positioning."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Complete profile audit with scores
✓ New optimized headline (5 options)
✓ Rewritten About section (long and short)
✓ Optimized experience descriptions
✓ Featured section strategy
✓ Skills reorganization plan
✓ Banner redesign brief
✓ Implementation checklist
✓ Estimated time savings vs. manual: 90 minutes










═══════════════════════════════════════
🔗 CHAIN: RAPID RESPONSE TO SITUATIONS
═══════════════════════════════════════

PURPOSE: Handle unexpected situations quickly and 
professionally
TIME: 15 minutes manually
AUTOMATED: 5 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO 1: NEGATIVE COMMENT/CRITICISM

STEP 1: SITUATION ASSESSMENT
Agent: Engagement Specialist

Prompt:
"A negative/critical comment was left on my post:

CONTEXT: [PASTE ORIGINAL POST]
COMMENT: [PASTE THE COMMENT]

Assess:
1. Is this legitimate criticism or bad faith?
2. Is there merit to their point?
3. Are they attacking me personally?
4. Public visibility (how many will see)?
5. Are they a competitor/hater?

Recommend response type:
- Engage constructively (if legitimate)
- Politely disagree (if different opinion)
- Ignore/delete (if bad faith/spam)
- Report (if abuse/spam)

Return recommendation with reasoning."

STEP 2: RESPONSE DRAFTING (If engaging)
Agent: Engagement Specialist

Prompt:
"Draft response to the criticism:

If legitimate criticism:
- Acknowledge their point
- Show you're listening
- Provide your perspective
- Maintain professionalism

If different opinion:
- Respect the difference
- Share your reasoning
- Don't get defensive
- Invite continued dialogue

If bad faith:
- Brief, professional response
- Don't engage the negativity
- Move on quickly

Provide 3 versions of the response, from most 
to least engaging with the criticism."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO 2: URGENT OPPORTUNITY (Timeboxed)

STEP 1: RAPID ASSESSMENT
Agent: Opportunities Manager

Prompt:
"Time-sensitive opportunity:

DETAILS: [PASTE OPPORTUNITY]
DEADLINE: [WHEN THEY NEED RESPONSE]

Quick assessment (5 min):
1. Legitimacy check
2. Alignment with goals
3. Feasibility
4. Value assessment
5. Recommendation: pursue or pass?

If pursuing, provide:
- Immediate response
- Questions to ask
- Timeline for full evaluation
- Any red flags to watch"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO 3: VIRAL POST (Unexpected Success)

STEP 1: LEVERAGE STRATEGY
Agent: Strategist + Content Creator

Prompt:
"One of my posts is going viral:

POST: [PASTE POST]
CURRENT STATS: [IMPRESSIONS, ENGAGEMENT]

Create rapid response plan:

IMMEDIATE (Next 4 hours):
1. Engage with every comment thoughtfully
2. Send connection requests to engaged people
3. Pin relevant featured content

TODAY:
1. Prepare follow-up post that continues conversation
2. Draft newsletter section on this topic
3. Create X thread version

THIS WEEK:
1. Cross-platform amplification
2. Reach out to engaged high-value people
3. Consider content series continuation

DO NOT:
- Post low-quality content right after
- Try to force another viral moment
- Get distracted from strategy"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO 4: CONTENT WRITER'S BLOCK

STEP 1: BREAKTHROUGH GENERATION
Agent: Content Creator + Strategist

Prompt:
"I'm stuck for content ideas today. Help me 
break through.

CURRENT SITUATION:
- Need to post today
- Feeling uninspired
- Blank slate

Give me:

QUICK IDEAS (5 posts I could write in 20 minutes):
1-5. [Simple, personal, honest posts I could 
     write from scratch]

FROM MY EXPERIENCE:
- Reflect on recent client work (any lessons?)
- Recent challenges I've overcome
- Something I learned this week
- A frustrating tool experience
- A pattern I've noticed

FROM MY CONTENT BANK:
- Prioritized ideas I haven't gotten to
- Quick-win topics from my banks
- Series continuations from past posts

FROM CURRENT EVENTS:
- Any AI news I have opinion on
- Industry topics needing my perspective
- African tech scene news to react to

Just help me get ONE post out today."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCENARIO 5: MISSED WEEK RECOVERY

STEP 1: GRACEFUL RETURN
Agent: Strategist + Content Creator

Prompt:
"I missed a week of posting due to [reason]. 
Help me return gracefully.

RECOVERY STRATEGY:

DAY 1 RETURN POST:
- Acknowledge the break (briefly, not defensively)
- Explain if appropriate (or don't)
- Get back into value delivery
- Don't apologize excessively

Provide 3 return post options:
A) Casual mention of break, then value
B) Turn the break into a lesson/insight
C) Just get back to normal without mention

REBUILDING MOMENTUM:
- First week: 5 solid posts
- Extra engagement with commenters
- Reconnect with dormant conversations
- Address any missed opportunities

NEVER:
- Beat myself up publicly
- Promise this won't happen again
- Explain repeatedly what happened
- Change fundamental strategy due to break"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

USE THIS CHAIN WHEN:
- Something unexpected happens
- Time-sensitive decision needed
- You're stuck or overwhelmed
- Need quick professional response







