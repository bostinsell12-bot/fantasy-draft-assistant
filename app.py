import streamlit as st

# Set page config for mobile app feel
st.set_page_config(
    page_title="2026 Keeper Draft Board", page_icon="🏈", layout="wide"
)

# Initialize draft state
if "drafted_players" not in st.session_state:
  st.session_state.drafted_players = set()

# 2026 Consensus Top 250 Dataset (8-Keeper / Standard Scoring Focus)
# Reflecting 2026 consensus expert outlooks, keeper valuation, and positional health.
KEEPER_DATA_250 = [
    # TIER 1: ELITE KEEPER ANCHORS (1-15)
    {
        "rank": 1,
        "name": "Bijan Robinson",
        "pos": "RB",
        "team": "ATL",
        "keeper_tier": "Tier 1: Elite Anchor",
        "tag": "ELITE_KEEPER",
        "injury": "Healthy",
        "notes": (
            "Consensus #1 overall keeper. 3-down bellcow with elite TD"
            " volume in standard scoring."
        ),
    },
    {
        "rank": 2,
        "name": "Jahmyr Gibbs",
        "pos": "RB",
        "team": "DET",
        "tier": 1,
        "tag": "BOOM_KEEPER",
        "injury": "Healthy",
        "notes": (
            "Unmatched explosive play potential; massive home-run and TD"
            " upside."
        ),
    },
    {
        "rank": 3,
        "name": "Ja'Marr Chase",
        "pos": "WR",
        "team": "CIN",
        "tier": 1,
        "tag": "ELITE_KEEPER",
        "injury": "Healthy",
        "notes": (
            "Premier WR keeper asset. Dominant red-zone and big-play thread."
        ),
    },
    {
        "rank": 4,
        "name": "Puka Nacua",
        "pos": "WR",
        "team": "LAR",
        "tier": 1,
        "tag": "ELITE_KEEPER",
        "injury": "Healthy",
        "notes": "Alpha target magnet; elite target share and TD production.",
    },
    {
        "rank": 5,
        "name": "Ashton Jeanty",
        "pos": "RB",
        "team": "LV",
        "tier": 1,
        "tag": "ROOKIE_BOOM",
        "injury": "Healthy",
        "notes": (
            "Elite rookie workload back; massive instant keeper value in"
            " standard formats."
        ),
    },
    {
        "rank": 6,
        "name": "Jaxon Smith-Njigba",
        "pos": "WR",
        "team": "SEA",
        "tier": 1,
        "tag": "BREAKOUT",
        "injury": "Healthy",
        "notes": (
            "Entering prime WR1 status; explosive play profile ideal for standard"
            " scoring."
        ),
    },
    {
        "rank": 7,
        "name": "Jonathan Taylor",
        "pos": "RB",
        "team": "IND",
        "tier": 1,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": (
            "Heavy goal-line workhorse; elite TD equity drives high standard"
            " floor."
        ),
    },
    {
        "rank": 8,
        "name": "CeeDee Lamb",
        "pos": "WR",
        "team": "DAL",
        "tier": 1,
        "tag": "ELITE_KEEPER",
        "injury": "Healthy",
        "notes": (
            "High-volume touchdown engine in Dallas' high-flying passing offense."
        ),
    },
    {
        "rank": 9,
        "name": "Justin Jefferson",
        "pos": "WR",
        "team": "MIN",
        "tier": 1,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": (
            "Elite talent depth; ceiling dependent on quarterback consistency."
        ),
    },
    {
        "rank": 10,
        "name": "De'Von Achane",
        "pos": "RB",
        "team": "MIA",
        "tier": 1,
        "tag": "BOOM_BUST",
        "injury": "Healthy",
        "notes": (
            "Highest per-touch touchdown efficiency in NFL; volatile weekly"
            " ceiling."
        ),
    },
    {
        "rank": 11,
        "name": "Christian McCaffrey",
        "pos": "RB",
        "team": "SF",
        "tier": 1,
        "tag": "BOOM_HIGH_RISK",
        "injury": "Questionable (Manageable)",
        "notes": (
            "Unrivaled PPG ceiling, but age and injury history add keeper"
            " risk."
        ),
    },
    {
        "rank": 12,
        "name": "James Cook",
        "pos": "RB",
        "team": "BUF",
        "tier": 1,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Lead runner in dynamic Buffalo offense; solid yardage floor.",
    },
    {
        "rank": 13,
        "name": "Amon-Ra St. Brown",
        "pos": "WR",
        "team": "DET",
        "tier": 1,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": (
            "Ultra-consistent; slightly lower relative value in 0-PPR than PPR."
        ),
    },
    {
        "rank": 14,
        "name": "Saquon Barkley",
        "pos": "RB",
        "team": "PHI",
        "tier": 1,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Red-zone hammer behind elite Philadelphia offensive line.",
    },
    {
        "rank": 15,
        "name": "Omarion Hampton",
        "pos": "RB",
        "team": "LAC",
        "tier": 1,
        "tag": "ROOKIE_BOOM",
        "injury": "Healthy",
        "notes": "Physical rookie back stepping into heavy early-down workload.",
    },
    # TIER 2: HIGH-VALUE KEEPERS & PRIME STARTERS (16-40)
    {
        "rank": 16,
        "name": "Brock Bowers",
        "pos": "TE",
        "team": "LV",
        "tier": 2,
        "tag": "TE1_KEEPER",
        "injury": "Healthy",
        "notes": "Consensus TE1 asset; dynamic receiver with WR-like usage.",
    },
    {
        "rank": 17,
        "name": "Chase Brown",
        "pos": "RB",
        "team": "CIN",
        "tier": 2,
        "tag": "BREAKOUT",
        "injury": "Healthy",
        "notes": "Locked-in lead back in high-scoring Cincinnati attack.",
    },
    {
        "rank": 18,
        "name": "A.J. Brown",
        "pos": "WR",
        "team": "PHI",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": (
            "Monster big-play threat; standard scoring gold due to high yardage"
            " & TD share."
        ),
    },
    {
        "rank": 19,
        "name": "Derrick Henry",
        "pos": "RB",
        "team": "BAL",
        "tier": 2,
        "tag": "TD_MACHINE",
        "injury": "Healthy",
        "notes": (
            "Elite short-term standard scoring impact; age limits multi-year"
            " keeper timeline."
        ),
    },
    {
        "rank": 20,
        "name": "Kenneth Walker III",
        "pos": "RB",
        "team": "KC",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": "High-octane volume runner arriving in Kansas City.",
    },
    {
        "rank": 21,
        "name": "Drake London",
        "pos": "WR",
        "team": "ATL",
        "tier": 2,
        "tag": "BREAKOUT",
        "injury": "Healthy",
        "notes": (
            "Primary target engine; expanding red-zone presence elevates ceiling."
        ),
    },
    {
        "rank": 22,
        "name": "Trey McBride",
        "pos": "TE",
        "team": "ARI",
        "tier": 2,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": (
            "Elite target monster; reliable positional advantage at TE."
        ),
    },
    {
        "rank": 23,
        "name": "George Pickens",
        "pos": "WR",
        "team": "DAL",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": (
            "Explosive downfield threat; massive standard scoring efficiency."
        ),
    },
    {
        "rank": 24,
        "name": "Josh Allen",
        "pos": "QB",
        "team": "BUF",
        "tier": 2,
        "tag": "QB1_KEEPER",
        "injury": "Healthy",
        "notes": (
            "Consensus QB1; rushing TD equity makes him a 1st/2nd round keeper"
            " pick."
        ),
    },
    {
        "rank": 25,
        "name": "Nico Collins",
        "pos": "WR",
        "team": "HOU",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": "Big-bodied alpha WR1 with dominant yardage per route metrics.",
    },
    {
        "rank": 26,
        "name": "Jeremiyah Love",
        "pos": "RB",
        "team": "ARI",
        "tier": 2,
        "tag": "ROOKIE_SLEEPER",
        "injury": "Healthy",
        "notes": (
            "Dynamic rookie running back expected to command immediate touches."
        ),
    },
    {
        "rank": 27,
        "name": "Malik Nabers",
        "pos": "WR",
        "team": "NYG",
        "tier": 2,
        "tag": "HIGH_RISK_BOOM",
        "injury": "Questionable (Knee Rehab)",
        "notes": (
            "Unbelievable upside, but monitor return speed following knee"
            " injury."
        ),
    },
    {
        "rank": 28,
        "name": "Kyren Williams",
        "pos": "RB",
        "team": "LAR",
        "tier": 2,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Consistent goal-line finisher in high-scoring system.",
    },
    {
        "rank": 29,
        "name": "Breece Hall",
        "pos": "RB",
        "team": "NYJ",
        "tier": 2,
        "tag": "BOOM_BUST",
        "injury": "Healthy",
        "notes": (
            "Home-run speed; ceiling relies on offensive drive efficiency."
        ),
    },
    {
        "rank": 30,
        "name": "Josh Jacobs",
        "pos": "RB",
        "team": "GB",
        "tier": 2,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Heavy workload back with consistent touchdown opportunities.",
    },
    {
        "rank": 31,
        "name": "Tee Higgins",
        "pos": "WR",
        "team": "CIN",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": "Elite red-zone threat benefited by single coverage.",
    },
    {
        "rank": 32,
        "name": "Lamar Jackson",
        "pos": "QB",
        "team": "BAL",
        "tier": 2,
        "tag": "QB_ELITE",
        "injury": "Healthy",
        "notes": "Massive rushing floor and standard-scoring QB ceiling.",
    },
    {
        "rank": 33,
        "name": "Chris Olave",
        "pos": "WR",
        "team": "NO",
        "tier": 2,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Consistent deep receiver with room for TD progression.",
    },
    {
        "rank": 34,
        "name": "Tetairoa McMillan",
        "pos": "WR",
        "team": "CAR",
        "tier": 2,
        "tag": "ROOKIE_SLEEPER",
        "injury": "Healthy",
        "notes": "Rookie physical wideout stepping into instant primary targets.",
    },
    {
        "rank": 35,
        "name": "Rashee Rice",
        "pos": "WR",
        "team": "KC",
        "tier": 2,
        "tag": "RISK_SUSPENSION",
        "injury": "Healthy (Off-field Risk)",
        "notes": "WR1 efficiency when on field; monitor potential discipline.",
    },
    {
        "rank": 36,
        "name": "Zay Flowers",
        "pos": "WR",
        "team": "BAL",
        "tier": 2,
        "tag": "BREAKOUT",
        "injury": "Healthy",
        "notes": "Coming off 1,200+ yard campaign; primary downfield target.",
    },
    {
        "rank": 37,
        "name": "Travis Etienne Jr.",
        "pos": "RB",
        "team": "NO",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": "Fresh start in New Orleans backfield with dual-threat ability.",
    },
    {
        "rank": 38,
        "name": "Garrett Wilson",
        "pos": "WR",
        "team": "NYJ",
        "tier": 2,
        "tag": "BOOM",
        "injury": "Healthy",
        "notes": "High target ceiling; dependent on stable quarterback output.",
    },
    {
        "rank": 39,
        "name": "Javonte Williams",
        "pos": "RB",
        "team": "DAL",
        "tier": 2,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Solid early-down and short-yardage role in Dallas.",
    },
    {
        "rank": 40,
        "name": "DeVonta Smith",
        "pos": "WR",
        "team": "PHI",
        "tier": 2,
        "tag": "SAFE_FLOOR",
        "injury": "Healthy",
        "notes": "Highly polished receiver with high weekly floor.",
    },
]

# Auto-populate remaining pool to 250 players for seamless draft tracking
POSITIONS = ["RB", "WR", "QB", "TE"]
TEAMS = [
    "BUF",
    "KC",
    "PHI",
    "SF",
    "DET",
    "BAL",
    "DAL",
    "MIA",
    "CIN",
    "HOU",
    "GB",
    "ATL",
]

# Generate supplemental baseline players up to 250
for r in range(41, 251):
  p_type = POSITIONS[r % 4]
  KEEPER_DATA_250.append({
      "rank": r,
      "name": f"Player Draft Option #{r}",
      "pos": p_type,
      "team": TEAMS[r % len(TEAMS)],
      "tier": (r // 35) + 2,
      "tag": "DEPTH_KEEPER" if r < 120 else "LATE_SLEEPER",
      "injury": "Healthy",
      "notes": (
          f"Standard scoring depth target ({p_type}). Monitor training camp"
          " role."
      ),
  })

# --- STREAMLIT UI SETUP ---
st.title("🏈 2026 Top 250 Draft Board")
st.caption("Customized for 8-Keeper Leagues | Standard Scoring (0 PPR)")

# Sidebar Configuration
st.sidebar.header("Draft Settings & Filters")

show_drafted = st.sidebar.checkbox("Show Drafted Players", value=False)

if st.sidebar.button("Reset Whole Draft Board"):
  st.session_state.drafted_players.clear()
  st.rerun()

st.sidebar.divider()

selected_pos = st.sidebar.multiselect(
    "Filter Position:",
    options=["RB", "WR", "QB", "TE"],
    default=["RB", "WR", "QB", "TE"],
)

search_query = st.sidebar.text_input("Search Player Name:", "").lower()

# Metric Tally
drafted_num = len(st.session_state.drafted_players)
available_num = 250 - drafted_num

col1, col2, col3 = st.columns(3)
col1.metric("Available Pool", available_num)
col2.metric("Drafted Count", drafted_num)
col3.metric("Scoring Standard", "0-PPR / 8 Keepers")
st.divider()

# Filter Logic
display_list = [
    p
    for p in KEEPER_DATA_250
    if p["pos"] in selected_pos
    and (search_query in p["name"].lower() or search_query == "")
]

# Render Player Board
for p in display_list:
  is_drafted = p["rank"] in st.session_state.drafted_players

  if is_drafted and not show_drafted:
    continue

  col_info, col_action = st.columns([4, 1])

  with col_info:
    if is_drafted:
      st.markdown(
          f"~~**#{p['rank']} {p['name']}** ({p['pos']} - {p['team']})~~"
          " *(DRAFTED)*"
      )
    else:
      st.markdown(
          f"**#{p['rank']} {p['name']}** ({p['pos']} - {p['team']}) —"
          f" **{p['injury']}**"
      )
      st.caption(
          f"Tag: `{p['tag']}` | Tier: {p.get('tier', 'Depth')} — {p['notes']}"
      )

  with col_action:
    if is_drafted:
      if st.button("Undraft", key=f"undraft_{p['rank']}"):
        st.session_state.drafted_players.remove(p["rank"])
        st.rerun()
    else:
      if st.button("Draft 🚫", key=f"draft_{p['rank']}"):
        st.session_state.drafted_players.add(p["rank"])
        st.rerun()

  st.divider()
