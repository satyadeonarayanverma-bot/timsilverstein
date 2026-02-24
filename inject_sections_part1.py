import os

file_path = r"c:\Users\ADITYA VERMA\OneDrive\Documents\New folder (20)\altcloudaiclone\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero text updates
content = content.replace(
    'Deliver the True\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<span style="color: #33a1fd">Promise of\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAI</span>',
    'Secure Cloud <span style="color: #33a1fd">Transformation</span><br>Starts with Strong <span style="color: #33a1fd">Architecture</span>'
)
content = content.replace(
    '<p>Unburdened by Legacy Tools, <br>Processes,\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tand Talent</p>',
    '<p>Modernize Platforms. Strengthen Security.<br>\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tOperate with Confidence.</p>'
)
# Match the hero subtext correctly using a generic replace because the spacing might vary
hero_find = """Cloudiva.ai is a next-generation,\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAI-Forward\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAWS Consulting Partner, unlocking the power\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tof AI to deliver measurable improvements in\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tspeed, precision and cost-efficiency for its\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcustomers."""
hero_replace = """<b>Cloudiva.ai</b> is a cloud transformation and security-focused consulting partner<br>\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\thelping organizations <b>modernize infrastructure</b>, <b>strengthen governance</b>, and<br>\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tbuild resilient cloud platforms through <b>architecture-led strategy</b> and<br>\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b>continuous protection</b>."""
content = content.replace(hero_find, hero_replace)

# 2. Re-inject Cloud Services section
# Find the start of the `AI-Forward Cloud Services` block which is element `2b7c9a0`
start_idx = content.find('<div class="elementor-element elementor-element-2b7c9a0')
if start_idx != -1:
    # Find where to end: the section immediately follows it, maybe element `7bed48a e-flex e-con-boxed e-con e-parent` 
    # Actually wait, let's just replace the blocks up to the start of "Transforming Traditional Mindsets"
    end_idx = content.find('<div class="elementor-element elementor-element-7bed48a')
    if end_idx != -1:
        new_cloud_services = """<section class="cloud-services-section">
											<div class="cs-stars"></div>
											<div class="cs-grid-floor"></div>
											<div class="cs-container">
												<h2 class="cs-heading">Cloud Transformation <span class="cs-highlight">Services</span></h2>
												<p class="cs-subheading">
													We help organizations move from legacy complexity to <strong>secure</strong>, modern cloud platforms<br>
													through <strong>architecture-led strategy</strong>, <strong>structured migration</strong>, <strong>intelligent<br>
													modernization</strong>, and <strong>continuous operations</strong>.
												</p>
												<div class="cs-grid">
													<!-- Card 1 -->
													<div class="cs-card">
														<div class="cs-icon-wrapper">
															<svg class="stroke-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
														</div>
														<h3>Strategy &amp; Advisory</h3>
														<ul>
															<li>Cloud assessments</li>
															<li>Architecture planning</li>
															<li>Governance strategy</li>
															<li>Security alignment</li>
														</ul>
													</div>
													<!-- Card 2 -->
													<div class="cs-card">
														<div class="cs-icon-wrapper">
															<svg class="stroke-icon" viewBox="0 0 24 24"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/><path d="M12 9v6"/><path d="M9 12l3-3 3 3"/></svg>
														</div>
														<h3>Cloud Migration</h3>
														<ul>
															<li>Datacenter exit</li>
															<li>Workload transition</li>
															<li>Data migration</li>
															<li>Platform onboarding</li>
														</ul>
													</div>
													<!-- Card 3 -->
													<div class="cs-card">
														<div class="cs-icon-wrapper">
															<svg class="stroke-icon" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
														</div>
														<h3>Platform Modernization</h3>
														<ul>
															<li>Container adoption</li>
															<li>Application refactoring</li>
															<li>API integration</li>
															<li>Platform engineering</li>
														</ul>
													</div>
													<!-- Card 4 -->
													<div class="cs-card">
														<div class="cs-icon-wrapper">
															<svg class="stroke-icon" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><rect x="9" y="11" width="6" height="4" rx="1"/><path d="M10 11V9a2 2 0 0 1 4 0v2"/></svg>
														</div>
														<h3>Security</h3>
														<ul>
															<li>Governance automation</li>
															<li>Threat detection &amp; response</li>
															<li>Vulnerability assessments</li>
															<li>VAPT &amp; adversarial testing</li>
														</ul>
													</div>
												</div>
											</div>
										</section>

										<style>
										.cloud-services-section {
											background: radial-gradient(circle at center, #0B1D3A 0%, #030A16 70%);
											position: relative;
											padding: 100px 20px 80px;
											color: #fff;
											overflow: hidden;
											font-family: inherit;
										}
										.cs-stars {
											position: absolute;
											top: 0; left: 0; right: 0; bottom: 0;
											background-image: 
											radial-gradient(1.5px 1.5px at 20px 30px, #eee, rgba(0,0,0,0)),
											radial-gradient(1.5px 1.5px at 140px 70px, #fff, rgba(0,0,0,0)),
											radial-gradient(2px 2px at 250px 160px, #ddd, rgba(0,0,0,0)),
											radial-gradient(1.5px 1.5px at 90px 40px, #fff, rgba(0,0,0,0)),
											radial-gradient(2px 2px at 330px 80px, #fff, rgba(0,0,0,0)),
											radial-gradient(1.5px 1.5px at 460px 120px, #ddd, rgba(0,0,0,0));
											background-repeat: repeat;
											background-size: 500px 500px;
											opacity: 0.6;
										}
										.cs-grid-floor {
											position: absolute;
											left: 0; right: 0; bottom: -50px;
											height: 150px;
											background: linear-gradient(to top, rgba(51, 161, 253, 0.4), transparent);
											transform: perspective(200px) rotateX(60deg);
											pointer-events: none;
										}
										.cs-container {
											max-width: 1200px;
											margin: 0 auto;
											position: relative;
											z-index: 2;
											text-align: center;
										}
										.cs-heading {
											font-size: 3rem;
											font-weight: 700;
											margin-bottom: 20px;
											color: #ffffff;
										}
										.cs-highlight {
											color: #33a1fd;
										}
										.cs-subheading {
											font-size: 1.1rem;
											line-height: 1.6;
											color: #a0aec0;
											margin-bottom: 60px;
										}
										.cs-subheading strong {
											color: #fff;
											font-weight: 600;
										}
										.cs-grid {
											display: grid;
											grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
											gap: 30px;
											text-align: left;
										}
										.cs-card {
											background: rgba(13, 27, 42, 0.6);
											border: 1px solid rgba(51, 161, 253, 0.2);
											border-radius: 12px;
											padding: 40px 30px;
											backdrop-filter: blur(10px);
											-webkit-backdrop-filter: blur(10px);
											box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.05), 0 10px 30px rgba(0,0,0,0.5);
											transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
											position: relative;
											overflow: hidden;
										}
										.cs-card::before {
											content: '';
											position: absolute;
											top: 0; left: 0; right: 0;
											height: 2px;
											background: linear-gradient(90deg, transparent, rgba(51, 161, 253, 0.8), transparent);
											opacity: 0;
											transition: opacity 0.3s ease;
										}
										.cs-card:hover {
											transform: translateY(-5px);
											border-color: rgba(51, 161, 253, 0.5);
											box-shadow: inset 0 0 20px rgba(51, 161, 253, 0.1), 0 15px 40px rgba(0,0,0,0.6);
										}
										.cs-card:hover::before {
											opacity: 1;
										}
										.cs-icon-wrapper {
											width: 50px; height: 50px;
											border-radius: 12px;
											background: rgba(51, 161, 253, 0.1);
											border: 1px solid rgba(51, 161, 253, 0.2);
											display: flex; align-items: center; justify-content: center;
											margin-bottom: 25px;
										}
										.cs-icon-wrapper svg {
											width: 24px; height: 24px;
											stroke: #33a1fd;
											fill: none;
											stroke-width: 1.5;
										}
										.cs-card h3 {
											font-size: 1.4rem;
											font-weight: 600;
											color: #ffffff;
											margin-bottom: 20px;
										}
										.cs-card ul {
											list-style: none; padding: 0; margin: 0;
										}
										.cs-card li {
											position: relative;
											padding-left: 20px;
											margin-bottom: 12px;
											color: #cbd5e1;
											font-size: 0.95rem;
											line-height: 1.4;
										}
										.cs-card li::before {
											content: '▹';
											position: absolute;
											left: 0; top: 0;
											color: #33a1fd;
											font-size: 1.1rem;
										}
										@media (max-width: 768px) {
											.cs-heading { font-size: 2.2rem; }
											.cs-grid { grid-template-columns: 1fr; }
										}
										</style>\n\t\t\t\t\t\t\t\t\t\t"""
        content = content[:start_idx] + new_cloud_services + content[end_idx:]
        print("Successfully injected Cloud Services.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
