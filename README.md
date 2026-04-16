# 🔍 Competitive Research Tool - Streamlit UI

A user-friendly web interface for your competitive research tool, powered by Streamlit and Firecrawl.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Firecrawl API key ([get one here](https://www.firecrawl.dev/))
- Your existing Python scripts: `deepcomp_enhanced.py` and `compile_to_csv_enhanced.py`

### Local Setup (3 minutes)

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Add your API key:**
Create a `.env` file in the same directory:
```bash
FIRECRAWL_API_KEY=your_actual_api_key_here
```

3. **Make sure your scripts are in the same folder:**
```
your-project/
├── streamlit_app.py          # The Streamlit UI (this file)
├── deepcomp_enhanced.py       # Your existing scraper
├── compile_to_csv_enhanced.py # Your existing compiler
├── requirements.txt
├── .env                       # Your API key
└── README.md
```

4. **Run the app:**
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501` 🎉

## 🌐 Deploy to Streamlit Cloud (Free for teams!)

### Step 1: Push to GitHub

1. Create a new **private** GitHub repository
2. Add your files:
```bash
git init
git add streamlit_app.py requirements.txt README.md
git add deepcomp_enhanced.py compile_to_csv_enhanced.py
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

**⚠️ Important:** Add `.env` to your `.gitignore` - never commit API keys!

```bash
echo ".env" >> .gitignore
echo "outputs/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .gitignore
git commit -m "Add gitignore"
git push
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file: `streamlit_app.py`
6. Click "Advanced settings" → "Secrets"
7. Add your secret:
```toml
FIRECRAWL_API_KEY = "your_actual_api_key_here"
```
8. Click "Deploy"!

Your app will be live at: `https://your-app-name.streamlit.app`

### Step 3: Share with Your Team

1. Share the URL with your team (5-20 people)
2. They can access it immediately - no installation needed!
3. Multiple people can use it simultaneously

## 📖 How to Use

### Research Modes

**🤖 AI Features & Capabilities**
- Extracts AI-powered features
- Identifies branded AI solutions
- Analyzes automation levels
- Generates capability gaps vs SimplePractice

**👥 Groups & Service Offerings**
- Group practice features and pricing
- Service offerings (onboarding, data transfer, support)
- Insurance and billing capabilities
- Market intelligence

### Research Types

1. **Single Competitor**: Deep dive into one competitor
2. **Multiple Competitors**: Research several at once (or all)
3. **Head-to-Head Comparison**: Feature-by-feature vs SimplePractice

### Workflow

1. Select research focus and type in sidebar
2. Choose competitors
3. Click "Run Research"
4. Wait for results (usually 2-10 minutes depending on # of competitors)
5. View summaries, data tables, and download files

## 📊 Outputs

The tool generates several types of outputs:

### For AI-Focused Research:
- `compiled_ai_features.csv` - All AI capabilities
- `ai_maturity_summary.csv` - AI maturity assessments
- `care_aide_capability_gaps.csv` - Feature-by-feature gaps
- `branded_solutions.csv` - Named AI products
- `comparison_summary.txt` - Human-readable comparisons

### For Groups-Focused Research:
- `groups_offerings.csv` - Groups-specific features
- `service_offerings.csv` - Data transfer, onboarding, support
- `insurance_offerings.csv` - Insurance and billing
- `market_intelligence.csv` - Market presence and news
- `groups_focused_summary.txt` - Comprehensive summary

All outputs are saved in `outputs/YYYY-MM-DD/` with timestamp.

## 🔧 Troubleshooting

### "Missing required files" error
Make sure `deepcomp_enhanced.py` and `compile_to_csv_enhanced.py` are in the same directory as `streamlit_app.py`.

### "Firecrawl API Key Required" error
- **Local:** Check your `.env` file exists and has the correct key
- **Cloud:** Verify secrets are configured in Streamlit Cloud settings

### Research takes too long
- Start with single competitor first
- Firecrawl can take 1-3 minutes per competitor
- For all competitors, expect 15-30 minutes total

### No results showing
- Check the `outputs/` directory was created
- Verify research completed without errors
- Look at terminal/logs for error messages

## 💰 Cost Estimates

### Streamlit Cloud (Free Tier)
- ✅ Free for public repos
- ✅ Free for private repos (community plan)
- ✅ Sufficient for small teams (5-20 people)
- ✅ No credit card required

### Firecrawl API Costs
- Typically $0.01-0.05 per competitor researched
- Full competitive scan (16 competitors): ~$0.50-1.00
- Monthly for small team: ~$5-20 depending on usage

**Total Monthly Cost: $0-20** (mostly Firecrawl usage)

## 🔐 Security Notes

1. **API Key Protection:**
   - Never commit `.env` files to git
   - Use Streamlit secrets for cloud deployment
   - Rotate keys if exposed

2. **Private Repositories:**
   - Use private GitHub repos for competitive data
   - Control team access via GitHub permissions

3. **Data Storage:**
   - All outputs stored in `outputs/` directory
   - Consider adding cleanup jobs for old data
   - Streamlit Cloud apps have temporary filesystem

## 📈 Next Steps / Enhancements

Consider adding:
- [ ] Scheduled research runs (daily/weekly)
- [ ] Email notifications when research completes
- [ ] Historical trend tracking
- [ ] Export to Google Sheets/Airtable
- [ ] Custom competitor definitions
- [ ] Visual charts and graphs
- [ ] Search/filter within results

## 🆘 Support

- **Streamlit Issues:** [Streamlit Community](https://discuss.streamlit.io/)
- **Firecrawl Issues:** [Firecrawl Docs](https://docs.firecrawl.dev/)
- **GitHub Issues:** Open an issue in your repository

## 📝 License

This tool wraps your existing competitive research scripts with a Streamlit UI.
Ensure you have proper licensing for Firecrawl API usage.

---

**Built with ❤️ using Streamlit + Firecrawl**
