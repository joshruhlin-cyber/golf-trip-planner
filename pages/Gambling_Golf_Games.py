import streamlit as st

st.set_page_config(
    page_title="Golf Games Guide",
    page_icon="🏌️",
    layout="centered"
)
st.sidebar.page_link("Golf_Trip_Planner.py", label="⛳ Trip Planner")
st.sidebar.page_link("pages/Gambling_Golf_Games.py", label="🏌️ Gambling Games")

# Same CSS as main app
st.markdown("""
<style>
    .stApp { background-color: #f8faf8; }
    .hero {
        background: linear-gradient(135deg, #1a5c2a 0%, #2d8a47 50%, #1a5c2a 100%);
        padding: 40px 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        color: white;
    }
    .hero h1 { font-size: 2.4em; font-weight: 800; margin: 0; color: white; }
    .hero p { font-size: 1.1em; opacity: 0.9; margin-top: 10px; color: white; }
    .section-header {
        background: linear-gradient(90deg, #1a5c2a, #2d8a47);
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        font-size: 1.1em;
        font-weight: 700;
        margin: 25px 0 15px 0;
    }
    .card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        border-left: 5px solid #2d8a47;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .card h3 { margin: 0 0 10px 0; color: #1a5c2a; font-size: 1.1em; }
    .card p { margin: 4px 0; color: #444; font-size: 0.95em; }
    .badge {
        display: inline-block;
        background: #e8f5e9;
        color: #1a5c2a;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.8em;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebarNav"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🏌️ Golf Games Guide</h1>
    <p>Popular betting games and formats for your round — sorted by group size.</p>
</div>
""", unsafe_allow_html=True)

games = {
    "2 Players": [
        {
            "name": "Match Play",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "The simplest head-to-head format. Each hole is its own contest — win the hole, win a point. The player who wins the most holes wins the match. Ties on a hole are called 'halved.' Great with or without handicaps.",
            "how": "Set a bet per hole or a flat match bet. Win a hole = 1 up. Whoever is ahead at the end wins. If tied after 18, it's a draw."
        },
        {
            "name": "Nassau",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "Three bets in one — front nine, back nine, and total round. Most popular golf betting game in the world. Clean, simple, and endlessly replayable.",
            "how": "Set a dollar amount (e.g. $5 Nassau = $5 front, $5 back, $5 overall). Lowest score wins each segment. Either player can 'press' when down 2 holes, starting a new side bet for remaining holes."
        },
        {
            "name": "Stroke Play",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "Total strokes for the round. Lowest score wins. Simple and straightforward — great for a flat bet on the whole round.",
            "how": "Play your round, count every stroke. Lowest total wins. Use handicaps to even the playing field."
        },
        {
            "name": "Hammer",
            "complexity": "Medium",
            "betting": "Yes",
            "desc": "A high-stakes game where either player can 'hammer' at any point to double the bet. The other player must accept or concede the hole.",
            "how": "Set a starting bet per hole. At any point before holing out, either player can call 'Hammer!' The opponent either accepts (bet doubles) or concedes the hole. Hammers can keep doubling."
        },
    ],
    "3 Players": [
        {
            "name": "Nines (Nine Point Game)",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "Each hole has 9 points to distribute. The best score gets 5, second gets 3, third gets 1. Ties split the points. Perfect for threesomes.",
            "how": "Points per hole: 5-3-1 (clear winner). 4-4-1 (two tied for best). 5-2-2 (one wins, two tied for second). 3-3-3 (all tie). Tally points after 18. Highest total wins the pot."
        },
        {
            "name": "Rabbit",
            "complexity": "Medium",
            "betting": "Yes",
            "desc": "Win a hole outright and you 'catch the rabbit.' Hold onto it as long as you can — but if someone else wins a hole outright, the rabbit runs free and they grab it.",
            "how": "The rabbit is won by the sole low scorer on a hole. If the rabbit holder ties, it stays. If another player wins outright, the rabbit transfers. The player holding the rabbit at the turn and at the end of the round wins."
        },
        {
            "name": "Bingo Bango Bongo",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "Three points up for grabs on every hole regardless of score. Great for mixed skill groups since it rewards different aspects of the game.",
            "how": "Bingo = first ball on the green. Bango = closest to the pin once all are on the green. Bongo = first ball in the hole. One point each. Tally at the end — most points wins."
        },
        {
            "name": "Wolf",
            "complexity": "Medium",
            "betting": "Yes",
            "desc": "One player is the Wolf each hole and gets to choose a partner after watching each tee shot — or go it alone for double points. Rotates each hole.",
            "how": "Rotate the Wolf role each hole. After each tee shot, the Wolf decides to partner with that player or pass. After all shots, the Wolf either has a partner (2v1) or goes Lone Wolf (1v2, worth double). Low team score wins the hole."
        },
    ],
    "4 Players": [
        {
            "name": "Skins",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "Each hole is worth a skin. Win a hole outright and you take the skin. If two or more players tie, the skin carries over to the next hole — making it worth more. Carryovers build massive pressure on the back nine.",
            "how": "Set a dollar value per skin (e.g. $2). Win a hole with the low score = collect the skin. Any tie = skin carries to next hole. Count up skins at the end and pay out."
        },
        {
            "name": "Nassau",
            "complexity": "Easy",
            "betting": "Yes",
            "desc": "Works great with 4 players in two teams. Three bets — front nine, back nine, and overall. Most popular golf betting format in America.",
            "how": "Split into two teams of two. Set a bet per segment (e.g. $5 Nassau). Low team score wins each nine and the overall. Either team can press when down 2 — starting a new side bet for remaining holes."
        },
        {
            "name": "Wolf (4 Players)",
            "complexity": "Medium",
            "betting": "Yes",
            "desc": "Same as 3-player Wolf but even better with four. The Wolf picks a partner after each tee shot or goes Lone Wolf against the field for double stakes.",
            "how": "Rotate Wolf each hole (every 4 holes each player is Wolf 4-5 times in 18). Wolf picks a partner after watching each tee shot in order. Lone Wolf beats the other 3 = double payout. Low team score wins."
        },
        {
            "name": "Vegas",
            "complexity": "Medium",
            "betting": "Yes",
            "desc": "Teams of two combine their scores into a two-digit number — lowest score goes first. Lowest team number wins the hole. A birdie flips the opponent's score, which can swing the hole dramatically.",
            "how": "Teams of 2. Each hole, combine scores lowest-first (e.g. 3 and 5 = 35). Opponent team does same. Lowest number wins the difference in points. If one team birdies, the opponent's digits flip (35 becomes 53)."
        },
        {
            "name": "Stableford",
            "complexity": "Easy",
            "betting": "No",
            "desc": "Points-based format where you score relative to par. Encourages aggressive play since bad holes only cost 0 points instead of blowing up your scorecard.",
            "how": "Double bogey or worse = 0 pts. Bogey = 1 pt. Par = 2 pts. Birdie = 3 pts. Eagle = 4 pts. Most points at the end wins. Great for mixed handicap groups."
        },
        {
            "name": "Scramble",
            "complexity": "Easy",
            "betting": "No",
            "desc": "Everyone tees off, pick the best shot, everyone plays from there. Repeat until holed. The most fun format for casual groups and corporate outings.",
            "how": "All 4 players hit. Team picks the best shot. Everyone plays their next shot from that spot. Repeat until in the hole. Record one team score per hole."
        },
    ]
}

for group_size, game_list in games.items():
    st.markdown(f'<div class="section-header">👥 {group_size}</div>', unsafe_allow_html=True)
    for game in game_list:
        with st.expander(f"🏌️ {game['name']}"):
            st.markdown(f"""
            <div style="margin-bottom: 10px;">
                <span class="badge">⚡ {game['complexity']}</span>
                <span class="badge">💰 Betting: {game['betting']}</span>
            </div>
            <p><strong>Overview:</strong> {game['desc']}</p>
            <p><strong>How to Play:</strong> {game['how']}</p>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p style="text-align:center; color:#888; font-size:0.85em;">🏌️ Golf Games Guide — part of the Golf Trip Planner</p>', unsafe_allow_html=True)