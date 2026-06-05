import re

def gen_dropdown(id_target, options, selected_val):
    items = []
    for val in options:
        active_cls = ' active' if val == selected_val else ''
        items.append(f'<div class="dropdown-item{active_cls}" onclick="selectDropdownValue(this, \'{id_target}\', \'{val}\', event)">{val}</div>')
    
    return f'''
                <div class="custom-dropdown">
                  {''.join(items)}
                </div>
'''

hours = [f"{h:02d}" for h in range(24)]
mins = [f"{m:02d}" for m in range(0, 60, 5)]

html = f'''        <div class="time-cards">
          <div class="time-card">
            <span class="label">외출 시간</span>
            <div class="time-value">
              <div class="time-part" onclick="toggleDropdown(this)">
                <span id="out-hour">08</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
{gen_dropdown("out-hour", hours, "08")}
              </div>
              <span class="colon">:</span>
              <div class="time-part" onclick="toggleDropdown(this)">
                <span id="out-minute">30</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
{gen_dropdown("out-minute", mins, "30")}
              </div>
            </div>
          </div>
          <div class="time-card">
            <span class="label">귀가 시간</span>
            <div class="time-value">
              <div class="time-part" onclick="toggleDropdown(this)">
                <span id="in-hour">18</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
{gen_dropdown("in-hour", hours, "18")}
              </div>
              <span class="colon">:</span>
              <div class="time-part" onclick="toggleDropdown(this)">
                <span id="in-minute">30</span>
                <svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
{gen_dropdown("in-minute", mins, "30")}
              </div>
            </div>
          </div>
        </div>'''

with open('e:/포폴/우산비서/usanbiseo/Usanbiseo/settings.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="time-cards">.*?</div>\s*</section>', html + '\n      </section>', content, flags=re.DOTALL)

with open('e:/포폴/우산비서/usanbiseo/Usanbiseo/settings.html', 'w', encoding='utf-8') as f:
    f.write(content)
