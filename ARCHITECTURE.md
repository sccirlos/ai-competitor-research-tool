# 🏗️ Architecture Overview

## System Components

```
┌─────────────────────────────────────────────────────────┐
│                    Your Team (5-20 people)              │
│                                                         │
│     👤 User 1    👤 User 2    👤 User 3    👤 User 4   │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Browser Access
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Streamlit Cloud (Free Tier)                │
│                                                         │
│  ┌─────────────────────────────────────────────────┐  │
│  │           streamlit_app.py (UI Layer)           │  │
│  │                                                 │  │
│  │  • Research configuration                      │  │
│  │  • Competitor selection                        │  │
│  │  • Progress tracking                           │  │
│  │  • Results visualization                       │  │
│  │  • File downloads                              │  │
│  └─────────────────┬───────────────────────────────┘  │
│                    │                                   │
│                    │ Python function calls             │
│                    │                                   │
│  ┌─────────────────▼───────────────────────────────┐  │
│  │      Your Existing Python Scripts               │  │
│  │                                                 │  │
│  │  ┌──────────────────────────────────────────┐  │  │
│  │  │  deepcomp_enhanced.py                   │  │  │
│  │  │  • Web scraping orchestration           │  │  │
│  │  │  • Data extraction logic                │  │  │
│  │  │  • Competitor analysis                  │  │  │
│  │  └──────────────┬───────────────────────────┘  │  │
│  │                 │                               │  │
│  │  ┌──────────────▼───────────────────────────┐  │  │
│  │  │  compile_to_csv_enhanced.py             │  │  │
│  │  │  • JSON to CSV conversion               │  │  │
│  │  │  • Data aggregation                     │  │  │
│  │  │  • Report generation                    │  │  │
│  │  └──────────────┬───────────────────────────┘  │  │
│  └─────────────────┼───────────────────────────────┘  │
│                    │                                   │
└────────────────────┼───────────────────────────────────┘
                     │
                     │ API Requests
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│               Firecrawl API (3rd Party)                 │
│                                                         │
│  • Web scraping                                        │
│  • Content extraction                                  │
│  • AI-powered data parsing                            │
│                                                         │
│  Cost: ~$0.01-0.05 per competitor                     │
└─────────────────────────────────────────────────────────┘
                     │
                     │ Scrapes
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            Competitor Websites (Public)                 │
│                                                         │
│  SimplePractice, Jane, TherapyNotes, etc.              │
└─────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. User Initiates Research
```
User clicks "Run Research"
    ↓
Streamlit UI collects parameters:
  - Research mode (AI or Groups)
  - Competitors to analyze
  - Research type (single/multiple/comparison)
    ↓
Passes to deepcomp_enhanced.py
```

### 2. Scraping Phase
```
deepcomp_enhanced.py
    ↓
For each competitor:
    ↓
  Call Firecrawl API with custom prompt
    ↓
  Firecrawl scrapes competitor website
    ↓
  Returns structured JSON data
    ↓
  Save to outputs/YYYY-MM-DD/raw/{competitor}.json
    ↓
Next competitor...
```

### 3. Compilation Phase
```
All JSONs collected
    ↓
compile_to_csv_enhanced.py
    ↓
Aggregates data across competitors
    ↓
Generates multiple CSV files:
  - compiled_features.csv
  - compiled_ai_features.csv
  - groups_offerings.csv
  - service_offerings.csv
  - insurance_offerings.csv
  - market_intelligence.csv
  - care_aide_capability_gaps.csv
    ↓
Also generates text reports
    ↓
All saved to outputs/YYYY-MM-DD/
```

### 4. Results Display
```
Streamlit UI detects completion
    ↓
Loads CSV files and text reports
    ↓
Displays in interactive tables
    ↓
Provides download buttons
    ↓
Users can view/download/analyze
```

## Key Design Decisions

### Why Streamlit?
✅ **Zero frontend code needed** - Pure Python
✅ **Built-in deployment** - Streamlit Cloud is free
✅ **Minimal changes to existing code** - Just a wrapper layer
✅ **Perfect for internal tools** - Great for 5-20 person teams
✅ **Easy maintenance** - One codebase, simple updates

### Why Keep Existing Scripts?
✅ **No rewrite needed** - Saves weeks of development
✅ **Battle-tested logic** - Your scripts already work
✅ **Incremental improvement** - Can enhance over time
✅ **Easy to understand** - Clear separation of concerns

### Data Storage Strategy
- **Temporary file system** on Streamlit Cloud
- **Outputs regenerated** each research run
- **Users download** important results
- **Consider adding** cloud storage (S3/GCS) for history

## Scalability Considerations

### Current Setup (Good for 5-20 users)
- ✅ Multiple simultaneous users
- ✅ Each user can run independent research
- ⚠️ Results not persisted between sessions
- ⚠️ No user-specific data separation

### If You Need to Scale Beyond 20 Users
1. **Add persistent storage** (PostgreSQL, MongoDB)
2. **Implement user authentication** (Streamlit auth or OAuth)
3. **Add job queue** (Celery, Redis) for long-running tasks
4. **Consider upgrading** to Streamlit Teams ($250/year)
5. **Add caching** to reduce redundant API calls

### Cost at Scale
- **20 users, weekly research, 5 competitors each:**
  - Firecrawl: ~100 API calls/week = $5-10/week = $20-40/month
  - Streamlit: Free (Community) or $250/year (Teams)
  - Total: ~$20-65/month

## Security & Compliance

### API Key Protection
```
Local Development:
  .env file (git-ignored)
      ↓
  Loaded by python-dotenv
      ↓
  Used by deepcomp_enhanced.py

Cloud Deployment:
  Streamlit secrets (encrypted)
      ↓
  Accessed via st.secrets
      ↓
  Injected into environment
      ↓
  Used by deepcomp_enhanced.py
```

### Data Privacy
- ✅ **No user data stored** beyond session
- ✅ **API key encrypted** in Streamlit Cloud
- ✅ **Private GitHub repo** for code
- ✅ **All web scraping is public data**
- ⚠️ **No authentication** in basic setup (anyone with URL can access)

### Recommended Security Enhancements
1. Add password protection (simple)
2. Implement user authentication (moderate)
3. Audit logs for research runs (moderate)
4. Rate limiting per user (advanced)
5. Role-based access control (advanced)

## Maintenance Requirements

### Weekly
- Monitor Firecrawl API usage/costs
- Check for any errors in logs

### Monthly
- Review and archive old output files
- Update competitor list if needed
- Check for dependency updates

### Quarterly
- Review and update Python packages
- Assess if usage patterns have changed
- Consider feature enhancements

## Future Enhancements (Optional)

### Quick Wins (1-2 hours each)
- [ ] Add export to Google Sheets
- [ ] Email notifications on completion
- [ ] Favorite/bookmark competitors
- [ ] Dark mode toggle

### Medium Effort (1-2 days each)
- [ ] Historical trend charts
- [ ] Scheduled automated research
- [ ] User accounts and saved searches
- [ ] API endpoint for programmatic access

### Advanced Features (1 week+)
- [ ] Real-time collaboration
- [ ] Custom competitor definitions
- [ ] AI-powered insights on top of data
- [ ] Integration with Slack/Teams
- [ ] Mobile-responsive design

## Comparison to Alternatives

### vs. Building a Custom Web App
- **Time:** Weeks/months vs. hours
- **Cost:** $5k-50k+ vs. $0-20/month
- **Maintenance:** High vs. Low
- **Verdict:** Streamlit wins for internal tools

### vs. No-Code Tools (Retool, Bubble)
- **Flexibility:** More customizable with code
- **Cost:** Cheaper at small scale
- **Learning curve:** Steeper but familiar (Python)
- **Verdict:** Streamlit wins for Python developers

### vs. Jupyter Notebooks
- **User experience:** Much better UI
- **Sharing:** Easier to share with non-technical users
- **Production-ready:** More polished
- **Verdict:** Streamlit wins for team tools

---

**This architecture prioritizes:**
1. ✅ Ease of maintenance (Streamlit auto-deploys, pure Python)
2. ✅ Speed to launch (Hours, not weeks)
3. ✅ Scalability (Handles 5-20 users easily, can grow)
4. ✅ Cost effectiveness ($0-20/month vs. thousands)

Perfect fit for your requirements! 🎯
