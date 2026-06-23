import streamlit as st
import yt_dlp
import os

# වෙබ් පිටුවේ සැකසුම්
st.set_page_config(page_title="Universal Video Downloader", page_icon="🎬")
st.title("🎬 All-in-One Video Downloader")
st.write("YouTube, TikTok, Instagram හෝ Facebook ලින්ක් එකක් දීලා වීඩියෝ එක සවුන්ඩ් එක්කම ඩවුන්ලෝඩ් කරගන්න.")

# පරිශීලකයාගෙන් ලින්ක් එක ලබා ගැනීම
link = st.text_input("Paste Video Link Here:", placeholder="https://...")

if link.strip():
    # තාවකාලික ෆයිල් එකේ නම
    temp_filename = "downloaded_video.mp4"
    
    if st.button("Process & Download"):
        with st.spinner("Processing video... Please wait (This may take a while for YouTube videos)..."):
            try:
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
                    
                # YouTube සහ අනෙකුත් හැම වෙබ් අඩවියකටම ගැලපෙන හොඳම සෙටින්ග්ස්
                ydl_opts = {
                    'outtmpl': temp_filename,
    
    # 🤫 මෙන්න මේ රහස් කේතය (Format) එකතු කරන්න:
    # මේකෙන් TikTok සර්වර් එකේ තියෙන Watermark නැති 'bytevc1' හෝ හොඳම clean වීඩියෝ එක තෝරාගන්නවා
    'format': 'bestvideo[ext=mp4][vcodec^=bytevc1]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'merge_output_format': 'mp4',
    
    'cookiefile': 'cookies.txt',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ytl:
                    ytl.download([link])
                
                st.success("🎉 Video processed successfully!")
                
                # බ්‍රවුසර් එක හරහා පරිශීලකයාට ෆයිල් එක ලබා දීම
                with open(temp_filename, "rb") as file:
                    st.download_button(
                        label="📥 Click here to Save Video File",
                        data=file,
                        file_name="My_Downloaded_Video.mp4",
                        mime="video/mp4"
                    )
                    
            except Exception as e:
                st.error(f"Something went wrong: {e}")
