# TheArtInOurWorlds-NASA-Space-Apps
NASA space apps Cairo 2022 local winner (Cairo).

This project is the solution designed for the NASA space apps hackathon 2022 by team NASART solving challenge: The Art in Our Worlds. 

This project won for its use of NASA's data.

# Challenge Description
NASA is moving its data to the cloud, and Machine Learning/Artificial Intelligence (ML/AI) can offer an innovative means to analyze 
and use this massive archive of free and open data. Your challenge is to create an application using ML/AI techniques that allows users to input 
short text phrases, matches that input to NASA science data or imagery, and displays the results for the user in a creative and artistic manner. 

Challenge link: https://2022.spaceappschallenge.org/challenges/2022-challenges/art-worlds/details

Team link: https://2022.spaceappschallenge.org/challenges/2022-challenges/art-worlds/teams/nasart/project

# Treasure Hunt
NASA spends every year billions of dollars in their research ($25.2 billions for fiscal year 2021), and the research this money has funded landed rovers on Mars, put people on the moon, and started exploring Jupiter's atmosphere, building a strong knowledge base along the way, but what good is this billion dollar treaure if it's put in a treasue chest without a key to access it ? What good is this amazing knowledge if it's not easily accessible to everyone ? Our solution is the key to reach this billion-dollar knowledge

# Product Design 
We wanted to design a product, not just a solution to the challenge. We followed the design thinking methodolgy that one of its principles is user-centricity and empathy, we didn't want to target space enthusiasts, we wanted to target ALL audiences.
![design thinking](https://user-images.githubusercontent.com/76780379/194407584-d0ebaa2c-290c-453f-b1f1-86d56473fb81.jpg)

# What do we mean by saying ALL audiences ?
The core of this project is a search engine that retrieves documents, pictures, videos, and can manipulate images in a creative way. Who might be the outcasts for such project ?

We wanted our product to achieve 2 things: DivErsItY & [inclusion]

Inclusion: we wanted visually impaired people to be able to use the product easily that's why we added a speech-to-text feature instead of typing the input text and a text-to-speech feature to read the retrieved documents or the description of the image.

Diversity: why do we have to search using a specific language like English ? By integrating with Google APIs, our product supports every language in the text input and translates the retrieved documents with the detected language.

# Detailed Solution Pipeline
1. Extracting images and their description from NASA earth book
- There was a need for a dataset that has images, the images description, and where to find these images, we used NASA’s earth book found in the challenge’s resources to extract such dataset that is going to be used later when we are filtering the images.
- This is implemented using python programming language

2. Speech to Text Transcription

![STT](https://user-images.githubusercontent.com/76780379/194410094-548f1b7d-6cdd-4ef2-ba40-9136ccc88e5b.png)

- It takes voice input from the user and maps it to its corresponding text
- It is implemented with machine learning using DeepSpeech model

3. Summarization model

![text_summarization-icon](https://user-images.githubusercontent.com/76780379/194410525-06f8c706-f8cc-4501-a144-935798e75aaf.png)

- This machine learning model summarizes images and videos description so that the input to the similarity model is a little shorter thus much more efficient.
- The model used is SpaCy 

4. Documents Similarity

![similarity](https://user-images.githubusercontent.com/76780379/194411207-f7a82a60-b471-499b-b650-f7457a8d8eb7.jpg)


- The core of the solution is allowing users to input short text phrases that gets matched with NASA science data or imagery.
- It takes input from the user that can be one word, or short text phrases.
- This feature is implemented with machine learning using BERT model (Bi-directional Representations from Transformers), that makes use of Transformer, an attention mechanism that learns contextual relations between words in a text, it return a list on indices containing the top 10 matches for the input text.

5. Creative Distortion of retrieved Images

![james small](https://user-images.githubusercontent.com/76780379/194413234-0cbff933-eb86-46e3-a8f1-34219f5587fc.jpg)
![james hot](https://user-images.githubusercontent.com/76780379/194413258-1af7c95b-77fb-4b4e-aefa-cd36d07aa213.jpg)

- In this feature, we wanted to target the lovers of the space, showing them the retrieved picture from the similarity (if found) in many ways, creatively distorting it, we implemented 3 techniques that can do this.

    1. Accessing a single-color channel of the image and changing its color map (needs one picture)

    2. Taking 2 pictures and creatively blending them together (mix-up technique in data augmentation)

    3. Taking 2 pictures and generating a third one using magenta, a pre trained style transfer generative adversarial network

6. Text to Speech

- This feature is continuation of the speech to text feature, to aid the visually impaired people with the search results.

- This machine learning model is Google Text to Speech, it is integrated with an API that can classify what is the input language

# Tech Stack
Our solution is implemented with:

Programming Languages : Python 3.9, JavaScript

Markup Language: HTML

Styling Language: CSS

Libraries used (sorted alphabetically): 
BeautifulSoup, cv2, Deepspeech, deep_translator, diffusers, ebooklib, ffmpeg, flask, gtts, IPython, langdetect, libasound2-dev, libportaudio2, libportaudiocpp0
,matplotlib, mediapy, nltk, numpy, os, pandas, PIL, portaudio19-dev, pytextrank, random, scipy, sklearn, tensorflow_hub, transformers, warning, wave, wget ,zipfile

# Demo
![interface](https://user-images.githubusercontent.com/76780379/193410488-dd3184a2-65dd-474a-bc56-9ca379fa142e.jpg)

