# 🎧 Music-to-Image Generation Tool 🎨

A Python-based tool that analyzes audio tracks from online sources (YouTube, Spotify, etc.) and extracts key audio features **without downloading the file locally**. Perfect for real-time audio analysis and music-related projects.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python Version](https://img.shields.io/badge/python-3.9-blue) ![License](https://img.shields.io/badge/license-MIT-blue)

---

## 🚀 Overview

This tool is designed for developers, data scientists, and audio engineers who need to analyze audio tracks from various platforms without storing them locally. It extracts key audio features like MFCCs, Zero Crossing Rate, and Spectral Centroid. The project also includes a lightweight Flask API for future scalability and online analysis.

---

## 🔥 Features

- **No Local Downloading:** Stream and analyze audio directly from YouTube, Spotify, etc.
- **Feature Extraction:** Automatically extract MFCCs, Zero Crossing Rate (ZCR), Spectral Bandwidth, and more.
- **Scalable Flask API:** Lightweight and flexible architecture for further development.
- **Real-time Processing:** Potential to expand towards real-time music processing for live performances or applications.

---

## 📦 Installation

To install and run the project, follow these steps:


# Clone the repository
git clone https://github.com/matt-64/music-to-image-generation.git

# Navigate to the project directory
cd music-to-image-generation

# Install the required dependencies
pip install -r requirements.txt
⚙️ Usage
1. Analyze Local Audio


2. Analyze YouTube or Spotify Audio


📊 Audio Features Extracted
Here are the audio features currently extracted by the tool:

MFCCs (Mel-Frequency Cepstral Coefficients)
Zero Crossing Rate (ZCR)
Spectral Centroid
Spectral Bandwidth
RMS Energy
Tonnetz (Tonal Centroid Features)
Each feature is visualized using matplotlib to provide graphical insights into the audio.

🌐 Flask API (Future)
A lightweight Flask API is currently in development. This will allow users to submit audio URLs via API calls and receive the extracted features in JSON format. Stay tuned for updates!



🛠️ Roadmap
 Basic audio feature extraction from local files
 Online audio analysis from YouTube/Spotify
 Implement Flask API for remote analysis
 Add support for SoundCloud and other platforms
 Real-time audio processing for live performances


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Acknowledgements
This project leverages Librosa for audio analysis and yt-dlp for streaming YouTube content.
Inspired by the power of Flask for building flexible web APIs.

Let's revolutionize the way we analyze music! 🎶🎨