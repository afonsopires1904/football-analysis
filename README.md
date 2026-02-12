# Football Data Analysis - Premier League 2023/24

## Author
Afonso Pires

## Description
Statistical analysis of the Premier League 2023/24 season using Python, Pandas, and Matplotlib. This project explores goal patterns, shot efficiency, team performance, and tactical insights from 380 matches.

## Data Source
- **Source:** [Football-Data.co.uk](https://www.football-data.co.uk/)
- **Season:** 2023/24
- **League:** Premier League (England Division 0)
- **Total Matches:** 380
- **Teams:** 20

## Technologies Used
- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical computations

## Project Structure
```
football-analysis/
├── data/
│   └── premier_league.csv          # Dataset
├── src/
│   ├── download_data.py            # Data download script
│   ├── explore_data.py             # Initial exploration
│   ├── goals_analysis.py           # Goals statistics
│   ├── shots_analysis.py           # Shot efficiency analysis
│   └── dashboard.py                # Complete dashboard
├── outputs/
│   └── graphs/
│       ├── shots_vs_goals.png      # Scatter plot with trend line
│       └── dashboard.png           # 4-panel dashboard
├── requirements.txt
└── README.md
```

## Analyses Performed

### 1. Goals Statistics
- **Top 5 Teams by Wins:** Identified the most successful teams of the season
- **Goals Distribution:** Analyzed goal frequency per match (histogram)
- **Home vs Away Performance:** Compared scoring patterns by venue
- **Highest Scoring Match:** Found the match with the most total goals

**Key Findings:**
- Average goals per match: ~2.8
- Most common result: 2-1 or 1-1
- Home teams scored more frequently than away teams

---

### 2. Shot Efficiency Analysis
- **Shots on Target vs Goals:** Correlation analysis with scatter plot
- **Conversion Rate:** Calculated efficiency (Goals / Shots on Target × 100)
- **Top 5 Most Efficient Teams:** Teams that convert chances into goals
- **Low Efficiency Teams:** Teams with many shots but few goals

**Key Insights:**
- **Correlation:** Strong positive correlation (y = 0.37x + 7)
- Average conversion rate: **~37%** (1 goal per 3 shots on target)
- Top efficient teams: Newcastle, Arsenal, Man City
- Teams above the trend line are more clinical finishers

---

### 3. Interactive Visualizations
**4-Panel Dashboard includes:**
1. **Top 5 Teams - Total Wins** (Horizontal bar chart)
2. **Goals Distribution per Match** (Histogram)
3. **Shot Efficiency Analysis** (Pie chart) - **56.1%** of teams with most shots win
4. **Half-Time Lead Analysis** (Pie chart) - **72.7%** of teams leading at HT maintain their lead

**Scatter Plot Features:**
- Team labels with yellow boxes
- Red dashed trend line with equation
- Top 5 efficiency rankings overlay
- Saved as high-resolution PNG (300 DPI)

---

### 4. Custom Analysis: Tactical Insights

#### A. Does the team with more shots win?
- **Result:** **56.1%** of matches
- Teams with more shots have a significant advantage
- However, 43.9% still lose/draw despite shot dominance

#### B. Half-Time Lead Retention
- **Result:** **72.7%** maintain their lead
- Strong indicator of final result
- Only 27.3% of teams come back or equalize

## Main Discoveries

1. **Home Advantage is Real**
   - Home teams win more frequently than away teams
   - Higher conversion rates when playing at home

2. **Shot Volume ≠ Guaranteed Victory**
   - Having more shots gives ~56% win probability
   - Shot quality (on target) matters more than quantity

3. **Half-Time Leads are Crucial**
   - 73% of HT leads are maintained
   - Scoring first significantly increases win probability

4. **Efficiency Varies Widely**
   - Top teams convert ~40-50% of shots on target
   - Bottom teams struggle with ~25-30% conversion
   - Finishing quality separates top from mid-table teams

5. **Predictable Score Patterns**
   - Most matches end with 2-4 total goals
   - Low-scoring (0-1 goals) and high-scoring (6+) are rare

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/afonsopires1904/football-analysis.git
cd football-analysis
```

### 2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

**Required packages:**
- pandas
- matplotlib
- numpy

### 3. Download Data
```bash
python3 src/download_data.py
```

### 4. Run Analyses
```bash
# Explore dataset
python3 src/explore_data.py

# Goals analysis
python3 src/goals_analysis.py

# Shots efficiency with scatter plot
python3 src/shots_analysis.py

# Generate complete dashboard
python3 src/dashboard.py
```

### 5. View Results
- **Graphs:** Check `outputs/graphs/` folder
- **Dashboard:** `outputs/graphs/dashboard.png`
- **Scatter plot:** `outputs/graphs/shots_vs_goals.png`

## Requirements
```
pandas>=2.0.0
matplotlib>=3.7.0
numpy>=1.24.0
```

## Dataset Columns Reference

### Key Columns Used:
- **FTHG/FTAG:** Full Time Home/Away Goals
- **HTR/FTR:** Half Time/Full Time Result (H/D/A)
- **HS/AS:** Home/Away Shots (total)
- **HST/AST:** Home/Away Shots on Target ⭐
- **HY/AY:** Home/Away Yellow Cards
- **HR/AR:** Home/Away Red Cards

**Full documentation:** [Football-Data.co.uk Notes](https://www.football-data.co.uk/notes.txt)

## Future Improvements
- [ ] Add temporal analysis (performance over season weeks)
- [ ] Implement predictive models (ML for match outcome prediction)
- [ ] Compare multiple seasons
- [ ] Add player-level statistics
- [ ] Interactive dashboard with Plotly/Dash
- [ ] Defensive metrics (clean sheets, goals conceded)

## License
This project is for educational purposes. Data provided by Football-Data.co.uk.

## Contact
**Afonso Pires**
- GitHub: [@afonsopires1904](https://github.com/afonsopires1904)

---

*Project developed as part of Python data analysis learning journey.*
*Last updated: February 2026*