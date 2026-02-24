import sys

file_path = "c:\\Users\\ADITYA VERMA\\OneDrive\\Documents\\New folder (20)\\altcloudaiclone\\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<div class="elementor-element elementor-element-4184679 e-flex e-con-boxed e-con e-parent"' in line:
        start_idx = i
    if '<div id="comments" class="comments-template">' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_html = '''
										<div class="elementor-element elementor-element-4184679 e-flex e-con-boxed e-con e-parent"
											data-id="4184679" data-element_type="container"
											data-settings="{&quot;background_background&quot;:&quot;classic&quot;}"
											style="padding: 60px 0; display: flex; flex-direction: column; align-items: center;">
											<div class="e-con-inner" style="width: 100%; max-width: 1200px; display: flex; flex-direction: column; align-items: center;">
												<div class="elementor-element elementor-element-4882b97 elementor-widget elementor-widget-heading"
													data-id="4882b97" data-element_type="widget"
													data-widget_type="heading.default"
													style="margin-bottom: 40px; text-align: center;">
													<h2 class="elementor-heading-title elementor-size-default" style="font-size: 2.5rem; font-weight: bold; margin: 0; color: #fff;">
														Technology <span style="color:#33a1fd">Partners</span></h2>
												</div>
												<div class="elementor-element elementor-element-579a789 e-con-full e-flex e-con e-child"
													data-id="579a789" data-element_type="container"
													style="display: flex; justify-content: center; width: 100%;">
													<div class="elementor-element elementor-element-7463f6e e-con-full e-flex e-con e-child"
														data-id="7463f6e" data-element_type="container"
														style="display: flex; justify-content: center; align-items: center; width: auto; max-width: 300px; transition: transform 0.3s ease; padding: 20px; border-radius: 12px; background: rgba(10, 30, 70, 0.4); border: 1px solid rgba(51, 161, 253, 0.3); box-shadow: 0 5px 15px rgba(0,0,0,0.3) inset;"
														onmouseover="this.style.transform='translateY(-5px) scale(1.05)'; this.style.borderColor='rgba(51, 161, 253, 0.8)';"
														onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.borderColor='rgba(51, 161, 253, 0.3)';">
														<div class="elementor-element elementor-element-8f4c475 elementor-widget__width-initial elementor-widget elementor-widget-image"
															data-id="8f4c475" data-element_type="widget"
															data-widget_type="image.default" style="width: 100%; text-align: center;">
															<img loading="lazy" decoding="async" src="assets/37e65b7d_Frame-495-1.png"
																class="attachment-large size-large wp-image-1578" alt="AWS Partner Logo"
																style="max-width: 100%; height: auto; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));">
														</div>
													</div>
												</div>
											</div>
										</div>
'''
    new_lines = lines[:start_idx] + [new_html + "\n"] + lines[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Success")
else:
    print(f"Failed to find insertion point. start={start_idx} end={end_idx}")
