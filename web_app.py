import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="TikTok Downloader", page_icon="🚀")
st.title("🚀 TikTok Video Downloader")
st.write("Paste your TikTok link below to download the video.")

link = st.text_input("Paste TikTok Link Here:", placeholder="https://www.tiktok.com/...")

if link.strip():
    # වීඩියෝ එකට තාවකාලික නමක් දීම
    temp_filename = "tiktok_video.mp4"
    
    if st.button("Process Video"):
        with st.spinner("Processing... Please wait..."):
            try:
                # පරණ ෆයිල් එකක් තිබුණොත් අයින් කරනවා
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
                    
                ydl_opts = {
                    'outtmpl': temp_filename,
                    'format': 'best',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ytl:
                    ytl.download([link])
                
                st.success("🎉 Video processed successfully!")
                
                # වීඩියෝ ෆයිල් එක බ්‍රවුසර් එක හරහා පරිශීලකයාගේ ෆෝන් එකට/PC එකට ඩවුන්ලෝඩ් කිරීමට දීම
                with open(temp_filename, "rb") as file:
                    st.download_button(
                        label="📥 Click here to Download Video File",
                        data=file,
                        file_name="Downloaded_TikTok_Video.mp4",
                        mime="video/mp4"
                    )
                    
            except Exception as e:
                st.error(f"Something went wrong: {e}")
