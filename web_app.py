import streamlit as st
import yt_dlp
import os

# 1. වෙබ් පිටුවේ මූලික සැකසුම් (Page Title & Layout)
st.set_page_config(page_title="Universal Video Downloader", page_icon="🎬", layout="centered")

# 2. CSS පාවිච්චි කරලා පිටුව ලස්සන කිරීම (Custom Styling)
st.markdown("""
    <style>
    /* මුළු පිටුවේම Background එක සහ Text පාට වෙනස් කිරීම */
    .stApp {
        background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
        color: #ffffff;
    }
    
    /* Input Box එක ලස්සන කිරීම */
    div.stTextInput > div > div > input {
        background-color: #2a2640 !important;
        color: white !important;
        border: 2px solid #6c5ce7 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }
    
    /* Buttons ලස්සන කිරීම */
    div.stButton > button {
        background: linear-gradient(90deg, #6c5ce7 0%, #a8a5ff 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 30px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        box-shadow: 0px 4px 15px rgba(108, 92, 231, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    /* Button එක උඩට මවුස් එක ගෙනිච්චම වෙනස් වන හැටි */
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0px 6px 20px rgba(108, 92, 231, 0.6) !important;
    }
    
    /* Card/Container පෙනුම */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. වෙබ් පිටුවේ පෙනුම (UI Elements)
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #a8a5ff;'>🎬 Universal Downloader</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ddd;'>Download videos from YouTube, TikTok (No Watermark), Facebook & Instagram instantly.</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ලින්ක් එක ගන්නා තැන
link = st.text_input("🔗 Paste Your Video Link Here:", placeholder="https://...")

# හිස් ඉඩක් තැබීමට
st.write("")

if link.strip():
    temp_filename = "downloaded_video.mp4"
    
    if st.button("🚀 Process & Download Video"):
        with st.spinner("⚡ Processing video... Please wait..."):
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
                
                st.success("🎉 Video processed successfully!")
                
                with open(temp_filename, "rb") as file:
                    st.download_button(
                        label="📥 Click here to Save Video File",
                        data=file,
                        file_name="My_Downloaded_Video.mp4",
                        mime="video/mp4"
                    )
                    
            except Exception as e:
                st.error(f"Something went wrong: {e}")
