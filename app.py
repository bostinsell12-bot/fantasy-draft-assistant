import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. INITIAL DATA & SESSION STATE SETUP
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Fantasy Draft Board", layout="wide")

INITIAL_DRAFT_BOARD = [
    {"id": 1, "name": "Christian McCaffrey", "pos": "RB", "team": "SF", "tier": 1, "proj": 310.5},
    {"id": 2, "name": "CeeDee Lamb", "pos": "WR", "team": "DAL", "tier": 1, "proj": 295.0},
    {"id": 3, "name": "Tyreek Hill", "pos": "WR", "team": "MIA", "tier": 1, "proj": 290.0},
    {"id": 4, "name": "Breece Hall", "pos": "RB", "team": "NYJ", "tier": 1, "proj": 275.0},
    {"id": 5, "name": "Ja'Marr Chase", "pos": "WR", "team": "CIN", "tier": 1, "proj": 280.0},
    {"id": 6, "name": "Justin Jefferson", "pos": "WR", "team": "MIN", "tier": 1, "proj": 278.0},
    {"id": 7, "name": "Amon-Ra St. Brown", "pos": "WR", "team": "DET", "tier": 1, "proj": 270.0},
    {"id": 8, "name": "Bijan Robinson", "pos": "RB", "team": "ATL", "tier": 1, "proj": 265.0},
    {"id": 9, "name": "Patrick Mahomes", "pos": "QB", "team": "KC", "tier": 2, "proj": 340.0},
    {"id": 10, "name": "Josh Allen", "pos": "QB", "team": "BUF", "tier": 2, "proj": 355.0},
    {"id": 11, "name": "Travis Kelce", "pos": "TE", "team": "KC", "tier": 2, "proj": 220.0},
    {"id": 12, "name": "Sam LaPorta", "pos": "TE", "team": "DET", "tier": 2, "proj": 205.0},
]

# Initialize persistent session state variables
if "available" not in st.session_state:
    st.session_state.available = pd.DataFrame(INITIAL_DRAFT_BOARD)

if "my_team" not in st.session_state:
    st.session_state.my_team = []

if "roster_counts" not in st.session_state:
    st.session_state.roster_counts = {'QB': 0, 'RB': 0, 'WR': 0, 'TE': 0}


# Helper function to remove or draft players
def draft_player(player_id, is_mine=False):
    df = st.session_state.available
    player_row = df[df['id'] == player_id]

    if not player_row.empty:
        player = player_row.iloc[0].to_dict()

        # Remove from available board
        st.session_state.available = df[df['id'] != player_id]

        # Add to team if user pick
        if is_mine:
            st.session_state.my_team.append(player)
            pos = player['pos']
            if pos in st.session_state.roster_counts:
                st.session_state.roster_counts[pos] += 1
            st.toast(f"✅ Drafted {player['name']} ({player['pos']}) to your team!", icon="🎉")
        else:
            st.toast(f"🚫 {player['name']} ({player['pos']}) drafted by rival.", icon="❌")


def reset_draft():
    st.session_state.available = pd.DataFrame(INITIAL_DRAFT_BOARD)
    st.session_state.my_team = []
    st.session_state.roster_counts = {'QB': 0, 'RB': 0, 'WR': 0, 'TE': 0}


# -----------------------------------------------------------------------------
# 2. UI SIDEBAR (Roster Summary & Quick Pick Actions)
# -----------------------------------------------------------------------------
st.sidebar.title("🏈 My Roster Summary")

# Positional counts display
col_qb, col_rb, col_wr, col_te = st.sidebar.columns(4)
col_qb.metric("QB", st.session_state.roster_counts['QB'])
col_rb.metric("RB", st.session_state.roster_counts['RB'])
col_wr.metric("WR", st.session_state.roster_counts['WR'])
col_te.metric("TE", st.session_state.roster_counts['TE'])

st.sidebar.markdown("---")

if st.session_state.my_team:
    st.sidebar.subheader("My Players")
    my_team_df = pd.DataFrame(st.session_state.my_team)
    st.sidebar.dataframe(
        my_team_df[['name', 'pos', 'team', 'proj']],
        use_container_width=True,
        hide_index=True
    )
else:
    st.sidebar.info("No players drafted yet.")

st.sidebar.markdown("---")
if st.sidebar.button("🔄 Reset Board", type="secondary"):
    reset_draft()
    st.rerun()

# -----------------------------------------------------------------------------
# 3. MAIN DASHBOARD DISPLAY
# -----------------------------------------------------------------------------
st.title("⚡ Offline Fantasy Draft Assistant")

# Filters Row
filter_col1, filter_col2 = st.columns([1, 2])
with filter_col1:
    pos_filter = st.selectbox("Filter Position", ["ALL", "QB", "RB", "WR", "TE"])

with filter_col2:
    search_query = st.text_input("🔍 Quick Search Player Name", "")

# Filter dataframe based on controls
df_display = st.session_state.available.copy()

if pos_filter != "ALL":
    df_display = df_display[df_display['pos'] == pos_filter]

if search_query:
    df_display = df_display[df_display['name'].str.contains(search_query, case=False, na=False)]

st.subheader("Available Draft Board")

# Table display with interactive pick buttons
if df_display.empty:
    st.warning("No available players match your filter/search criteria.")
else:
    # Display header
    hdr_col1, hdr_col2, hdr_col3, hdr_col4, hdr_col5, hdr_col6 = st.columns([1, 3, 1, 1, 1, 2])
    hdr_col1.markdown("**ID**")
    hdr_col2.markdown("**Name**")
    hdr_col3.markdown("**Pos**")
    hdr_col4.markdown("**Team**")
    hdr_col5.markdown("**Proj**")
    hdr_col6.markdown("**Draft Actions**")

    st.markdown("---")

    for idx, row in df_display.iterrows():
        p_id = row['id']
        c1, c2, c3, c4, c5, c6 = st.columns([1, 3, 1, 1, 1, 2])

        c1.text(row['id'])
        c2.markdown(f"**{row['name']}**")
        c3.text(row['pos'])
        c4.text(row['team'])
        c5.text(row['proj'])

        # Action Buttons
        btn_col1, btn_col2 = c6.columns(2)
        if btn_col1.button("My Pick", key=f"my_{p_id}", type="primary"):
            draft_player(p_id, is_mine=True)
            st.rerun()

        if btn_col2.button("Rival Pick", key=f"rival_{p_id}"):
            draft_player(p_id, is_mine=False)
            st.rerun()
