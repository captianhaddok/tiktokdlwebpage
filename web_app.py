import streamlit as st
import yt_dlp
import os

# 1. වෙබ් පිටුවේ සැකසුම්
st.set_page_config(page_title="X-Downloader | Premium", page_icon="⚡", layout="centered")

# 2. සුපිරිම Cyberpunk / Neon CSS එකතු කිරීම
st.markdown("""
    <style>
    /* මුළු සයිට් එකේම Background එකට Animated Gradient එකක් දීම */
    .stApp {
        background: linear-gradient(-45deg, #0f0c20, #15102a, #060314, #1a0b2e);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Premium Header Card */
    .premium-header {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 35px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
        margin-bottom: 30px;
    }
    
    .main-title {
        font-size: 40px !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 50%, #9b51e0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Supported Platforms Badge Line */
    .platform-badges {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 15px;
        flex-wrap: wrap;
    }
    
    .badge {
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .yt { color: #ff0000; border-color: #ff0000; }
    .tt { color: #00f2fe; border-color: #00f2fe; }
    .fb { color: #1877f2; border-color: #1877f2; }
    .ig { color: #f50057; border-color: #f50057; }
    
    /* Input Box එක සිරාම Neon එකක් කිරීම */
    div.stTextInput > div > div > input {
        background-color: rgba(20, 15, 38, 0.7) !important;
        color: #ffffff !important;
        border: 1px solid rgba(0, 242, 254, 0.3) !important;
        border-radius: 14px !important;
        padding: 16px !important;
        font-size: 16px !important;
        box-shadow: inset 0px 2px 4px rgba(0,0,0,0.5) !important;
        transition: all 0.4s ease !important;
    }
    
    div.stTextInput > div > div > input:focus {
        border-color: #00f2fe !important;
        box-shadow: 0px 0px 15px rgba(0, 242, 254, 0.4) !important;
    }
    
    /* ⚡ Ultimate Neon Download Button */
    div.stButton > button {
        background: linear-gradient(90deg, #00f2fe 0%, #9b51e0 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 16px 30px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 14px !important;
        box-shadow: 0px 0px 20px rgba(0, 242, 254, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
        margin-top: 10px;
    }
    
    div.stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0px 0px 30px rgba(155, 81, 224, 0.6) !important;
        background: linear-gradient(90deg, #9b51e0 0%, #00f2fe 100%) !important;
    }
    
    div.stButton > button:active {
        transform: scale(0.98) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. UI එක පෙන්වීම
st.markdown("""
    <div class="premium-header">
        <div class="main-title">⚡ X-Downloader</div>
        <p style="color: #b3b0cb; font-size: 15px; margin-bottom: 5px;">The Ultimate Multi-Platform Video Extraction Tool</p>
        <div class="platform-badges">
            <span class="badge yt">🛑 YouTube</span>
            <span class="badge tt">🎵 TikTok (Clean)</span>
            <span class="badge fb">🔹 Facebook</span>
            <span class="badge ig">📸 Instagram</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Input එකක් ගැනීම
link = st.text_input("⚡", placeholder="Paste your link here (YouTube, TikTok, m3u8...)...")

# පොඩි හිස් තැනක්
st.write("")

if link.strip():
    temp_filename = "downloaded_video.mp4"
    
    if st.button("🚀 Start High-Speed Download"):
        with st.spinner("⚡ Bypassing restrictions & extracting stream data..."):
            try:
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
                    
                ydl_opts = {
                    'outtmpl': temp_filename,
                    'format': 'bestvideo[ext=mp4][vcodec^=bytevc1]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'merge_output_format': 'mp4',
                    'cookiefile': 'cookies.txt', 
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ytl:
                    ytl.download([link])
                
                st.success("🎯 Video extracted successfully!")
                
                with open(temp_filename, "rb") as file:
                    st.download_button(
                        label="📥 SAVE TO DEVICE",
                        data=file,
                        file_name="X_Downloaded_Video.mp4",
                        mime="video/mp4"
                    )
                    
            except Exception as e:
                st.error(f"Extraction failed: {e}")
