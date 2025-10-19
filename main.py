import streamlit as st
import tensorflow as tf
import numpy as np
from gtts import gTTS
import os

def generate_voice_message(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    audio_file = "voice_message.mp3"
    tts.save(audio_file)
    return audio_file

# Load the language dictionaries for English, Kannada, and Hindi
language_texts = {
    'English': {
        'title': "Plant Disease Detection System",
        'description': "Welcome to the Plant Disease Detection System! 🌿🔍",
        'upload': "Choose an Image:",
        'predict_button': "Predict",
        'disease_recognition': "Disease Recognition",
        'treatment': "Recommended Treatment",
        'about': "About",
        'home': "Home",
        'mission': "Our mission is to help in identifying plant diseases efficiently.",
        'how_it_works': """
        ### How It Works
        1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
        2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
        3. **Results:** View the results and recommendations for further action.
        """,
        'why_choose_us': """
        ### Why Choose Us?
        - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
        - **User-Friendly:** Simple and intuitive interface for seamless user experience.
        - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.
        """,
        'get_started': """
        ### Get Started
        Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Detection System!
        """,
        'about_us': """
        ### About Us
        Learn more about the project, our team, and our goals on the **About** page.
        """,
        'results': "Our Prediction",
        'no_treatment': "No treatment available.",
        'about_data':"""
        #### About Dataset
        This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github report.
        This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
        A new directory containing 33 test images is created later for prediction purpose.""",
        'content':"""
        #### Content
        1. train (70295 images)
        2. test (33 images)
        3. validation (17572 images)
        """,
        'class_name':['Apple scab',
        'Apple Black rot',
        'Cedar apple rust',
        'Apple healthy',
        'Blueberry healthy',
        'Cherry(including sour) Powdery mildew',
        'Cherry(including sour) healthy',
        'Corn(maize) Cercospora leaf spot Gray leaf spot',
        'Corn(maize) Common rust',
        'Corn(maize) Northern Leaf Blight',
        'Corn(maize) healthy',
        'Grape Black rot',
        'Grape Esca(Black Measles)',
        'Grape Leaf blight(Isariopsis Leaf Spot)',
        'Grape healthy',
        'Orange Haunglongbing(Citrus greening)',
        'Peach Bacterial spot',
        'Peach healthy',
        'Pepper,bell Bacterial spot',
        'Pepper,bell healthy',
        'Potato Early blight',
        'Potato Late blight',
        'Potato healthy',
        'Raspberry healthy',
        'Soybean healthy',
        'Squash Powdery mildew',
        'Strawberry Leaf scorch',
        'Strawberry healthy',
        'Tomato Bacterial spot',
        'Tomato Early blight',
        'Tomato Late blight',
        'Tomato Leaf Mold',
        'Tomato Septoria leaf spot',
        'Tomato Spider mites Two-spotted spider mite',
        'Tomato Target Spot',
        'Tomato Yellow Leaf Curl Virus',
        'Tomato mosaic virus',
        'Tomato healthy'],
        "treats":"RECOMMENDED TREATMENT",
        "voice":"en",
        "predict":"Model is predicting it's",
        "voice_predict":"The model predicts that the plant is affected by"
        },

    'ಕನ್ನಡ': {
        'title': "ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ವ್ಯವಸ್ಥೆ",
        'description': "ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ವ್ಯವಸ್ಥೆಗೆ ಸ್ವಾಗತ! 🌿🔍",
        'upload': "ಚಿತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        'predict_button': "ಅನ್ವೇಷಿಸಿ",
        'disease_recognition': "ರೋಗ ಪತ್ತೆ",
        'treatment': "ಶಿಫಾರಸು ಮಾಡಿದ ಚಿಕಿತ್ಸೆ",
        'about': "ಬಗ್ಗೆ",
        'home': "ಮನೆ",
        'mission': "ನಮ್ಮ ಗುರಿ ಸಸ್ಯ ರೋಗಗಳನ್ನು ಸಮರ್ಥವಾಗಿ ಗುರುತಿಸಲು ಸಹಾಯ ಮಾಡುವುದು.",
        'how_it_works': """
        ### ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ
        1. **ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ:** **ರೋಗ ಪತ್ತೆ** ಪುಟಕ್ಕೆ ಹೋಗಿ, ಅನುಮಾನಾಸ್ಪದ ರೋಗಗಳುಳ್ಳ ಸಸ್ಯದ ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
        2. **ವಿಶ್ಲೇಷಣೆ:** ನಮ್ಮ ವ್ಯವಸ್ಥೆ ಸಸ್ಯದ ಸಾಧ್ಯವಾದ ರೋಗಗಳನ್ನು ಗುರುತಿಸಲು ಉದಾತ್ತ ಅಲ್ಗಾರಿದಮ್‌ಗಳನ್ನು ಬಳಸಿ ಚಿತ್ರವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸುತ್ತದೆ.
        3. **ಫಲಿತಾಂಶಗಳು:** ಫಲಿತಾಂಶಗಳನ್ನು ವೀಕ್ಷಿಸಿ ಮತ್ತು ಮುಂದಿನ ಕ್ರಮಕ್ಕಾಗಿ ಶಿಫಾರಸುಗಳನ್ನು ಪಡೆಯಿರಿ.
        """,
        'why_choose_us': """
        ### ಏಕೆ ನಮ್ಮನ್ನು ಆರಿಸಬೇಕು?
        - **ನಿಖರತೆ:** ನಮ್ಮ ವ್ಯವಸ್ಥೆ ನಿಖರವಾದ ರೋಗ ಪತ್ತೆಗೆ ಅತ್ಯಾಧುನಿಕ ಯಾಂತ್ರಿಕ ಅಧ್ಯಯನ ತಂತ್ರಜ್ಞಾನಗಳನ್ನು ಬಳಸುತ್ತದೆ.
        - **ಬಳಕೆದಾರ ಸ್ನೇಹಿ:** ಸರಳ ಮತ್ತು ಬೌದ್ಧಿಕ ಇಂಟರ್‌ಫೇಸ್, ಬಳಕೆದಾರ ಅನುಭವಕ್ಕಾಗಿ.
        - **ವೇಗ ಮತ್ತು ಸಮರ್ಥತೆ:** ನಿಮ್ಮನ್ನು ತ್ವರಿತವಾಗಿ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳಲು, ಕ್ಷಣಗಳಲ್ಲಿ ಫಲಿತಾಂಶಗಳನ್ನು ಪಡೆಯಿರಿ.
        """,
        'get_started': """
        ### ಪ್ರಾರಂಭಿಸಿ
        **ರೋಗ ಪತ್ತೆ** ಪುಟದಲ್ಲಿ ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ, ಮತ್ತು ನಮ್ಮ ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ವ್ಯವಸ್ಥೆಯ ಶಕ್ತಿಯನ್ನು ಅನುಭವಿಸಿ!
        """,
        'about_us': """
        ### ನಮ್ಮ ಬಗ್ಗೆ
        ಈ ಯೋಜನೆ, ನಮ್ಮ ತಂಡ ಮತ್ತು ನಮ್ಮ ಗುರಿಗಳನ್ನು ಕುರಿತು ಹೆಚ್ಚಿನದನ್ನು ತಿಳಿಯಲು **ಬಗ್ಗೆ** ಪುಟವನ್ನು ನೋಡಿ.
        """,
        'results': "ನಮ್ಮ ಪ್ರಿಡಿಕ್ಷನ್",
        'no_treatment': "ಚಿಕಿತ್ಸೆ ಲಭ್ಯವಿಲ್ಲ.",
        'about_data':"""
        #### ಡೇಟಾಸೆಟ್ ಬಗ್ಗೆ
        ಈ ಡೇಟಾಸೆಟ್ ಮೂಲ ಡೇಟಾಸೆಟ್‌ನಿಂದ ಆಫ್‌ಲೈನ್ ಆಗ್ಮೆಂಟೇಶನ್ ಬಳಸಿ ಪುನಃ ರಚಿಸಲಾಗಿದೆ. ಮೂಲ ಡೇಟಾಸೆಟ್ ಈ ಗಿಥಬ್ ರೆಪೋದಲ್ಲಿ ಕಂಡುಬರುತ್ತದೆ.
        ಈ ಡೇಟಾಸೆಟ್ 87 ಸಾವಿರಕ್ಕೂ ಹೆಚ್ಚು ಆರ್‌ಜಿಬಿ ಚಿತ್ರಗಳನ್ನು ಹೊಂದಿದೆ, ಇದರಲ್ಲಿ ಆರೋಗ್ಯಕರ ಮತ್ತು ರೋಗಗ್ರಸ್ತ ಬೆಳೆಗಳ ಎಲೆಗಳು 38 ವಿಭಿನ್ನ ವರ್ಗಗಳಲ್ಲಿ ವರ್ಗೀಕರಿಸಲ್ಪಟ್ಟಿವೆ. ಒಟ್ಟು ಡೇಟಾಸೆಟ್ ತರಬೇತಿ ಮತ್ತು ಧ್ರುವೀಕರಣ ಸೆಟ್‌ನಲ್ಲಿ 80/20 ಅನುಪಾತದಲ್ಲಿ ಹಂಚಲ್ಪಟ್ಟಿದೆ.
        ತರುವಾಯ, ಭವಿಷ್ಯವಾಣಿ ಉದ್ದೇಶಕ್ಕಾಗಿ 33 ಪರೀಕ್ಷಾ ಚಿತ್ರಗಳನ್ನು ಹೊಂದಿರುವ ಹೊಸ ಡೈರೆಕ್ಟರಿ ರಚಿಸಲ್ಪಟ್ಟಿದೆ.
        """,
        'content':"""
        #### ವಿಷಯ
        1. ತರಬೇತಿ (70,295 ಚಿತ್ರಗಳು)
        2. ಪರೀಕ್ಷೆ (33 ಚಿತ್ರಗಳು)
        3. ಧ್ರುವೀಕರಣ (17,572 ಚಿತ್ರಗಳು)
        """,
        'class_name':[
    'Apple scab (ಆಪಲ್ ಚರ್ಮರೋಗ)',
    'Apple Black rot (ಆಪಲ್ ಕಪ್ಪು ಕೀಟ)',
    'Cedar apple rust (ಸೀಡರ್ ಆಪಲ್ ಕಾತು)',
    'Apple healthy (ಆಪಲ್ ಆರೋಗ್ಯಕರ)',
    'Blueberry healthy (ಬ್ಲೂಬೆರz ಆರೋಗ್ಯಕರ)',
    'Cherry(including sour Powdery mildew (ಚೆರ್ರಿ (ತಿಂಡಿಗೂ ಒಳಗೊಂಡಂತೆ) ಪುಡಿಕಾಯಿಗಳು)',
    'Cherry(including sour healthy (ಚೆರ್ರಿ (ತಿಂಡಿಗೂ ಒಳಗೊಂಡಂತೆ) ಆರೋಗ್ಯಕರ)',
    'Corn(maize) Cercospora leaf spot Gray leaf spot (ಮಕ್ಕು (ಮೆಳೆಯ) ಸೆರ್ಕೋಸ್ಟೋರಾ ಎಲೆ ಕಲೆ ಸೋಲು, ಕಪ್ಪು ಎಲೆ ಕಲೆ)',
    'Corn(maize) Common rust (ಮಕ್ಕು (ಮೆಳೆಯ) ಸಾಮಾನ್ಯ ಕಾತು)',
    'Corn(maize) Northern Leaf Blight (ಮಕ್ಕು (ಮೆಳೆಯ) ಉತ್ತರ ಎಲೆ ಕಿರಿದಾಗ)',
    'Corn(maize)healthy (ಮಕ್ಕು (ಮೆಳೆಯ) ಆರೋಗ್ಯಕರ)',
    'Grape Black rot (ದ್ರಾಕ್ಷಿ ಕಪ್ಪು ಕೀಟ)',
    'Grape Esca (Black Measles) (ದ್ರಾಕ್ಷಿ ಎಸ್ಕಾ (ಕಪ್ಪು ತಲೆಕೀಲು))',
    'Grape Leaf blight (Isariopsis Leaf Spot) (ದ್ರಾಕ್ಷಿ ಎಲೆ ಕಿರಿದಾಗ (ಇಸರಿೋನೋಪ್ಸಿಸ್ ಎಲೆ ಕಲೆ))',
    'Grape healthy (ದ್ರಾಕ್ಷಿ ಆರೋಗ್ಯಕರ)',
    'Orange Haunglongbing (Citrus greening) (ಕಿತ್ತಳೆ ಹಂಗ್ಲೊಂಗ್‌ಬಿಂಗ್ (ಸಿಟ್ರಸ್ ಹಸಿರು))',
    'Peach Bacterial spot (ಮಡಿಕೆ ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ)',
    'Peach healthy (ಮಡಿಕೆ ಆರೋಗ್ಯಕರ)',
    'Pepper, bell Bacterial spot (ಮೆಣಸು, ಬೆಳ್ಳ ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ)',
    'Pepper, bell healthy (ಮೆಣಸು, ಬೆಳ್ಳ ಆರೋಗ್ಯಕರ)',
    'Potato Early blight (ಆಲೂಗಡ್ಡೆ ಮಾಡಿ ಕಿರಿದಾಗ)',
    'Potato Late blight (ಆಲೂಗಡ್ಡೆ ಮಾಡಿ ಕಿರಿದಾಗ)',
    'Potato healthy (ಆಲೂಗಡ್ಡೆ ಆರೋಗ್ಯಕರ)',
    'Raspberry healthy (ರಾಸ್ಪ್ಬೆರಿ ಆರೋಗ್ಯಕರ)',
    'Soybean healthy (ಸೋಯಾಬೀನ್ ಆರೋಗ್ಯಕರ)',
    'Squash Powdery mildew (ಸುಂದರ ಕುಂಡೆ ಪುಡಿಕಾಯಿಗಳು)',
    'Strawberry Leaf scorch (ಹಣ್ಣು ಕಾಳೆ ಎಲೆ ದಾಹ)',
    'Strawberry healthy (ಹಣ್ಣು ಕಾಳೆ ಆರೋಗ್ಯಕರ)',
    'Tomato Bacterial spot (ಟೊಮೆಟೋ ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ)',
    'Tomato Early blight (ಟೊಮೆಟೋ ಮಾಡಿ ಕಿರಿದಾಗ)',
    'Tomato Late blight (ಟೊಮೆಟೋ ಮಾಡಿ ಕಿರಿದಾಗ)',
    'Tomato Leaf Mold (ಟೊಮೆಟೋ ಎಲೆ ಹಾರಿಕೊಳ್ಳುವುದು)',
    'Tomato Septoria leaf spot (ಟೊಮೆಟೋ ಸೆಪ್ಟೋರಿಯಾ ಎಲೆ ಕಲೆ)',
    'Tomato Spider mites Two-spotted spider mite (ಟೊಮೆಟೋ ಜೀನು ಕೀಟ ಎರಡು ಬಿಂದುದಾರ ಕೀಟ)',
    'Tomato Target Spot (ಟೊಮೆಟೋ ಲಕ್ಷ್ಯ ಕಲೆ)',
    'Tomato Yellow Leaf Curl Virus (ಟೊಮೆಟೋ ಹಳದಿ ಎಲೆ ಕಂಚು ವೈರಸ್)',
    'Tomato mosaic virus (ಟೊಮೆಟೋ ಮೋಸಾಯಿಕ್ ವೈರಸ್)',
    'Tomato healthy (ಟೊಮೆಟೋ ಆರೋಗ್ಯಕರ)'
    
],
    "treats":"ಶಿಫಾರಸು ಮಾಡಿದ ಚಿಕಿತ್ಸೆಯು",
    "voice":"kn",
    "predict":"ಪತ್ತೆ ಯಾದ ರೋಗ",
    "voice_predict":"ಸಸ್ಯಯಲ್ಲಿ ಪತ್ತೆ ಯಾದ ರೋಗ"

    },
    'हिन्दी': {
        'title': "पौध रोग पहचान प्रणाली",
        'description': "पौध रोग पहचान प्रणाली में आपका स्वागत है! 🌿🔍",
        'upload': "एक चित्र चुनें:",
        'predict_button': "अनुमान लगाएं",
        'disease_recognition': "रोग पहचान",
        'treatment': "अनुशंसित उपचार",
        'about': "के बारे में",
        'home': "मुख पृष्ठ",
        'mission': "हमारा उद्देश्य पौधों की बीमारियों को शीघ्रता से पहचानना है।",
        'how_it_works': """
        ### यह कैसे काम करता है
        1. **चित्र अपलोड करें:** **रोग पहचान** पृष्ठ पर जाएं और संदेहास्पद रोग वाले पौधे का चित्र अपलोड करें।
        2. **विश्लेषण:** हमारा सिस्टम संभावित रोगों की पहचान करने के लिए उन्नत एल्गोरिदम का उपयोग करके चित्र को प्रोसेस करेगा।
        3. **परिणाम:** परिणाम देखें और आगे की कार्रवाई के लिए सिफारिशें प्राप्त करें।
        """,
        'why_choose_us': """
        ### हमें क्यों चुनें?
        - **सटीकता:** हमारा सिस्टम पौधों की बीमारियों की सटीक पहचान के लिए अत्याधुनिक मशीन लर्निंग तकनीकों का उपयोग करता है।
        - **उपयोगकर्ता-अनुकूल:** सरल और सहज इंटरफ़ेस उपयोगकर्ता अनुभव के लिए।
        - **तेज़ और कुशल:** त्वरित निर्णय लेने के लिए सेकंडों में परिणाम प्राप्त करें।
        """,
        'get_started': """
        ### आरंभ करें
        साइडबार में **रोग पहचान** पृष्ठ पर क्लिक करें, चित्र अपलोड करें और हमारे पौध रोग पहचान प्रणाली की शक्ति का अनुभव करें!
        """,
        'about_us': """
        ### हमारे बारे में
        इस परियोजना, हमारी टीम और हमारे उद्देश्यों के बारे में अधिक जानने के लिए **के बारे में** पृष्ठ देखें।
        """,
        'results': "हमारी भविष्यवाणी",
        'no_treatment': "उपलब्ध कोई उपचार नहीं।",
        'about_data':"""
        #### डाटासेट के बारे में
        यह डाटासेट मूल डाटासेट से ऑफ़लाइन ऑग्मेंटेशन का उपयोग करके फिर से बनाया गया है। मूल डाटासेट इस गिटहब रिपॉजिटरी पर पाया जा सकता है।
        इस डाटासेट में लगभग 87,000 आरजीबी छवियाँ शामिल हैं, जिनमें स्वस्थ और बीमार फसलों की पत्तियाँ होती हैं, जिन्हें 38 अलग-अलग वर्गों में वर्गीकृत किया गया है। कुल डाटासेट को 80/20 अनुपात में प्रशिक्षण और मान्यता सेट में विभाजित किया गया है, जिसमें निर्देशिका संरचना को संरक्षित किया गया है।
        भविष्यवाणी के उद्देश्य के लिए बाद में 33 परीक्षण छवियों वाली एक नई निर्देशिका बनाई गई है।
        """,
        'content':"""
        #### सामग्री
        1. प्रशिक्षण (70,295 छवियाँ)
        2. परीक्षण (33 छवियाँ)
        3. मान्यता (17,572 छवियाँ)
        """,
        'class_name': [
    'Apple scab ( सेब का चर्म रोग)',
    'Apple Black rot (सेब काला सड़न)',
    'Apple Cedar apple rust (सेब सिडर सेब का जंग)',
    'Apple healthy (सेब स्वस्थ)',
    'Blueberry healthy (ब्लूबेरी स्वस्थ)',
    'Cherry(including sour) Powdery mildew (चेरी (खट्टी शामिल) पाउडरी फफूंदी)',
    'Cherry(including sour) healthy (चेरी (खट्टी शामिल) स्वस्थ)',
    'Corn(maize) Cercospora leaf spot Gray leaf spot (मक्का सार्कोस्पोरा पत्ते की दाग ग्रे पत्ते का दाग)',
    'Corn(maize) Common rust (मक्का सामान्य जंग)',
    'Corn(maize) Northern Leaf Blight (मक्का उत्तरी पत्ते की बीमारी)',
    'Corn(maize) healthy (मक्का स्वस्थ)',
    'Grape Black rot (अंगूर काला सड़न)',
    'Grape Esca (Black Measles) (अंगूर एस्का (काले दाने))',
    'Grape Leaf blight (Isariopsis Leaf Spot) (अंगूर पत्ते की बीमारी (इसारीओप्सिस पत्ते का दाग))',
    'Grape healthy (अंगूर स्वस्थ)',
    'Orange Haunglongbing (Citrus greening) (संतरा हुआंगलोंगबिंग (सिट्रस हरियाली))',
    'Peach Bacterial spot (आड़ू बैक्टीरियल दाग)',
    'Peach healthy (आड़ू स्वस्थ)',
    'Pepper, bell Bacterial spot (शिमला मिर्च बैक्टीरियल दाग)',
    'Pepper, bell healthy (शिमला मिर्च स्वस्थ)',
    'Potato Early blight (आलू )जल्दी बीमारी )',
    'Potato Late blight (आलू )लेट बीमारी)',
    'Potato healthy (आलू )स्वस्थ)',
    'Raspberry healthy (रसभरी )स्वस्थ)',
    'Soybean healthy (सोयाबीन )स्वस्थ)',
    'Squash Powdery mildew (कद्दू )पाउडरी फफूंदी)',
    'Strawberry Leaf scorch (स्ट्रॉबेरी )पत्ते की झुलस)',
    'Strawberry healthy (स्ट्रॉबेरी )स्वस्थ)',
    'Tomato Bacterial spot (टमाटर )बैक्टीरियल दाग)',
    'Tomato Early blight (टमाटर )जल्दी बीमारी)',
    'Tomato Late blight (टमाटर )लेट बीमारी)',
    'Tomato Leaf Mold (टमाटर )पत्ते की फफूंदी)',
    'Tomato Septoria leaf spot (टमाटर )सेप्टोरिया पत्ते का दाग)',
    'Tomato Spider mites Two-spotted spider mite (टमाटर )स्पाइडर माइट्स दो-बिंदु वाले स्पाइडर माइट)',
    'Tomato Target Spot (टमाटर )लक्ष्य दाग)',
    'Tomato Yellow Leaf Curl Virus (टमाटर पीले पत्ते की लहर वायरस)',
    'Tomato mosaic virus (टमाटर मोज़ाइक वायरस)',
    'Tomato healthy (टमाटर )स्वस्थ)'
        ],
    "treats":'अनुशंसित उपचार',
    "voice":"hi",
    "predict":"रोग का पता चला",
    "voice_predict":"पौधे में रोग का पता चला"
    }
}

# Sidebar for language selection
st.sidebar.title("Dashboard")
language = st.sidebar.selectbox("Select Language", ['English', 'ಕನ್ನಡ', 'हिन्दी'])

# Retrieve the text in the selected language
texts = language_texts[language]
        
#tensorflow model prediction
def cnn_prediction(test_image):
    cnn = tf.keras.models.load_model('trained_plant_disease_system_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = cnn.predict(input_arr)
    result_index = np.argmax(predictions) #Return index of max element
    return result_index

# Dictionary with disease treatments
disease_treatments = {
    "Apple scab":"Apply fungicides like captan or sulfur. Prune infected leaves.",
    "Apple Black rot": "Remove infected fruit and use fungicides like benomyl.",
    "Cedar apple rust": "Use fungicides and remove nearby cedar trees.",
    "Apple healthy": "No treatment necessary.",
    "Blueberry healthy": "No treatment necessary.",
    "Cherry(including sour) Powdery mildew": "Apply sulfur or potassium bicarbonate-based fungicides.",
    "Cherry(including sour) healthy": "No treatment necessary.",
    "Corn(maize) Cercospora leaf spot Gray leaf spot": "Apply fungicides and rotate crops to reduce infection.",
    "Corn(maize) Common rust": "Apply fungicides or use resistant varieties.",
    "Corn(maize) Northern Leaf Blight": "Use resistant varieties and apply fungicides if necessary.",
    "Corn(maize) healthy": "No treatment necessary.",
    "Grape Black rot": "Remove affected plant parts and apply fungicides like mancozeb.",
    "Grape Esca(Black Measles)": "Use fungicides and prune diseased wood.",
    "Grape Leaf blight(Isariopsis Leaf Spot)": "Apply fungicides like copper-based sprays.",
    "Grape healthy": "No treatment necessary.",
    "Orange Haunglongbing(Citrus greening)": "No cure; remove affected trees to prevent spreading.",
    "Peach Bacterial spot": "Use bactericides containing copper and remove infected parts.",
    "Peach healthy": "No treatment necessary.",
    "Pepper,bell Bacterial spot": "Apply copper-based sprays and remove infected leaves.",
    "Pepper, bell healthy": "No treatment necessary.",
    "Potato Early blight": "Apply fungicides like chlorothalonil or mancozeb.",
    "Potato Late blight": "Use fungicides and practice crop rotation.",
    "Potato healthy": "No treatment necessary.",
    "Raspberry healthy": "No treatment necessary.",
    "Soybean healthy": "No treatment necessary.",
    "Squash Powdery mildew": "Apply sulfur or potassium bicarbonate-based fungicides.",
    "Strawberry Leaf scorch": "Remove infected leaves and use fungicides.",
    "Strawberry healthy": "No treatment necessary.",
    "Tomato Bacterial spot": "Use copper-based sprays and remove infected leaves.",
    "Tomato Early blight": "Apply fungicides like chlorothalonil or copper-based fungicides.",
    "Tomato Late blight": "Apply fungicides and ensure good air circulation.",
    "Tomato Leaf Mold": "Use fungicides and increase ventilation around plants.",
    "Tomato Septoria leaf spot": "Apply fungicides and remove infected leaves.",
    "Tomato Spider mites Two-spotted spider mite": "Use miticides and increase humidity.",
    "Tomato Target Spot": "Use fungicides and prune infected leaves.",
    "Tomato Yellow Leaf Curl Virus": "Remove infected plants and control whitefly vectors.",
    "Tomato mosaic virus": "No cure; remove infected plants.",
    "Tomato healthy": "No treatment necessary.",
    "Apple scab (ಆಪಲ್ ಚರ್ಮರೋಗ)": "ಕ್ಯಾಪ್ಟಾನ್ ಅಥವಾ ಗಂಧಕದಂತಹ ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿರಿ. ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ಕಡಿದಿಡಿ.",
    "Apple Black rot (ಆಪಲ್ ಕಪ್ಪು ಕೀಟ)": "ಸೋಂಕಿತ ಹಣ್ಣನ್ನು ತೆಗೆದುಹಾಕಿ, ಬೆನೋಮಿಲ್ ಬಳಸಿ.",
    "Cedar apple rust (ಸೀಡರ್ ಆಪಲ್ ಕಾತು)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸಮೀಪದ ಸೀಡರ್ ಮರಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Apple healthy (ಆಪಲ್ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Blueberry healthy (ಬ್ಲೂಬೆರಿ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Cherry(including sour Powdery mildew (ಚೆರ್ರಿ (ತಿಂಡಿಗೂ ಒಳಗೊಂಡಂತೆ) ಪುಡಿಕಾಯಿಗಳು)": "ಸಲ್ಫರ್ ಅಥವಾ ಪೊಟ್ಯಾಸಿಯಂ ಬಿಕಾರ್ಬೋನೇಟ್ ಆಧಾರಿತ ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ.",
    "Cherry(including sour) healthy (ಚೆರ್ರಿ (ತಿಂಡಿಗೂ ಒಳಗೊಂಡಂತೆ) ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Corn(maize) Cercospora leaf spot Gray leaf spot (ಮಕ್ಕು (ಮೆಳೆಯ) ಸೆರ್ಕೋಸ್ಟೋರಾ ಎಲೆ ಕಲೆ ಸೋಲು, ಕಪ್ಪು ಎಲೆ ಕಲೆ)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಬೆಳೆ ಹಾರಾಟವನ್ನು ಅಭ್ಯಾಸ ಮಾಡಿ.",
    "Corn(maize) Common rust (ಮಕ್ಕು (ಮೆಳೆಯ) ಸಾಮಾನ್ಯ ಕಾತು)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಅಥವಾ ತಾಳುವಿಕೆಯ ಜಾತಿಗಳನ್ನು ಬಳಸಿರಿ.",
    "Corn(maize) Northern Leaf Blight (ಮಕ್ಕು (ಮೆಳೆಯ) ಉತ್ತರ ಎಲೆ ಕಿರಿದಾಗ)": "ತಾಳುವಿಕೆಯ ಜಾತಿಗಳನ್ನು ಬಳಸಿರಿ ಮತ್ತು ಅಗತ್ಯವಿದ್ದರೆ ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ.",
    "Corn(maize) healthy (ಮಕ್ಕು (ಮೆಳೆಯ) ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Grape Black rot (ದ್ರಾಕ್ಷಿ ಕಪ್ಪು ಕೀಟ)": "ಸೋಂಕಿತ ಭಾಗಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಮ್ಯಾಂಕೋಜೆಬ್ ಸೇರಿದಂತೆ ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ.",
    "Grape Esca (Black Measles) (ದ್ರಾಕ್ಷಿ ಎಸ್ಕಾ (ಕಪ್ಪು ತಲೆಕೀಲು))": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಮರದ ಭಾಗಗಳನ್ನು ಕಡಿದಿಡಿ.",
    "Grape Leaf blight (Isariopsis Leaf Spot) (ದ್ರಾಕ್ಷಿ ಎಲೆ ಕಿರಿದಾಗ (ಇಸರಿೋನೋಪ್ಸಿಸ್ ಎಲೆ ಕಲೆ))": "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳನ್ನು ಬಳಸಿ.",
    "Grape healthy (ದ್ರಾಕ್ಷಿ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Orange Haunglongbing (Citrus greening) (ಕಿತ್ತಳೆ ಹಂಗ್ಲೊಂಗ್‌ಬಿಂಗ್ (ಸಿಟ್ರಸ್ ಹಸಿರು))": "ಚಿಕಿತ್ಸೆ ಇಲ್ಲ; ಸೋಂಕಿತ ಮರಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Peach Bacterial spot (ಮಡಿಕೆ ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ)": "ತಾಮ್ರವನ್ನು ಹೊಂದಿರುವ ಬ್ಯಾಕ್ಟೀರಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಭಾಗಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Peach healthy (ಮಡಿಕೆ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Pepper, bell Bacterial spot (ಮೆಣಸು, ಬೆಳ್ಳ ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ)": "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Pepper, bell healthy (ಮೆಣಸು, ಬೆಳ್ಳ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Potato Early blight (ಆಲೂಗಡ್ಡೆ ಮಾಡಿ ಕಿರಿದಾಗ)": "ಕ್ಲೋರೋಥಾಲೊನಿಲ್ ಅಥವಾ ಮ್ಯಾಂಕೋಜೆಬ್ ಸೇರಿದಂತೆ ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ.",
    "Potato Late blight (ಆಲೂಗಡ್ಡೆ ಮಾಡಿ ಕಿರಿದಾಗ)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಬೆಳೆ ಹಾರಾಟವನ್ನು ಅಭ್ಯಾಸ ಮಾಡಿ.",
    "Potato healthy (ಆಲೂಗಡ್ಡೆ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Raspberry healthy (ರಾಸ್ಪ್ಬೆರಿ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Soybean healthy (ಸೋಯಾಬೀನ್ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Squash Powdery mildew (ಸುಂದರ ಕುಂಡೆ ಪುಡಿಕಾಯಿಗಳು)": "ಸಲ್ಫರ್ ಅಥವಾ ಪೊಟ್ಯಾಸಿಯಂ ಬಿಕಾರ್ಬೋನೇಟ್ ಆಧಾರಿತ ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ.",
    "Strawberry Leaf scorch (ಹಣ್ಣು ಕಾಳೆ ಎಲೆ ದಾಹ)": "ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ.",
    "Strawberry healthy (ಹಣ್ಣು ಕಾಳೆ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Tomato Bacterial spot (ಟೊಮೆಟೋ ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಕಲೆ)": "ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Tomato Early blight (ಟೊಮೆಟೋ ಮಾಡಿ ಕಿರಿದಾಗ)":"ತಾಮ್ರ ಆಧಾರಿತ ಸ್ಪ್ರೇಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Tomato Late blight (ಟೊಮೆಟೋ ಮಾಡಿ ಕಿರಿದಾಗ)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಉತ್ತಮ ಗಾಳಿಯ ಪ್ರವಹವಿರುವಂತೆ ಪರಿಶೀಲಿಸಿ.",
    "Tomato Leaf Mold (ಟೊಮೆಟೋ ಎಲೆ ಹಾರಿಕೊಳ್ಳುವುದು)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸಸ್ಯಗಳ ಸುತ್ತಲಿನ ವಾತಾವರಣವನ್ನು ಸುಧಾರಿಸಿ.",
    "Tomato Septoria leaf spot (ಟೊಮೆಟೋ ಸೆಪ್ಟೋರಿಯಾ ಎಲೆ ಕಲೆ)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Tomato Spider mites Two-spotted spider mite (ಟೊಮೆಟೋ ಜೀನು ಕೀಟ ಎರಡು ಬಿಂದುದಾರ ಕೀಟ)": "ಮಿಟಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ತೇವಾಂಶವನ್ನು ಹೆಚ್ಚಿಸಿ.",
    "Tomato Target Spot (ಟೊಮೆಟೋ ಲಕ್ಷ್ಯ ಕಲೆ)": "ಫುಂಗಿಸೈಡ್ಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ಕಡಿದಿಡಿ.",
    "Tomato Yellow Leaf Curl Virus (ಟೊಮೆಟೋ ಹಳದಿ ಎಲೆ ಕಂಚು ವೈರಸ್)": "ಸೋಂಕಿತ ಸಸಿಗಳನ್ನು ತೆಗೆದುಹಾಕಿ ಮತ್ತು ವೈಟ್ಫ್ಲೈ ವೆಕ್ಟರ್‌ಗಳನ್ನು ನಿಯಂತ್ರಿಸಿ.",
    "Tomato mosaic virus (ಟೊಮೆಟೋ ಮೋಸಾಯಿಕ್ ವೈರಸ್)": "ಚಿಕಿತ್ಸೆ ಇಲ್ಲ; ಸೋಂಕಿತ ಸಸಿಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.",
    "Tomato healthy (ಟೊಮೆಟೋ ಆರೋಗ್ಯಕರ)": "ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ.",
    "Apple scab (सेब का चर्म रोग)": "कप्तान या गंधक जैसे फफूंदनाशक का उपयोग करें। संक्रमित पत्तियों को काटें।",
    "Apple Black rot (सेब काला सड़न)": "संक्रमित फलों को हटाएं और बेनोमिल जैसे फफूंदनाशक का उपयोग करें।",
    "Cedar apple rust (सिडर सेब का जंग)": "फफूंदनाशक का उपयोग करें और पास के सिडर पेड़ों को हटा दें।",
    "Apple healthy (सेब स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Blueberry healthy (ब्लूबेरी स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Cherry(including sour) Powdery mildew (चेरी (खट्टी शामिल) पाउडरी फफूंदी)": "गंधक या पोटैशियम बाइकार्बोनेट आधारित फफूंदनाशक का उपयोग करें।",
    "Cherry(including sour) healthy (चेरी (खट्टी शामिल) स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Corn(maize) Cercospora leaf spot Gray leaf spot (मक्का सार्कोस्पोरा पत्ते की दाग ग्रे पत्ते का दाग)": "फफूंदनाशक का उपयोग करें और संक्रमण को कम करने के लिए फसल चक्रण करें।",
    "Corn(maize) Common rust (मक्का सामान्य जंग)": "फफूंदनाशक का उपयोग करें या प्रतिरोधी किस्में लगाएं।",
    "Corn(maize) Northern Leaf Blight (मक्का उत्तरी पत्ते की बीमारी)": "प्रतिरोधी किस्मों का उपयोग करें और यदि आवश्यक हो तो फफूंदनाशक का उपयोग करें।",
    "Corn(maize) healthy (मक्का स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Grape Black rot (अंगूर काला सड़न)": "संक्रमित पौधों के हिस्सों को हटाएं और मैनकोजेब जैसे फफूंदनाशक का उपयोग करें।",
    "Grape Esca (Black Measles) (अंगूर एस्का (काले दाने))": "फफूंदनाशक का उपयोग करें और संक्रमित लकड़ी को काटें।",
    "Grape Leaf blight (Isariopsis Leaf Spot) (अंगूर पत्ते की बीमारी (इसारीओप्सिस पत्ते का दाग))": "तांबा आधारित स्प्रे का उपयोग करें।",
    "Grape healthy (अंगूर स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Orange Haunglongbing (Citrus greening) (संतरा हुआंगलोंगबिंग (सिट्रस हरियाली))": "कोई उपचार नहीं है; संक्रमण फैलने से बचने के लिए संक्रमित पेड़ों को हटा दें।",
    "Peach Bacterial spot (आड़ू बैक्टीरियल दाग)": "तांबा युक्त जीवाणुनाशक का उपयोग करें और संक्रमित हिस्सों को हटा दें।",
    "Peach healthy (आड़ू स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Pepper, bell Bacterial spot (शिमला मिर्च बैक्टीरियल दाग)": "तांबा आधारित स्प्रे का उपयोग करें और संक्रमित पत्तियों को हटा दें।",
    "Pepper, bell healthy (शिमला मिर्च स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Potato Early blight (आलू जल्दी बीमारी)": "क्लोरोथालोनिल या मैनकोजेब जैसे फफूंदनाशक का उपयोग करें।",
    "Potato Late blight (आलू लेट बीमारी)": "फफूंदनाशक का उपयोग करें और फसल चक्रण का अभ्यास करें।",
    "Potato healthy (आलू स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Raspberry healthy (रसभरी स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Soybean healthy (सोयाबीन स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Squash Powdery mildew (कद्दू पाउडरी फफूंदी)": "गंधक या पोटैशियम बाइकार्बोनेट आधारित फफूंदनाशक का उपयोग करें।",
    "Strawberry Leaf scorch (स्ट्रॉबेरी पत्ते की झुलस)": "संक्रमित पत्तियों को हटा दें और फफूंदनाशक का उपयोग करें।",
    "Strawberry healthy (स्ट्रॉबेरी स्वस्थ)": "कोई उपचार आवश्यक नहीं है।",
    "Tomato Bacterial spot (टमाटर बैक्टीरियल दाग)": "तांबा आधारित स्प्रे का उपयोग करें और संक्रमित पत्तियों को हटा दें।",
    "Tomato Early blight (टमाटर जल्दी बीमारी)": "क्लोरोथालोनिल या तांबा आधारित फफूंदनाशक का उपयोग करें।",
    "Tomato Late blight (टमाटर लेट बीमारी)": "फफूंदनाशक का उपयोग करें और अच्छी हवा का संचार सुनिश्चित करें।",
    "Tomato Leaf Mold (टमाटर पत्ते की फफूंदी)": "फफूंदनाशक का उपयोग करें और पौधों के आसपास की हवा का वेंटिलेशन बढ़ाएं।",
    "Tomato Septoria leaf spot (टमाटर सेप्टोरिया पत्ते का दाग)": "फफूंदनाशक का उपयोग करें और संक्रमित पत्तियों को हटा दें।",
    "Tomato Spider mites Two-spotted spider mite (टमाटर स्पाइडर माइट्स दो-बिंदु वाले स्पाइडर माइट)": "माइटिसाइड का उपयोग करें और नमी बढ़ाएं।",
    "Tomato Target Spot (टमाटर लक्ष्य दाग)": "फफूंदनाशक का उपयोग करें और संक्रमित पत्तियों को काटें।",
    "Tomato Yellow Leaf Curl Virus (टमाटर पीले पत्ते की लहर वायरस)": "संक्रमित पौधों को हटा दें और सफेद मक्खी वेक्टरों को नियंत्रित करें।",
    "Tomato mosaic virus (टमाटर मोज़ाइक वायरस)": "कोई उपचार नहीं; संक्रमित पौधों को हटा दें।",
    "Tomato healthy (टमाटर स्वस्थ)": "कोई उपचार आवश्यक नहीं है।"
        }

# Main Page
app_mode = st.sidebar.selectbox(texts['home'], [texts['home'], texts['about'], texts['disease_recognition']])

#Main Page
if(app_mode== texts["home"]):
    st.header(texts["title"])
    image_path = "image.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown(f"### {texts['description']}")
    st.markdown(f"### {texts['mission']}")
    st.markdown(texts['how_it_works'])
    st.markdown(texts['why_choose_us'])
    st.markdown(texts['get_started'])
    st.markdown(texts['about_us'])

#About Project
elif(app_mode==texts["about"]):
    st.header(texts["about"])
    st.markdown(texts['about_data'])
    st.markdown(texts['content'])
    
#Prediction Page
elif(app_mode== texts["disease_recognition"]):
    st.header(texts["disease_recognition"])
    test_image = st.file_uploader(texts["upload"])
    
    if test_image is not None:
        st.image(test_image, use_column_width=True)
    
    if st.button(texts['predict_button']):
        st.write(texts['results'])
        
        result_index = cnn_prediction(test_image)
        predicted_disease = {texts['class_name'][result_index]}
        st.success(f"{texts['predict']} : {predicted_disease}")
        if isinstance(predicted_disease, set):
           predicted_disease = next(iter(predicted_disease))  # Extract an element from the set

        # Now use the string to get the treatment
        treatment = disease_treatments.get(predicted_disease, texts['no_treatment'])
        st.info(f"{texts['treats']} : {treatment}")
        
        # Generate and play voice message
        voice_message = f"{texts['voice_predict']} {predicted_disease}. {texts['treats']}: {treatment}."
        language_code = texts['voice']  # Make sure this is a string 
        audio_file = generate_voice_message(voice_message, language=language_code)  # Change language code as needed
        st.audio(audio_file)

        # Clean up the audio file
        if os.path.exists(audio_file):
            os.remove(audio_file)

