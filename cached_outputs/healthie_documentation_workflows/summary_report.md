# Competitive Research Summary

**Focus Area:** Documentation & Clinical Workflows

**Generated:** 2026-04-14

**Competitors Analyzed:** Blueprint, Ensora, Freed, Healthie, Jane, Mentalyc, Simplepractice, Therapynotes, Upheal, Yungsidekick

---

## Upheal

### Documentation Workflow Overview

- Documentation-related features found: 5

### Core Note and Treatment Plan Capabilities

- **Template Builder**: 170+ clinically approved note sections available. Clinicians can customize note templates by selecting from pre-built sections or creating custom Smart Sections via AI prompts.
- **Browser Extension**: One-click copy of AI-generated notes into external EHR systems via Chrome extension. Available for paid plans.
- **API Access**: Two API approaches: (1) Processing API for generating insights from recordings without storing data, (2) Application API for accessing all Upheal entities. Allows third-party integration of AI capabilities.
- **Note Generation from Manual Input**: Generate full AI notes from brief text summaries or dictated observations without capturing live sessions. Available in Free plan.
- **Note Generation from Uploaded Recordings**: Upload past session recordings to generate AI notes retroactively. Available in Free plan.

### Workflow Support Before, During, and After Sessions

- Session analytics currently only available for English-language sessions with individual clients (not couples)
- Audio recordings deleted by default after processing - retention must be explicitly enabled
- Client consent required for data processing under HIPAA/GDPR/PHIPA/PIPEDA
- Some features (like AI Assistant logistics management) marked as 'coming soon'
- Treatment plan auto-updates based on client progress marked as 'coming soon'
- PDF/manual case snapshot upload for treatment plans marked as 'coming soon'

### Relevant AI Features in This Area

- **AI Progress Notes**: Automatically generates clinical progress notes from recorded therapy sessions in real-time. Supports 10 note formats (SOAP, DAP, GIRP, BIRP, EMDR, PIRP, SIRP, PIE, Intake, MSE). Notes are instantly generated after sessions and can be edited manually or via AI prompts. The AI learns and adapts to clinician writing style over time with every edit.
- **AI Transcription**: Converts audio and video recordings of therapy sessions into text transcripts. Supports 8 languages: English, Spanish, Portuguese, German, French, Italian, Mandarin, and Hindi. Works with in-person sessions, virtual sessions (any platform), Upheal's built-in telehealth, uploaded recordings, and dictated summaries.
- **AI Treatment Plans (Golden Thread)**: Auto-generates insurance-compliant treatment plans that connect intake forms, session notes, and client progress into a continuous narrative of medical necessity. Creates case snapshots from past sessions/intake forms, generates customizable treatment goals and objectives, and auto-syncs treatment plan elements into progress notes. Supports 170+ therapy modalities. Built against top payer documentation criteria to reduce audit flags.
- **AI Assistant (HIPAA-compliant ChatGPT Alternative)**: Conversational AI assistant with full access to client history, past sessions, treatment plans, and notes. Helps clinicians prepare for sessions by summarizing last session and ongoing themes, identifies patterns and recurring themes across client history, drafts clinical documents (referral letters, discharge summaries, resource lists), and assists with administrative tasks. Lives natively inside Upheal's secure workflow with full clinical context.
- **Smart Edit**: AI-powered note editing via plain-language prompts. Allows clinicians to instantly modify structure, content, tone, and language of clinical documentation. Can shorten, expand, anonymize, translate, or restructure notes using natural language commands.
- **Smart Sections**: Custom AI-generated note sections that allow clinicians to create personalized note templates beyond the standard 170+ clinically approved sections. Clinicians prompt the AI to create custom sections that reflect their clinical voice and documentation structure.
- **Session Analytics**: AI-powered analysis of therapy sessions providing metrics including: talking ratio (therapist vs client speech time), speech cadence (average pacing for both parties), sentiment analysis (positive vs negative language patterns), and tense analysis (future vs past-focused language percentage). Visualized in session map showing metrics over the course of the session.
- **AI Writing Style Learning**: AI learns and adapts to individual clinician's writing style over time. With every edit made to AI-generated notes, the system improves its ability to match the clinician's preferred tone, structure, and clinical voice in future note generations.
- **Multi-language AI Note Generation**: Captures and generates clinical notes from therapy sessions held in 8 languages: English, Spanish, Portuguese, German, French, Italian, Mandarin, and Hindi. Can also translate notes between languages using Smart Edit feature.

### Key Limitations or Missing Capabilities

- Session analytics currently only available for English-language sessions with individual clients (not couples)
- Audio recordings deleted by default after processing - retention must be explicitly enabled
- Client consent required for data processing under HIPAA/GDPR/PHIPA/PIPEDA
- Some features (like AI Assistant logistics management) marked as 'coming soon'
- Treatment plan auto-updates based on client progress marked as 'coming soon'
- PDF/manual case snapshot upload for treatment plans marked as 'coming soon'

### Pricing / Gating Notes

- **Free**: $0
- **Premium**: $1 per session, capped at $69
- Payment processing fees: 2.9% + $0.30 per transaction if using Stripe integration for client payments
- No per-note charges - all AI features included in $1/session Premium pricing
- No usage caps on AI features in Premium plan (unlimited AI Assistant chat, unlimited notes)

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/upheal.json_

---

## Blueprint

### Documentation Workflow Overview

- Documentation-related features found: 8

### Core Note and Treatment Plan Capabilities

- **Session Recording**: Optional audio recording of therapy sessions that serves as input for AI transcription and documentation features. Recording can be enabled/disabled per session.
- **Customizable Note Templates**: Fully customizable documentation templates tailored to specific practice needs and payor requirements. Works alongside AI-generated content to ensure compliance.
- **Clinical Assessments & Measurement Tools**: Digital clinical assessment tools and measurement-informed care instruments that integrate with AI features. Data from assessments automatically incorporated into AI-generated notes and treatment plans.
- **Outcomes Benchmarking (Enterprise)**: Population-level outcomes analysis benchmarked against dataset of 7+ million assessments. Provides visibility into clinical trends and treatment effectiveness.
- **API & Embedded Widgets**: API-first architecture and embeddable widgets for custom integrations with existing EHR systems. Enables organizations to deploy Blueprint's AI capabilities within their own infrastructure.
- **Chrome Extension**: Browser extension that allows use of Blueprint platform on top of existing EHR without switching tabs. Facilitates AI-assisted documentation in third-party systems.
- **SSO & Directory Sync**: Single sign-on and directory synchronization for managing users at scale in organizational deployments.
- **Role-Based Permissions**: Configurable permissions system for different roles within organizations (clinicians, supervisors, administrators).

### Workflow Support Before, During, and After Sessions

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

### Relevant AI Features in This Area

- **Session Transcription**: Automatically transcribes therapy session audio in real-time, converting spoken conversation into text for clinical documentation. Described as accurate even with non-native English speakers and strong accents.
- **Automated Progress Note Generation**: Automatically generates complete clinical progress notes from session transcriptions and existing client data. Integrates information from assessments, homework assignments, and measurement-informed care tools. Notes are generated in draft form for clinician review and editing before finalization. Saves therapists 60%+ of documentation time.
- **AI Treatment Plan Generation**: Drafts smart treatment plans based on session content, client history, diagnosis, and clinical best practices. Generates structured plans including goals, objectives, interventions, and timelines. Clinician reviews and customizes before implementation.
- **Session Prep & Pre-Session Summaries**: Provides automated preparation before each session including a summary of the previous session, reminders of key focus areas, and relevant client history. Surfaces actionable context to help clinicians come prepared.
- **Clinical Decision Support - Assessment & Homework Suggestions**: Provides AI-powered suggestions for evidence-based assessments and worksheets to assign clients between sessions. Offers personalized recommendations for digital homework and interventions based on client needs and treatment goals. Enhances client engagement and treatment outcomes.
- **After-Visit Summary Generation**: Automatically generates patient-facing after-visit summaries following therapy sessions. Provides clients with a clear overview of session content, homework, and next steps.
- **Discharge Summary Generation**: Automates generation of discharge summaries documenting the client's treatment journey, progress, outcomes, and recommendations for follow-up care. Facilitates referrals and continuity of care.
- **Referral Letter & Transfer Summary Generation**: Automatically generates referral letters and transfer summaries for continuity of care when clients transition to other providers or levels of care.
- **Service Verification Letter Generation**: Automatically generates service verification letters documenting client treatment dates, sessions, and other administrative details as needed.
- **Session Safety Cues & In-Session Insights**: Provides real-time safety cues during therapy sessions to support clinician awareness of risk factors. Surfaces actionable insights during the session to enhance care delivery.
- **Post-Session Clinical Insights & Care Enhancement Suggestions**: Provides AI-generated session-level insights after each session, including evidence-based treatment considerations, suggestions to enhance care quality, and tools for continuity of care. Helps clinicians identify patterns and opportunities for intervention.
- **Interactive AI Assistant Chat (Pro)**: Conversational AI interface that allows clinicians to chat with the AI Assistant for complex clinical questions, administrative task delegation, and advanced practice management. Can handle queries about revenue breakdown, utilization goals, SEO website improvements, and marketing strategies. Goes beyond documentation to support broader practice needs.
- **Analytics Dashboards**: Provides practice analytics and insights through visual dashboards. Appears to include AI-driven analysis of practice patterns and performance metrics.

### Key Limitations or Missing Capabilities

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

### Pricing / Gating Notes

- **Core**: $0
- **Plus**: $0.99
- **Pro**: $1.49
- No monthly minimums or contracts - only pay per session used
- Session credits never expire (prepaid credits do not rollover between plan tiers if auto-upgraded)
- Credit card processing fees apply for billing features (standard payment processing)
- 50% discount on first purchase available for first 7 days (promotional)
- Volume discounts available for enterprise/organization deployments
- No additional cost for EHR platform - completely free forever
- No per-user fees for Core EHR features

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/blueprint.json_

---

## Freed

### Documentation Workflow Overview

- Documentation-related features found: 13

### Core Note and Treatment Plan Capabilities

- **Specialty-Specific Templates**: Pre-made templates designed for specific medical specialties (pediatrics, psychiatry, mental health, family medicine, internal medicine, OB/GYN, functional medicine, etc.). Templates are made by real practicing clinicians. Customizable and shareable across colleagues.
- **Custom Template Builder**: Allows clinicians to define exact sections and subsections they want in notes, with granular control. Supports custom AI prompts to instruct the AI directly. Unlimited template versions for different scenarios.
- **Learn My Format**: One-click setup where clinician edits a note and asks Freed to learn their formatting preferences. AI automatically creates a new template based on the edits for future use. Never uses PHI for training.
- **Offline Recording Support**: Handles offline and low-connectivity environments for visit recording. Can record visits without internet connection.
- **File Upload Recording**: Supports uploading pre-recorded audio files in addition to live recordings. Allows batch processing of recorded visits.
- **Team Template Libraries**: Shared template libraries for consistent documentation across multiple clinicians in a practice or organization.
- **Shared Patients (Beta)**: Allows multiple clinicians to access and document for shared patients, enabling coordinated team care.
- **Single Sign-On (SSO)**: SSO options for enterprise and group practice authentication and access management.
- **Organization-wide BAA**: Single Business Associate Agreement covering entire organization for HIPAA compliance.
- **Dedicated Account Management**: Dedicated account manager for group practices and healthcare organizations.
- **Live Clinic Onboarding**: Live onboarding sessions for clinic teams and organizations to get started with Freed.
- **Priority Support**: Priority customer support for group practices.
- **7-Day Free Trial**: Free 7-day trial with access to Premier features and full functionality. No credit card or commitment required.

### Workflow Support Before, During, and After Sessions

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

### Relevant AI Features in This Area

- **Ambient AI Medical Scribe**: Listens to patient conversations in real-time or from uploaded recordings, transcribes clinical encounters, and generates structured clinical notes (SOAP, DAP, or custom formats). Filters out filler words and background noise, derives medications, dosages, and abbreviations, and adapts terminology to be medically precise.
- **AI Clinician Assistant**: Persistent AI chat assistant that provides pre-charting support, clinical decision support with cited evidence-based sources, note editing and summarization, prior visit retrieval, and custom clinical document generation. Consolidates Magic Edit, pre-charting chat, and transcript/note summarization into one unified interface. Can answer clinical questions, restructure notes, pull ICD-10 codes, and generate custom care documents.
- **Magic Edit**: AI-powered note editing feature that allows clinicians to make sweeping changes to notes using simple voice or text commands. Can restructure notes, add details, change formatting, adjust tone, or reorganize content (e.g., 'organize supplement recommendations by body system' or 'change all patient name to client') without manual retyping. Now consolidated into the Clinician Assistant.
- **Visit Prep and Pre-charting**: Automatically surfaces patient visit history summaries, medication and supplement dosages, top insights from past visits, and procedural details before appointments. Provides quick summaries of last visit, follow-up items, and patient context without manual chart searching. Clinicians can also input information before visits and pause/restart recordings.
- **ICD-10 Code Generation**: Automatically generates ICD-10 diagnosis codes based on visit content and note documentation. Analyzes transcript and note to identify relevant diagnoses and selects the most appropriate billable, clinician-useful codes. Codes appear immediately when note is complete. Provides dropdown menu with alternative code recommendations. Specialty-aware predictions that adapt to clinician's specialty and commonly documented conditions.
- **CPT and E/M Code Suggestions**: Part of the Freed Coding Assistant (included in Premier and Groups), provides CPT and E/M code suggestions in addition to ICD-10 codes. Offers post-visit coding optimizations and includes clinic-wide Coding Dashboard for tracking.
- **Patient Instructions Generator**: Automatically generates patient-friendly instructions and post-visit summaries from complex medical notes. Converts clinical documentation into clear, organized guidance with simple summaries and clear action items. Every note comes with instructions that are ready to send. Clinician controls when and how to email instructions to patients.
- **Clinical Letter Generation**: Auto-generates clinical letters using visit context, including referral letters, absence notes, return-to-work certifications, exemption notes, caregiver letters, and more. Growing library of 14+ letter types. Professional formatting with clean greeting and sign-off. Letters are instantly generated after visits and can be edited, copied, or downloaded as PDFs.
- **Treatment Plan Generator**: As therapy progresses, generates and documents measurable treatment goals, patient progress, and specific interventions from cognitive behavioral approaches to medication management. Creates structured treatment plans based on visit discussions.
- **AI Template Learning**: AI learns clinician's preferred note formatting, phrasing, terminology (e.g., 'client' vs 'patient'), and structure from their edits. One-click setup where clinician edits a note and asks Freed to 'learn my format.' System automatically creates new templates for future use based on learned preferences. Continuously improves with use.
- **EHR Push (AI-Powered Field Mapping)**: Chrome extension with AI agent that automatically maps note sections to correct EHR fields and transfers notes with a single click. Works with any browser-based EHR without requiring traditional API integrations or IT setup. The AI agent navigates the EHR interface and intelligently places content in appropriate fields.
- **Multilingual Transcription and Translation**: AI scribe understands and transcribes visits conducted in 90+ languages. Supports code-switching (switching between languages mid-conversation). Automatically translates final notes into fluent English while maintaining accuracy and clinical context. Patient instructions retain plain English while medical terminology is preserved in notes.
- **AI Hallucination Detection**: Notes are double-checked before delivery. System scans for AI hallucinations or inconsistencies, checks notes for consistency and accuracy. Uses data feedback loops to continuously improve. Human clinicians regularly review safely anonymized samples to validate model performance. Most hallucinations occur during brief or incomplete visits.
- **Timestamped Transcripts**: Provides full, searchable transcripts of clinical conversations with timestamps. Useful for complex case reference and detailed review. Allows clinicians to locate specific parts of conversations quickly.

### Key Limitations or Missing Capabilities

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

### Pricing / Gating Notes

- **Starter**: $39/month
- **Core**: $79/month
- **Premier**: $119/month ($104/month when billed annually)
- **Groups**: Custom pricing
- **Front Desk Starter**: $149/month per 250 calls
- Front Desk AI is a separate product with separate pricing: $149/month per 250 calls (Starter). Advanced plan pricing not yet disclosed.
- Student discount available: 50% off for students, trainees, or fellows (requires proof of enrollment).
- Annual billing discount: Premier tier is $1,248/year ($104/month effective rate vs $119/month).
- Group pricing is custom and negotiated per organization.
- No refunds by default for cancellations (subscription continues until end of billing cycle).
- Usage beyond 40 visits/month on Starter tier requires upgrade to Core tier ($79/month for unlimited).

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/freed.json_

---

## Yungsidekick

### Documentation Workflow Overview

- Documentation-related features found: 8

### Core Note and Treatment Plan Capabilities

- **Multiple Input Methods**: Supports live session recording, pre-recorded audio file uploads, and Dictate Recap voice summaries. Works with online and in-person sessions.
- **Multiple Note Formats**: AI generates progress notes in SOAP, DAP, BIRP, GIRP, and custom formats based on clinician preference.
- **EHR Integration**: Direct integration with EHR systems like Healthie. Automatically identifies clients from connected EHR accounts and syncs SOAP notes and treatment plans between platforms. Export capabilities to other clinical software.
- **Session Preparation Highlights**: AI generates session preparation highlights to help clinicians prepare for upcoming appointments.
- **Visual Progress Charts**: Displays client progress through visual charts tracking depression, anxiety, and other clinical indicators over time.
- **Organizational Roles & Permissions**: Group practice plans include organizational role management and permission controls for team members.
- **Shared Templates**: Group practices can share custom note templates across team members for consistency.
- **Centralized Minute Tracking**: Group practices get centralized tracking of session minutes across all clinicians.

### Workflow Support Before, During, and After Sessions

- Requires internet connection for all AI processing
- Requires up-to-date web browser for platform access
- Requires audio recording capability (microphone or recording device)
- Session audio must be uploaded/recorded through platform for AI processing
- Specific AI models and underlying technology not publicly disclosed
- No API access documented for AI outputs or programmatic integration
- Minute-based pricing limits may constrain usage for high-volume practices (overage charges apply at $0.03/minute)
- Audio file size limits not publicly disclosed

### Relevant AI Features in This Area

- **AI Audio Transcription**: Converts therapy session audio recordings into text transcripts. Supports live recording, pre-recorded file uploads, and audio from online/in-person sessions. Processes audio and generates transcript within 1 minute.
- **AI Progress Note Generation**: Automatically generates clinical progress notes in multiple formats (SOAP, DAP, BIRP, GIRP) from session transcripts or dictated recaps. Produces EHR-ready documentation within 1 minute. Extracts symptoms, medications, treatment goals, and clinical observations from session content.
- **AI Treatment Plan Generation**: AI extracts and synthesizes treatment goals from session content to automatically generate treatment plans. Includes ICD-10 code suggestions for diagnosis coding. Plans sync with integrated EHR systems.
- **AI Session Reports (Therapist and Client)**: Generates detailed analytical reports from session transcripts. Therapist reports include clinical patterns, resilience strategies, therapeutic relationship observations, and session insights. Client reports provide session summaries suitable for patient review between appointments.
- **AI Meta Reports (Psychological Profiles)**: Consolidates data from multiple therapy sessions to build comprehensive psychological profiles and client histories. Analyzes patterns across sessions to provide holistic view of client progress and therapeutic journey.
- **AI-Powered Measurement-Based Progress Tracking**: Real-time analysis that tracks depression and anxiety levels session-by-session. Flags weekly diagnostic markers for depression, anxiety, and life satisfaction. Displays client progress through visual charts and identifies nuanced shifts between formal assessments. Designed for earlier detection of clinical concerns through continuous monitoring.
- **AI Clinical Assistant (Conversational Query System)**: Therapists can consult an AI assistant for client-specific insights. Assistant can quote exact words from sessions, recall details from client biography or treatment plan, retrieve information across multiple sessions, monitor treatment plans, and provide diagnostic marker summaries. Acts as intelligent search and retrieval system across client records.
- **Dictate Recap Feature**: Alternative to session recording - therapists provide spoken session recap in their own words after the session ends. AI processes the dictated summary to generate progress notes and reports without storing sensitive full-session audio. Uses templated script guidance to ensure comprehensive recap.
- **Custom AI Template Builder**: Allows clinicians to create custom documentation templates using natural language prompts. AI structures notes according to user-defined sections and clinical preferences (e.g., EMDR eight-phase protocol, trauma-focused SOAP, IFS notes, supervision reports, discharge summaries). Users provide section-specific prompts, and AI extracts and organizes relevant session data to match template structure. Preserves clinician's clinical voice and documentation style.
- **AI Automatic Anonymization**: Automatically anonymizes transcripts and reports by removing or replacing identifiable names, details, and sensitive context before storage. Therapists can choose complete anonymization while retaining clinical utility. System can use coded identifiers (e.g., 'Client_1023') instead of real names to remove data from PHI category.

### Key Limitations or Missing Capabilities

- Requires internet connection for all AI processing
- Requires up-to-date web browser for platform access
- Requires audio recording capability (microphone or recording device)
- Session audio must be uploaded/recorded through platform for AI processing
- Specific AI models and underlying technology not publicly disclosed
- No API access documented for AI outputs or programmatic integration
- Minute-based pricing limits may constrain usage for high-volume practices (overage charges apply at $0.03/minute)
- Audio file size limits not publicly disclosed

### Pricing / Gating Notes

- **Flexible (Trial/Pay-as-you-go)**: $0/month base + $0.03 per minute
- **Starter**: $9.99
- **Basic**: $39.99 (discounted from $53)
- **Professional**: $99.99 (discounted from $145)
- **Group Practice**: Custom pricing
- Overage charges: $0.03 per minute of session audio beyond plan limits
- Group practice custom pricing - exact costs not publicly disclosed, requires sales contact
- No other AI-specific add-on costs identified (all AI features included in base plans)

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/yungsidekick.json_

---

## Simplepractice

### Documentation Workflow Overview

- Documentation-related features found: 2

### Core Note and Treatment Plan Capabilities

- **Note Taker (AI Progress Notes)**: AI-powered tool for automated transcription and progress note generation. Includes real-time transcription, dictation, file upload, and pre-session summaries.
- **AI Support Chatbot**: AI-powered chatbot for quick answers and connection to support team.

### Workflow Support Before, During, and After Sessions

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

### Relevant AI Features in This Area

- **Real-time Session Transcription**: Creates live transcript during telehealth or in-person appointments. Transcription supports multiple languages (English, Spanish, French, German, Italian, Portuguese, Dutch, Polish, Swedish, Norwegian, Catalan, Croatian, Czech, Romanian) and diverse accents. Transcript available for review for up to 7 days or until note is signed and locked, whichever comes first.
- **AI-Generated Progress Notes**: Automatically generates draft progress notes from session transcripts in multiple formats (SOAP, DAP, BIRP). Adapts to clinician's documentation style by analyzing previous progress notes for the same client. Learns formatting, note sections, writing style, complexity level, and overall structure preferences. Saves average of 5 hours per week per clinician.
- **Voice Dictation for Notes**: Allows clinicians to dictate session information post-session without recording the live session. Clinician speaks thoughts into the tool, and AI generates a structured, professional note. Available via web browser and SimplePractice for Clinicians mobile app.
- **Audio/Text File Upload for Note Generation**: Clinicians can upload pre-recorded audio files or text files to generate progress notes. Useful for sessions recorded outside SimplePractice or for importing existing notes.
- **Pre-Session Client Summary**: Generates AI-powered summary of previous sessions to help clinicians prepare for upcoming appointments. Available only via web browser.
- **AI Customer Support Chatbot**: AI-powered chatbot provides quick answers to user questions and connects users with SimplePractice support team. Used within SimplePractice account for support requests.
- **AI Fraud Detection**: AI used internally to detect and prevent potentially fraudulent activity in accounts. Background security feature.

### Key Limitations or Missing Capabilities

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

### Pricing / Gating Notes

- **Starter**: $49/month (promotional: $24/month for first 3 months)
- **Essential**: $79/month (promotional: $39/month for first 3 months)
- **Plus**: $99/month (promotional: $49/month for first 3 months)
- Note Taker: $35/month per clinician (after 30-day free trial) - applies to all plan tiers
- No per-note usage fees or caps on Note Taker usage
- No additional storage fees for AI-generated notes or transcripts
- ePrescribe (separate add-on): $49/month per clinician plus $89 one-time setup fee
- Group appointments feature: $20/month add-on for Essential plan (included in Plus plan)

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/simplepractice.json_

---

## Therapynotes

### Documentation Workflow Overview

- Documentation-related features found: 15

### Core Note and Treatment Plan Capabilities

- **Progress Notes (SOAP/DAP/BIRP)**: SOAP, DAP, and BIRP format progress note templates with structured fields (diagnosis, medications, mental status, risk assessment) and free-text areas. Auto-populates diagnosis, medications, and treatment objectives from prior notes and Treatment Plan.
- **Custom Progress Note Templates**: Template builder allowing Practice/Clinical Administrators to create custom Progress Note templates. Can start from SOAP, DAP, BIRP, or Standard template and add/remove/reorder components. Active/inactive status controls clinician visibility.
- **Treatment Plans**: Structured treatment planning with diagnosis, presenting problem, treatment objectives, and frequency. Created after Intake Note (prompted via To-Do). Diagnosis and objectives auto-pull into subsequent Progress Notes.
- **Auto-Save and Recovery**: Notes auto-save content approximately every 60 seconds while working. If browser crashes or closes, auto-saved content can be recovered when note is re-opened. System prompts to restore auto-saved data.
- **Quick History**: Allows clinicians to view specific fields from previous notes and pull that information forward into the current note with one click. Supports continuity across sessions (medications, interventions, etc.).
- **Draft Saving and To-Do Integration**: Notes can be saved as drafts multiple times before signing. Unsigned notes generate To-Do list items for tracking. Drafts accessible from To-Do list, calendar, or patient Documents tab.
- **Electronic Signature and Note Locking**: Clinicians electronically sign notes when complete, finalizing them for billing and compliance. Signed notes are locked (amendment workflow not documented).
- **Integrated Diagnosis Coding**: Searchable DSM-5 and ICD-10 diagnosis databases built into notes. Diagnosis codes auto-populate from Treatment Plan or most recent note. Supports multiple diagnoses with descriptions and justifications.
- **Medication Management in Notes**: Medication fields with UMLS RxNorm database auto-suggest for generic, brand-name, and supplements. Captures dose, frequency, symptoms treated, and instructions. Medications auto-pull from previous notes or Client History Form.
- **Risk Assessment Documentation**: Structured risk assessment fields for suicidal, homicidal, self-harm, and other risk areas. Captures level of risk, intent, plans, means, risk factors, and protective factors. Supports multiple risk areas per note.
- **Current Mental Status Exam**: Comprehensive mental status exam fields in Progress Notes. One-click autofill for 'All Normal' or 'All Not Assessed'. Individual fields can be selected from dropdown or custom text entry.
- **Outcome Measures Integration**: Outcome measures can be sent to clients, completed (by client or clinician), and viewed within Progress Notes. Includes timeline charts and insights for tracking progress over time.
- **Psychotherapy Notes (Process Notes)**: Separate psychotherapy note type for therapist's personal observations and impressions, kept separate from medical record per HIPAA. Different access controls than progress notes.
- **Activity Log and Audit Trail**: Activity log tracks user logins, failed attempts, note editing, note signing, and other user activities. Supports audit readiness and compliance monitoring.
- **Appointment-Linked Note Creation**: Notes must be linked to scheduled appointments with appropriate service type. Note type determined by appointment service type. Creates structured workflow but requires calendar scheduling for all documentation.

### Workflow Support Before, During, and After Sessions

- Notes cannot be created without scheduled appointment - no standalone documentation
- Auto-save occurs every ~60 seconds (not instant, not configurable)
- TherapyFuel Scribe requires minimum 8 minutes of session audio to generate transcript
- Scribe transcript processing takes up to 5 minutes after session ends
- Custom template creation/editing restricted to Practice/Clinical Administrator roles
- No offline mode or mobile app mentioned for documentation
- Split-screen note review requires manual window management (drag tabs)
- No version history or change tracking for draft notes mentioned
- Amendment workflow for signed notes not documented

### Relevant AI Features in This Area

- **TherapyFuel Scribe**: Records and transcribes therapy sessions (in-person or telehealth), then generates progress notes from the transcript. Requires minimum 8 minutes of audio. Transcript processing takes up to 5 minutes. Clinician must review and edit generated content before signing.
- **Progress Note Generation from Session Summary**: Clinician enters brief session summary text, and AI generates Subjective, Objective, Assessment, and Plan sections. Works with any Progress Note template (SOAP, DAP, BIRP, custom). Clinician reviews and edits before finalizing.
- **Client History Summary**: AI-generated summary of patient's Client History Form responses, appearing at top of intake forms and when writing Intake Notes. Used for session prep and quick chart review. Clinicians can rate summary quality for improvement.
- **Contact Note Generation**: Generates Contact Notes from secure message threads, summarizing client interactions for record-keeping. Includes 'Adjust Tone' feature (formal, concise, descriptive). Primarily for non-session documentation.

### Key Limitations or Missing Capabilities

- Notes cannot be created without scheduled appointment - no standalone documentation
- Auto-save occurs every ~60 seconds (not instant, not configurable)
- TherapyFuel Scribe requires minimum 8 minutes of session audio to generate transcript
- Scribe transcript processing takes up to 5 minutes after session ends
- Custom template creation/editing restricted to Practice/Clinical Administrator roles
- No offline mode or mobile app mentioned for documentation
- Split-screen note review requires manual window management (drag tabs)
- No version history or change tracking for draft notes mentioned
- Amendment workflow for signed notes not documented

### Pricing / Gating Notes

- **Solo**: $69/month
- **Group**: $79/month + $50/month per additional clinician
- **TherapyFuel AI Add-on**: $40/month per clinician
- TherapyFuel AI: $40/month per clinician
- Premium Telehealth: $15/month per clinician
- Electronic Billing: $0.14 per electronic claim, ERA claim, and eligibility request

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/therapynotes.json_

---

## Healthie

### Documentation Workflow Overview

- Documentation-related features found: 20

### Core Note and Treatment Plan Capabilities

- **Custom Charting Templates**: Pre-built industry templates (SOAP, ADIME, Free Text) plus fully customizable templates via drag-and-drop Form Builder. Support for structured fields, free-text, rich text formatting, multiple field types.
- **Auto-save for Chart Notes**: Continuous auto-save while editing notes; green indicator shows last save timestamp; prevents data loss during documentation.
- **Smart Fields**: Auto-populate chart note fields from intake form responses (client demographics, insurance, health data). Reduces duplicate data entry.
- **Pre-fill from Prior Notes**: Enable templates to auto-populate from previous session notes for same client. Pulls from most recent note using same template. Saves time on follow-up sessions.
- **Smart Phrases (Text Shortcuts)**: Create and save standard charting phrases/snippets for quick insertion during documentation. Can be shared across team members.
- **Sign and Lock Notes**: Digital signature with timestamp; locking prevents edits (except addendums); multiple providers can sign; full Chart Note History audit trail.
- **Addendums**: Add addendums to signed/locked notes while preserving original note integrity. Supports compliance requirements.
- **Quick Profile Panel**: Side panel accessible during charting shows customizable client info: goals, medications, recent metrics, care plan, past notes summary. Reduces need to navigate away from note.
- **Workflows Dashboard**: Centralized view of appointments requiring action. Filter by provider, client, date range, documentation type. Shows chart note status (Created, Signed, Locked). Tracks incomplete documentation across organization.
- **ICD-10 Diagnosis Integration**: ICD-10 code search/selection fields in charting templates. Diagnoses auto-populate to client profile and billing forms (CMS 1500, Superbills).
- **CPT/Billing Fields in Charts**: CPT codes, units, fee per unit can be embedded in charting templates. Auto-populates billing forms.
- **Import Chart Note to Care Plan**: When adding recommendations to care plan, can import content directly from specific chart note fields. One-directional flow (chart → care plan).
- **Care Plan / Treatment Plan Builder**: Create care/treatment plans with goals, recommendations, documents. Save as templates for reuse. Only one active plan at a time (visible to client). Track goal completion, streaks, progress.
- **Group Session Charting**: Create chart notes for group sessions (not just individual). Same template-based workflow.
- **View Multiple Chart Notes at Once**: Side-by-side view of multiple chart notes for same client. Aids in reviewing history.
- **E-fax Chart Notes**: HIPAA-compliant e-fax of chart notes to other providers.
- **Export Chart Notes / Chart Summary**: Export individual notes or download full client chart summary.
- **Share Chart Notes with Clients**: Option to share specific chart notes or post-session summaries with clients via portal.
- **Zoom Integration for Telehealth**: Direct integration with HIPAA-compliant Zoom. Video sessions, cloud recording. Required for AI Scribe functionality.
- **Audit Logs**: Chart Note History tracks all signatures, timestamps, actions. Phase 1 audit logs via API capture appointment, charting note, claim, login history.

### Workflow Support Before, During, and After Sessions

- Charting functionality only available via web browser (not mobile app)
- AI Scribe requires HIPAA-compliant Zoom integration (cannot use other video platforms)
- AI Scribe supports one-on-one sessions only (no group sessions)
- AI Scribe is post-session only (not real-time/ambient during session)
- Phone dial-in for AI Scribe must be direct to Zoom (speaker phone may cause incomplete transcripts)
- No explicit version history or rollback capability for chart notes
- Deleted documents recovery requires contacting support (not self-service)
- Pre-fill pulls from most recent note with same template (cannot select specific prior note)
- Only one active care plan at a time per client

### Relevant AI Features in This Area

- **AI Scribe by Healthie**: Automatically transcribes Zoom telehealth sessions and generates chart note drafts within 10-15 seconds after session completion. Analyzes transcript and populates any charting template (SOAP, ADIME, custom forms) based on field labels. Requires clinician review and editing.

### Key Limitations or Missing Capabilities

- Charting functionality only available via web browser (not mobile app)
- AI Scribe requires HIPAA-compliant Zoom integration (cannot use other video platforms)
- AI Scribe supports one-on-one sessions only (no group sessions)
- AI Scribe is post-session only (not real-time/ambient during session)
- Phone dial-in for AI Scribe must be direct to Zoom (speaker phone may cause incomplete transcripts)
- No explicit version history or rollback capability for chart notes
- Deleted documents recovery requires contacting support (not self-service)
- Pre-fill pulls from most recent note with same template (cannot select specific prior note)
- Only one active care plan at a time per client

### Pricing / Gating Notes

- **Core**: $19.99/month ($18/month annual)
- **Essentials**: $49.99/month ($45/month annual)
- **Plus**: $129.99/month (~$117/month annual)
- **Group**: $149.99+/month
- **Enterprise**: Custom pricing
- AI Scribe add-on: $35/month for 40 hours (Extra Light) up to $2,000/month for 2,500 hours (Extra Large)
- AI Scribe overages: $0.85/hour (rounded up), billed monthly
- Dedicated Inbound E-Fax: $9.99/month add-on (Essentials plan)
- Annual billing saves 10% on base plan cost

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/healthie.json_

---

## Jane

### Documentation Workflow Overview

- Documentation-related features found: 15

### Core Note and Treatment Plan Capabilities

- **Custom Chart Templates**: Modular template builder with 15+ chart parts including Note, Smart Options & Narrative, Dropdowns, Checkboxes, Range/Scale, Body Chart annotation, Vitals, Signatures, and more. Template Library offers community-shared templates by discipline. Practitioners can enable/disable templates per their profile.
- **Smart Options & Narrative**: Quick-click charting tool that auto-generates narrative text from selected options. Practitioners define subjects and choices (with optional short labels), select findings via buttons/checkboxes/dropdowns, and Jane generates a prose summary. Supports intro, middle, and outro text customization.
- **Phrases (Keyboard Shortcuts)**: Create keyboard shortcuts for frequently used text (up to 2000 characters per phrase). Type shortcut in chart, expands to full text. Supports formatting. Specific to each practitioner profile.
- **Sign & Lock Charts**: Draft-to-signed-to-locked workflow. Charts remain in draft state until practitioner clicks 'Sign', which locks the entry with digital timestamp and signature. Post-signing changes tracked as 'Amendments' with timestamps. Only chart author can sign their own entries.
- **Day View Charting Dashboard**: Visual dashboard showing practitioner's daily appointments with chart status indicators (no chart, unlocked/draft, locked/signed). One-click access to patient charts from appointments. Only visible to practitioners (not admin staff) for tracking documentation completion.
- **Treatment Plans**: Organize chart entries by patient concern/diagnosis. Create named plans with up to 3 diagnosis codes and suggested visit count. Link chart entries to plans. Treatment Plans Report shows open plans and visit progress across caseload. Separate plans per discipline/concern recommended.
- **Supervision Workflow**: Supervisees can request supervisor signature on charts. Charts go to supervisor queue for review. Supervisors can leave feedback (not part of patient record), send back for changes (chart returns to draft with 'Changes Requested' tag), or sign off. Dashboard shows chart status summary.
- **Activity Log (Audit Trail)**: Tracks all user actions within the account for HIPAA compliance including chart access, creation, modification, report generation, staff profile changes. Filterable by staff member, action type, and date range. Full Access users and Account Owner can view clinic-wide data.
- **Duplicate Chart Entry**: Copy entire previous chart entry (all content and formatting) to reuse as starting point for new note. Acts as built-in copy/paste for chart content.
- **Outcome Measure Surveys**: Create clinical surveys with scored questions to quantify patient experience at specific points in time. Surveys can be sent before or after appointments. Results appear in patient chart.
- **Intake Forms**: Customizable forms sent to patients before appointments to collect information and consent. Can be included in online booking workflow. Data captured in patient chart.
- **Diagnosis & CPT Codes**: Add ICD-10 diagnosis codes and CPT codes to chart entries by typing '#' followed by code name or number. Available as part of US insurance billing features. Up to 12 diagnosis codes per entry. Manual entry (not auto-suggested).
- **Chart Privacy Controls**: Set default chart privacy level per staff member (All Staff, All Staff in my Discipline, My Eyes Only). Practitioners can share charts with specific individuals. Permissions can be added or revoked as needed.
- **Telehealth In-Session Charting**: Picture-in-Picture mode floats video window while charting in background. Split screen option to resize windows for simultaneous video and chart viewing. Can create/edit charts during online appointments.
- **Rich Text Formatting**: Format chart entry text with bold, underline, italics, highlighting, and text color. Formatting cannot be changed after chart is signed.

### Workflow Support Before, During, and After Sessions

- AI Scribe only available in United States and Canada
- Phrases limited to 2000 characters each
- No bulk chart signing capability (must sign individually)
- No conditional logic or branching in chart templates
- No explicit autosave mechanism documented
- No version control for draft chart entries
- Integrated fax requires separate Documo subscription
- SMS appointment reminders availability varies by region

### Relevant AI Features in This Area

- **AI Scribe (Smart SOAP Note)**: Records or uploads audio of clinical sessions and uses AI to transcribe and generate SOAP notes. Supports customizable prompts for note formatting, global prompt settings for clinic-wide standards, and test mode with sample transcripts. Clinicians review, edit, and sign AI-generated drafts.

### Key Limitations or Missing Capabilities

- AI Scribe only available in United States and Canada
- Phrases limited to 2000 characters each
- No bulk chart signing capability (must sign individually)
- No conditional logic or branching in chart templates
- No explicit autosave mechanism documented
- No version control for draft chart entries
- Integrated fax requires separate Documo subscription
- SMS appointment reminders availability varies by region

### Pricing / Gating Notes

- **Balance**: $54
- **Practice**: $79 base + $35/month per full-time practitioner
- **Thrive**: $99 base + $40/month per full-time practitioner
- AI Scribe Unlimited: $15/month per practitioner (beyond 5 free notes/month)
- Group Telehealth: Add-on pricing not disclosed in public documentation
- Insurance Billing (US): Add-on pricing not disclosed; requires separate Claim.MD clearinghouse account
- Jane Websites: Add-on pricing not disclosed
- Documo subscription required for integrated outbound fax (separate cost)
- Part-time practitioners: $17.50/month (Practice plan) or $20/month (Thrive plan)
- Full-time practitioners: $35/month (Practice plan) or $40/month (Thrive plan)

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/jane.json_

---

## Mentalyc

### Documentation Workflow Overview

- Documentation-related features found: 17

### Core Note and Treatment Plan Capabilities

- **Progress Note Creation (AI-Generated)**: AI generates structured clinical notes from recorded, uploaded, dictated, or typed session content. Supports multiple input methods: live recording, audio file upload, voice-to-text dictation, manual typing. 10-15 minute processing time.
- **Template System (100+ Templates)**: SOAP, DAP, BIRP, GIRP, PIE, SIRP, EMDR, Play Therapy, Psychiatry, and 100+ other formats. Custom template builder allows selection of sections to include/exclude. Different client types: Individual, Child, Couple, Family, Group.
- **Custom Template Builder**: Visual interface allows clinicians to select which sections to include or exclude from notes (e.g., Presenting Problems, Psychological Factors, Biological Factors, EMDR-specific sections). Templates control what sections AI includes in generated note.
- **Treatment Plan Generation (AI)**: AI generates SMART goals and treatment plans from session notes. Goals derived from session content, not generic libraries. Diagnosis optional. Goals link to progress tracking. Clinician reviews, edits, approves.
- **Note Editing and Finalization**: Clinicians can freely edit any section of AI-generated notes. Can add custom content, diagnoses, risk notes. Sign and finalize when complete. Audio recordings deleted after note creation (max 3-day retention).
- **EHR Integration (Browser Extension)**: One-click transfer of notes to EHR via Chrome browser extension. Works with SimplePractice, TherapyNotes, Jane App, and most web-based EHRs. One-way transfer (copy note to EHR); not bidirectional API integration.
- **Session Recording (Live)**: Live recording during in-person or telehealth sessions (with client consent). Recording is unobtrusive and happens in background. No real-time transcription displayed during session.
- **Audio File Upload**: Upload pre-recorded session audio files in various formats. AI processes uploaded audio to generate notes.
- **Prior Session Referencing (Continuity of Care)**: Notes automatically reference prior sessions to maintain the 'golden thread' of treatment. Treatment plans pull from session history. Progress tracking aggregates data across sessions.
- **Supervision Notes**: Generate supervision session notes. Available for supervisors and supervisees.
- **Group Therapy Notes**: Generate individual progress notes for each group member in group therapy sessions.
- **Client Session Summaries**: Generate summaries of sessions that can be shared with clients.
- **Consent Forms & BAA**: Ready-to-use consent form templates and Business Associate Agreement (BAA) available within app. BAA can be signed directly in app profile.
- **Session Analytics**: Analytics on session content and patterns. Part of AI Progress Tracker functionality.
- **Child, Couple, and Family Therapy Support**: Specialized templates and note formats for child, couple, and family therapy sessions.
- **EMDR, Play Therapy, Psychiatry Modalities**: Specialized templates for EMDR, Play Therapy, and Psychiatry sessions with modality-specific sections.
- **Progress Charts (Symptom & Goal Tracking)**: Visual charts showing symptom trends and goal attainment over time. Part of AI Progress Tracker. Can review before sessions to prepare.

### Workflow Support Before, During, and After Sessions

- Behavioral health only - not suitable for medical, surgical, or primary care documentation
- No real-time transcription or live note preview during sessions (record-then-process model)
- 10-15 minute processing delay after session before notes are available
- One-way EHR integration via browser extension (not bidirectional API sync)
- Cannot automatically pull patient data from EHR (diagnoses, medications, prior notes)
- Cannot write structured data to discrete EHR fields (e.g., auto-populate diagnosis codes)
- No ability to select or switch AI models (locked into proprietary engine)
- Cannot combine multiple recordings or add recordings to existing dictations
- Monthly note caps (Mini: 40, Basic: 100, Pro: 160, Super: 330)
- No autosave or draft functionality publicly documented
- No version control or note history/recovery
- No explicit note locking mechanism after signing
- No pre-session automated summary or prep tool
- Browser-based (requires Chrome browser for EHR integration)
- Requires client consent for session recording

### Relevant AI Features in This Area

- **AI Progress Note Generation**: Generates structured clinical notes from recorded, uploaded, dictated, or typed session content. Supports SOAP, DAP, BIRP, GIRP, PIE, SIRP, EMDR, Play Therapy, Psychiatry, and 100+ other formats. 10-15 minute processing time after session.
- **AI Treatment Planner**: Generates SMART treatment goals and intervention plans from saved session notes. Goals derived from documented symptoms and session content, not generic libraries. Diagnosis is optional. Goals link to progress tracking. Clinician can edit, refine, or replace suggested goals before approving.
- **AI Transcription / Voice-to-Text Dictation**: Clinicians can dictate session summaries via voice instead of typing or recording full session. Transcription is processed after dictation (not real-time). Alternative to live recording or manual typing.
- **Alliance Genie™ (AI Therapeutic Alliance Tracking)**: Analyzes therapeutic relationship across 27 clinical areas (emotional bond, collaboration, pacing, ruptures, engagement shifts, resistance patterns, sensitive topic handling). Provides session-level feedback like a supervisor would. Fully automated; no client burden (unlike traditional alliance scales like WAI or SRS). Indirectly supports documentation by providing insights into session dynamics that inform case conceptualization.
- **AI Progress Tracker**: Automatically tracks symptom trends and goal attainment over time by analyzing progress note content. Generates visual charts showing progress at a glance. Supports longitudinal documentation, treatment planning, insurance reporting, and medical necessity documentation.
- **Medical Necessity Documentation (AI-Assisted)**: AI automatically includes medical necessity language in notes to support insurance compliance and reduce treatment denial risk. Embedded in note generation process.
- **CPT Code Auto-Computation**: Automatically suggests CPT codes based on session type and duration. Clinician confirms suggested codes.

### Key Limitations or Missing Capabilities

- Behavioral health only - not suitable for medical, surgical, or primary care documentation
- No real-time transcription or live note preview during sessions (record-then-process model)
- 10-15 minute processing delay after session before notes are available
- One-way EHR integration via browser extension (not bidirectional API sync)
- Cannot automatically pull patient data from EHR (diagnoses, medications, prior notes)
- Cannot write structured data to discrete EHR fields (e.g., auto-populate diagnosis codes)
- No ability to select or switch AI models (locked into proprietary engine)
- Cannot combine multiple recordings or add recordings to existing dictations
- Monthly note caps (Mini: 40, Basic: 100, Pro: 160, Super: 330)
- No autosave or draft functionality publicly documented
- No version control or note history/recovery
- No explicit note locking mechanism after signing
- No pre-session automated summary or prep tool
- Browser-based (requires Chrome browser for EHR integration)
- Requires client consent for session recording

### Pricing / Gating Notes

- **Mini**: $19.99/month (or $14.99/month billed annually)
- **Basic**: $39.99/month (annual billing saves $120/year)
- **Pro**: $69.99/month (annual billing saves $120/year)
- **Super**: $119.99/month (annual billing saves $240/year)
- Higher tier required for treatment planning ($39.99/mo Basic tier minimum)
- Higher tier required for advanced templates and modalities ($69.99/mo Pro tier for EMDR, Play, Psychiatry, 100+ templates)
- Higher tier required for child/couple/family therapy ($69.99/mo Pro tier)
- Higher tier required for full Alliance Genie access ($69.99/mo Pro tier)
- Highest tier required for group therapy notes ($119.99/mo Super tier)
- Mid-cycle overage if monthly note cap exceeded (requires upgrade to higher tier)
- Annual billing offers discount but requires upfront payment ($60-$240 savings depending on tier)
- Team/group practice pricing available but not publicly detailed on pricing page

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/mentalyc.json_

---

## Ensora

### Documentation Workflow Overview

- Documentation-related features found: 10

### Core Note and Treatment Plan Capabilities

- **Progress Notes - Basic Templates**: Standard progress note templates including SOAP, DAP, and BIRP formats. Multiple access points to create notes (from client page, calendar/agenda, or cases tab). Notes linked to service entries for billing. Autosave preserves draft work. E-signature support to sign and lock notes.
- **Progress Notes - Dynamic Form Builder**: Create custom progress note forms with custom fields, sections, and notes. Build client, case, organization, and progress note forms. Support for various input types. Full template customization. User reviews note customization is more limited than desired and 'difficult to make your own documents'.
- **Treatment Plans with Goals & Objectives**: Create treatment plans with multiple goals and objectives. Track goal status. Information from previous treatment plans automatically included when creating new plans. Goal/Objective Library for creating reusable goals and objectives. Can link diagnostic codes (ICD-10) to treatment plans. Diagnostic impressions can be pulled from previous assessments.
- **Wiley Treatment Planner Integration**: Evidence-based, structured templates for treatment planning. Pre-built goals, objectives, and interventions. Saves time with standardized, insurance-compliant language. Integrates directly into note workflow. Can be used for initial notes and updates.
- **Autosave & Draft Management**: Draft notes auto-save as clinicians fill them in, with message displayed in top right corner. However, manual save still required to finalize drafts. User reviews report 'routine to lose data when entering' if users leave page without pressing green Save button. No version history or recovery beyond draft autosave publicly documented.
- **Sign & Lock Workflow**: E-signature functionality to sign progress notes. Once signed, notes lock the associated service record (except status field), requiring special permission to edit. Supports billing integrity and compliance. Audit Notes Report available to show signed progress notes. Good for compliance but may create friction for corrections.
- **Diagnosis Linking (ICD-10)**: Link diagnostic codes to cases, notes, and treatment plans. Classify diagnoses as Primary, Secondary, Tertiary, Quaternary. Diagnostic impressions can be pulled from previous assessments. Manual linking required - does not auto-populate into new notes.
- **Standard Form Sets**: Pre-built clinical document sets that work together. Typically includes assessment, treatment plan, progress note, and discharge summary. Some automation for data flow between documents in a set (rather than typing same information repeatedly).
- **Case-Based Organization**: Clinical information organized within client 'Cases' - essentially folders containing notes, treatment plans, diagnoses, and other clinical data. Each client can have multiple cases for different treatment episodes. Progress notes tied to service entries/appointments for billing purposes.
- **Telehealth (Video Sessions)**: Browser-based telehealth for individual and group sessions. Required for AI Session Assistant functionality. Available as add-on in lower tiers, unlimited in Premier tier.

### Workflow Support Before, During, and After Sessions

- AI Session Assistant only works with TheraNest telehealth sessions (not in-person or external telehealth platforms)
- Browser-based system appears to require internet connection (no offline capability documented)
- AI Session Assistant requires browser extension installation
- Service-note dependency may create workflow friction if documentation precedes or is separate from billing
- No mobile documentation apps mentioned
- No real-time collaboration or co-documentation features documented
- Limited API or integration capabilities publicly documented (third-party HiBoop integration mentioned for outcomes tracking)
- Manual save required to finalize drafts despite autosave functionality
- Clinical data (goals, objectives, diagnoses) does not auto-populate into new notes - manual linking required
- No version history, note recovery, or rollback capabilities beyond draft autosave
- Once notes are signed, special permission required to edit (compliance feature but potential friction)

### Relevant AI Features in This Area

- **AI Session Assistant - Telehealth Note Generation**: Records telehealth sessions via browser extension and converts them into SOAP-formatted progress note drafts. Captures clinical details, themes, client statements, symptoms, and interventions. Designed specifically for mental health therapy (not generic transcription). Draft ready moments after session ends. Fully editable by clinician.
- **AI Session Assistant - Case Summaries**: Pre-session preparation tool that provides consolidated view of ALL case history (not just latest notes). Summarizes past cases, identifies patterns and trends, provides nuanced clinical context. Designed to replace endless tab-switching and enable quick session prep. Highlights patterns that transcription-based tools miss.
- **AI Notes Enhancement**: Post-documentation refinement tool that reviews completed progress notes and provides mental health-specific suggestions. Can enhance language, improve clarity, and improve professionalism. Clinician reviews each suggestion and accepts or rejects. Does NOT generate notes from scratch - only enhances text already written by clinician.

### Key Limitations or Missing Capabilities

- AI Session Assistant only works with TheraNest telehealth sessions (not in-person or external telehealth platforms)
- Browser-based system appears to require internet connection (no offline capability documented)
- AI Session Assistant requires browser extension installation
- Service-note dependency may create workflow friction if documentation precedes or is separate from billing
- No mobile documentation apps mentioned
- No real-time collaboration or co-documentation features documented
- Limited API or integration capabilities publicly documented (third-party HiBoop integration mentioned for outcomes tracking)
- Manual save required to finalize drafts despite autosave functionality
- Clinical data (goals, objectives, diagnoses) does not auto-populate into new notes - manual linking required
- No version history, note recovery, or rollback capabilities beyond draft autosave
- Once notes are signed, special permission required to edit (compliance feature but potential friction)

### Pricing / Gating Notes

- **Essentials**: $29/therapist/month ($27/month annual)
- **Advanced**: $59/therapist/month ($54/month annual)
- **Premier**: $89/therapist/month ($82/month annual)
- AI Session Assistant: $35/clinician/month (included in Premier tier)
- Wiley Treatment Planner: $25/therapist/month (included in Premier tier)
- Telehealth: Pricing not specified for lower tiers (unlimited in Premier)
- Credit card payment processing fees may apply
- Claims processing: Free in Premier tier, 30 free per practice per month in Advanced, additional fees for Essentials tier not specified
- Eligibility checks: Free in Premier tier, 30 free per practice per month in Advanced, additional fees for Essentials tier not specified
- Text & phone reminders: Free in Premier tier, 30 free per practice per month in Advanced, additional fees for Essentials tier not specified

### Short Summary

This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.

_Raw data source: raw/ensora.json_

---

