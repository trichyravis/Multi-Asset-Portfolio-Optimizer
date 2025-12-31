"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - COMPONENTS
Reusable professional components for Portfolio Optimizer
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
from config import COLORS, TYPOGRAPHY


# ═══════════════════════════════════════════════════════════════════════════════
# METRIC DISPLAY COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class MetricsDisplay:
    """Display key metrics in a professional grid"""
    
    @staticmethod
    def render_metrics(metrics: list, columns: int = 4):
        """
        Render metrics in a grid
        
        Args:
            metrics: List of metric dicts with keys: title, value, emoji, description (optional)
            columns: Number of columns
        """
        cols = st.columns(columns)
        
        for idx, metric in enumerate(metrics):
            with cols[idx % columns]:
                st.markdown(f"""
                <div class="metric-card">
                    <div style="font-size: 24px; margin-bottom: 8px;">{metric.get('emoji', '📊')}</div>
                    <div class="metric-label">{metric['title']}</div>
                    <div class="metric-value">{metric['value']}</div>
                    {'<div style="color: #ADD8E6; font-size: 11px; margin-top: 4px;">' + metric.get('description', '') + '</div>' if metric.get('description') else ''}
                </div>
                """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class Section:
    """Display a professional section with title"""
    
    @staticmethod
    def render(title: str, emoji: str = "📊"):
        """
        Render a section title
        
        Args:
            title: Section title
            emoji: Optional emoji prefix
        """
        st.markdown(f"### {emoji} {title}")
        st.markdown("---")


# ═══════════════════════════════════════════════════════════════════════════════
# COMPARISON TABLE COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class ComparisonTable:
    """Display comparison data in professional format"""
    
    @staticmethod
    def render(df, title: str = None):
        """
        Render comparison table
        
        Args:
            df: Pandas DataFrame
            title: Optional table title
        """
        if title:
            st.markdown(f"**{title}**")
        
        st.dataframe(
            df,
            use_container_width=True,
            height=300
        )


# ═══════════════════════════════════════════════════════════════════════════════
# TABS COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class TabsDisplay:
    """Display content in tabs"""
    
    @staticmethod
    def render(tabs_dict: dict):
        """
        Render tabs
        
        Args:
            tabs_dict: Dictionary with tab names as keys and content/functions as values
        """
        tab_list = st.tabs(list(tabs_dict.keys()))
        
        for tab, (tab_name, content) in zip(tab_list, tabs_dict.items()):
            with tab:
                if callable(content):
                    content()
                else:
                    st.write(content)


# ═══════════════════════════════════════════════════════════════════════════════
# INFO BOX COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class InfoBox:
    """Display information boxes"""
    
    @staticmethod
    def success(message: str):
        """Display success message"""
        st.markdown(f"""
        <div class="success-box">
            ✅ {message}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def warning(message: str):
        """Display warning message"""
        st.markdown(f"""
        <div class="warning-box">
            ⚠️ {message}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def error(message: str):
        """Display error message"""
        st.markdown(f"""
        <div class="error-box">
            ❌ {message}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def info(message: str):
        """Display info message"""
        st.markdown(f"""
        <div class="info-box">
            ℹ️ {message}
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# BUTTON COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class PrimaryButton:
    """Render primary action buttons"""
    
    @staticmethod
    def render(label: str, key: str = None, help_text: str = None) -> bool:
        """
        Render primary button
        
        Args:
            label: Button label
            key: Streamlit key
            help_text: Hover help text
            
        Returns:
            Button click state
        """
        return st.button(
            label=label,
            key=key,
            help=help_text,
            use_container_width=True,
            type="primary"
        )


# ═══════════════════════════════════════════════════════════════════════════════
# CARD COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class Card:
    """Display professional cards"""
    
    @staticmethod
    def render(title: str, content: str, emoji: str = "📊", columns: int = None):
        """
        Render a card
        
        Args:
            title: Card title
            content: Card content
            emoji: Optional emoji
            columns: Number of columns (if using st.columns)
        """
        st.markdown(f"""
        <div class="section-container">
            <h3 style="margin-top: 0; color: #003366;">
                <span style="font-size: 20px; margin-right: 10px;">{emoji}</span>
                {title}
            </h3>
            <p style="color: #666666; line-height: 1.6;">{content}</p>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# STATS DISPLAY COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class StatsDisplay:
    """Display statistics in a professional format"""
    
    @staticmethod
    def render_stat(label: str, value: str, change: str = None, is_positive: bool = True):
        """
        Render individual statistic
        
        Args:
            label: Stat label
            value: Stat value
            change: Optional change indicator (e.g., "+12%")
            is_positive: If True, change is green; if False, change is red
        """
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div style="color: #003366; font-weight: bold;">{label}</div>
            <div style="font-size: 24px; color: #FFD700; font-weight: bold;">{value}</div>
            """, unsafe_allow_html=True)
        
        if change:
            with col2:
                change_color = "#2ecc71" if is_positive else "#e74c3c"
                st.markdown(f"""
                <div style="color: {change_color}; font-weight: bold; font-size: 16px; text-align: right;">
                    {change}
                </div>
                """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# DIVIDER COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class Divider:
    """Display professional dividers"""
    
    @staticmethod
    def render_gold():
        """Render gold divider"""
        st.markdown("""
        <hr style="border: none; border-top: 2px solid #FFD700; margin: 20px 0;">
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_default():
        """Render default divider"""
        st.markdown("---")


# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

class SidebarSection:
    """Render sidebar sections"""
    
    @staticmethod
    def render_header(title: str, emoji: str = "📋"):
        """
        Render sidebar header
        
        Args:
            title: Header text
            emoji: Optional emoji
        """
        st.sidebar.markdown(f"""
        <div style="color: #FFD700; font-weight: bold; margin-top: 20px; margin-bottom: 10px;">
            {emoji} {title}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_info(text: str):
        """
        Render sidebar info text
        
        Args:
            text: Info text (supports markdown)
        """
        st.sidebar.markdown(f"""
        <div style="color: #ADD8E6; font-size: 12px; line-height: 1.4;">
            {text}
        </div>
        """, unsafe_allow_html=True)
