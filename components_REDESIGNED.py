"""
═══════════════════════════════════════════════════════════════════════════════
🏔️ THE MOUNTAIN PATH - PROFESSIONAL COMPONENTS
Reusable UI components for portfolio optimizer
═══════════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
from config_REDESIGNED import COLORS, HERO_HEADER, METRIC_CARD


class HeroHeader:
    """Professional hero header with branding."""
    
    @staticmethod
    def render(title: str, subtitle: str, description: str, emoji: str = "🏔️"):
        """Render hero header."""
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, {COLORS["primary_dark"]} 0%, {COLORS["primary_light"]} 50%, {COLORS["primary_dark"]} 100%);
            padding: {HERO_HEADER["padding"]};
            border-radius: {HERO_HEADER["border_radius"]};
            border: {HERO_HEADER["border_width"]} solid {HERO_HEADER["border_color"]};
            box-shadow: {HERO_HEADER["box_shadow"]};
            text-align: center;
            margin-bottom: 2rem;
        '>
            <div style='font-size: {HERO_HEADER["emoji_size"]}; margin-bottom: 1rem;'>{emoji}</div>
            <h1 style='
                color: {HERO_HEADER["title_color"]};
                font-size: {HERO_HEADER["title_font_size"]};
                font-weight: {HERO_HEADER["title_font_weight"]};
                letter-spacing: {HERO_HEADER["title_letter_spacing"]};
                margin: 0;
            '>{title}</h1>
            <h3 style='
                color: {HERO_HEADER["subtitle_color"]};
                font-size: {HERO_HEADER["subtitle_font_size"]};
                font-weight: {HERO_HEADER["subtitle_font_weight"]};
                margin: 0.5rem 0;
            '>{subtitle}</h3>
            <p style='
                color: {HERO_HEADER["description_color"]};
                font-size: {HERO_HEADER["description_font_size"]};
                margin: 0.5rem 0 0 0;
            '>{description}</p>
        </div>
        """, unsafe_allow_html=True)


class SidebarSection:
    """Professional sidebar section."""
    
    @staticmethod
    def render_header(emoji: str, title: str, step_number: int = None):
        """Render sidebar section header."""
        if step_number:
            st.markdown(f"""
            <div style='
                color: {COLORS["accent_gold"]};
                font-size: 18px;
                font-weight: 700;
                margin: 1.5rem 0 0.5rem 0;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            '>
                {emoji} <span style="color: {COLORS['text_white']};">Step {step_number}: {title}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='
                color: {COLORS["accent_gold"]};
                font-size: 16px;
                font-weight: 700;
                margin: 1.5rem 0 0.5rem 0;
            '>{emoji} {title}</div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def render_description(text: str):
        """Render sidebar description text."""
        st.caption(f"💡 {text}")


class WeightAllocationDisplay:
    """Professional weight allocation display with sliders."""
    
    @staticmethod
    def render(tickers: list, default_weights: dict = None):
        """
        Render weight allocation interface.
        
        Args:
            tickers: List of asset tickers
            default_weights: Dict of default weights
            
        Returns:
            Dict of allocated weights
        """
        if default_weights is None:
            default_weights = {ticker: 100/len(tickers) for ticker in tickers}
        
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, rgba(0, 51, 102, 0.5) 0%, rgba(0, 77, 128, 0.5) 100%);
            padding: 1.5rem;
            border-radius: 15px;
            border: 2px solid {COLORS["accent_gold"]};
            margin: 1rem 0;
        '>
            <h3 style='color: {COLORS["text_white"]}; margin-top: 0;'>
                ⚖️ Manual Weight Allocation
            </h3>
            <p style='color: {COLORS["text_white"]}; margin-bottom: 1rem;'>
                Total Assets: <strong>{len(tickers)}</strong> | 
                Default: <strong>Equal Weights ({100/len(tickers):.1f}% each)</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Sliders
        col1, col2 = st.columns([2, 1])
        
        weights = {}
        with col1:
            st.write(f"<p style='color: {COLORS['text_white']}; font-weight: 700;'>Weight Sliders:</p>", 
                    unsafe_allow_html=True)
            for ticker in tickers:
                weight = st.slider(
                    f"Weight - {ticker}:",
                    min_value=0.0,
                    max_value=100.0,
                    value=default_weights.get(ticker, 100/len(tickers)),
                    step=0.1,
                    key=f"weight_{ticker}",
                )
                weights[ticker] = weight
        
        with col2:
            st.write(f"<p style='color: {COLORS['text_white']}; font-weight: 700;'>Summary:</p>", 
                    unsafe_allow_html=True)
            total_weight = sum(weights.values())
            
            # Color based on validity
            if abs(total_weight - 100.0) < 0.01:
                status_color = "#2ecc71"
                status_text = "✅ VALID"
            else:
                status_color = "#e74c3c"
                status_text = "❌ INVALID"
            
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, #003d70 0%, #005a9d 100%);
                padding: 1rem;
                border-radius: 10px;
                border: 2px solid {status_color};
                text-align: center;
            '>
                <p style='color: {COLORS["text_white"]}; font-size: 12px; margin: 0.25rem 0;'>
                    Total Weight
                </p>
                <p style='color: {status_color}; font-size: 24px; font-weight: 700; margin: 0.25rem 0;'>
                    {total_weight:.1f}%
                </p>
                <p style='color: {COLORS["text_white"]}; font-size: 12px; margin: 0.25rem 0;'>
                    {status_text}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Reset button
        if st.button("🔄 Reset to Equal Weights", use_container_width=True):
            st.rerun()
        
        # Validate
        total_weight = sum(weights.values())
        if abs(total_weight - 100.0) > 0.01:
            st.error(f"❌ Portfolio weights must sum to 100%. Current: {total_weight:.1f}%")
            return None
        
        # Convert to normalized weights
        return {ticker: weights[ticker] / 100.0 for ticker in tickers}


class MetricsDisplay:
    """Professional metrics display cards."""
    
    @staticmethod
    def render_metric_card(title: str, value: str, emoji: str, description: str = None, highlight: bool = False):
        """Render single metric card."""
        border_color = COLORS["accent_gold"] if highlight else "#444"
        
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, #003d70 0%, #005a9d 100%);
            padding: 1.5rem;
            border-radius: 15px;
            border: 2px solid {border_color};
            box-shadow: 0 4px 15px rgba(0, 51, 102, 0.2);
            text-align: center;
        '>
            <div style='font-size: 28px; margin-bottom: 0.5rem;'>{emoji}</div>
            <p style='color: {COLORS["text_white"]}; font-size: 12px; margin: 0.25rem 0; opacity: 0.8;'>
                {title}
            </p>
            <p style='color: {COLORS["accent_gold"]}; font-size: 24px; font-weight: 700; margin: 0.5rem 0;'>
                {value}
            </p>
            {f'<p style="color: {COLORS["text_white"]}; font-size: 11px; margin: 0;">{description}</p>' if description else ''}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_metrics_grid(metrics: list, columns: int = 4):
        """Render grid of metrics."""
        cols = st.columns(columns)
        for idx, metric in enumerate(metrics):
            with cols[idx % columns]:
                MetricsDisplay.render_metric_card(
                    title=metric.get("title", ""),
                    value=metric.get("value", ""),
                    emoji=metric.get("emoji", "📊"),
                    description=metric.get("description"),
                    highlight=metric.get("highlight", False)
                )


class ResultsDisplay:
    """Professional results comparison display."""
    
    @staticmethod
    def render_comparison_header():
        """Render comparison header."""
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, {COLORS["primary_dark"]} 0%, {COLORS["primary_light"]} 50%, {COLORS["primary_dark"]} 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid {COLORS["accent_gold"]};
            text-align: center;
            margin: 2rem 0;
        '>
            <h2 style='color: {COLORS["accent_gold"]}; margin: 0;'>📊 Optimization Results</h2>
            <p style='color: {COLORS["text_white"]}; margin: 0.5rem 0 0 0;'>
                Comparison: Your Manual Allocation vs Optimized Portfolio
            </p>
        </div>
        """, unsafe_allow_html=True)


class Footer:
    """Professional footer."""
    
    @staticmethod
    def render(author: str, platform: str):
        """Render footer."""
        st.markdown(f"""
        <div style='
            border-top: 1px solid rgba(255, 255, 255, 0.3);
            padding: 2rem;
            text-align: center;
            margin-top: 3rem;
            color: #888;
            font-size: 12px;
        '>
            <p style='margin: 0.5rem 0;'>
                <strong>{author}</strong><br>
                {platform}
            </p>
            <p style='margin: 1rem 0 0 0; opacity: 0.7;'>
                © 2024 | Professional Portfolio Optimization | Powered by Modern Portfolio Theory
            </p>
        </div>
        """, unsafe_allow_html=True)
