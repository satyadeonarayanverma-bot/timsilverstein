import os

index_path = r'c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html'
about_path = r'c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\about-us.html'

with open(index_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find the end of <header>
header_end_idx = text.find('</header>') + len('</header>')

# Find the end of the body content / start of the JS bundles
js_bundle_idx = text.find('<script type="speculationrules">')

header_part = text[:header_end_idx]
footer_part = text[js_bundle_idx:]

# Ensure the body background is dark
# We will inject a custom main container
custom_content = """
<style>
/* CLOUDIVA.AI PREMIUM MODERN CSS */

:root {
  --primary-blue: #33a1fd;
  --bg-deep: #02040A;
  --bg-slate: #0A192F;
  --glass-bg: rgba(15, 23, 42, 0.6);
  --glass-border: rgba(51, 161, 253, 0.15);
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
}

body {
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

.about-page-wrapper {
  background: radial-gradient(circle at top right, #0A192F 0%, #02040A 100%);
  position: relative;
  overflow: hidden;
  padding-bottom: 150px;
}

/* Background Animated Glows */
.about-page-wrapper::before {
  content: '';
  position: absolute;
  top: -20%; left: -10%;
  width: 60%; height: 60%;
  background: radial-gradient(circle, rgba(51,161,253,0.15) 0%, transparent 60%);
  filter: blur(80px);
  z-index: 0;
  animation: pulse-glow 8s infinite alternate ease-in-out;
}
.about-page-wrapper::after {
  content: '';
  position: absolute;
  bottom: -10%; right: -10%;
  width: 50%; height: 50%;
  background: radial-gradient(circle, rgba(51,161,253,0.1) 0%, transparent 60%);
  filter: blur(80px);
  z-index: 0;
}

@keyframes pulse-glow {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.1); opacity: 1; }
}

.about-container {
  max-width: 1300px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  padding: 0 40px;
}

/* Hero Section */
.about-hero {
  padding: 180px 0 100px;
  text-align: center;
}
.about-hero h1 {
  font-size: 5rem;
  font-weight: 800;
  letter-spacing: -2px;
  margin-bottom: 20px;
  background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.about-hero h1 span {
  color: var(--primary-blue);
  background: none;
  -webkit-text-fill-color: var(--primary-blue);
}
.about-hero p.lead {
  font-size: 1.4rem;
  font-weight: 300;
  color: var(--text-muted);
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

/* Grid Layout container */
.about-grid {
  display: flex;
  flex-direction: column;
  gap: 80px;
  margin-top: 50px;
}

/* Row Style */
.about-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: stretch;
}
.about-row.reverse {
  direction: rtl;
}
.about-row.reverse > * {
  direction: ltr; /* keep text left to right inside */
}

/* Glassmorphism Cards */
.glass-card {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  padding: 50px;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.02), 0 20px 40px rgba(0,0,0,0.4);
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), border-color 0.4s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.glass-card:hover {
  transform: translateY(-10px);
  border-color: rgba(51, 161, 253, 0.5);
  box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.05), 0 30px 60px rgba(0,0,0,0.6);
}

.glass-card .icon-wrapper {
  width: 60px;
  height: 60px;
  background: rgba(51, 161, 253, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 25px;
  border: 1px solid rgba(51, 161, 253, 0.2);
}
.glass-card .icon-wrapper svg {
  width: 30px;
  height: 30px;
  stroke: var(--primary-blue);
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.glass-card h2 {
  font-size: 2.2rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}

.glass-card p {
  font-size: 1.15rem;
  line-height: 1.8;
  color: #cbd5e1;
  margin-bottom: 15px;
}
.glass-card p:last-child {
  margin-bottom: 0;
}

/* Visual Feature Graphic container */
.visual-feature {
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  min-height: 400px;
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(11, 29, 58, 0.9) 100%);
  border: 1px solid rgba(51, 161, 253, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}
.visual-feature::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: 
      linear-gradient(rgba(51, 161, 253, 0.1) 1px, transparent 1px),
      linear-gradient(90deg, rgba(51, 161, 253, 0.1) 1px, transparent 1px);
  background-size: 30px 30px;
  opacity: 0.3;
  transform: perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px);
  animation: grid-move 20s linear infinite;
}
@keyframes grid-move {
  0% { transform: perspective(500px) rotateX(60deg) translateY(0) translateZ(-200px); }
  100% { transform: perspective(500px) rotateX(60deg) translateY(60px) translateZ(-200px); }
}

/* Floating Stats in Visuals */
.floating-badge {
  position: absolute;
  background: rgba(2, 4, 10, 0.8);
  border: 1px solid rgba(51, 161, 253, 0.4);
  backdrop-filter: blur(10px);
  padding: 15px 25px;
  border-radius: 12px;
  color: #fff;
  font-weight: 600;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  gap: 10px;
}
.floating-badge.b1 { top: 20%; left: 10%; animation: float 6s ease-in-out infinite; }
.floating-badge.b2 { bottom: 20%; right: 10%; animation: float 6s ease-in-out infinite alternate-reverse; }
.badge-highlight { color: var(--primary-blue); font-size: 1.2rem; }

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-15px); }
  100% { transform: translateY(0px); }
}

@media (max-width: 1024px) {
  .about-row {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .visual-feature {
    display: none; /* Hide abstract visuals on mobile to focus on content */
  }
}
@media (max-width: 768px) {
  .about-hero h1 { font-size: 3.5rem; }
  .about-hero { padding: 140px 0 60px; }
  .glass-card { padding: 30px; }
  .glass-card h2 { font-size: 1.8rem; }
}

</style>

<main class="about-page-wrapper">
  <div class="about-container">
    
    <div class="about-hero">
      <h1>About <span>Cloudiva.ai</span></h1>
      <p class="lead">Delivering the Promise of AI in the Cloud</p>
    </div>

    <div class="about-grid">
      
      <!-- Row 1: Who We Are -->
      <div class="about-row">
        <div class="glass-card">
          <div class="icon-wrapper">
            <svg viewBox="0 0 24 24">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
            </svg>
          </div>
          <h2>Who We Are</h2>
          <p><strong>Cloudiva.ai</strong> is an AI-Forward cloud consulting and platform engineering company focused on helping organizations transform how they build, modernize, and operate technology. We combine deep cloud architecture expertise with intelligent automation and modern engineering practices to design scalable digital platforms that enable real business outcomes.</p>
          <p>Our approach goes beyond traditional migration or infrastructure delivery. We partner with enterprises to create secure, resilient, and future-ready cloud environments that accelerate innovation while maintaining governance and operational excellence.</p>
        </div>
        
        <div class="visual-feature">
          <div class="floating-badge b1"><span class="badge-highlight">AI</span> Forward</div>
          <div class="floating-badge b2"><span class="badge-highlight">Cloud</span> Native</div>
        </div>
      </div>

      <!-- Row 2: What We Do -->
      <div class="about-row reverse">
        <div class="glass-card">
          <div class="icon-wrapper">
            <svg viewBox="0 0 24 24">
              <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
            </svg>
          </div>
          <h2>What We Do</h2>
          <p>We help organizations move from legacy complexity to intelligent cloud ecosystems — delivering transformation across strategy, modernization, data foundations, and operations.</p>
          <p>From defining cloud roadmaps to building AI-ready platforms, our teams focus on practical execution, measurable value, and long-term sustainability.</p>
        </div>
        
        <div class="visual-feature" style="background: linear-gradient(135deg, rgba(11, 29, 58, 0.9) 0%, rgba(15, 23, 42, 0.8) 100%);">
           <div class="floating-badge b1" style="top: 40%; left: 30%;"><span class="badge-highlight">Intelligent</span> Ecosystems</div>
        </div>
      </div>

      <!-- Row 3: Our Philosophy -->
      <div class="about-row">
        <div class="glass-card">
          <div class="icon-wrapper">
            <svg viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            </svg>
          </div>
          <h2>Our Philosophy</h2>
          <p>Technology transformation should not be driven by trends — it should be guided by architecture, automation, and outcomes.</p>
          <p>At Cloudiva.ai, we believe in building platforms that evolve with your business, enabling teams to innovate faster while staying secure and cost-efficient.</p>
        </div>

        <div class="glass-card" style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(20, 35, 65, 0.95) 100%); border-left: 4px solid var(--primary-blue);">
          <div class="icon-wrapper">
            <svg viewBox="0 0 24 24">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            </svg>
          </div>
          <h2>Why Cloudiva.ai</h2>
          <p>We bring together cloud architects, engineers, and transformation specialists who understand both enterprise complexity and modern innovation.</p>
          <p>Our goal is simple — help organizations unlock the true potential of cloud and AI through thoughtful design, strong governance, and intelligent engineering.</p>
        </div>
      </div>

    </div>
  </div>
</main>
<div id="page" class="site">
"""

final_text = header_part + custom_content + '\n' + footer_part

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(final_text)

print('about-us.html successfully rebuilt with stunning professional design.')

