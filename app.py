
import streamlit as st
from config_enhanced import ASSET_CLASSES, ASSET_STATS, PAGE_CONFIG
from styles_enhanced import apply_main_styles, render_header, render_footer

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)
apply_main_styles()

# ═══════════════════════════════════════════════════════════════════════════════
# CUSTOM SIDEBAR STYLING
# ═══════════════════════════════════════════════════════════════════════════════

sidebar_css = """
<style>
    /* Sidebar background - dark blue gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #003366 0%, #004d80 100%);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #003366 0%, #004d80 100%);
    }
    
    /* All text in sidebar - white */
    [data-testid="stSidebar"] {
        color: white !important;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Navigation links - white text */
    [data-testid="stSidebar"] a {
        color: #FFD700 !important;
    }
    
    /* Profile section */
    .sidebar-profile {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #FFD700;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
    }
    
    .profile-name {
        font-size: 16px;
        font-weight: bold;
        color: #FFD700;
        margin-bottom: 10px;
    }
    
    .profile-text {
        font-size: 12px;
        color: white;
        margin: 5px 0;
        line-height: 1.4;
    }
    
    .linkedin-button {
        display: inline-block;
        background: #0A66C2;
        color: white !important;
        padding: 10px 15px;
        border-radius: 5px;
        text-align: center;
        margin-top: 12px;
        font-weight: bold;
        text-decoration: none !important;
        border: none;
        cursor: pointer;
        width: 100%;
        box-sizing: border-box;
        transition: background 0.3s;
    }
    
    .linkedin-button:hover {
        background: #004182 !important;
        text-decoration: none !important;
    }
    
    .sidebar-divider {
        border-top: 1px solid #FFD700;
        margin: 15px 0;
        opacity: 0.5;
    }
    
    .sidebar-footer {
        border-top: 1px solid #FFD700;
        padding-top: 15px;
        margin-top: 30px;
        text-align: center;
        font-size: 11px;
        color: #FFD700;
    }
    
    /* Sidebar expanders */
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        background: rgba(255, 215, 0, 0.1);
        color: white;
    }
    
    /* Sidebar buttons */
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid #FFD700;
        width: 100%;
        margin: 5px 0;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: #FFD700;
        color: #003366;
    }
</style>
"""

st.markdown(sidebar_css, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CUSTOM SIDEBAR CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div class="sidebar-profile">
        <div class="profile-name">👤 Prof. V. Ravichandran</div>
        <div class="profile-text">28+ Years Corporate Finance & Banking Experience</div>
        <div class="profile-text">10+ Years Academic Excellence</div>
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank" class="linkedin-button">
            🔗 LinkedIn Profile
        </a>
    </div>
    
    <div class="sidebar-divider"></div>
    
    <div style="text-align: center; margin: 20px 0; color: #FFD700; font-weight: bold;">
        📊 Portfolio Optimizer
    </div>
    <div style="text-align: center; font-size: 12px; color: white; margin-bottom: 20px;">
        Advanced optimization using Modern Portfolio Theory (MPT)
    </div>
    
    <div class="sidebar-divider"></div>
    
    <div class="sidebar-footer">
        🏔️ The Mountain Path<br>
        World of Finance
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE HEADER
# ═══════════════════════════════════════════════════════════════════════════════

render_header()

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════

if "selected_classes" not in st.session_state:
    st.session_state.selected_classes = []
if "selected_assets" not in st.session_state:
    st.session_state.selected_assets = {}

# ═══════════════════════════════════════════════════════════════════════════════
# TITLE
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #003366; font-size: 2.5rem; border: none;'>🏠 Portfolio Optimization</h1>
        <p style='color: #003366; font-size: 1.1rem;'>The Mountain Path - World of Finance</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# WELCOME SECTION
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h2 style='color: #FFD700; margin-top: 0;'>📚 Welcome to Professional Portfolio Optimization</h2>
        <p style='color: white; font-size: 1.05rem;'>This tool helps you build a diversified investment portfolio using Modern Portfolio Theory (MPT).</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; height: 100%;'>
            <h4 style='color: #FFD700; margin-top: 0;'>✨ What We Do:</h4>
            <ul style='color: white;'>
                <li>📊 Analyze your portfolio composition</li>
                <li>🎯 Optimize asset allocation</li>
                <li>📈 Visualize efficient frontiers</li>
                <li>💡 Recommend optimal weights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; height: 100%;'>
            <h4 style='color: #FFD700; margin-top: 0;'>🎯 6-Step Process:</h4>
            <ol style='color: white;'>
                <li><strong>Select Asset Classes</strong></li>
                <li><strong>Select Specific Assets</strong></li>
                <li><strong>Allocate Weights</strong></li>
                <li><strong>View Analysis</strong></li>
                <li><strong>Choose Objective</strong></li>
                <li><strong>Optimize & Results</strong></li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

st.markdown("")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: SELECT ASSET CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
    <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h3 style='color: #FFD700; margin-top: 0;'>🎯 STEP 1: SELECT ASSET CLASSES</h3>
        <p style='color: white;'>Choose one or more asset classes for your portfolio:</p>
    </div>
    """, unsafe_allow_html=True)

class_cols = st.columns(2)

for idx, (class_name, class_data) in enumerate(ASSET_CLASSES.items()):
    col = class_cols[idx % 2]
    with col:
        is_selected = st.checkbox(
            f"{class_data['emoji']} {class_name}",
            value=class_name in st.session_state.selected_classes,
            key=f"class_{class_name}"
        )
        
        if is_selected:
            if class_name not in st.session_state.selected_classes:
                st.session_state.selected_classes.append(class_name)
        else:
            if class_name in st.session_state.selected_classes:
                st.session_state.selected_classes.remove(class_name)
        
        st.markdown(f"""
            <div style='background-color: #004d80; padding: 0.75rem; border-radius: 0.25rem; color: white; margin-left: 1.5rem;'>
            <strong>{class_data['description']}</strong><br>
            <small>Risk: {class_data['risk']} | Return: {class_data['return']}</small>
            </div>
            """, unsafe_allow_html=True)

selected_count = len(st.session_state.selected_classes)
if selected_count > 0:
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 0.75rem; border-radius: 0.25rem; margin-top: 1rem; margin-bottom: 2rem;'>
            <p style='color: #FFD700; margin: 0;'>✅ Selected {selected_count} asset class(es)</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div style='background-color: #004d80; padding: 0.75rem; border-radius: 0.25rem; margin-top: 1rem; margin-bottom: 2rem;'>
            <p style='color: #FFD700; margin: 0;'>⚠️ Select at least 1 asset class to continue</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("")

# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: SELECT SPECIFIC ASSETS
# ═══════════════════════════════════════════════════════════════════════════════

if selected_count > 0:
    st.markdown("""
        <div style='background-color: #003366; padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🎯 STEP 2: SELECT SPECIFIC ASSETS</h3>
            <p style='color: white;'>Choose specific investments from each asset class:</p>
        </div>
        """, unsafe_allow_html=True)
    
    for class_name in st.session_state.selected_classes:
        class_data = ASSET_CLASSES[class_name]
        
        with st.expander(f"{class_data['emoji']} {class_name} (Individual assets)", expanded=True):
            # Get assets for this class
            class_assets = {k: v for k, v in ASSET_STATS.items() if v.get('class') == class_name}
            
            cols = st.columns(2)
            
            for idx, (asset_name, asset_data) in enumerate(class_assets.items()):
                col = cols[idx % 2]
                with col:
                    is_selected = st.checkbox(
                        f"{asset_data.get('emoji', '📊')} {asset_name}",
                        value=asset_name in st.session_state.selected_assets,
                        key=f"asset_{asset_name}"
                    )
                    
                    if is_selected:
                        st.session_state.selected_assets[asset_name] = True
                    else:
                        st.session_state.selected_assets.pop(asset_name, None)
    
    total_assets = len(st.session_state.selected_assets)
    if total_assets > 0:
        st.markdown(f"""
            <div style='background-color: #004d80; padding: 0.75rem; border-radius: 0.25rem; margin-top: 1.5rem; margin-bottom: 2rem;'>
                <p style='color: #FFD700; margin: 0;'>✅ Selected {total_assets} total asset(s)</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style='background-color: #004d80; padding: 0.75rem; border-radius: 0.25rem; margin-top: 1.5rem; margin-bottom: 2rem;'>
                <p style='color: #FFD700; margin: 0;'>⚠️ Select at least 1 asset to continue</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # NAVIGATION
    # ═══════════════════════════════════════════════════════════════════════════════
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if total_assets > 0:
            st.markdown("""
                <div style='text-align: center; margin-bottom: 1rem;'>
                <p style='color: #003366; font-size: 0.95rem;'>✅ Ready to continue!</p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("➡️ NEXT: Allocate Weights", width='stretch', type="primary"):
                st.switch_page("pages/2_⚖️_Weights.py")
        else:
            st.button("➡️ NEXT: Allocate Weights", width='stretch', disabled=True)

else:
    st.markdown("""
        <div style='background-color: #003366; padding: 2rem; border-radius: 0.5rem; text-align: center;'>
            <p style='color: white; font-size: 1.1rem;'>👇 Start by selecting an asset class above</p>
        </div>
        """, unsafe_allow_html=True)

render_footer()
