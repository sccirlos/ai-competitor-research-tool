# Competitive Research Summary

**Generated:** 2026-04-14

**Competitors Analyzed:** Blueprint, Ensora, Freed, Healthie, Jane, Mentalyc, Simplepractice, Therapynotes, Upheal, Yungsidekick

---

## 📊 Quick Stats

- **Total Competitors:** 10
- **General Features Found:** 61
- **AI Features Found:** 88
- **Branded Solutions Found:** 20

---

## 🏢 Competitor Breakdown

### Upheal

**Pricing Tiers:**

- **Free:** $0
- **Premium:** $1 per session, capped at $69

**Feature Summary:**

- General Features: 5
- AI Features: 9

**Branded Solutions:**

- **Golden Thread:** Insurance-compliant treatment planning system that connects intake forms, session notes, and client progress into a continuous narrative of medical necessity for payer requirements
- **UphealOS:** AI-powered EHR replacement specifically designed for private-pay mental health practices, unifying client payments, scheduling, documentation, telehealth, forms, and marketing

**AI Maturity:** Upheal is a mature, AI-native mental health EHR with comprehensive AI integration across clinical workflows. The platform positions AI as core infrastructure rather than add-on features. Key maturity indicators: (1) Full-stack AI automation from transcription → note generation → treatment planning → clinical assistant, (2) Privacy-first architecture with SOC 2 Type II certification and default audio deletion, (3) Personalization via writing style learning, (4) Multi-language support (8 languages), (5) API access for third-party integration, (6) Transparent opt-in consent model for AI training data. Underlying AI models not publicly disclosed, but functionality suggests LLM-based (likely OpenAI or similar) with healthcare-specific fine-tuning. Platform emphasizes human-in-the-loop workflow where AI generates outputs but clinicians maintain control and review all documentation. Pricing model (usage-based with monthly cap) indicates confidence in AI accuracy and value. Limitations: No disclosed accuracy metrics, hallucination handling, or clinical validation studies. Session analytics limited to English and individual sessions. Some advanced features still in development. Overall: High AI maturity with production-grade deployment, strong compliance posture, and clinician-centric design philosophy.

**Technical Constraints:**
  - Session analytics currently only available for English-language sessions with individual clients (not couples)
  - Audio recordings deleted by default after processing - retention must be explicitly enabled
  - Client consent required for data processing under HIPAA/GDPR/PHIPA/PIPEDA
  - Some features (like AI Assistant logistics management) marked as 'coming soon'
  - Treatment plan auto-updates based on client progress marked as 'coming soon'
  - PDF/manual case snapshot upload for treatment plans marked as 'coming soon'

**Additional Costs:**
  - Payment processing fees: 2.9% + $0.30 per transaction if using Stripe integration for client payments
  - No per-note charges - all AI features included in $1/session Premium pricing
  - No usage caps on AI features in Premium plan (unlimited AI Assistant chat, unlimited notes)

---

### Blueprint

**Pricing Tiers:**

- **Core:** $0
- **Plus:** $0.99
- **Pro:** $1.49

**Feature Summary:**

- General Features: 8
- AI Features: 13

**Branded Solutions:**

- **Blueprint 2.0:** Next-generation AI-assisted EHR platform that moves beyond basic documentation automation to provide comprehensive clinical support throughout the entire client care journey. Positions AI as a tool that enhances care delivery, not just reduces paperwork.
- **Blueprint AI Assistant:** Embedded AI assistant that works alongside therapists before, during, and after sessions to automate documentation, provide clinical insights, and handle administrative tasks. Designed to take work off therapists' plates while maintaining clinical oversight and quality.
- **Blueprint AI Notetaker:** AI-powered documentation tool that automates session transcription and clinical note generation, saving therapists up to 90% of documentation time. Focuses specifically on eliminating the documentation burden that contributes to clinician burnout.
- **Rula Recap (Powered by Blueprint):** AI-driven clinical scribe and documentation assistant deployed at enterprise scale for Rula's network of 21,000+ mental health clinicians. White-labeled implementation of Blueprint's clinical documentation technology integrated into Rula's existing infrastructure via API.

**AI Maturity:** Blueprint demonstrates advanced AI maturity with a comprehensive suite of AI-powered clinical documentation and decision support tools specifically designed for behavioral health. The platform has moved beyond basic transcription to offer end-to-end AI assistance across the entire client care journey (pre-session prep, in-session cues, post-session insights).

KEY STRENGTHS:
- Purpose-built for behavioral health with clinical domain expertise
- High automation with mandatory human oversight (clinician-in-the-loop model)
- Enterprise-scale deployment (70,000+ clinicians, including 21,000+ via Rula partnership)
- Strong compliance posture (HIPAA, PHIPA, SOC 2 Type II certified with BAA)
- Proven time savings (60-90% reduction in documentation time)
- API-first architecture for enterprise integration
- Multiple deployment models (standalone EHR, embedded widget, Chrome extension, API)

TECHNOLOGY APPROACH:
- Uses third-party AI providers for processing under contractual protection
- Prompt engineering to enhance clinical note quality
- Multi-modal data integration (audio transcription + client records + assessments)
- Real-time and post-session AI analysis
- De-identified data used for model improvement (not individual patient data)

LIMITATIONS & GAPS:
- Specific AI models/providers not publicly disclosed (likely proprietary or under NDA)
- No published accuracy rates or clinical validation studies
- Hallucination handling relies primarily on mandatory clinician review
- Limited technical transparency about underlying technology
- Many features still "Coming soon" per comparison page
- English-centric (other language support not mentioned)
- Data processing restricted to US (all stored/processed domestically)

MATURITY LEVEL: Advanced - Blueprint shows enterprise-grade AI deployment with sophisticated clinical workflows, strong compliance, and proven scale. However, limited technical transparency and reliance on third-party AI providers (without disclosure) suggest the AI is integrated/configured rather than fully proprietary. The mandatory human review model demonstrates appropriate clinical safety awareness.

**Technical Constraints:**
  - AI features only available in Plus and Pro tiers, not included in free Core tier
  - Session credits are usage-based - must purchase credits to use AI features
  - All data processed and stored in the United States (may affect international users)
  - Requires session recording for full AI documentation features (optional but recommended)
  - Clinician review and approval required for all AI-generated content - no auto-submission
  - English language appears to be primary supported language (handles accents well but other languages not mentioned)
  - Chrome extension required for use on top of existing EHR systems
  - Third-party AI providers used for processing under BAA (specific providers not disclosed)
  - API integration requires enterprise plan for full implementation
  - Many features listed as 'Coming soon' in comparison chart - platform still under active development

**Additional Costs:**
  - No monthly minimums or contracts - only pay per session used
  - Session credits never expire (prepaid credits do not rollover between plan tiers if auto-upgraded)
  - Credit card processing fees apply for billing features (standard payment processing)
  - 50% discount on first purchase available for first 7 days (promotional)
  - Volume discounts available for enterprise/organization deployments
  - No additional cost for EHR platform - completely free forever
  - No per-user fees for Core EHR features

---

### Freed

**Pricing Tiers:**

- **Starter:** $39/month
- **Core:** $79/month
- **Premier:** $119/month ($104/month when billed annually)
- **Groups:** Custom pricing
- **Front Desk Starter:** $149/month per 250 calls

**Feature Summary:**

- General Features: 13
- AI Features: 14

**Branded Solutions:**

- **Front Desk AI Assistant:** 24/7 AI-powered phone receptionist that handles incoming patient calls, triages requests, and manages clinic communications to reduce administrative burden on staff.
- **Freed Coding Assistant:** Advanced AI-powered medical coding solution that extends beyond basic ICD-10 generation to include CPT/E/M codes, post-visit optimizations, and clinic-wide coding analytics.
- **Freed Clinician Assistant:** Unified AI assistant that consolidates multiple documentation and clinical support tools into a single interface, providing evidence-based clinical decision support, note editing, and patient history retrieval at point of care.

**AI Maturity:** Freed demonstrates high AI maturity with a sophisticated multi-layered AI architecture designed specifically for clinical documentation:

**Technical Architecture:**
- Custom-trained Automatic Speech Recognition (ASR) models with clinical terminology (27,000+ medications and terms)
- Large Language Models for summarization, formatting, and specialty-aware corrections
- Multi-step processing pipeline: audio recording → clinical transcription → specialty adaptation → personalization → accuracy validation
- Evidence-based clinical decision support with 50+ whitelisted medical sources (PubMed, NEJM, JAMA, etc.)
- Agentic AI for EHR field mapping and navigation
- Machine learning for template learning and continuous improvement from clinician edits
- Multilingual support (90+ languages with code-switching)

**Automation Sophistication:**
- Primarily human-in-the-loop: AI generates complete clinical documentation, codes, letters, and instructions automatically, but clinicians retain control through review and approval
- Adaptive learning system that improves over time based on individual clinician feedback
- Hallucination detection and multi-layer safety checks with human oversight
- Context-aware processing that carries forward patient history and adapts to specialty needs

**Data Privacy & Compliance:**
- HIPAA-compliant and SOC 2 Type II certified
- HITECH-compliant
- PHI encrypted at-rest and in-transit
- AI models are HIPAA-compliant and do not retain data
- PHI never used for AI training purposes
- Patient recordings auto-deleted after processing
- BAAs with all AI/cloud vendors (including Microsoft Azure)
- PHI isolation for clinical decision support (CDS queries processed within Freed's environment)
- Data residency in US-based Microsoft Azure data centers

**Clinical Validation:**
- Processes 2,000,000+ notes monthly (as of documentation date)
- Human clinicians regularly review anonymized samples for model performance validation
- Specialty-aware models trained on real clinical workflows
- Templates designed by practicing clinicians
- Multi-layer accuracy checking before note delivery
- Cited sources for all clinical recommendations

**Product Maturity:**
- Three branded AI solutions (Clinician Assistant, Coding Assistant, Front Desk AI)
- Comprehensive feature set beyond basic transcription: coding, letters, instructions, treatment plans, pre-charting, clinical decision support
- Sophisticated pricing tiers that gate advanced AI features (visit prep, coding, EHR push, clinician assistant) to higher tiers
- Enterprise-ready with SSO, team features, and dedicated support
- Active product development (beta features: Clinician Assistant, Shared Patients; coming soon: Advanced Front Desk, seamless code sync)

**Limitations & Considerations:**
- Technology is explicitly described as requiring clinician review (not autonomous)
- Known accuracy challenges in noisy environments, speaker attribution, and brief visits
- Some features still in beta or development
- No traditional EHR API integrations (uses browser-based push method instead)
- Starter tier usage caps (40 visits/month)

**Overall Assessment:**
Freed represents a mature, clinician-focused AI platform with strong technical foundations, comprehensive privacy controls, and a clear philosophy of augmenting (not replacing) clinical judgment. The platform shows significant investment in safety, validation, and continuous improvement while maintaining appropriate human oversight requirements.

**Technical Constraints:**
  - Patient recordings are temporarily stored until note summaries and quality checks are complete, then automatically deleted. Clinicians can set notes to auto-delete after 30 days.
  - EHR Push feature requires browser-based EHR (web interface) and Chrome browser extension. Not compatible with desktop-only EHR systems without web interface.
  - Front Desk AI Assistant integration with EHRs is listed as 'coming soon' in Advanced plan - not yet available in Starter plan.
  - AI accuracy can be impacted by voice-to-text errors in noisy environments or misheard terms.
  - Speaker attribution can struggle with distinguishing between patient and clinician statements. System does not distinguish male/female voices to avoid gender bias.
  - AI hallucinations are more likely during brief or incomplete visits where the system may fill gaps or add 'normal findings' not explicitly stated.
  - Starter tier is limited to 40 visits/notes per month.
  - Clinician Assistant is currently in beta.
  - Shared Patients feature is in beta (Groups tier only).
  - Direct EHR API integrations are not standard - system uses browser-based 'push' mechanism instead of traditional integrations.
  - Seamless EHR integration for clinical codes listed as 'coming soon' - codes currently need to be copied manually or via EHR Push.

**Additional Costs:**
  - Front Desk AI is a separate product with separate pricing: $149/month per 250 calls (Starter). Advanced plan pricing not yet disclosed.
  - Student discount available: 50% off for students, trainees, or fellows (requires proof of enrollment).
  - Annual billing discount: Premier tier is $1,248/year ($104/month effective rate vs $119/month).
  - Group pricing is custom and negotiated per organization.
  - No refunds by default for cancellations (subscription continues until end of billing cycle).
  - Usage beyond 40 visits/month on Starter tier requires upgrade to Core tier ($79/month for unlimited).

---

### Yungsidekick

**Pricing Tiers:**

- **Flexible (Trial/Pay-as-you-go):** $0/month base + $0.03 per minute
- **Starter:** $9.99
- **Basic:** $39.99 (discounted from $53)
- **Professional:** $99.99 (discounted from $145)
- **Group Practice:** Custom pricing

**Feature Summary:**

- General Features: 8
- AI Features: 10

**AI Maturity:** YungSidekick demonstrates advanced AI maturity with a comprehensive suite of AI-powered clinical documentation and analytics features. The platform employs a human-in-the-loop framework where AI assists but never replaces clinical judgment - all outputs require clinician review and approval. Key strengths include: (1) Full automation of transcription, note generation, treatment planning, and progress tracking with 1-minute turnaround time, (2) Advanced analytics including measurement-based outcome tracking, meta-reporting across sessions, and diagnostic marker flagging for depression/anxiety, (3) Conversational AI assistant for intelligent retrieval of client information, (4) Sophisticated privacy controls including automatic anonymization and immediate audio deletion, (5) Custom template builder using natural language prompts, and (6) Complete HIPAA/GDPR compliance with BAAs covering all third-party AI providers. However, AI maturity is limited by lack of transparency around underlying models and technology stack - specific AI models (GPT, Claude, proprietary) are not disclosed, no accuracy rates or validation studies are publicly documented, and no API access for programmatic integration is available. The platform positions AI as a documentation efficiency tool rather than a clinical decision support system, explicitly disclaiming diagnostic or therapeutic recommendation capabilities. Data handling is privacy-forward: audio deleted immediately post-processing, no PHI used for model training, processing in isolated environments, and therapist control over anonymization. Overall assessment: Operationally mature AI deployment focused on workflow automation with strong privacy guardrails, but limited technical transparency and no movement toward autonomous clinical decision-making.

**Technical Constraints:**
  - Requires internet connection for all AI processing
  - Requires up-to-date web browser for platform access
  - Requires audio recording capability (microphone or recording device)
  - Session audio must be uploaded/recorded through platform for AI processing
  - Specific AI models and underlying technology not publicly disclosed
  - No API access documented for AI outputs or programmatic integration
  - Minute-based pricing limits may constrain usage for high-volume practices (overage charges apply at $0.03/minute)
  - Audio file size limits not publicly disclosed

**Additional Costs:**
  - Overage charges: $0.03 per minute of session audio beyond plan limits
  - Group practice custom pricing - exact costs not publicly disclosed, requires sales contact
  - No other AI-specific add-on costs identified (all AI features included in base plans)

---

### Simplepractice

**Pricing Tiers:**

- **Starter:** $49/month (promotional: $24/month for first 3 months)
- **Essential:** $79/month (promotional: $39/month for first 3 months)
- **Plus:** $99/month (promotional: $49/month for first 3 months)

**Feature Summary:**

- General Features: 2
- AI Features: 7

**Branded Solutions:**

- **Note Taker:** AI-powered clinical documentation automation tool designed to reduce administrative burden on mental health practitioners by 5 hours per week. Addresses the core problem of time-consuming progress note writing that takes clinicians away from client care.

**AI Maturity:** SimplePractice has achieved moderate AI maturity with a focused, production-ready clinical documentation solution. 

**Current State:**
- **Primary AI Product:** Note Taker, launched in 2025, is the flagship AI offering powered by Claude (Anthropic). It's a mature, HITRUST-certified, HIPAA-compliant solution with real-world clinical validation (4 out of 5 clinicians report time savings).
- **Underlying Technology:** Confirmed partnership with Anthropic's Claude for all Note Taker functionality. No proprietary AI models disclosed.
- **Scope:** Narrow focus on clinical documentation automation. No AI for treatment planning, diagnosis, coding assistance, or clinical decision support (though future roadmap mentions treatment plans and intake paperwork).
- **Adoption Model:** Add-on pricing ($35/month) rather than base inclusion suggests cautious market testing and revenue optimization strategy.

**Maturity Indicators:**
- **High:** HIPAA/HITRUST compliance built-in, BAA coverage for AI partner, de-identification strategy, multi-language support, adaptive learning from clinician style.
- **Medium:** Human-in-the-loop requirement (mandatory review/editing), refinement limits (5 per session), no accuracy metrics publicly disclosed.
- **Low:** No API access, no integration with external platforms, limited to SimplePractice ecosystem, no clinical validation studies cited.

**Data Governance:**
- Strong privacy stance: data never leaves SimplePractice environment, no third-party AI provider access to raw PHI, transcripts deleted after 7 days or note finalization.
- Future opt-out mechanism planned for de-identified data use in model improvement (not yet implemented as of documentation review).
- Will never sell PHI; uses "Safe Harbor" HIPAA de-identification method.

**Future Direction:**
Roadmap includes AI for treatment plans, intake paperwork automation, and dictation enhancements, indicating expansion beyond progress notes. However, no timelines or commitments provided.

**Positioning:**
SimplePractice takes a conservative, compliance-first approach to AI, prioritizing clinician control, data security, and ethical AI principles over rapid feature expansion. The product is production-grade and clinically validated but not cutting-edge in terms of AI capabilities or automation depth.

**Technical Constraints:**
  - Note Taker only works with SimplePractice Telehealth (not external telehealth platforms)
  - No public-facing API available for AI outputs or integrations
  - Pre-session summaries only available via web browser (not mobile app)
  - Recording time limits: Telehealth sessions up to 4 hours, in-person mobile sessions up to 2.5 hours
  - Transcript available for review only for 7 days or until note is signed/locked (whichever comes first)
  - Up to 5 refinements allowed per appointment for AI-generated notes
  - Requires previous finalized note for same client to learn documentation style (first note may be less tailored)
  - Note Taker requires clinician to have Note Taker add-on enabled for their account
  - Works with couple and group appointments but may require more in-depth editing
  - State-specific consent requirements for audio recording must be handled by clinician

**Additional Costs:**
  - Note Taker: $35/month per clinician (after 30-day free trial) - applies to all plan tiers
  - No per-note usage fees or caps on Note Taker usage
  - No additional storage fees for AI-generated notes or transcripts
  - ePrescribe (separate add-on): $49/month per clinician plus $89 one-time setup fee
  - Group appointments feature: $20/month add-on for Essential plan (included in Plus plan)

---

### Therapynotes

**Pricing Tiers:**

- **Solo:** $69/month
- **Group:** $79/month for first clinician, $50/month per additional clinician
- **Enterprise:** $79/month for first clinician, $50/month per additional clinician (minimum 30 users)
- **TherapyFuel AI Add-on:** $40/month per clinician
- **Premium Telehealth Add-on:** $15/month per clinician

**Feature Summary:**

- AI Features: 8

**Branded Solutions:**

- **TherapyFuel:** AI-powered documentation suite designed to automate clinical note-taking, treatment planning, insurance data entry, and messaging summaries for behavioral health providers

**AI Maturity:** 
TherapyNotes has positioned TherapyFuel as a comprehensive AI documentation suite, not standalone point solutions. Launched with Client History Summarization as first AI feature, then rapidly expanded to full suite including transcription, progress notes, treatment plans, and tone adjustment. 

**Maturity Level: Mid-stage adoption**
- Technology: Uses stock LLM from third-party vendor (not custom-trained model), relying on prompt engineering rather than proprietary AI training
- Privacy-first approach: HITRUST AI certified, strong BAA framework, no data retention, vendor contractually prohibited from training on PHI
- Human-in-the-loop design: All AI outputs require clinician review/approval before finalization
- Limitations acknowledged: Bias cannot be fully eliminated, not intended as clinical decision-making tool
- Pricing: Per-clinician subscription model ($40/mo) rather than usage-based, with practice-wide benefits if 1+ clinician subscribes

**Notable gaps:**
- No disclosure of which LLM vendor/model used (OpenAI GPT, Anthropic, etc.)
- No published accuracy rates or clinical validation studies
- No mention of hallucination detection/mitigation strategies
- Limited template support (individual therapy only, no groups/couples yet)
- No API access documented for AI features
- No on-premise deployment option

**Strengths:**
- Fully integrated into existing EHR workflow (no separate login/platform)
- Strong privacy/security posture with third-party certifications
- Transparent about limitations and bias risks
- Clinician can customize AI "voice" extensively
- Audio immediately deleted after transcription (privacy-by-design)


**Technical Constraints:**
  - TherapyFuel currently supports Therapy Progress Notes and Treatment Plans only - not yet compatible with group notes, couples/family therapy, or other specialized note templates
  - Only one Approach to Treatment can be selected per note generation (though interventions from multiple approaches can be manually added)
  - Transcripts from TherapyFuel Scribe are automatically deleted 30 days after session or when note is signed, whichever comes first - limited troubleshooting support available after deletion
  - No API access for AI features publicly documented
  - No offline/on-premise deployment - cloud-based only
  - TherapyFuel Scribe requires manual start/stop during session (not auto-activated)

**Additional Costs:**
  - Real-Time Eligibility (RTE) Verification: $0.14 per request
  - Electronic Insurance Claims: $0.14 per electronic claim
  - Paper Insurance Claims: $1.00 per mailed claim
  - Electronic Remittance Advice (ERA): $0.14 per claim in ERA
  - Appointment Reminders (text/voice): $0.14 per reminder
  - Credit Card Processing: 3.1% + $0.30 per transaction
  - ePrescribe: $65/month per prescriber

---

### Healthie

**Pricing Tiers:**

- **Core:** $18-19.99/month
- **Essentials:** $45-49.99/month
- **Plus:** $129.99/month
- **Group:** $149.99/month base + $50/month per additional provider
- **Enterprise:** Contact for pricing

**Feature Summary:**

- General Features: 7
- AI Features: 7

**Branded Solutions:**

- **Intelligence by Healthie:** Native AI suite designed to increase efficiency and personalization of healthcare workflows across the platform. Positions AI as augmentation to provider capabilities rather than replacement, with healthcare-specific guardrails and compliance built in. First major AI-native initiative from Healthie, launched in 2025.
- **Healthie Harbor (AI Partners):** Marketplace ecosystem enabling customers to connect third-party AI tools and applications directly to Healthie platform. Allows customers to bring their own AI stack (e.g., OpenAI, Claude) or integrate with vetted AI partner solutions for specialized use cases.

**AI Maturity:** Healthie demonstrates moderate-to-advanced AI maturity with its 'Intelligence by Healthie' initiative launched in 2025. The platform takes an 'AI-native' approach, integrating AI across clinical, administrative, and developer workflows rather than offering standalone AI tools. Their flagship AI Scribe product (launched October 2025) shows production-ready capabilities with HIPAA/HITRUST/ONC compliance, human-in-the-loop design, and clear data privacy boundaries (no third-party data sharing, no model training on customer data). Beta testing over 1 year indicates thoughtful validation. Underlying technology relies on established LLMs and APIs (Zoom transcription, MCP protocol) rather than proprietary models. Pricing model is usage-based and transparent. The platform's API-first architecture and Dev Assist tool demonstrate commitment to extensibility and developer ecosystem. However, AI features beyond Scribe lack detailed public documentation on pricing, availability, and technical specs, suggesting they may be in earlier stages. No publicly disclosed accuracy metrics, hallucination handling, or clinical validation processes beyond user satisfaction surveys (70% accuracy ratings for Scribe). The Harbor marketplace approach allows customers to bring their own AI stack, positioning Healthie as an AI-ready platform rather than AI product vendor. Overall: Production-ready for core use case (clinical documentation), emerging for broader AI capabilities, strong on compliance and privacy, but limited transparency on roadmap and feature maturity beyond Scribe.

**Technical Constraints:**
  - AI Scribe only supports 1:1 Zoom sessions (not group sessions or in-person meetings)
  - AI Scribe requires HIPAA-compliant Zoom integration via Healthie Calendar
  - Minimum session duration: AI Scribe does not generate notes if transcription stopped within 30 seconds of appointment start
  - AI Scribe not available in staging/sandbox environments for testing
  - Dev Assist currently limited to sandbox use only; production requires API product purchase
  - Dial-in participants for AI Scribe must dial directly into Zoom meeting or transcripts may be incomplete
  - No analytics dashboard or reporting to track AI Scribe usage or activity currently available
  - AI Scribe limited to 40 hours per month in base plan; overages charged at $0.85/hour

**Additional Costs:**
  - AI Scribe: $35/month for 40 hours (base tier)
  - AI Scribe overages: $0.85 per hour beyond included 40 hours
  - AI Scribe larger bundles available for scaling practices (pricing not publicly disclosed)
  - Third-party AI tools via Harbor marketplace: Fees charged by third-party vendors (not Healthie)
  - Dev Assist production use: Requires API product purchase (pricing not publicly disclosed)
  - External AI assistants for Dev Assist: Costs for OpenAI, Claude, or Cursor subscriptions paid directly to those vendors

---

### Jane

**Pricing Tiers:**

- **Balance:** $54 USD/month
- **Practice:** $79 USD/month base + $17.50/month per part-time practitioner or $35/month per full-time practitioner
- **Thrive:** $99 USD/month base + $20/month per part-time practitioner or $40/month per full-time practitioner

**Feature Summary:**

- General Features: 5
- AI Features: 3

**AI Maturity:** Jane has launched its first AI-powered feature (AI Scribe) as of August 2025, with nearly 8,500 practitioners using it as of February 2026. The platform demonstrates early-stage AI maturity with a focused, compliant implementation: (1) Single core AI feature (Smart SOAP Note transcription/summarization) with strong privacy framework (HIPAA/PIPEDA/PHIPA compliant, BAA available, no data used for model training); (2) Human-in-the-loop design requiring clinician review/approval of all AI outputs; (3) Customization layer via Global and template-specific prompts; (4) Freemium adoption strategy (5 free notes/month across all tiers) to drive usage; (5) Built-in-house integration (no separate apps required). Limitations: (1) AI provider/underlying technology not disclosed publicly; (2) Geographic restriction (US/Canada only); (3) No API for AI outputs; (4) No disclosed accuracy metrics, hallucination handling, or clinical validation processes; (5) No mention of future AI roadmap beyond 'more sample transcripts' for prompt testing. Jane positions AI as an 'assistant, not authority' per their AI Principles, emphasizing transparency and human oversight. The platform appears to be in early experimentation phase with AI, testing market adoption before expanding capabilities. No branded AI solution bundles or multi-feature AI suites detected - AI Scribe is a standalone add-on.

**Technical Constraints:**
  - AI Scribe only available in US and Canada
  - Maximum audio file size: 200MB
  - Maximum recording length: 90 minutes (warning at 80 minutes)
  - Supported audio formats only: mp3, mp4, wav, m4a, OGG, webm
  - Requires microphone access for live recording
  - Directional headset microphones may only capture clinician voice, not client voice
  - Recordings do not include post-processing - only captures what microphone picks up
  - AI Scribe subscriptions managed per practitioner (not clinic-wide)
  - Requires Full Access user permissions to manage AI Scribe subscriptions and deletion policies
  - AI processing requires internet connectivity
  - No API disclosed for AI outputs
  - Third-party AI provider not disclosed (potential vendor lock-in)

**Additional Costs:**
  - AI Scribe Unlimited: $15 USD per month per practitioner (for unlimited notes beyond 5 free notes/month)
  - Proration applies for mid-month subscription changes
  - Group Telehealth: add-on cost not specified on pricing page
  - Insurance Billing: add-on cost not specified (available for Practice and Thrive tiers)
  - Integrated Outbound Fax requires Documo subscription (separate vendor)
  - Part-time practitioners: $17.50/month (Practice) or $20/month (Thrive)
  - Full-time practitioners: $35/month (Practice) or $40/month (Thrive)

---

### Mentalyc

**Pricing Tiers:**

- **Mini Plan:** $19.99/month or $14.99/month (annual)
- **Basic Plan:** $39.99/month or $29.99/month (annual)
- **Pro Plan:** $69.99/month or $59.99/month (annual)
- **Super Plan:** $119.99/month or $99.99/month (annual)
- **Team Plan:** $59.99/seat/month (intro) or $49.99/seat/month (annual intro), regularly $119.99/$99.99
- **Free Trial:** $0

**Feature Summary:**

- General Features: 11
- AI Features: 10

**Branded Solutions:**

- **Alliance Genie:** Therapeutic relationship monitoring and rupture detection system that evaluates session quality across clinical dimensions
- **AI Treatment Planner:** Automated treatment plan generation system that creates insurance-ready, modality-specific clinical plans from session content
- **AI Progress Tracker (Impact Tracker):** Longitudinal outcome monitoring system that tracks symptom trends and goal attainment without requiring separate client assessments
- **Mentalyc AI Note Taker:** Core AI clinical documentation platform that converts therapy sessions into structured, insurance-ready progress notes across multiple formats
- **Mentalyc Team Plan (Group Practice Solution):** Multi-clinician practice management platform with supervision workflows, centralized billing, and unlimited AI-powered documentation

**AI Maturity:** Mentalyc demonstrates high AI maturity as a specialized behavioral health documentation platform. The company has built proprietary AI models trained specifically on therapy sessions (not general medical visits), enabling clinical nuance capture that general-purpose LLMs miss. 

KEY MATURITY INDICATORS:
- Purpose-built AI trained on therapy-specific formats (SOAP, DAP, BIRP, etc.) and clinical language
- Multi-modal AI capabilities: transcription, clinical documentation, treatment planning, outcome tracking, and relationship analytics
- Human-in-the-loop architecture with full audit trails (not black-box AI)
- 90% time reduction with 3-minute turnaround for 50-minute sessions
- Specific accuracy claims: "Most therapists review and export without substantive edits"
- Advanced features like Alliance Genie (27-area therapeutic relationship evaluation) and longitudinal Progress Tracker
- Full HIPAA/SOC 2 Type II compliance with BAA for all accounts
- Explicit data privacy: never trains on user data, never sells data, auto-deletes audio
- Multi-format output (10+ note types), 25+ modality support, multi-client types

LIMITATIONS:
- Does not disclose specific underlying models (e.g., which LLM provider)
- Does not publish accuracy rates, hallucination handling protocols, or clinical validation studies
- No mention of how AI handles ambiguous clinical scenarios or edge cases
- Subprocessor/AI vendor details not disclosed in BAA
- No API access mentioned for AI outputs
- Accuracy is session-dependent (audio quality, length, modality match)

MATURITY LEVEL: Advanced - Mentalyc has moved beyond basic transcription to offer a comprehensive AI-powered clinical workflow platform with specialized mental health training, but lacks transparency on underlying models and validation methodologies.

**Technical Constraints:**
  - Session length limits: 75 minutes for Mini and Basic plans, 130 minutes for Pro, Super, and Team plans
  - Note accuracy depends on three factors: audio quality, session length, and modality match
  - Note editing recommended on computer rather than mobile devices
  - Chrome Extension required for direct EHR integration (web-based EHRs only)
  - Audio recordings are audio-only (no video capture)
  - Fair usage policy applies to Team plan unlimited notes
  - Requires clear, written consent from patients before collecting PHI via platform
  - AI generates drafts that require clinician review - every note must be verified by licensed professional
  - Play therapy and non-verbal sessions work best with dictation/summary mode rather than live recording
  - Free trial limited to 15 notes over 14 days

**Additional Costs:**
  - No usage-based AI fees disclosed - costs are tier-based only
  - No per-note charges beyond plan limits
  - Overage options: Not publicly disclosed (users must upgrade tier or purchase additional notes)
  - Annual billing offers savings of up to $300 compared to monthly billing
  - Team plan offers introductory pricing ($49.99-59.99/seat) vs regular pricing ($99.99-119.99/seat)

---

### Ensora

**Pricing Tiers:**

- **Essentials:** $29/therapist/month
- **Advanced:** $59/therapist/month
- **Premier:** $89/therapist/month

**Feature Summary:**

- General Features: 2
- AI Features: 7

**Branded Solutions:**

- **AI Session Assistant:** AI-powered documentation assistant that eliminates post-session note-writing burden. Positions as 'therapist-informed AI' built specifically for mental health professionals (not generic AI tools). Core problem solved: spending 5-10 hours per week on documentation instead of client care or personal time. Promises to help therapists 'end the day on time' and 'be more present in sessions' by automating the heavy lifting of clinical note generation while keeping clinician in control.
- **AI Notes Enhancement:** Built-in AI assistant that polishes and professionalizes manually-typed clinical notes. Positions as a time-saver that 'helps you refine your clinical notes' without sacrificing quality or security. Core problem solved: time spent on tedious note formatting, expanding abbreviations, fixing typos, and ensuring professional documentation standards. Unlike AI Session Assistant (which generates notes from audio), this enhances text the clinician has already written.

**AI Maturity:** TheraNest by Ensora Health demonstrates moderate-to-advanced AI maturity with two distinct AI product offerings targeting different documentation workflows. The platform takes a conservative, clinician-centric approach emphasizing human oversight, data privacy, and professional control. AI Session Assistant (branded add-on, $35/month) represents their premium AI offering for telehealth note generation, while AI Notes Enhancement (included in all tiers) serves as an accessible entry point for AI-assisted documentation. Both products are built on HIPAA/SOC 2/HITRUST-certified infrastructure with strong privacy commitments (no AI training on PHI, 24-hour recording deletion, signed BAA). However, technical transparency is limited—underlying AI models and providers are not disclosed, and specific accuracy metrics or clinical validation studies are not publicly shared. The platform acknowledges AI hallucination risks and requires clinician review of all outputs (strict human-in-the-loop model). Current limitations include telehealth-only support for session recording (no in-person session transcription), 1:1 session restriction (no group therapy support), and manual field mapping for structured SOAP templates. Ensora Health has publicly committed to 'Responsible AI Principles' aligned with HHS Trustworthy AI standards, with governance through a Compliance and Security Council. The company announced plans in February 2025 to expand AI across its product portfolio, including automated treatment plan generation and RCM intelligence, suggesting ongoing investment in AI capabilities. Overall assessment: Production-ready AI with strong compliance foundations, but conservative scope and limited technical disclosure compared to competitors offering more advanced features like real-time ambient AI, dictation, or in-person session transcription.

**Technical Constraints:**
  - AI Session Assistant only works for 1:1 telehealth sessions conducted within TheraNest platform—not available for group sessions or in-person sessions
  - AI Session Assistant requires telehealth session to be recorded; both clinician and client must give consent (consent required once, stored in client chart)
  - AI Session Assistant generates summary in single combined field; if template uses separate SOAP fields, content must be manually copied and pasted
  - Session recordings are automatically deleted within 24 hours; transcripts are not stored—cannot be retrieved after deletion
  - AI notes enhancement must be manually enabled for customers who signed up before May 21, 2025 (not default)
  - AI-generated content cannot be exported independently of existing documentation
  - AI model cannot be customized by individual users
  - AI may occasionally generate inaccurate or 'hallucinated' responses that sound correct but are not based on real data—clinician review essential
  - Requires active paid subscription for AI Session Assistant; feature unavailable if subscription lapses
  - Subject to Fair Usage Policy for AI features (specific limits not publicly disclosed)
  - Underlying AI model/technology provider not publicly disclosed—cannot verify specific capabilities or limitations of base model

**Additional Costs:**
  - AI Session Assistant: $35 per clinician per month (promotional: $17.50/month for first 6 months if added by March 31, 2026)
  - Telehealth add-on required for AI Session Assistant if not on Premier plan: $12 per therapist per month (Essentials and Advanced tiers)
  - AMA CPT License Fee: $19.50 per therapist annually, billed each December (required for accurate billing/documentation, affects AI code translation feature)
  - Additional practice admin users: $19/month on Essentials/Advanced, $29/month on Premier (may need access to review AI-generated documentation)

---

## 🤖 AI Features Overview

### Blueprint (13 AI features)

- **Session Transcription** (Not publicly disclosed (likely speech-to-text AI model)): Automatically transcribes therapy session audio in real-time, converting spoken conversation into text for clinical documentation. Described as accurate even with non-native English speakers and strong accents.
- **Automated Progress Note Generation** (Not publicly disclosed (likely large language model with prompt engineering for clinical notes)): Automatically generates complete clinical progress notes from session transcriptions and existing client data. Integrates information from assessments, homework assignments, and measurement-informed care tools. Notes are generated in draft form for clinician review and editing before finalization. Saves therapists 60%+ of documentation time.
- **AI Treatment Plan Generation** (Not publicly disclosed (appears to be LLM-based with clinical knowledge)): Drafts smart treatment plans based on session content, client history, diagnosis, and clinical best practices. Generates structured plans including goals, objectives, interventions, and timelines. Clinician reviews and customizes before implementation.
- **Session Prep & Pre-Session Summaries** (Not publicly disclosed (likely NLP/LLM for summarization)): Provides automated preparation before each session including a summary of the previous session, reminders of key focus areas, and relevant client history. Surfaces actionable context to help clinicians come prepared.
- **Clinical Decision Support - Assessment & Homework Suggestions** (Not publicly disclosed (likely AI-powered recommendation system based on clinical guidelines)): Provides AI-powered suggestions for evidence-based assessments and worksheets to assign clients between sessions. Offers personalized recommendations for digital homework and interventions based on client needs and treatment goals. Enhances client engagement and treatment outcomes.

_...and 8 more (see CSV for full list)_

### Ensora (7 AI features)

- **AI Session Assistant - Telehealth Session Recording & SOAP Note Generation** (Not publicly disclosed. HIPAA and SOC 2-compliant AI engine with transcription and summarization capabilities. Likely combines speech-to-text with large language model for clinical summarization.): Automatically records telehealth sessions (with consent) and generates SOAP-formatted (Subjective, Objective, Assessment, Plan) session summaries within minutes. Captures key client statements, symptoms, interventions, and clinical details specific to mental health therapy. Draft is ready for clinician review immediately after session ends. Requires both therapist and client consent. Only works for 1:1 telehealth sessions conducted within TheraNest; not available for group sessions.
- **AI Session Assistant - Case Summaries** (Not publicly disclosed. Same HIPAA and SOC 2-compliant AI engine as session recording feature.): Automatically summarizes all past client documentation (signed progress notes, assessments, treatment plans) to provide clear, organized case summaries before each session. Unlike transcription-based tools, this feature analyzes historical clinical documentation to highlight nuanced patterns, trends, and themes across multiple sessions—not just the latest one. Helps clinicians quickly review client history without tab-switching.
- **AI Notes Enhancement - Language & Clarity Improvement** (Not publicly disclosed. HIPAA and SOC 2-compliant AI engine.): Reviews and enhances manually-typed clinical notes to improve clarity, professionalism, and wording. Available in key documentation fields including Subjective, Objective, Assessment, Plan, Session Focus, and Therapeutic Intervention notes. Clinician writes notes as usual, then can click 'Improve with AI' to see suggested enhancements. Can accept ('Replace') or discard ('x') each suggestion. If accepted, suggested text appears in note field and can be further edited before finalizing.
- **AI Notes Enhancement - Spelling & Grammar Correction** (Not publicly disclosed. HIPAA and SOC 2-compliant AI engine.): Automatically detects and corrects spelling and grammar mistakes in clinical notes. Part of the AI notes enhancement suite. Clinician can review and accept or reject each correction.
- **AI Notes Enhancement - Abbreviation Expansion** (Not publicly disclosed. HIPAA and SOC 2-compliant AI engine.): Converts clinical shorthand and abbreviations into full text. Examples: 'DOB' → 'date of birth', 'BPD' → 'Borderline Personality Disorder'. Part of the AI notes enhancement suite. Helps create more professional, comprehensive documentation without manual typing.

_...and 2 more (see CSV for full list)_

### Freed (14 AI features)

- **Ambient AI Medical Scribe** (Automatic Speech Recognition (ASR) specifically trained for clinical use, combined with Large Language Models (LLMs) for summarization and formatting. Trained on over 27,000 medications and clinical terms.): Listens to patient conversations in real-time or from uploaded recordings, transcribes clinical encounters, and generates structured clinical notes (SOAP, DAP, or custom formats). Filters out filler words and background noise, derives medications, dosages, and abbreviations, and adapts terminology to be medically precise.
- **AI Clinician Assistant** (Large Language Models with access to 50+ verified US-based medical sources including PubMed, NEJM, AHA, JAMA, BMJ. Includes context-aware processing of patient history and visit data.): Persistent AI chat assistant that provides pre-charting support, clinical decision support with cited evidence-based sources, note editing and summarization, prior visit retrieval, and custom clinical document generation. Consolidates Magic Edit, pre-charting chat, and transcript/note summarization into one unified interface. Can answer clinical questions, restructure notes, pull ICD-10 codes, and generate custom care documents.
- **Magic Edit** (AI-powered natural language processing for contextual note editing): AI-powered note editing feature that allows clinicians to make sweeping changes to notes using simple voice or text commands. Can restructure notes, add details, change formatting, adjust tone, or reorganize content (e.g., 'organize supplement recommendations by body system' or 'change all patient name to client') without manual retyping. Now consolidated into the Clinician Assistant.
- **Visit Prep and Pre-charting** (AI summarization and context extraction from historical patient data): Automatically surfaces patient visit history summaries, medication and supplement dosages, top insights from past visits, and procedural details before appointments. Provides quick summaries of last visit, follow-up items, and patient context without manual chart searching. Clinicians can also input information before visits and pause/restart recordings.
- **ICD-10 Code Generation** (AI analysis of clinical transcripts and notes to identify diagnoses and map to ICD-10 codes): Automatically generates ICD-10 diagnosis codes based on visit content and note documentation. Analyzes transcript and note to identify relevant diagnoses and selects the most appropriate billable, clinician-useful codes. Codes appear immediately when note is complete. Provides dropdown menu with alternative code recommendations. Specialty-aware predictions that adapt to clinician's specialty and commonly documented conditions.

_...and 9 more (see CSV for full list)_

### Healthie (7 AI features)

- **AI Scribe - Automatic Transcription and Chart Note Generation** (Large Language Models (LLMs), Zoom Real-Time Media Services transcription API): Automatically transcribes 1:1 Zoom telehealth sessions and generates structured, editable chart notes in provider-selected templates (SOAP, ADIME, intake, progress notes, or custom). Produces transcript in .vtt format and complete chart note within 10-15 seconds after session ends. Supports video, audio-only, and dial-in phone calls.
- **Medical Record Summaries** (AI/LLMs (specific model not disclosed)): AI condenses large volumes of patient data into actionable insights, saving time for providers and improving relevance of clinical decisions. Part of Intelligence by Healthie suite.
- **Patient Messaging Assistance** (AI/LLMs (specific model not disclosed)): Suggests appropriate responses for incoming patient messages to ensure faster, more accurate communication for patient engagement. Part of Intelligence by Healthie suite.
- **Workflow Automation via Natural Language** (AI/LLMs with natural language processing): Simplifies complex tasks through natural language commands. Examples include generating follow-up prompts, reminder emails, and other workflow actions triggered by plain language instructions.
- **Intelligent Task Management** (AI automation engine): AI seamlessly integrates actions like creating tasks after meeting notes are generated, enabling end-to-end automation. Can trigger follow-up tasks based on session content or clinical workflows.

_...and 2 more (see CSV for full list)_

### Jane (3 AI features)

- **AI Scribe - Smart SOAP Note Generation** (Third-party AI provider (specific vendor not publicly disclosed; uses pre-trained models)): AI-powered transcription and summarization of clinical session recordings. Converts audio from live recordings, uploads, or dictation into structured SOAP notes. Uses customizable prompts (Global Prompt for all notes + per-template prompts) to organize session information according to clinician preferences. Supports multiple audio formats (mp3, mp4, wav, m4a, OGG, webm) up to 200MB and 90 minutes in length.
- **AI Scribe - Audio Transcription** (Third-party AI provider (likely speech-to-text engine; specific technology not disclosed)): Automatic speech recognition that transcribes audio recordings of clinical sessions into text. Practitioners can record live during sessions, upload pre-recorded audio files, or dictate notes post-session. Transcript is then processed by AI to generate structured clinical notes.
- **AI Scribe - Customizable Prompt Templates** (Prompt engineering layer on top of third-party AI language model): Template library with customizable AI prompts that guide how session audio is structured into clinical documentation. Includes Global Prompt (applies to all notes) and template-specific prompts. Practitioners can use default prompts, select from Jane's template library, or create custom prompts tailored to their documentation style and clinical needs. Prompts can be tested with sample transcripts before use.

### Mentalyc (10 AI features)

- **AI Progress Note Generation** (Machine learning algorithms, large language models, and statistical models trained on therapy sessions (specific model names not disclosed)): Automatically converts therapy sessions into structured clinical notes in multiple formats (SOAP, DAP, BIRP, GIRP, PIRP, SIRP, PIE, intake notes, Mental Status Exams). Processes 50-minute sessions into finished notes in under 3 minutes. Supports live recording, audio uploads, dictation, and text input.
- **AI Treatment Planner** (Generative AI platform trained on therapy-specific frameworks and clinical language (specific model not disclosed)): Generates SMART-goal treatment plans based on actual session content with one click. Creates insurance-ready interventions grounded in therapeutic modalities like CBT, EMDR, and DBT. Automatically pulls goals from sessions and tracks progress.
- **Alliance Genie** (AI-powered analytics using machine learning algorithms (specific models not disclosed)): Evaluates sessions across 5 clinical dimensions and 27 areas including Therapeutic Framework, Session Management, Therapeutic Relationship, and Therapeutic Process. Identifies ruptures, missed bids, and engagement shifts. Tracks therapeutic alliance patterns and provides detailed reports with quotes and transcript references. Offers another perspective to notice subtle shifts in the therapeutic relationship.
- **AI Progress Tracker (Impact Tracker)** (Statistical models and machine learning for longitudinal tracking (specific models not disclosed)): Provides longitudinal clinical progress monitoring, tracking symptom trends and goal attainment across sessions without requiring client questionnaires. Identifies patterns, goal progress, and symptom changes across sessions. Monitors symptom changes without extra forms.
- **Automatic CPT Code Computation** (AI-powered billing code detection based on session content analysis (specific technology not disclosed)): Automatically generates billing codes (CPT codes) based on session content and therapeutic activities documented in the note.

_...and 5 more (see CSV for full list)_

### Simplepractice (7 AI features)

- **Real-time Session Transcription** (Claude by Anthropic (confirmed in FAQs)): Creates live transcript during telehealth or in-person appointments. Transcription supports multiple languages (English, Spanish, French, German, Italian, Portuguese, Dutch, Polish, Swedish, Norwegian, Catalan, Croatian, Czech, Romanian) and diverse accents. Transcript available for review for up to 7 days or until note is signed and locked, whichever comes first.
- **AI-Generated Progress Notes** (Claude by Anthropic): Automatically generates draft progress notes from session transcripts in multiple formats (SOAP, DAP, BIRP). Adapts to clinician's documentation style by analyzing previous progress notes for the same client. Learns formatting, note sections, writing style, complexity level, and overall structure preferences. Saves average of 5 hours per week per clinician.
- **Voice Dictation for Notes** (Claude by Anthropic): Allows clinicians to dictate session information post-session without recording the live session. Clinician speaks thoughts into the tool, and AI generates a structured, professional note. Available via web browser and SimplePractice for Clinicians mobile app.
- **Audio/Text File Upload for Note Generation** (Claude by Anthropic): Clinicians can upload pre-recorded audio files or text files to generate progress notes. Useful for sessions recorded outside SimplePractice or for importing existing notes.
- **Pre-Session Client Summary** (Claude by Anthropic): Generates AI-powered summary of previous sessions to help clinicians prepare for upcoming appointments. Available only via web browser.

_...and 2 more (see CSV for full list)_

### Therapynotes (8 AI features)

- **AI Progress Note Generation (from session summary)** (Large language model (LLM) via third-party vendor - stock model, not custom-trained): Clinician enters treatment approach and brief session summary; AI generates SOAP (Subjective, Objective, Assessment, Plan) note fields. System uses minimal PHI (pronouns, age) from client profile to personalize output.
- **TherapyFuel Scribe (AI Session Transcription)** (Audio-to-text transcription processor (likely speech recognition model such as Whisper or similar)): Records in-person or telehealth therapy sessions, generates full session transcript, uses transcript to draft progress notes. Audio recording starts/stops manually by clinician.
- **AI Treatment Plan Generation** (Large language model (LLM) via third-party vendor): Generates personalized treatment plans with goals, objectives, and interventions based on clinician-entered treatment approach, clinical targets, diagnosis, and presenting problem. Number of objectives/interventions per goal customizable in user settings.
- **Client History Form Summarization** (Large language model (LLM) - first AI feature launched by TherapyNotes): AI-generated summary of patient's Client History Form responses. Appears at top of form and during Intake Note writing for quick reference.
- **AI Contact Note Generation (from Secure Messaging)** (Large language model (LLM)): Generates contact notes from secure messaging conversations. Clinician navigates to message thread, clicks 'Generate Contact Note', AI summarizes interaction for record-keeping.

_...and 3 more (see CSV for full list)_

### Upheal (9 AI features)

- **AI Progress Notes** (Not publicly disclosed (appears to use advanced NLP models, likely LLM-based)): Automatically generates clinical progress notes from recorded therapy sessions in real-time. Supports 10 note formats (SOAP, DAP, GIRP, BIRP, EMDR, PIRP, SIRP, PIE, Intake, MSE). Notes are instantly generated after sessions and can be edited manually or via AI prompts. The AI learns and adapts to clinician writing style over time with every edit.
- **AI Transcription** (Not publicly disclosed (likely speech-to-text model, possibly Whisper or similar)): Converts audio and video recordings of therapy sessions into text transcripts. Supports 8 languages: English, Spanish, Portuguese, German, French, Italian, Mandarin, and Hindi. Works with in-person sessions, virtual sessions (any platform), Upheal's built-in telehealth, uploaded recordings, and dictated summaries.
- **AI Treatment Plans (Golden Thread)** (Not publicly disclosed (likely LLM-based with clinical domain training)): Auto-generates insurance-compliant treatment plans that connect intake forms, session notes, and client progress into a continuous narrative of medical necessity. Creates case snapshots from past sessions/intake forms, generates customizable treatment goals and objectives, and auto-syncs treatment plan elements into progress notes. Supports 170+ therapy modalities. Built against top payer documentation criteria to reduce audit flags.
- **AI Assistant (HIPAA-compliant ChatGPT Alternative)** (Not publicly disclosed (likely LLM-based, positioned as secure alternative to ChatGPT/Copilot/Gemini)): Conversational AI assistant with full access to client history, past sessions, treatment plans, and notes. Helps clinicians prepare for sessions by summarizing last session and ongoing themes, identifies patterns and recurring themes across client history, drafts clinical documents (referral letters, discharge summaries, resource lists), and assists with administrative tasks. Lives natively inside Upheal's secure workflow with full clinical context.
- **Smart Edit** (Not publicly disclosed (likely LLM-based text editing)): AI-powered note editing via plain-language prompts. Allows clinicians to instantly modify structure, content, tone, and language of clinical documentation. Can shorten, expand, anonymize, translate, or restructure notes using natural language commands.

_...and 4 more (see CSV for full list)_

### Yungsidekick (10 AI features)

- **AI Audio Transcription** (Not publicly disclosed (likely third-party speech-to-text model under BAA)): Converts therapy session audio recordings into text transcripts. Supports live recording, pre-recorded file uploads, and audio from online/in-person sessions. Processes audio and generates transcript within 1 minute.
- **AI Progress Note Generation** (Not publicly disclosed (proprietary AI model or adapted large language model under BAA)): Automatically generates clinical progress notes in multiple formats (SOAP, DAP, BIRP, GIRP) from session transcripts or dictated recaps. Produces EHR-ready documentation within 1 minute. Extracts symptoms, medications, treatment goals, and clinical observations from session content.
- **AI Treatment Plan Generation** (Not publicly disclosed): AI extracts and synthesizes treatment goals from session content to automatically generate treatment plans. Includes ICD-10 code suggestions for diagnosis coding. Plans sync with integrated EHR systems.
- **AI Session Reports (Therapist and Client)** (Not publicly disclosed): Generates detailed analytical reports from session transcripts. Therapist reports include clinical patterns, resilience strategies, therapeutic relationship observations, and session insights. Client reports provide session summaries suitable for patient review between appointments.
- **AI Meta Reports (Psychological Profiles)** (Not publicly disclosed): Consolidates data from multiple therapy sessions to build comprehensive psychological profiles and client histories. Analyzes patterns across sessions to provide holistic view of client progress and therapeutic journey.

_...and 5 more (see CSV for full list)_

---

## 📁 Data Files

Detailed data is available in the following CSV files:

- **compiled_features.csv** - All general features across competitors
- **compiled_ai_features.csv** - AI-specific features
- **ai_maturity_summary.csv** - AI maturity assessments
- **branded_solutions.csv** - Named products and solutions

---

_End of Report_
