import os
import re

file_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Subtext
# Find: <p>Unburdened by Legacy Tools, <br>Processes, and Talent</p>
old_hero_subtext = "<p>Unburdened by Legacy Tools, <br>\n																			Processes, and Talent</p>"
new_hero_subtext = "<p>Modernize Platforms. Strengthen Security. Operate with Confidence.</p>"
# We might need a regex if spacing is weird
content = re.sub(
    r"<p>Unburdened by Legacy Tools, <br>\s*Processes.*and Talent</p>",
    new_hero_subtext,
    content
)

# 2. Overwrite the AI-Forward Cloud Services block with our dark 4-card layout
start_idx = content.find('<div class="elementor-element elementor-element-2b7c9a0')
if start_idx != -1:
    end_idx = content.find('<section class="why-choose-section">', start_idx)
    if end_idx != -1:
        new_cloud_services = """<section class="cloud-services-section">
    <div class="cs-container">
        <h2 class="cs-heading">Cloud Transformation <span class="highlight">Services</span></h2>
        <p class="cs-subheading">We help organizations move from legacy complexity to <strong>secure</strong>, modern cloud platforms through <strong>architecture-led strategy</strong>, <strong>structured migration</strong>, <strong>intelligent modernization</strong>, and <strong>continuous operations</strong>.</p>
        
        <div class="cs-grid">
            <!-- Advisory & Strategy -->
            <div class="cs-card">
                <div class="cs-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4m0 12v4M4.93 4.93l2.83 2.83m8.48 8.48l2.83 2.83M2 12h4m12 0h4M4.93 19.07l2.83-2.83m8.48-8.48l2.83-2.83"/></svg>
                </div>
                <h3>Advisory &amp; Strategy</h3>
                <ul class="cs-list">
                    <li><span>+</span> Cloud Advisory</li>
                    <li><span>+</span> Accelerated Assessments</li>
                    <li><span>+</span> Cloud Readiness Workshops</li>
                    <li><span>+</span> Cloud Governance</li>
                </ul>
            </div>

            <!-- Migrations -->
            <div class="cs-card">
                <div class="cs-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14m-7-7l7 7-7 7"/></svg>
                </div>
                <h3>Migrations</h3>
                <ul class="cs-list">
                    <li><span>+</span> Rapid, Fixed-Cost Migrations</li>
                    <li><span>+</span> VMware and DC exit</li>
                    <li><span>+</span> Database migrations</li>
                    <li><span>+</span> COTS App migrations</li>
                </ul>
            </div>

            <!-- Modernization -->
            <div class="cs-card">
                <div class="cs-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="2" x2="12" y2="22"/><path d="M2 12l10-10 10 10-10 10Z"/></svg>
                </div>
                <h3>Modernization</h3>
                <ul class="cs-list">
                    <li><span>+</span> Replatforming &amp; Refactoring</li>
                    <li><span>+</span> Containerization</li>
                    <li><span>+</span> Mainframe Modernization</li>
                    <li><span>+</span> Serverless Architecture</li>
                </ul>
            </div>

            <!-- Managed Services & Ops -->
            <div class="cs-card">
                <div class="cs-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                </div>
                <h3>Managed Services &amp; Ops</h3>
                <ul class="cs-list">
                    <li><span>+</span> Managed Cloud Operations</li>
                    <li><span>+</span> DevOps as a Service</li>
                    <li><span>+</span> Security Operations (SecOps)</li>
                    <li><span>+</span> FinOps &amp; Cost Optimization</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<style>
.cloud-services-section {
    background: #02040A; /* Dark theme to match */
    padding: 100px 20px;
    color: #fff;
    font-family: inherit;
    border-bottom: 1px solid rgba(51, 161, 253, 0.1);
}
.cs-container {
    max-width: 1200px;
    margin: 0 auto;
}
.cs-heading {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 20px;
    text-align: center;
    color: #ffffff;
}
.cs-heading .highlight {
    color: #33a1fd;
}
.cs-subheading {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 60px;
    font-size: 1.15rem;
    line-height: 1.6;
    color: #94a3b8;
}
.cs-subheading strong {
    color: #ffffff;
}
.cs-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
}
.cs-card {
    background: rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(51, 161, 253, 0.15);
    border-radius: 12px;
    padding: 35px 25px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
}
.cs-card:hover {
    transform: translateY(-5px);
    background: rgba(15, 23, 42, 0.7);
    border-color: rgba(51, 161, 253, 0.4);
    box-shadow: 0 15px 30px rgba(0,0,0,0.5), inset 0 0 15px rgba(51, 161, 253, 0.1);
}
.cs-icon {
    width: 50px; height: 50px;
    border-radius: 12px;
    background: rgba(51, 161, 253, 0.1);
    color: #33a1fd;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 25px;
}
.cs-icon svg {
    width: 24px; height: 24px;
}
.cs-card h3 {
    font-size: 1.4rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 20px;
}
.cs-list {
    list-style: none;
    padding: 0;
    margin: 0;
    flex-grow: 1;
}
.cs-list li {
    font-size: 0.95rem;
    color: #cbd5e1;
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    line-height: 1.5;
}
.cs-list li span {
    color: #33a1fd;
    font-weight: bold;
    margin-right: 10px;
    font-size: 1.1rem;
    line-height: 1;
}

@media (max-width: 1024px) {
    .cs-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
    .cs-heading { font-size: 2.2rem; }
    .cs-grid { grid-template-columns: 1fr; }
}
</style>
"""
        content = content[:start_idx] + new_cloud_services + content[end_idx:]
        print("Successfully reinjected Cloud Services block.")
    else:
        print("Failed to find end index")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
