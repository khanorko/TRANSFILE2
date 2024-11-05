import streamlit as st
import whisper
import tempfile
import os

st.title("Audio/Video Transcription App")

uploaded_file = st.file_uploader("Upload an MP3, WAV, or Video file", type=['mp3', 'wav', 'mp4', 'mov', 'mkv'])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_filename = temp_file.name

    # Display upload progress
    st.info("File uploaded successfully!")
    progress_text = "Transcribing..."
    progress_bar = st.progress(0)

    # Load the Whisper model
    with st.spinner("Loading Whisper model..."):
        model = whisper.load_model("base")
        progress_bar.progress(50)

    # Transcribe the audio/video file
    with st.spinner("Transcribing..."):
        result = model.transcribe(temp_filename)
        transcript = result['text']
        progress_bar.progress(100)

    st.success("Transcription completed!")

    # Save the transcript to a text file (optional)
    transcript_filename = "transcript.txt"
    with open(transcript_filename, 'w') as f:
        f.write(transcript)

    # Provide option to display the transcript
    if st.button("Show Transcript"):
        st.text_area("Transcript", transcript, height=300)

    # Clean up temporary files
    os.remove(temp_filename)
