import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="TikTok Downloader", page_icon="🚀")
st.title("🚀 TikTok Video Downloader")
st.write("Paste your TikTok link below to download the video with sound.")

link = st.text_input("Paste TikTok Link Here:", placeholder="https://www.tiktok.com/...")

if link.strip():
    temp_filename = "tiktok_video.mp4"
    
    if st.button("Process Video"):
        with st.spinner("Processing video and audio... Please wait..."):
            try:
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
                    
                # සවුන්ඩ් ප්‍රශ්නය විසඳීමට format එක වෙනස් කර ඇත
                ydl_opts = {
                    'outtmpl': temp_filename,
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', # හොඳම වීඩියෝ සහ ඕඩියෝ එකතු කරයි
                    'merge_output_format': 'mp4', # අවසාන ෆයිල් එක mp4 එකක් ලෙස සකසයි
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ytl:
                    ytl.download([link])
                
                st.success("🎉 Video processed successfully with sound!")
                
                with open(temp_filename, "rb") as file:
                    st.download_button(
                        label="📥 Click here to Download Video File",
                        data=file,
                        file_name="Downloaded_TikTok_Video.mp4",
                        mime="video/mp4"
                    )
                    
            except Exception as e:
                st.error(f"Something went wrong: {e}")
