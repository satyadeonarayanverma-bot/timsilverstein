import os
import re

file_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 2. Why Organizations Choose Section ---
# Overwrite the "Transforming Traditional Mindsets to AI-Forward Execution" block
start_idx = content.find('<div class="elementor-element elementor-element-14ee2ba')
if start_idx != -1:
    end_idx = content.find('<div class="elementor-element elementor-element-a654f97', start_idx)
    if end_idx != -1:
        new_why_choose = """<section class="why-choose-section">
    <div class="stars"></div>
    <div class="grid-floor"></div>
    <div class="why-container">
        <h2 class="why-heading">Why Organizations Choose <span class="highlight">Cloudiva.ai</span></h2>
        
        <div class="cards-grid">
            <!-- Card 1 -->
            <div class="glass-card">
                <div class="card-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                </div>
                <h3>Architecture First</h3>
                <p>We don't just migrate workloads — we design resilient, scalable foundations that align with enterprise architecture standards and long-term business goals.</p>
            </div>

            <!-- Card 2 -->
            <div class="glass-card">
                <div class="card-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                </div>
                <h3>Security by Design</h3>
                <p>Security and compliance are integrated directly into our infrastructure blueprints, ensuring governance is automated from day one, not bolted on later.</p>
            </div>

            <!-- Card 3 -->
            <div class="glass-card">
                <div class="card-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                </div>
                <h3>Intelligent Automation</h3>
                <p>We automate aggressively using Infrastructure as Code (IaC) and DevSecOps pipelines, accelerating delivery while eliminating manual errors and drift.</p>
            </div>

            <!-- Card 4 -->
            <div class="glass-card">
                <div class="card-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                </div>
                <h3>Execution Focused</h3>
                <p>We prioritize practical implementations over theory. Our engineers are hyper-focused on delivering tangible outcomes that improve platform velocity.</p>
            </div>
        </div>
    </div>
</section>

<style>
.why-choose-section {
    background: radial-gradient(circle at top, #060B19 0%, #02040A 100%);
    position: relative;
    padding: 100px 20px 80px;
    color: #fff;
    overflow: hidden;
    font-family: inherit;
}
.stars {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
      radial-gradient(1px 1px at 40px 60px, #ffffff, rgba(0,0,0,0)),
      radial-gradient(1.5px 1.5px at 150px 140px, #e2e8f0, rgba(0,0,0,0)),
      radial-gradient(2px 2px at 300px 80px, #cbd5e1, rgba(0,0,0,0)),
      radial-gradient(1px 1px at 450px 220px, #ffffff, rgba(0,0,0,0)),
      radial-gradient(1.5px 1.5px at 100px 300px, #94a3b8, rgba(0,0,0,0));
    background-repeat: repeat;
    background-size: 600px 600px;
    opacity: 0.5;
}
.grid-floor {
    position: absolute;
    left: 0; right: 0; bottom: -50px;
    height: 200px;
    background: linear-gradient(to top, rgba(51, 161, 253, 0.2), transparent);
    background-size: 50px 50px;
    background-image:
      linear-gradient(to right, rgba(51, 161, 253, 0.1) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(51, 161, 253, 0.1) 1px, transparent 1px);
    transform: perspective(300px) rotateX(70deg);
    pointer-events: none;
}
.why-container {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
    text-align: center;
}
.why-heading {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 60px;
    color: #ffffff;
}
.why-heading .highlight {
    color: #33a1fd;
}
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    text-align: left;
}
.glass-card {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(51, 161, 253, 0.2);
    border-radius: 12px;
    padding: 40px 30px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.05), 0 15px 30px rgba(0,0,0,0.6);
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}
.glass-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(51, 161, 253, 0.8), transparent);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.glass-card:hover {
    transform: translateY(-8px);
    border-color: rgba(51, 161, 253, 0.5);
    box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.15), 0 20px 40px rgba(0,0,0,0.8);
}
.glass-card:hover::before {
    opacity: 1;
}
.card-icon {
    width: 50px; height: 50px;
    border-radius: 12px;
    background: rgba(51, 161, 253, 0.1);
    border: 1px solid rgba(51, 161, 253, 0.2);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 25px;
    color: #33a1fd;
}
.card-icon svg {
    width: 24px; height: 24px;
}
.glass-card h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 15px;
}
.glass-card p {
    font-size: 1rem;
    line-height: 1.6;
    color: #94a3b8;
    margin: 0;
}
@media (max-width: 768px) {
    .why-heading { font-size: 2.2rem; }
    .cards-grid { grid-template-columns: 1fr; }
}
</style>
"""
        content = content[:start_idx] + new_why_choose + content[end_idx:]
        print("Successfully injected Why Choose section.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
