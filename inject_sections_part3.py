import os
import re

file_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 3. Security-Driven Cloud Innovation Section ---
# This was inserted right before the "Industries" section (elementor-element-a654f97)
start_idx = content.find('<div class="elementor-element elementor-element-a654f97')
if start_idx != -1:
    new_security_section = """<section class="security-cloud-section">
    <div class="security-container">
        <h2 class="security-heading">Security-Driven Cloud <span class="highlight">Innovation</span></h2>
        
        <div class="security-grid">
            <!-- Main Featured Card (Left) -->
            <div class="security-card featured-card">
                <div class="card-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
                </div>
                <h3>Enterprise Grade Security</h3>
                <p>We bake security into every layer of our cloud architectures. From identity management to threat detection and zero-trust frameworks, our implementations ensure your workloads are protected against modern adversaries while maintaining strict compliance requirements.</p>
                <div class="tech-stack">
                    <span class="tech-tag">Zero Trust Architecture</span>
                    <span class="tech-tag">Automated Compliance</span>
                    <span class="tech-tag">Continuous Threat Detection</span>
                </div>
            </div>

            <!-- Right Column Grid -->
            <div class="security-subgrid">
                <!-- Top Right Card -->
                <div class="security-card">
                    <div class="card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                    </div>
                    <h3>Performance At Scale</h3>
                    <p>Designed for high availability and low latency, ensuring your applications perform flawlessly even under massive load, leveraging edge computing and precise auto-scaling.</p>
                </div>

                <!-- Bottom Right Cards (Split) -->
                <div class="security-card small-card">
                    <div class="card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
                    </div>
                    <h3>Modernization</h3>
                    <p>Transforming monolithic legacy apps into agile microservices.</p>
                </div>

                <div class="security-card small-card border-glow">
                    <div class="card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                    </div>
                    <h3>Data Intelligence</h3>
                    <p>Unlocking insights with secure, scalable data lakes.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
.security-cloud-section {
    background: linear-gradient(135deg, #02040A 0%, #060e20 100%);
    padding: 100px 20px;
    color: #fff;
    font-family: inherit;
    position: relative;
}
.security-cloud-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(51, 161, 253, 0.3), transparent);
}
.security-container {
    max-width: 1200px;
    margin: 0 auto;
}
.security-heading {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 50px;
    text-align: center;
    color: #ffffff;
}
.security-heading .highlight {
    color: #33a1fd;
}
.security-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}
.security-subgrid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto auto;
    gap: 30px;
}
.security-subgrid > .security-card:first-child {
    grid-column: span 2;
}
.security-card {
    background: rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(51, 161, 253, 0.15);
    border-radius: 16px;
    padding: 40px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
}
.security-card:hover {
    transform: translateY(-5px);
    background: rgba(15, 23, 42, 0.6);
    border-color: rgba(51, 161, 253, 0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 20px rgba(51, 161, 253, 0.1);
}
.featured-card {
    justify-content: center;
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.6) 0%, rgba(6, 11, 25, 0.8) 100%);
    border-top: 2px solid rgba(51, 161, 253, 0.5);
}
.small-card {
    padding: 30px 25px;
}
.border-glow {
    box-shadow: inset 0 0 15px rgba(51, 161, 253, 0.1);
}
.card-icon {
    width: 60px; height: 60px;
    border-radius: 14px;
    background: rgba(51, 161, 253, 0.1);
    color: #33a1fd;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 25px;
}
.small-card .card-icon {
    width: 45px; height: 45px;
    margin-bottom: 20px;
}
.security-card h3 {
    font-size: 1.6rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 15px;
}
.small-card h3 {
    font-size: 1.3rem;
}
.security-card p {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #94a3b8;
    margin: 0;
    flex-grow: 1;
}
.small-card p {
    font-size: 0.95rem;
}
.tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 30px;
}
.tech-tag {
    background: rgba(51, 161, 253, 0.1);
    border: 1px solid rgba(51, 161, 253, 0.3);
    color: #e2e8f0;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}
@media (max-width: 992px) {
    .security-grid { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
    .security-heading { font-size: 2.2rem; }
    .security-subgrid { grid-template-columns: 1fr; }
    .security-subgrid > .security-card:first-child { grid-column: span 1; }
}
</style>
"""
    content = content[:start_idx] + new_security_section + content[start_idx:]
    print("Successfully injected Security Cloud Innovation.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
