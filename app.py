"""
💕 Valentine's Proposal Website 💕
A romantic interactive proposal experience for your special someone.

Replace the placeholder images in the 'images/' folder with your own:
- story_1.jpg, story_2.jpg, story_3.jpg - Your relationship journey photos
- her_portrait.jpg - A beautiful solo photo of her (4:5 ratio recommended)
- us_final.jpg - Your favorite couple photo (16:9 ratio recommended)

Password: 02/01/2026 (The date you first met)

Music: Place 'gone_gone_gone.mp3' in the root folder for background music
"""

import streamlit as st
import os

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="💕 A Special Message For You",
    page_icon="💕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS - Soft Pink/Cream Theme
# ============================================================================
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main theme */
    .stApp {
        background: linear-gradient(135deg, #FFF5F5 0%, #FFE4EC 50%, #FFF0F5 100%);
        min-height: 100vh;
    }
    
    /* Custom container styling */
    .romantic-container {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 40px rgba(255, 107, 157, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 182, 193, 0.3);
    }
    
    /* Title styling */
    .romantic-title {
        font-family: 'Georgia', serif;
        color: #FF6B9D;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(255, 107, 157, 0.2);
    }
    
    .romantic-subtitle {
        font-family: 'Georgia', serif;
        color: #E75480;
        text-align: center;
        font-size: 1.3rem;
        font-style: italic;
        margin-bottom: 2rem;
    }
    
    /* Story text styling */
    .story-text {
        font-family: 'Georgia', serif;
        color: #8B4B6A;
        font-size: 1.1rem;
        line-height: 1.8;
        text-align: center;
        padding: 1rem;
    }
    
    /* Quote styling */
    .love-quote {
        font-family: 'Georgia', serif;
        color: #E75480;
        font-size: 1.4rem;
        font-style: italic;
        text-align: center;
        padding: 2rem;
        border-left: 4px solid #FF6B9D;
        background: rgba(255, 182, 193, 0.1);
        margin: 1.5rem 0;
    }
    
    /* Image containers */
    .portrait-container {
        aspect-ratio: 4/5;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        border-radius: 15px;
        border: 3px solid #FFB6C1;
        box-shadow: 0 8px 32px rgba(255, 107, 157, 0.25);
    }
    
    .wide-container {
        aspect-ratio: 16/9;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        border-radius: 15px;
        border: 3px solid #FFB6C1;
        box-shadow: 0 8px 32px rgba(255, 107, 157, 0.25);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #FF6B9D 0%, #E75480 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2.5rem;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 107, 157, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 157, 0.5);
    }
    
    /* Password input styling */
    .stTextInput>div>div>input {
        border-radius: 15px;
        border: 2px solid #FFB6C1;
        text-align: center;
        font-size: 1.2rem;
    }
    
    /* Heart animation */
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(5deg); }
    }
    
    .floating-heart {
        animation: float 3s ease-in-out infinite;
        display: inline-block;
    }
    
    /* Celebration text */
    .celebration-text {
        font-family: 'Georgia', serif;
        color: #FF6B9D;
        font-size: 2.5rem;
        text-align: center;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Progress dots */
    .progress-dots {
        text-align: center;
        padding: 1rem;
    }
    
    .dot {
        height: 12px;
        width: 12px;
        margin: 0 5px;
        background-color: #FFD1DC;
        border-radius: 50%;
        display: inline-block;
    }
    
    .dot.active {
        background-color: #FF6B9D;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'state' not in st.session_state:
    st.session_state.state = 0  # Start at password screen

if 'story_page' not in st.session_state:
    st.session_state.story_page = 0

# Check for celebration trigger from query params
query_params = st.query_params
if query_params.get('celebrate') == 'yes':
    st.session_state.state = 4
    st.query_params.clear()

# ============================================================================
# PLACEHOLDER IMAGES - Replace with your own photos!
# ============================================================================
# These are placeholder URLs - replace with paths to your local images
IMAGES = {
    'story_1': 'images/story_1.jpg',
    'story_2': 'images/story_2.jpg', 
    'story_3': 'images/story_3.jpg',
    'her_portrait': 'images/her_portrait.jpg',
    'us_final': 'images/us_final.jpg'
}

# Fallback placeholder images (will be used if local images don't exist)
PLACEHOLDER_IMAGES = {
    'story_1': 'https://placehold.co/600x600/FFE4EC/FF6B9D?text=📸+Our+Story+1',
    'story_2': 'https://placehold.co/600x600/FFD1DC/E75480?text=💕+Our+Story+2',
    'story_3': 'https://placehold.co/600x600/FFF0F5/FF6B9D?text=💖+Our+Story+3',
    'her_portrait': 'https://placehold.co/400x500/FFE4EC/FF6B9D?text=👸+Her+Portrait',
    'us_final': 'https://placehold.co/800x450/FFF0F5/E75480?text=💑+Us+Together'
}

def get_image(key):
    """Get image path, falling back to placeholder if local file doesn't exist"""
    local_path = IMAGES[key]
    if os.path.exists(local_path):
        return local_path
    return PLACEHOLDER_IMAGES[key]

# ============================================================================
# ROMANTIC CONTENT
# ============================================================================
STORY_CONTENT = [
    {
        'image': 'story_1',
        'title': '✨ Where It All Began...',
        'text': '''
        From the moment our paths crossed, something magical sparked between us.
        Every glance, every smile, every moment felt like destiny unfolding.
        '''
    },
    {
        'image': 'story_2', 
        'title': '💕 Growing Together...',
        'text': '''
        Through laughter and tears, through sunny days and stormy nights,
        we've grown stronger together. Every challenge became an adventure
        because I had you by my side.
        '''
    },
    {
        'image': 'story_3',
        'title': '💖 Building Our Dreams...',
        'text': '''
        With you, ordinary moments become extraordinary memories.
        You've taught me what true love means, and I fall deeper
        for you with every passing day.
        '''
    }
]

LOVE_QUOTES = [
    "Every love story is beautiful, but ours is my favorite.",
    "You are my today, all my tomorrows, and everything in between.",
    "In you, I've found my forever.",
    "Forever sounds perfect only because it's with you.",
]

# ============================================================================
# STATE 0: PASSWORD PROTECTION
# ============================================================================
def show_password_screen():
    st.markdown("""
        <div class="romantic-container">
            <h1 style="font-family: Georgia, serif; color: #E75480; text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">
                <span class="floating-heart">💕</span> A Special Message <span class="floating-heart">💕</span>
            </h1>
            <p style="font-family: Georgia, serif; color: #E75480; text-align: center; font-size: 1.3rem; font-style: italic; margin-bottom: 2rem;">This is for someone very special...</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="romantic-container" style="text-align: center;">
                <p class="story-text">Select the secret date to unlock something magical... 🔐</p>
                <p style="color: #E75480; font-family: Georgia, serif; font-style: italic; margin-top: 1rem;">💡 Hint: The date on which we first met</p>
            </div>
        """, unsafe_allow_html=True)
        
        import datetime
        selected_date = st.date_input(
            "Select the special date",
            value=datetime.date(2026, 1, 1),
            min_value=datetime.date(2020, 1, 1),
            max_value=datetime.date(2030, 12, 31),
            format="DD/MM/YYYY",
            label_visibility="collapsed"
        )
        
        if st.button("✨ Unlock the Magic ✨", use_container_width=True):
            # Check if date is 02/01/2026 (2nd January 2026)
            if selected_date == datetime.date(2026, 1, 2):
                st.session_state.state = 1
                st.rerun()
            else:
                st.error("💔 That's not the right date... Try again, my love!")

# ============================================================================
# STATE 1: STORY MONTAGE
# ============================================================================
def show_story_montage():
    current_story = STORY_CONTENT[st.session_state.story_page]
    
    # Progress dots
    dots = ""
    for i in range(3):
        active = "active" if i == st.session_state.story_page else ""
        dots += f'<span class="dot {active}"></span>'
    st.markdown(f'<div class="progress-dots">{dots}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="romantic-container">
            <h2 style="font-family: Georgia, serif; color: #E75480; text-align: center; font-size: 1.8rem;">{current_story['title']}</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Full width image for better landscape display
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.image(get_image(current_story['image']), use_container_width=True)
    
    st.markdown(f"""
        <div class="romantic-container">
            <p class="story-text" style="text-align: center;">{current_story['text']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.session_state.story_page < 2:
            if st.button("Continue Our Journey 💕 →", use_container_width=True):
                st.session_state.story_page += 1
                st.rerun()
        else:
            if st.button("See Something Special 💖 →", use_container_width=True):
                st.session_state.state = 2
                st.rerun()

# ============================================================================
# STATE 2: HER SPOTLIGHT
# ============================================================================
def show_her_spotlight():
    st.markdown("""
        <div class="romantic-container">
            <h1 style="font-family: Georgia, serif; color: #E75480; text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">
                <span class="floating-heart">👸</span> You <span class="floating-heart">👸</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(get_image('her_portrait'), use_container_width=True)
    
    st.markdown("""
        <div class="love-quote">
            "You make my world beautiful just by being in it. 
            Your smile lights up my darkest days, 
            and your love makes everything worthwhile."
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="romantic-container">
            <p class="story-text">
                From your infectious laughter to your caring heart,
                from your dreams to your quirks - I love every single part of you.
                You're not just my girlfriend, you're my best friend, my confidant,
                and the person I want to share every moment with.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("I Have Something to Ask You... 💕", use_container_width=True):
            st.session_state.state = 3
            st.rerun()

# ============================================================================
# STATE 3: THE PROPOSAL WITH MOVING "NO" BUTTON
# ============================================================================
def show_the_ask():
    st.markdown("""
        <div class="romantic-container">
            <h1 style="font-family: Georgia, serif; color: #E75480; text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">
                <span class="floating-heart">💖</span> The Question <span class="floating-heart">💖</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(get_image('her_portrait'), use_container_width=True)
    
    st.markdown("""
        <div class="love-quote" style="font-size: 1.8rem;">
            "Will you be my Valentine? 💕"
        </div>
    """, unsafe_allow_html=True)
    
    # Custom HTML/JS for the moving "No" button with fallback
    st.components.v1.html("""
    <style>
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 30px;
            padding: 30px;
            min-height: 120px;
            position: relative;
        }
        
        .yes-btn {
            background: linear-gradient(135deg, #FF6B9D 0%, #E75480 100%);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 18px 50px;
            font-size: 1.4rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(255, 107, 157, 0.4);
            transition: all 0.3s ease;
            font-family: 'Georgia', serif;
        }
        
        .yes-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 30px rgba(255, 107, 157, 0.6);
        }
        
        .no-btn {
            background: linear-gradient(135deg, #ccc 0%, #999 100%);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 18px 50px;
            font-size: 1.4rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.2s ease;
            font-family: 'Georgia', serif;
            position: absolute;
        }
        
        .message {
            text-align: center;
            font-family: 'Georgia', serif;
            color: #E75480;
            font-size: 1rem;
            margin-top: 20px;
            font-style: italic;
        }
    </style>
    
    <div class="button-container" id="container">
        <button class="yes-btn" onclick="sayYes()">💕 Yes! 💕</button>
        <button class="no-btn" id="noBtn" onmouseover="moveButton()" onclick="moveButton()">No</button>
    </div>
    <p class="message" id="message"></p>
    
    <script>
        const container = document.getElementById('container');
        const noBtn = document.getElementById('noBtn');
        const message = document.getElementById('message');
        
        const messages = [
            "Nice try! 😜",
            "Are you sure? 🥺",
            "Think again! 💕",
            "You can't escape love! 💖",
            "Just say yes! 😍",
            "Come on... 🌹",
            "Really? 💔",
            "One more time? 💗"
        ];
        
        let msgIndex = 0;
        
        function moveButton() {
            const containerRect = container.getBoundingClientRect();
            const btnRect = noBtn.getBoundingClientRect();
            
            // Calculate random position within the container
            const maxX = containerRect.width - btnRect.width - 20;
            const maxY = 100;
            
            const randomX = Math.random() * maxX;
            const randomY = Math.random() * maxY - 50;
            
            noBtn.style.transform = `translate(${randomX - containerRect.width/2 + 100}px, ${randomY}px)`;
            
            message.textContent = messages[msgIndex % messages.length];
            msgIndex++;
        }
        
        function sayYes() {
            document.body.innerHTML = `
                <div style="text-align: center; padding: 50px; font-family: Georgia, serif; background: linear-gradient(135deg, #FFE4EC 0%, #FFF0F5 100%); min-height: 200px;">
                    <h1 style="color: #E75480; font-size: 3rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">💕 YAY! 💕</h1>
                    <p style="color: #E75480; font-size: 2rem;">🎉🎉🎉</p>
                </div>
            `;
        }
    </script>
    """, height=200)
    
    # Fallback button for celebration
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎉 She Said YES! Celebrate! 🎉", use_container_width=True):
            st.session_state.state = 4
            st.rerun()
# ============================================================================
# STATE 4: CELEBRATION
# ============================================================================
def show_celebration():
    import glob
    import random
    import time
    
    # Initialize slideshow states
    if 'image_index' not in st.session_state:
        st.session_state.image_index = 0
    if 'video_index' not in st.session_state:
        st.session_state.video_index = 0
    if 'celebration_shown' not in st.session_state:
        st.session_state.celebration_shown = False
    
    # Trigger balloons on first load!
    if not st.session_state.celebration_shown:
        st.balloons()
        st.session_state.celebration_shown = True
    
    # Get gallery files
    image_files = sorted(glob.glob("gallery/images/*.*"))
    video_files = sorted(glob.glob("gallery/videos/*.*"))
    
    # Header
    st.markdown("""
        <div class="romantic-container" style="background: linear-gradient(135deg, #FFE4EC 0%, #FFF0F5 100%);">
            <h1 style="font-family: Georgia, serif; color: #E75480; text-align: center; font-size: 2.5rem; animation: pulse 2s ease-in-out infinite;">
                🎉💕 She Said YES! 💕🎉
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    quote = random.choice(LOVE_QUOTES)
    st.markdown(f"""
        <div class="love-quote" style="font-size: 1.4rem;">
            "{quote}"
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="romantic-container">
            <h2 style="text-align: center; color: #E75480; font-family: Georgia, serif;">
                💕 Happy Valentine's Day, My Love! 💕
            </h2>
            <p style="font-family: Georgia, serif; color: #8B4B6A; font-size: 1.2rem; line-height: 1.8; text-align: center; padding: 1rem;">
                Thank you for being the most amazing person in my life.
                I promise to love you, cherish you, and make you smile
                every single day of our forever together.
            </p>
            <p style="font-family: Georgia, serif; font-size: 1.3rem; color: #E75480; font-weight: bold; text-align: center;">
                I love you more than words could ever express. 
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # ========== MEDIA GALLERY SECTION ==========
    st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <h2 style="font-family: Georgia, serif; color: #E75480; font-size: 2rem;">
                📸 Our Beautiful Memories 🎬
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Two column layout
    col_images, col_videos = st.columns(2)
    
    with col_images:
        st.markdown("""
            <div style="text-align: center; padding: 0.5rem;">
                <h3 style="font-family: Georgia, serif; color: #E75480; font-size: 1.3rem;">📸 Photos</h3>
            </div>
        """, unsafe_allow_html=True)
        
        if image_files:
            # Convert images to base64 for JavaScript slideshow
            import base64
            image_data_list = []
            for img_path in image_files:
                with open(img_path, "rb") as f:
                    img_bytes = f.read()
                ext = img_path.split('.')[-1].lower()
                mime = f"image/{ext}" if ext != 'jpg' else "image/jpeg"
                img_b64 = base64.b64encode(img_bytes).decode()
                image_data_list.append(f"data:{mime};base64,{img_b64}")
            
            # Create JavaScript slideshow with fade effect
            images_js = str(image_data_list).replace("'", '"')
            
            slideshow_html = f"""
            <style>
                .slideshow-container {{
                    position: relative;
                    width: 100%;
                    background: linear-gradient(135deg, #FFE4EC 0%, #FFF0F5 100%);
                    border-radius: 20px;
                    padding: 10px;
                    border: 2px solid #FFB6C1;
                    box-shadow: 0 8px 25px rgba(255, 107, 157, 0.2);
                }}
                .slide-image {{
                    width: 100%;
                    border-radius: 15px;
                    transition: opacity 0.8s ease-in-out;
                }}
                .slide-counter {{
                    text-align: center;
                    color: #E75480;
                    font-family: Georgia, serif;
                    padding: 10px;
                }}
                .nav-buttons {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    padding: 10px;
                }}
                .nav-btn {{
                    background: linear-gradient(135deg, #FF6B9D 0%, #E75480 100%);
                    color: white;
                    border: none;
                    border-radius: 50%;
                    width: 40px;
                    height: 40px;
                    font-size: 18px;
                    cursor: pointer;
                    transition: transform 0.2s;
                }}
                .nav-btn:hover {{
                    transform: scale(1.1);
                }}
            </style>
            
            <div class="slideshow-container">
                <img id="slideImg" class="slide-image" src="{image_data_list[0]}" alt="Photo">
                <div class="slide-counter">
                    <span id="imgCounter">1</span> / {len(image_files)}
                </div>
                <div class="nav-buttons">
                    <button class="nav-btn" onclick="prevSlide()">◀</button>
                    <button class="nav-btn" onclick="nextSlide()">▶</button>
                </div>
            </div>
            
            <script>
                const images = {images_js};
                let currentIndex = 0;
                const totalImages = images.length;
                
                function showSlide(index) {{
                    const img = document.getElementById('slideImg');
                    img.style.opacity = 0;
                    setTimeout(() => {{
                        img.src = images[index];
                        img.style.opacity = 1;
                        document.getElementById('imgCounter').textContent = index + 1;
                    }}, 400);
                }}
                
                function nextSlide() {{
                    currentIndex = (currentIndex + 1) % totalImages;
                    showSlide(currentIndex);
                }}
                
                function prevSlide() {{
                    currentIndex = (currentIndex - 1 + totalImages) % totalImages;
                    showSlide(currentIndex);
                }}
                
                // Auto-advance every 4 seconds
                setInterval(nextSlide, 4000);
            </script>
            """
            
            st.components.v1.html(slideshow_html, height=500)
        else:
            st.markdown("""
                <div style="background: #FFE4EC; border-radius: 20px; padding: 2rem; text-align: center; border: 2px solid #FFB6C1;">
                    <p style="color: #E75480; font-family: Georgia, serif;">
                        📸 Add photos to<br><code>gallery/images/</code>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    with col_videos:
        st.markdown("""
            <div style="text-align: center; padding: 0.5rem;">
                <h3 style="font-family: Georgia, serif; color: #E75480; font-size: 1.3rem;">🎬 Videos</h3>
            </div>
        """, unsafe_allow_html=True)
        
        if video_files:
            # Convert videos to base64 for JavaScript slideshow
            import base64
            video_data_list = []
            for vid_path in video_files:
                with open(vid_path, "rb") as f:
                    vid_bytes = f.read()
                ext = vid_path.split('.')[-1].lower()
                mime = f"video/{ext}"
                vid_b64 = base64.b64encode(vid_bytes).decode()
                video_data_list.append(f"data:{mime};base64,{vid_b64}")
            
            videos_js = str(video_data_list).replace("'", '"')
            
            video_html = f"""
            <style>
                .video-container {{
                    background: linear-gradient(135deg, #FFE4EC 0%, #FFF0F5 100%);
                    border-radius: 20px;
                    padding: 10px;
                    border: 2px solid #FFB6C1;
                    box-shadow: 0 8px 25px rgba(255, 107, 157, 0.2);
                }}
                .slide-video {{
                    width: 100%;
                    border-radius: 15px;
                    transition: opacity 0.5s ease-in-out;
                }}
                .vid-counter {{
                    text-align: center;
                    color: #E75480;
                    font-family: Georgia, serif;
                    padding: 10px;
                }}
                .vid-nav-buttons {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    padding: 10px;
                }}
                .vid-nav-btn {{
                    background: linear-gradient(135deg, #FF6B9D 0%, #E75480 100%);
                    color: white;
                    border: none;
                    border-radius: 50%;
                    width: 40px;
                    height: 40px;
                    font-size: 18px;
                    cursor: pointer;
                    transition: transform 0.2s;
                }}
                .vid-nav-btn:hover {{
                    transform: scale(1.1);
                }}
            </style>
            
            <div class="video-container">
                <video id="slideVid" class="slide-video" src="{video_data_list[0]}" autoplay muted></video>
                <div class="vid-counter">
                    <span id="vidCounter">1</span> / {len(video_files)}
                </div>
                <div class="vid-nav-buttons">
                    <button class="vid-nav-btn" onclick="prevVid()">◀</button>
                    <button class="vid-nav-btn" onclick="nextVid()">▶</button>
                </div>
            </div>
            
            <script>
                const videos = {videos_js};
                let vidIndex = 0;
                const totalVids = videos.length;
                const vid = document.getElementById('slideVid');
                
                function showVid(index) {{
                    vid.style.opacity = 0;
                    setTimeout(() => {{
                        vid.src = videos[index];
                        vid.style.opacity = 1;
                        vid.play();
                        document.getElementById('vidCounter').textContent = index + 1;
                    }}, 300);
                }}
                
                function nextVid() {{
                    vidIndex = (vidIndex + 1) % totalVids;
                    showVid(vidIndex);
                }}
                
                function prevVid() {{
                    vidIndex = (vidIndex - 1 + totalVids) % totalVids;
                    showVid(vidIndex);
                }}
                
                // Auto-advance when video ends
                vid.addEventListener('ended', function() {{
                    nextVid();
                }});
            </script>
            """
            
            st.components.v1.html(video_html, height=500)
        else:
            st.markdown("""
                <div style="background: #FFE4EC; border-radius: 20px; padding: 2rem; text-align: center; border: 2px solid #FFB6C1;">
                    <p style="color: #E75480; font-family: Georgia, serif;">
                        🎬 Add videos to<br><code>gallery/videos/</code>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    



    # Footer hearts
    st.markdown("""
        <p style="text-align: center; font-size: 3rem; margin-top: 2rem;">
            💕💖🌹❤️🌹💖💕
        </p>
    """, unsafe_allow_html=True)
    
    # Continuous hearts effect (stops after some time)
    st.components.v1.html("""
    <style>
        .hearts-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 9999;
        }
        
        .heart {
            position: absolute;
            font-size: 20px;
            animation: fall linear forwards;
            opacity: 0.8;
        }
        
        @keyframes fall {
            0% {
                transform: translateY(-100px) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) rotate(360deg);
                opacity: 0;
            }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
    </style>
    
    <div class="hearts-container" id="hearts"></div>
    
    <script>
        const hearts = ['💕', '💖', '💗', '💓', '❤️', '🌹', '💐'];
        const container = document.getElementById('hearts');
        let heartCount = 0;
        const maxHearts = 50; // Stop after 50 hearts
        
        function createHeart() {
            if (heartCount >= maxHearts) return;
            
            const heart = document.createElement('span');
            heart.className = 'heart';
            heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
            heart.style.left = Math.random() * 100 + '%';
            heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
            heart.style.fontSize = (Math.random() * 15 + 15) + 'px';
            container.appendChild(heart);
            heartCount++;
            
            setTimeout(() => heart.remove(), 7000);
        }
        
        // Create hearts for 10 seconds then stop
        const interval = setInterval(createHeart, 200);
        setTimeout(() => clearInterval(interval), 10000);
    </script>
    """, height=0)


# ============================================================================
# BACKGROUND MUSIC PLAYER
# ============================================================================
def play_background_music():
    """
    Plays background music (Gone Gone Gone) in a low tone.
    Place 'gone_gone_gone.mp3' in the root folder of the app.
    """
    music_file = "gone_gone_gone.mp3"
    
    if os.path.exists(music_file):
        # Use local file
        import base64
        with open(music_file, "rb") as f:
            audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_src = f"data:audio/mp3;base64,{audio_base64}"
    else:
        # Fallback message - no audio available
        audio_src = None
    
    if audio_src:
        st.components.v1.html(f"""
        <audio id="bgMusic" autoplay loop style="display: none;">
            <source src="{audio_src}" type="audio/mpeg">
        </audio>
        <script>
            // Set volume to low (0.2 = 20% volume)
            var audio = document.getElementById('bgMusic');
            if (audio) {{
                audio.volume = 0.2;
                // Try to play (may need user interaction first)
                audio.play().catch(function(e) {{
                    console.log('Autoplay prevented, music will play on interaction');
                }});
            }}
        </script>
        """, height=0)

# ============================================================================
# MAIN APP LOGIC
# ============================================================================
def main():
    if st.session_state.state == 0:
        show_password_screen()
    elif st.session_state.state == 1:
        play_background_music()  # Start music after unlocking
        show_story_montage()
    elif st.session_state.state == 2:
        play_background_music()
        show_her_spotlight()
    elif st.session_state.state == 3:
        play_background_music()
        show_the_ask()
    elif st.session_state.state == 4:
        play_background_music()
        show_celebration()

if __name__ == "__main__":
    main()

