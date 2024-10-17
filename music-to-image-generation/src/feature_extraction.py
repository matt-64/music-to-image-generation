import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def analyze_audio(file_path):
    # Charger le fichier audio
    y, sr = librosa.load(file_path, sr=None)
    
    # Extraire les features
    features = {
        'Mel Spectrogram': librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128),
        'MFCC': librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13),
        'Chroma': librosa.feature.chroma_stft(y=y, sr=sr),
        'Zero Crossing Rate': librosa.feature.zero_crossing_rate(y),
        'Spectral Centroid': librosa.feature.spectral_centroid(y=y, sr=sr),
        'Spectral Bandwidth': librosa.feature.spectral_bandwidth(y=y, sr=sr),
        'Spectral Contrast': librosa.feature.spectral_contrast(y=y, sr=sr),
        'Tonal Centroid (Tonnetz)': librosa.feature.tonnetz(y=y, sr=sr),
        'RMS Energy': librosa.feature.rms(y=y)
    }
    
    # Afficher ou renvoyer les résultats
    for feature_name, feature_value in features.items():
        print(f"{feature_name}: {feature_value.shape}")
        
    return features

def plot_features(features, sr):
    plt.figure(figsize=(12, 8))
    
    # Mel Spectrogram
    plt.subplot(2, 2, 1)
    librosa.display.specshow(librosa.power_to_db(features['Mel Spectrogram'], ref=np.max),
                             sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel Spectrogram')
    
    # MFCC
    plt.subplot(2, 2, 2)
    librosa.display.specshow(features['MFCC'], x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    
    # Chroma
    plt.subplot(2, 2, 3)
    librosa.display.specshow(features['Chroma'], x_axis='time', y_axis='chroma', cmap='coolwarm')
    plt.colorbar()
    plt.title('Chroma')

    # Spectral Centroid
    plt.subplot(2, 2, 4)
    plt.semilogy(features['Spectral Centroid'].T, label='Spectral Centroid')
    plt.ylabel('Hz')
    plt.title('Spectral Centroid')
    
    plt.tight_layout()
    plt.show()

# Exemple d'utilisation :
audio_path = 'data/track1_test.wav'  # Remplacer par le chemin de votre fichier
features = analyze_audio(audio_path)
plot_features(features, sr=22050)  # Remplacer par le vrai taux d'échantillonnage si différent
