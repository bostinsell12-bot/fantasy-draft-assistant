import streamlit as st

# Embedded rankings dataset
FANTASY_DATA = {
    "last_updated": "2026-08-18",
    "scoring_format": "Standard / Non-PPR & Half-PPR compatible",
    "rankings": [
        {
            "rank": 1,
            "name": "Ja'Marr Chase",
            "position": "WR",
            "team": "CIN",
            "tier": 1,
            "tag": "ELITE_ANCHOR",
            "proj_points": 16.8,
            "notes": (
                "Consensus WR1 overall with massive target and touchdown"
                " ceiling."
            ),
        },
        {
            "rank": 2,
            "name": "Breece Hall",
            "position": "RB",
            "team": "NYJ",
            "tier": 1,
            "tag": "ELITE_ANCHOR",
            "proj_points": 15.5,
            "notes": (
                "Workhorse back with high explosive run and pass-catching"
                " volume."
            ),
        },
        {
            "rank": 3,
            "name": "Jaxon Smith-Njigba",
            "position": "WR",
            "team": "SEA",
            "tier": 1,
            "tag": "ELITE_ANCHOR",
            "proj_points": 14.9,
            "notes": "Alpha WR coming off a 100+ reception breakout season.",
        },
        {
            "rank": 4,
            "name": "Puka Nacua",
            "position": "WR",
            "team": "LAR",
            "tier": 1,
            "tag": "ELITE_ANCHOR",
            "proj_points": 14.7,
            "notes": "Dominant target share and route efficiency.",
        },
        {
            "rank": 5,
            "name": "Bijan Robinson",
            "position": "RB",
            "team": "ATL",
            "tier": 1,
            "tag": "ELITE_ANCHOR",
            "proj_points": 14.2,
            "notes": "Three-down workhorse back in a run-heavy scheme.",
        },
        {
            "rank": 6,
            "name": "Christian McCaffrey",
            "position": "RB",
            "team": "SF",
            "tier": 2,
            "tag": "BOOM",
            "proj_points": 15.1,
            "notes": "Overall RB1 upside with touchdown dependency advantages.",
        },
        {
            "rank": 7,
            "name": "Saquon Barkley",
            "position": "RB",
            "team": "PHI",
            "tier": 2,
            "tag": "SAFE_FLOOR",
            "proj_points": 13.8,
            "notes": "Goal-line priority behind an elite offensive line.",
        },
        {
            "rank": 8,
            "name": "Justin Jefferson",
            "position": "WR",
            "team": "MIN",
            "tier": 2,
            "tag": "BOOM",
            "proj_points": 13.5,
            "notes": "High rebound potential with quarterback stability.",
        },
        {
            "rank": 9,
            "name": "Amon-Ra St. Brown",
            "position": "WR",
            "team": "DET",
            "tier": 2,
            "tag": "SAFE_FLOOR",
            "proj_points": 13.2,
            "notes": "Consistent 8-10 target weekly floor.",
        },
        {
            "rank": 10,
            "name": "De'Von Achane",
            "position": "RB",
            "team": "MIA",
            "tier": 2,
            "tag": "BOOM",
            "proj_points": 13.0,
            "notes": "Unmatched speed and per-touch efficiency.",
        },
        {
            "rank": 11,
            "name": "Jonathan Taylor",
            "position": "RB",
            "team": "IND",
            "tier": 2,
            "tag": "SAFE_FLOOR",
            "proj_points": 12.8,
            "notes": "Pure early-down and red-zone workhorse.",
        },
        {
            "rank": 12,
            "name": "Brock Bowers",
            "position": "TE",
            "team": "LV",
            "tier": 2,
            "tag": "POSITIONAL_ADVANTAGE",
            "proj_points": 11.4,
            "notes": (
                "Clear TE1 overall with wide-receiver-level target share."
            ),
        },
        {
            "rank": 13,
            "name": "Josh Allen",
            "position": "QB",
            "team": "BUF",
            "tier": 3,
            "tag": "ELITE_QB",
            "proj_points": 22.5,
            "notes": (
                "Consensus elite fantasy QB with heavy rushing TD upside."
            ),
        },
        {
            "rank": 14,
            "name": "Lamar Jackson",
            "position": "QB",
            "team": "BAL",
            "tier": 3,
            "tag": "ELITE_QB",
            "proj_points": 21.8,
            "notes": "High floor with massive rushing and passing ceiling.",
        },
        {
            "rank": 15,
            "name": "Chase Brown",
            "position": "RB",
            "team": "CIN",
            "tier": 3,
            "tag": "BREAKOUT",
            "proj_points": 11.8,
            "notes": "Leading backfield duties in an explosive offense.",
        },
        {
            "rank": 16,
            "name": "James Cook",
            "position": "RB",
            "team": "BUF",
            "tier": 3,
            "tag": "SAFE_FLOOR",
            "proj_points": 11.2,
            "notes": "High efficiency and guaranteed touch share.",
        },
        {
            "rank": 17,
            "name": "Zay Flowers",
            "position": "WR",
            "team": "BAL",
            "tier": 3,
            "tag": "SLEEPER",
            "proj_points": 9.3,
            "notes": (
                "Coming off 1,200+ yard season with expanding TD ceiling."
            ),
        },
        {
            "rank": 18,
            "name": "Drake London",
            "position": "WR",
            "team": "ATL",
            "tier": 3,
            "tag": "BOOM",
            "proj_points": 11.0,
            "notes": "Top-5 ceiling if pass volume increases.",
        },
        {
            "rank": 19,
            "name": "Malik Nabers",
            "position": "WR",
            "team": "NYG",
            "tier": 3,
            "tag": "POTENTIAL_BUST",
            "proj_points": 10.5,
            "notes": (
                "Returning from knee injury with surrounding team volatility."
            ),
        },
        {
            "rank": 20,
            "name": "Rashee Rice",
            "position": "WR",
            "team": "KC",
            "tier": 3,
            "tag": "POTENTIAL_BUST",
            "proj_points": 10.2,
            "notes": (
                "Knee recovery and potential availability risk early in season."
            ),
        },
        {
            "rank": 21,
            "name": "Emeka Egbuka",
            "position": "WR",
            "team": "TB",
            "tier": 4,
            "tag": "SLEEPER",
            "proj_points": 9.8,
            "notes": "Elite route runner; strong value draft target.",
        },
        {
            "rank": 22,
            "name": "Ashton Jeanty",
            "position": "RB",
            "team": "DAL",
            "tier": 4,
            "tag": "BOOM",
            "proj_points": 10.4,
            "notes": "Rookie with direct line to lead early-down work.",
        },
        {
            "rank": 23,
            "name": "Cam Skattebo",
            "position": "RB",
            "team": "NYG",
            "tier": 4,
            "tag": "SLEEPER",
            "proj_points": 11.1,
            "notes": "Averaged 19.1 PPG when healthy as a rookie.",
        },
        {
            "rank": 24,
            "name": "Brian Thomas Jr.",
            "position": "WR",
            "team": "JAC",
            "tier": 4,
            "tag": "POTENTIAL_BUST",
            "proj_points": 9.2,
            "notes": "High target volatility and historical draft-cost drop.",
        },
        {
            "rank": 25,
            "name": "Bhayshul Tuten",
            "position": "RB",
            "team": "JAC",
            "tier": 4,
            "tag": "SLEEPER",
            "proj_points": 10.5,
            "notes": (
                "Stepping into vacant lead backfield role with high TD upside."
            ),
        },
    ],
}

# Streamlit App UI
st.title("Top 25 Fantasy Football Rankings")
st.caption(f"Last Updated: {FANTASY_DATA['last_updated']}")

# Filter by Tag
tag_filter = st.multiselect(
    "Filter by Tag:",
    options=[
        "ELITE_ANCHOR",
        "BOOM",
        "SAFE_FLOOR",
        "SLEEPER",
        "POTENTIAL_BUST",
        "BREAKOUT",
        "ELITE_QB",
        "POSITIONAL_ADVANTAGE",
    ],
    default=[],
)

# Display Rankings
for player in FANTASY_DATA["rankings"]:
  if not tag_filter or player["tag"] in tag_filter:
    st.subheader(
        f"{player['rank']}. {player['name']} ({player['position']} -"
        f" {player['team']})"
    )
    st.write(
        f"**Tier:** {player['tier']} | **Projected PPG:**"
        f" {player['proj_points']} | **Tag:** `{player['tag']}`"
    )
    st.info(player["notes"])
    st.divider()
