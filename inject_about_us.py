import os
import re

file_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\about-us.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the first massive Elementor Container which holds "About Us", "What We Do"
# In original Techflow, it starts with id 4efff48 and ends before 9952d93 ("Our Corporate Values")
start_idx = content.find('<div class="elementor-element elementor-element-4efff48')
if start_idx != -1:
    end_idx = content.find('<div class="elementor-element elementor-element-9952d93', start_idx)
    if end_idx != -1:
        new_about_us = """<section class="about-hero-section">
    <div class="about-hero-bg"></div>
    <div class="about-container">
        
        <!-- Header Section -->
        <div class="about-header text-center">
            <h1 class="main-title">About <span class="highlight">Us</span></h1>
            <p class="subtitle">Cloudiva.ai – Delivering the Promise of AI in the Cloud</p>
        </div>

        <div class="about-grid">
            <!-- Left Column: Text Content -->
            <div class="about-text-content">
                
                <div class="content-block glass-panel">
                    <h2>Who We Are</h2>
                    <p>At <strong>Cloudiva.ai</strong>, we believe the future isn't just in the cloud — it's <strong>intelligent, agile, and profoundly transformative</strong>. Born at the intersection of advanced artificial intelligence and cloud-native architecture, Cloudiva.ai empowers organizations to unlock the full value of their data through scalable, secure, and automated AI-Forward solutions.</p>
                </div>

                <div class="content-block glass-panel">
                    <h2>What We Do</h2>
                    <p>We are not just migrating workloads — we're elevating intelligence. Whether it's predictive analytics, intelligent automation, or generative AI applications, we help businesses reimagine operations and customer experiences using the best of modern cloud platforms.</p>
                </div>

                <div class="content-block glass-panel featured-block">
                    <h2>Our Philosophy</h2>
                    <p>With deep cloud engineering expertise and innovative AI models, Cloudiva.ai delivers <strong>faster insights, smarter systems, and a future-ready foundation</strong> — bringing the true promise of AI in the cloud to life.</p>
                </div>

                <div class="welcome-message">
                    <h3>Welcome to Cloudiva.ai.</h3>
                    <p class="tagline">Where the future learns, scales, and evolves — on the cloud.</p>
                </div>
            </div>

            <!-- Right Column: Visual/Stats/Image -->
            <div class="about-visual-content">
                <div class="visual-wrapper">
                    <!-- We can keep the existing image or use a stylized wrapper -->
                    <div class="image-glow"></div>
                    <img src="assets/883ed91b_AI-in-the-Cloud-927x1024.png" alt="AI in the Cloud" class="hero-image">
                    
                    <!-- Floating stats cards for visual interest -->
                    <div class="floating-stat float-1">
                        <span class="stat-number">AI</span>
                        <span class="stat-label">Forward</span>
                    </div>
                    <div class="floating-stat float-2">
                        <span class="stat-number">Cloud</span>
                        <span class="stat-label">Native</span>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</section>

<style>
.about-hero-section {
    background: radial-gradient(circle at top right, #0A192F 0%, #02040A 100%);
    position: relative;
    padding: 120px 20px 100px;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif; /* Setup generic fallback that looks clean */
    overflow: hidden;
}

.about-hero-bg {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        radial-gradient(1.5px 1.5px at 100px 50px, rgba(255,255,255,0.15), transparent),
        radial-gradient(2px 2px at 400px 150px, rgba(51, 161, 253, 0.2), transparent),
        radial-gradient(1px 1px at 800px 300px, rgba(255,255,255,0.1), transparent),
        radial-gradient(2.5px 2.5px at 1200px 600px, rgba(51, 161, 253, 0.15), transparent);
    background-size: 100% 100%;
    opacity: 0.8;
    z-index: 0;
}

.about-container {
    max-width: 1280px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

.text-center { text-align: center; }

.main-title {
    font-size: 4rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 15px;
    letter-spacing: -1px;
}

.main-title .highlight {
    color: #33a1fd;
    position: relative;
}

.subtitle {
    font-size: 1.4rem;
    color: #94a3b8;
    font-weight: 300;
    max-width: 700px;
    margin: 0 auto 80px;
    line-height: 1.6;
}

.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.about-text-content {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.glass-panel {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(51, 161, 253, 0.15);
    border-radius: 16px;
    padding: 35px 40px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.05), 0 10px 30px rgba(0,0,0,0.3);
    transition: transform 0.3s ease, border-color 0.3s ease;
}

.glass-panel:hover {
    transform: translateX(10px);
    border-color: rgba(51, 161, 253, 0.4);
}

.featured-block {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(11, 29, 58, 0.9) 100%);
    border-left: 4px solid #33a1fd;
}

.glass-panel h2 {
    font-size: 1.6rem;
    color: #ffffff;
    font-weight: 600;
    margin-bottom: 15px;
}

.glass-panel p {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #cbd5e1;
    margin: 0;
}

.glass-panel p strong {
    color: #ffffff;
    font-weight: 600;
}

.welcome-message {
    margin-top: 20px;
    padding-left: 20px;
    border-left: 2px solid rgba(51, 161, 253, 0.3);
}

.welcome-message h3 {
    font-size: 1.8rem;
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 10px;
}

.welcome-message .tagline {
    font-size: 1.2rem;
    color: #33a1fd;
    font-weight: 500;
}

/* Right Column Visuals */
.visual-wrapper {
    position: relative;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.image-glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80%;
    height: 80%;
    background: radial-gradient(circle, rgba(51,161,253,0.15) 0%, rgba(0,0,0,0) 70%);
    filter: blur(40px);
    z-index: 0;
    border-radius: 50%;
}

.hero-image {
    position: relative;
    z-index: 1;
    max-width: 100%;
    height: auto;
    border-radius: 20px;
    animation: float 6s ease-in-out infinite;
}

.floating-stat {
    position: absolute;
    background: rgba(10, 25, 47, 0.8);
    border: 1px solid rgba(51, 161, 253, 0.3);
    padding: 15px 25px;
    border-radius: 12px;
    backdrop-filter: blur(8px);
    z-index: 3;
    box-shadow: 0 15px 30px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.float-1 {
    top: 10%;
    left: 0;
    animation: float 5s ease-in-out infinite alternate;
}

.float-2 {
    bottom: 20%;
    right: 0;
    animation: float 7s ease-in-out infinite alternate-reverse;
}

.stat-number {
    font-size: 1.5rem;
    font-weight: 700;
    color: #33a1fd;
}

.stat-label {
    font-size: 0.85rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 5px;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
    100% { transform: translateY(0px); }
}

@media (max-width: 1024px) {
    .about-grid { grid-template-columns: 1fr; gap: 50px; }
    .glass-panel:hover { transform: translateY(-5px); }
    .visual-wrapper { max-width: 600px; margin: 0 auto; }
}

@media (max-width: 768px) {
    .main-title { font-size: 3rem; }
    .subtitle { font-size: 1.1rem; }
    .glass-panel { padding: 25px; }
}
</style>
"""
        content = content[:start_idx] + new_about_us + content[end_idx:]
        print("Successfully injected About Us section.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
