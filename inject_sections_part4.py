import os
import re

file_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 4. Industries We Serve Section ---
start_idx = content.find('<div class="elementor-element elementor-element-a654f97')
if start_idx != -1:
    end_idx = content.find('<div class="elementor-element elementor-element-4184679', start_idx)
    if end_idx != -1:
        new_industries = """<section class="industries-section">
    <div class="ind-container">
        <h2 class="ind-heading">Industries We <span class="highlight">Serve</span></h2>
        
        <div class="ind-grid">
            <!-- Telecom -->
            <div class="ind-card">
                <div class="ind-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
                </div>
                <h3>Telecom</h3>
                <p>We build massively scalable, low-latency infrastructure capable of handling high-throughput 5G data streams and automated network functions.</p>
            </div>

            <!-- Media & Entertainment -->
            <div class="ind-card">
                <div class="ind-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>
                </div>
                <h3>Media &amp; Entertainment</h3>
                <p>Delivering high-performance storage and compute architectures optimized for rendering pipelines and global content delivery networks.</p>
            </div>

            <!-- Life Sciences (Featured/Center) -->
            <div class="ind-card featured-ind-card">
                <div class="ind-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                </div>
                <h3>Life Sciences</h3>
                <p>Designing HIPAA-compliant, high-performance computing (HPC) environments to accelerate genomics research, drug discovery, and clinical trial data analysis while ensuring strict data privacy and sovereignty.</p>
            </div>

            <!-- Manufacturing -->
            <div class="ind-card">
                <div class="ind-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                </div>
                <h3>Manufacturing</h3>
                <p>Implementing resilient edge-to-cloud architectures that process IoT telemetry in real-time, enabling predictive maintenance and supply chain optimization.</p>
            </div>

            <!-- Financial Services -->
            <div class="ind-card">
                <div class="ind-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                </div>
                <h3>Financial Services</h3>
                <p>Architecting highly secure, immutable ledger environments and low-latency trading infrastructure that adhere to stringent PCI-DSS regulations.</p>
            </div>
        </div>
    </div>
</section>

<style>
.industries-section {
    background: radial-gradient(circle at bottom, #0B1D3A 0%, #030A16 100%);
    padding: 100px 20px;
    color: #fff;
    font-family: inherit;
    border-top: 1px solid rgba(51, 161, 253, 0.1);
}
.ind-container {
    max-width: 1200px;
    margin: 0 auto;
}
.ind-heading {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 60px;
    text-align: center;
    color: #ffffff;
}
.ind-heading .highlight {
    color: #33a1fd;
}
.ind-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}
.ind-card {
    background: rgba(13, 27, 42, 0.5);
    border: 1px solid rgba(51, 161, 253, 0.15);
    border-radius: 12px;
    padding: 40px 30px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}
.ind-card:hover {
    transform: translateY(-5px);
    border-color: rgba(51, 161, 253, 0.5);
    box-shadow: 0 15px 30px rgba(0,0,0,0.5), inset 0 0 15px rgba(51, 161, 253, 0.1);
}
.featured-ind-card {
    background: linear-gradient(145deg, rgba(51, 161, 253, 0.15) 0%, rgba(13, 27, 42, 0.8) 100%);
    border: 1px solid rgba(51, 161, 253, 0.4);
    box-shadow: inset 0 0 30px rgba(51, 161, 253, 0.1);
    transform: scale(1.05);
    z-index: 2;
}
.featured-ind-card:hover {
    transform: scale(1.05) translateY(-5px);
    border-color: rgba(51, 161, 253, 0.8);
    box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 0 40px rgba(51, 161, 253, 0.2);
}
.ind-icon {
    width: 64px; height: 64px;
    border-radius: 50%;
    background: rgba(51, 161, 253, 0.1);
    color: #33a1fd;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 25px;
    border: 1px solid rgba(51, 161, 253, 0.2);
}
.ind-icon svg {
    width: 32px; height: 32px;
}
.featured-ind-card .ind-icon {
    background: #33a1fd;
    color: #030A16;
    border: none;
    box-shadow: 0 0 20px rgba(51, 161, 253, 0.4);
}
.ind-card h3 {
    font-size: 1.4rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 15px;
}
.featured-ind-card h3 {
    font-size: 1.6rem;
    color: #33a1fd;
}
.ind-card p {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #94a3b8;
    margin: 0;
}
.featured-ind-card p {
    color: #cbd5e1;
    font-size: 1rem;
}
/* Layout adjustments */
.ind-card:nth-child(4) {
    grid-column: 1 / span 1;
}
.ind-card:nth-child(5) {
    grid-column: 3 / span 1;
}
.featured-ind-card {
    grid-column: 2 / span 1;
    grid-row: 1 / span 2;
}

@media (max-width: 992px) {
    .ind-grid { grid-template-columns: 1fr 1fr; }
    .featured-ind-card {
        grid-column: span 2;
        grid-row: auto;
        transform: scale(1);
    }
    .featured-ind-card:hover { transform: translateY(-5px); }
    .ind-card:nth-child(4), .ind-card:nth-child(5) { grid-column: auto; }
}
@media (max-width: 768px) {
    .ind-heading { font-size: 2.2rem; }
    .ind-grid { grid-template-columns: 1fr; }
    .featured-ind-card { grid-column: auto; }
}
</style>
"""
        content = content[:start_idx] + new_industries + content[end_idx:]
        print("Successfully injected Industries We Serve.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
